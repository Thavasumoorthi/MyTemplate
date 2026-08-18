# MyTemplate

## Overview
Short description of the application and assessment changes.

## Prerequisites
- Python 3.12

## Local Setup

git clone https://github.com/Sumukh/Ignite
cd Ignite

python -m venv env

Windows:
source env\Scripts\activate


pip install -r requirements.txt

## Run Application

python manage.py server

Application:
http://127.0.0.1:5000

## Run Tests

pytest qa/test_backend.py qa/test_ui.py -v

## Run QA Pipeline

make qa

## Individual Checks

make tests
make coverage
make lint
make security

## Reports

Reports are generated under:

reports/
coverage_report/

The GitHub Actions workflow also uploads these as artifacts.

## CI Pipeline

GitHub Actions runs on:
- Push
- Pull Request

The pipeline performs:
1. Dependency installation
2. Playwright browser installation
3. Application startup
4. Backend/UI tests
5. Coverage
6. Ruff linting
7. Bandit security scan
8. Report artifact upload