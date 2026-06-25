# Sample config for testing GitHub secret scanning.
# All values below are FAKE / non-functional and match detector patterns only.
# They grant access to nothing. Do not replace with real secrets.

# AWS (these are AWS's own documented example values - not live)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# GitHub personal access token (fake, correct shape)
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwx12"

# Stripe test-style secret key (fake)
STRIPE_SECRET_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dcEXAMPLE0000"

# Google API key (fake, correct shape)
GOOGLE_API_KEY = "AIzaSyD-1234567890abcdefghijklmnopqrstuv"

# Slack token (fake)
SLACK_TOKEN = "xoxb-000000000000-000000000000-EXAMPLEEXAMPLEEX"

# A fake private key block
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEdummyFAKEkeymaterialFORtestingONLYnotARealKey0000000000000000
1111111111111111111111111111111111111111111111111111111111111111
-----END RSA PRIVATE KEY-----"""
