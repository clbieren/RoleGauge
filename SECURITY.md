# Security Policy

## Reporting Vulnerabilities

RoleGauge handles potentially sensitive data (CVs, LinkedIn exports, GitHub tokens, candidate information). If you discover a security vulnerability, **please report it privately** rather than opening a public GitHub issue.

### How to Report

Send a detailed description of the vulnerability to:

**Email:** clbieren4@gmail.com  
**Subject:** `[SECURITY] RoleGauge Vulnerability Report`

Include:
- Description of the vulnerability
- Steps to reproduce (if applicable)
- Potential impact
- Suggested fix (if you have one)

### What to Expect

- We will acknowledge receipt within 48 hours
- We will investigate and work on a fix
- We will release a patch as soon as reasonably possible
- We will credit you in the release notes (unless you prefer anonymity)

## Security Best Practices

### For Self-Hosted Deployments

Since RoleGauge is self-hosted, **you are responsible for infrastructure security:**

1. **Use HTTPS in production** — All API and frontend communication should be encrypted
2. **Secure your database** — PostgreSQL should have strong authentication and network isolation
3. **Rotate secrets regularly** — Change `JWT_SECRET_KEY`, database passwords, and API keys
4. **Use strong `.env` values** — Generate cryptographically secure keys:
   ```bash
   openssl rand -hex 32
   ```
5. **Enable rate limiting** — Use Redis in production for shared rate limit state
6. **Audit access logs** — Monitor who accesses your instance
7. **Keep dependencies updated** — Run `pip install --upgrade -r requirements.txt` regularly

### Data Handling

- **By default, no data is sent to external AI providers** — Set `AI_PROVIDER=none` to use only local analysis
- **If you enable an AI provider**, understand that CV content, LinkedIn exports, and code snippets will be sent to that provider
- **No PII redaction** — RoleGauge does not automatically remove personal identifiable information before sending to AI providers
- **Data retention** — Analysis results are stored in PostgreSQL indefinitely. You must implement your own retention and deletion policies

### Authentication & Encryption

- Passwords are hashed with bcrypt (4.0.1)
- JWT tokens expire after `ACCESS_TOKEN_EXPIRE_MINUTES` (default: 30 minutes)
- API endpoints are rate-limited via Redis
- GitHub tokens are stored in `.env` and never logged

## Known Limitations

- **No PII redaction** for AI provider calls
- **No automatic backup** — You are responsible for backing up your PostgreSQL database
- **No GDPR/KVKK deletion endpoint** — You must handle data deletion requests manually
- **Test/development secrets in `.env.example`** — These are examples only and should be rotated in production

## Dependency Security

RoleGauge uses well-maintained open-source libraries. Keep your dependencies updated:

```bash
pip list --outdated
npm outdated
```

Security advisories are regularly published for Python packages on [PyPI](https://pypi.org) and Node packages on [npm](https://www.npmjs.com).

## License

RoleGauge is released under the MIT License. See [LICENSE](LICENSE) for details.

---

Thank you for helping keep RoleGauge secure! 🔒
