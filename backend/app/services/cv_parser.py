"""
CV Parser Service.
Rule-based extraction of structured data from PDF and DOCX resume files.
No AI — uses regex and heading-pattern matching for section detection.

Pipeline: PDF/DOCX → Raw text → Section detection → Structured JSON
"""

import logging
import os
import re
from typing import Any

logger = logging.getLogger(__name__)


# ──────────────────────────────────────────────
# Section Heading Aliases
# Flexible list to handle CV heading variations.
# ──────────────────────────────────────────────
SECTION_ALIASES: dict[str, list[str]] = {
    "personal_info": [
        "personal info", "personal information", "contact",
        "contact info", "contact information", "contact details",
        "about me", "about", "profile", "summary", "objective",
        "professional summary", "career objective", "personal details",
    ],
    "education": [
        "education", "academic", "academic background", "degrees",
        "qualifications", "qualification", "academic qualifications",
        "educational background", "schooling",
    ],
    "experience": [
        "experience", "work experience", "professional experience",
        "employment", "employment history", "work history",
        "career history", "career", "professional background",
        "relevant experience", "job experience",
    ],
    "projects": [
        "projects", "personal projects", "side projects", "portfolio",
        "key projects", "notable projects", "selected projects",
        "academic projects", "open source", "open-source projects",
    ],
    "skills": [
        "skills", "technical skills", "technologies", "tech stack",
        "competencies", "core competencies", "tools", "tools & technologies",
        "tools and technologies", "programming languages", "frameworks",
        "technical competencies", "areas of expertise", "expertise",
        "proficiencies",
    ],
    "certificates": [
        "certifications", "certificates", "credentials",
        "professional certifications", "licenses",
        "licenses & certifications", "licenses and certifications",
        "professional credentials", "accreditations",
    ],
    "languages": [
        "languages", "language skills", "spoken languages",
        "language proficiency", "foreign languages",
    ],
}

# Build reverse lookup: normalized_alias → section_key
_ALIAS_TO_SECTION: dict[str, str] = {}
for _section_key, _aliases in SECTION_ALIASES.items():
    for _alias in _aliases:
        _ALIAS_TO_SECTION[_alias.lower().strip()] = _section_key


def extract_text_from_pdf(file_path: str) -> str:
    """Extract all text from a PDF file using pdfplumber."""
    import pdfplumber

    text_parts: list[str] = []
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
    except Exception as e:
        logger.error(f"Failed to extract text from PDF '{file_path}': {e}")
        raise ValueError(f"Could not parse PDF file: {e}") from e

    return "\n".join(text_parts)


def extract_text_from_docx(file_path: str) -> str:
    """Extract all text from a DOCX file using python-docx."""
    from docx import Document

    text_parts: list[str] = []
    try:
        doc = Document(file_path)
        for para in doc.paragraphs:
            text_parts.append(para.text)
    except Exception as e:
        logger.error(f"Failed to extract text from DOCX '{file_path}': {e}")
        raise ValueError(f"Could not parse DOCX file: {e}") from e

    return "\n".join(text_parts)


