# Automating Microsoft Multi-Factor Authentication

## Overview

This project demonstrates a simple proof-of-concept for automating the login process to a Microsoft corporate account, including handling Multi-Factor Authentication. 
This example assumes you are using a corporate account with MFA enabled, as you will need access to https://mysignins.microsoft.com to update your MFA options. This URL cannot be accessed by person accounts.

## Setting up TOTP for the account

You will need to update your sign in options https://mysignins.microsoft.com to use TOTP. Click:
1. 'Add a sign-in method'
2. 'Microsoft Authenticator'
3. 'I want to use a different authenticator app'
4. 'Next'
5. 'Can't scan image?' under the QR code
6. Copy the 'Secret key' to .env
7. Run the function generate_totp to get the 6-digit code to complete setup
8. Delete the previous MFA in place, and set this TOTP to the default sign in method.

## Running the code

Install requirements 
> pip install -r requirements.txt

| Package            | Purpose                                                                |
|--------------------|------------------------------------------------------------------------|
| certifi            | Provides Mozilla’s CA Bundle – used for HTTPS requests.                |
| charset-normalizer | Character encoding auto-detection for text files (alternative to chardet).    |
| colorama           | Cross-platform colored terminal text.                                  |
| dotenv             | Loads environment variables from `.env` files (old version of python-dotenv). |
| greenlet           | Lightweight coroutines for concurrent programming (used by gevent, etc.).     |
| idna               | Internationalized Domain Names in Applications (IDNA) support.         |
| iniconfig          | Simple INI file parser used by pytest.                                 |
| packaging          | Tools for handling Python package versions and dependencies.           |
| pip                | The Python package installer.                                          |
| playwright         | End-to-end browser automation library.                                 |
| pluggy             | Plugin and hook system used by pytest and others.                      |
| pyee               | EventEmitter-style async event framework (used by Playwright).         |
| Pygments           | Syntax highlighter used in code display and documentation.             |
| pyotp              | Python One-Time Password library (TOTP/HOTP for 2FA).                  |
| pytest             | Testing framework for Python.                                          |
| pytest-base-url    | Pytest plugin to manage a base URL for tests.                          |
| pytest-playwright  | Pytest plugin to run Playwright tests.                                 |
| python-dotenv      | Loads environment variables from `.env` files.                         |
| python-slugify     | Creates slugs (URL-friendly text) from strings.                        |
| requests           | HTTP library for making API calls and web requests.                    |
| text-unidecode     | ASCII transliterations of Unicode text (used by slugify).              |
| typing_extensions  | Backport of Python’s typing features for older versions.               |
| urllib3            | HTTP client for Python – used internally by `requests`.                |

Update .env, then run using cmd
> python ado-login.py