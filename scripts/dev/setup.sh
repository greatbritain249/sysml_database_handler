#!/usr/bin/env bash

echo "[+] Installing application dependencies ..."

source .env

echo "[+] Creating a virtualenv (if it does not already exist)"
python3 -m venv venv

#Install all dependencies some use custom libraries that must be stored in your local Pypi server
pip install \
  --upgrade \
  -r requirements.txt

echo "[+] Installing auto-format pre-commit hooks"
pre-commit install

echo "[+] Done"