def extract_text(file_path: str) -> str:
    """Extract raw text from a CV file (PDF or DOCX)."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file format: '{ext}'. Only .pdf and .docx are accepted.")


def _detect_section(line: str) -> str | None:
    """
    Detect if a line is a section heading.
    Returns the canonical section key or None.

    Heuristics:
    - Line is short (< 60 chars)
    - Normalized text matches an alias
    - Handles headings with trailing colons, dashes, pipes
    - Handles ALL-CAPS headings
    """
    stripped = line.strip()
    if not stripped or len(stripped) > 60:
        return None

    # Clean trailing punctuation and decorators
    cleaned = re.sub(r'[:\-–—|•*#_=]+$', '', stripped).strip()
    # Remove leading bullets/numbers/decorators
    cleaned = re.sub(r'^[\d.\-–—|•*#_=>]+\s*', '', cleaned).strip()

    if not cleaned:
        return None

    normalized = cleaned.lower()

    # Direct alias match
    if normalized in _ALIAS_TO_SECTION:
        return _ALIAS_TO_SECTION[normalized]

    # Try removing common prefixes like "my " or trailing "s"
    for alias, section_key in _ALIAS_TO_SECTION.items():
        if normalized == alias or normalized == alias + "s":
            return section_key

    return None


def _split_into_sections(raw_text: str) -> dict[str, str]:
    """
    Split raw CV text into named sections based on heading detection.
    Returns: {section_key: section_text_content}
    """
    lines = raw_text.split("\n")
    sections: dict[str, list[str]] = {}
    current_section: str | None = None
    preamble_lines: list[str] = []

    for line in lines:
        detected = _detect_section(line)
        if detected:
            current_section = detected
            if current_section not in sections:
                sections[current_section] = []
        elif current_section:
            sections[current_section].append(line)
        else:
            # Lines before any section heading → treat as personal_info/preamble
            preamble_lines.append(line)

    # Merge preamble into personal_info
    if preamble_lines:
        if "personal_info" not in sections:
            sections["personal_info"] = []
        sections["personal_info"] = preamble_lines + sections.get("personal_info", [])

    return {k: "\n".join(v).strip() for k, v in sections.items() if v}


def _parse_personal_info(text: str) -> dict[str, str]:
    """Extract personal info fields from preamble/contact text."""
    info: dict[str, str] = {}

    # Try to extract name (usually first non-empty line)
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    if lines:
        # First substantial line is likely the name
        info["name"] = lines[0]

    # Email
    email_match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
    if email_match:
        info["email"] = email_match.group()

    # Phone
    phone_match = re.search(r'[\+]?[\d\s\-().]{7,15}', text)
    if phone_match:
        candidate = phone_match.group().strip()
        # Filter out very short matches that might be years
        if len(re.sub(r'\D', '', candidate)) >= 7:
            info["phone"] = candidate

    # LinkedIn URL
    linkedin_match = re.search(r'linkedin\.com/in/[\w-]+', text, re.IGNORECASE)
    if linkedin_match:
        info["linkedin"] = linkedin_match.group()

    # GitHub URL
    github_match = re.search(r'github\.com/[\w-]+', text, re.IGNORECASE)
    if github_match:
        info["github"] = github_match.group()

    # Location (look for common patterns)
    location_match = re.search(r'(?:location|address|city|based in)[:\s]+(.+)', text, re.IGNORECASE)
    if location_match:
        info["location"] = location_match.group(1).strip()

    return info


def _parse_education(text: str) -> list[dict[str, str]]:
    """Parse education section into structured entries."""
    entries: list[dict[str, str]] = []
    if not text.strip():
        return entries

    # Split by blank lines or lines that look like new entries (start with degree/year)
    blocks = re.split(r'\n\s*\n', text)
    for block in blocks:
        block = block.strip()
        if not block:
            continue

        entry: dict[str, str] = {"raw": block}
        lines = [l.strip() for l in block.split("\n") if l.strip()]

        if lines:
            entry["institution"] = lines[0]
        if len(lines) > 1:
            entry["degree"] = lines[1]

        # Extract years
        year_match = re.findall(r'((?:19|20)\d{2})', block)
        if year_match:
            entry["years"] = " - ".join(year_match[:2])

        entries.append(entry)

    return entries


def _parse_experience(text: str) -> list[dict[str, str]]:
    """Parse work experience section into structured entries."""
    entries: list[dict[str, str]] = []
    if not text.strip():
        return entries

    blocks = re.split(r'\n\s*\n', text)
    for block in blocks:
        block = block.strip()
        if not block:
            continue

        entry: dict[str, str] = {"raw": block}
        lines = [l.strip() for l in block.split("\n") if l.strip()]

        if lines:
            entry["title"] = lines[0]
        if len(lines) > 1:
            entry["company"] = lines[1]
        if len(lines) > 2:
            entry["description"] = " ".join(lines[2:])

        # Extract years/dates
        year_match = re.findall(r'((?:19|20)\d{2})', block)
        if year_match:
            entry["years"] = " - ".join(year_match[:2])

        entries.append(entry)

    return entries


def _parse_projects(text: str) -> list[dict[str, Any]]:
    """Parse projects section into structured entries with skills_mentioned."""
    entries: list[dict[str, Any]] = []
    if not text.strip():
        return entries

    blocks = re.split(r'\n\s*\n', text)
    for block in blocks:
        block = block.strip()
        if not block:
            continue

        lines = [l.strip() for l in block.split("\n") if l.strip()]

        project: dict[str, Any] = {
            "name": lines[0] if lines else "",
            "description": " ".join(lines[1:]) if len(lines) > 1 else "",
            "skills_mentioned": [],
        }

        # Extract technology mentions from description
        # Look for common tech keywords in parentheses or after "using", "with", "built with"
        tech_pattern = re.search(
            r'(?:using|with|built with|technologies?|tech stack|stack)[:\s]+(.+)',
            block, re.IGNORECASE
        )
        if tech_pattern:
            tech_text = tech_pattern.group(1)
            skills = [s.strip() for s in re.split(r'[,;|&]', tech_text) if s.strip()]
            project["skills_mentioned"] = skills
        else:
            # Fallback: extract bracketed or parenthesized tech lists
            bracket_match = re.findall(r'[(\[]([\w\s,./+-]+)[)\]]', block)
            for match in bracket_match:
                skills = [s.strip() for s in match.split(",") if s.strip() and len(s.strip()) > 1]
                project["skills_mentioned"].extend(skills)

        entries.append(project)

    return entries


def _parse_skills(text: str) -> list[str]:
    """Parse skills section into a flat list of skill names."""
    if not text.strip():
        return []

    skills: list[str] = []

    # Split by common delimiters: comma, semicolon, pipe, bullet, newline
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        # Remove leading bullets/dashes
        line = re.sub(r'^[\-•*▪◦]\s*', '', line)

        # Split by commas, semicolons, pipes
        parts = re.split(r'[,;|]', line)
        for part in parts:
            cleaned = part.strip()
            # Remove category prefixes like "Languages:" or "Databases:"
            cleaned = re.sub(r'^[\w\s]+:\s*', '', cleaned) if ':' in cleaned else cleaned
            if cleaned and len(cleaned) > 1 and len(cleaned) < 80:
                skills.append(cleaned)

    return skills


def _parse_certificates(text: str) -> list[dict[str, str]]:
    """Parse certifications section into structured entries."""
    entries: list[dict[str, str]] = []
    if not text.strip():
        return entries

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        # Remove leading bullets/dashes/numbers
        line = re.sub(r'^[\d.\-•*▪◦)\]]+\s*', '', line).strip()
        if not line or len(line) < 3:
            continue

        cert: dict[str, str] = {"name": line, "provider": ""}

        # Try to extract provider after dash or by-line
        provider_match = re.search(r'\s+[-–—]\s+(.+?)(?:\s*[(\[]|$)', line)
        if provider_match:
            cert["provider"] = provider_match.group(1).strip()
            cert["name"] = line[:provider_match.start()].strip()
        else:
            # Check for "by Provider" pattern
            by_match = re.search(r'\s+by\s+(.+)', line, re.IGNORECASE)
            if by_match:
                cert["provider"] = by_match.group(1).strip()
                cert["name"] = line[:by_match.start()].strip()

        entries.append(cert)

    return entries


def _parse_languages(text: str) -> list[str]:
    """Parse languages section into a list."""
    if not text.strip():
        return []

    languages: list[str] = []
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        line = re.sub(r'^[\-•*▪◦]\s*', '', line)
        # Split by commas
        parts = re.split(r'[,;]', line)
        for part in parts:
            cleaned = part.strip()
            if cleaned and len(cleaned) > 1:
                # Take just the language name, remove proficiency level
                lang = re.split(r'\s*[-–—:(]', cleaned)[0].strip()
                if lang:
                    languages.append(lang)

    return languages


def parse_cv(file_path: str) -> dict[str, Any]:
    """
    Full CV parsing pipeline.

    Pipeline: File → Raw text → Section detection → Structured JSON

    Returns:
        {
            "personal_info": {},
            "education": [],
            "experience": [],
            "projects": [{"name": "", "description": "", "skills_mentioned": []}],
            "skills": [],
            "certificates": [{"name": "", "provider": ""}],
            "languages": [],
            "raw_text": str,
            "detected_sections": [str],
        }
    """
    logger.info(f"Parsing CV file: {file_path}")

    # Step 1: Extract raw text
    raw_text = extract_text(file_path)
    if not raw_text.strip():
        raise ValueError("CV file appears to be empty or could not be read.")

    logger.debug(f"Extracted {len(raw_text)} chars of raw text")

    # Step 2: Detect and split sections
    sections = _split_into_sections(raw_text)
    detected_section_keys = list(sections.keys())
    logger.info(f"Detected sections: {detected_section_keys}")

    # Step 3: Parse each section into structured data
    result: dict[str, Any] = {
        "personal_info": _parse_personal_info(sections.get("personal_info", "")),
        "education": _parse_education(sections.get("education", "")),
        "experience": _parse_experience(sections.get("experience", "")),
        "projects": _parse_projects(sections.get("projects", "")),
        "skills": _parse_skills(sections.get("skills", "")),
        "certificates": _parse_certificates(sections.get("certificates", "")),
        "languages": _parse_languages(sections.get("languages", "")),
        "raw_text": raw_text,
        "detected_sections": detected_section_keys,
    }

    logger.info(
        f"CV parsed: {len(result['skills'])} skills, "
        f"{len(result['certificates'])} certs, "
        f"{len(result['projects'])} projects, "
        f"{len(result['experience'])} exp entries"
    )

    return result
