# 🔐 Secure2FA
Basic CLI-based 2FA (Two-Factor Authentication) system using Python.

## Features

- User registration with bcrypt password hashing
- Time-based OTP (TOTP) with `pyotp`
- Offline, CLI-based — no third-party auth servers
- Stores user data in `users.json`

## Installation

```bash
git clone https://github.com/yourusername/secure2fa.git
cd secure2fa
pip install -r requirements.txt
