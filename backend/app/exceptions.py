"""
Custom domain exceptions for RoleGauge Backend.
"""


class RoleGaugeException(Exception):
    """Base exception for all RoleGauge domain exceptions."""
    def __init__(self, message: str, status_code: int = 500, detail: str | None = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.detail = detail or message


class GitHubUserNotFoundError(RoleGaugeException):
    """Raised when the specified GitHub user does not exist."""
    def __init__(self, username: str):
        super().__init__(
            message=f"GitHub user '{username}' not found",
            status_code=404,
            detail=f"GitHub user '{username}' was not found on GitHub."
        )


class GitHubRateLimitError(RoleGaugeException):
    """Raised when GitHub API rate limit is exceeded."""
    def __init__(self, message: str = "GitHub API rate limit exceeded"):
        super().__init__(
            message=message,
            status_code=429,
            detail=f"{message}. Please provide a GITHUB_TOKEN or try again later."
        )


class GitHubTimeoutError(RoleGaugeException):
    """Raised when GitHub API request times out."""
    def __init__(self, message: str = "GitHub API request timed out"):
        super().__init__(
            message=message,
            status_code=504,
            detail=f"{message}. Please check network connectivity or try again later."
        )


class RoleNotFoundError(RoleGaugeException):
    """Raised when requested role or level does not exist in knowledge base."""
    def __init__(self, role_id: str, level: str | None = None, available_roles: list[str] | None = None):
        if level:
            msg = f"Level '{level}' not found for role '{role_id}'"
        else:
            avail = f" Available roles: {available_roles}" if available_roles else ""
            msg = f"Unknown role: '{role_id}'.{avail}"
        super().__init__(message=msg, status_code=400, detail=msg)


class AnalysisNotFoundError(RoleGaugeException):
    """Raised when requested analysis result ID is not found in database."""
    def __init__(self, analysis_id: str):
        super().__init__(
            message=f"Analysis result with ID '{analysis_id}' not found",
            status_code=404,
            detail=f"Analysis result with ID '{analysis_id}' not found in database."
        )
