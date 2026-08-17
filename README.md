# QAroad

A Python-based web test automation framework built with **Selenium WebDriver** and **Pytest**.

This project is designed to provide a structured approach to web application test automation using the **Page Object Model (POM)** and reusable test components.

## 🛠️ Technologies

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* Chrome / ChromeDriver

## 📁 Project Structure

```text
QAroad/
│
├── Components/
│   └── Reusable test components and common UI interactions
│
├── Data/
│   └── Test data and test input files
│
├── Helpers/
│   └── Utility functions and helper classes
│
├── PageObjects/
│   └── Page Object classes and page-specific interactions
│
├── Screenshots/
│   └── Screenshots captured during test execution
│
├── TestScripts/
│   └── Automated test cases
│
├── reports/
│   └── Test execution reports
│
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

### Components

Contains reusable components and common interactions that can be shared between different tests.

### Data

Contains test data required by the automated test cases.

### Helpers

Contains utility functions and helper classes used throughout the framework.

### PageObjects

Contains the application's Page Object classes.

Each page object is responsible for interacting with a specific page or section of the application.

### TestScripts

Contains the actual automated test cases.

### Screenshots

Stores screenshots generated during test execution, especially when they are required for debugging or test evidence.

### reports

Contains generated test execution reports.

---

# 🚀 Getting Started

## Prerequisites

Before setting up the project, make sure you have the following installed:

* Python 3.x
* Git
* Google Chrome
* ChromeDriver compatible with your Chrome version

## 1. Clone the Repository

Clone the repository using Git:

```bash
git clone https://github.com/masoudrze/QAroad.git
```

Navigate to the project directory:

```bash
cd QAroad
```

## 2. Create a Virtual Environment

Create a dedicated Python virtual environment for the project:

```bash
python -m venv .QAvenv
```

## 3. Activate the Virtual Environment

On Windows:

```bash
.QAvenv\Scripts\activate
```

After activation, the terminal should show the virtual environment name:

```text
(.QAvenv)
```

## 4. Install Dependencies

Install all required Python packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 5. Configure the Test Environment

Create a local `.env` file from the committed template:

```powershell
Copy-Item .env.example .env
```

Set the URL and test-account credentials in `.env`. The file also controls browser execution:

```env
BROWSER=chrome
HEADLESS=false
WINDOW_WIDTH=1920
WINDOW_HEIGHT=1080
```

Supported values for `BROWSER` are `chrome` and `firefox`. Set `HEADLESS=true` to run without a visible browser window. This is useful for CI environments.

---

# 🌐 WebDriver Setup

The framework uses Selenium Manager to discover or download a compatible browser driver when possible. If that is unavailable in your environment, set an explicit ChromeDriver path in `.env`:

```env
CHROMEDRIVER_PATH=chromedriver.exe
```

For Firefox, make sure Firefox and GeckoDriver are available on the system path.

---

# 🧪 Running Tests

Make sure the virtual environment is activated before running the tests:

```bash
.QAvenv\Scripts\activate
```

Run all tests with:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest TestScripts/Test_LoginClass.py -v
```

Run a specific test:

```bash
pytest TestScripts/Test_LoginClass.py::test_valid_admin_login -v
```

Run the smoke suite in headless mode by setting `HEADLESS=true` in `.env`:

```bash
pytest -m smoke -v
```

The project's `pytest.ini` file contains the Pytest configuration used by the framework.

---

# 📊 Test Reports

Test execution results are stored in the:

```text
reports/
```

directory.

Screenshots generated during test execution are stored in:

```text
Screenshots/
```

These artifacts can be useful when investigating failed test cases and debugging automation issues.

---

# 🏗️ Framework Architecture

The framework follows a structured automation architecture based on the **Page Object Model**.

The general flow is:

```text
TestScripts
     │
     ▼
PageObjects
     │
     ▼
Components / Helpers
     │
     ▼
Selenium WebDriver
     │
     ▼
Web Application
```

This separation helps keep test cases focused on **test scenarios and expected behavior**, while page-specific UI interactions remain inside the Page Object classes.

---

# 🔄 Typical Workflow

A typical test development workflow is:

```text
1. Add or update test data
        ↓
2. Create/update Page Object
        ↓
3. Add reusable component/helper if required
        ↓
4. Create test case in TestScripts
        ↓
5. Run the test with Pytest
        ↓
6. Review screenshots and reports
        ↓
7. Fix failures and improve the test
```

---

# 📦 Dependencies

Project dependencies are defined in:

```text
requirements.txt
```

To install all dependencies:

```bash
pip install -r requirements.txt
```

If dependencies are updated during development, update the requirements file:

```bash
pip freeze > requirements.txt
```

---

# ⚠️ Notes

* Do not commit the `.QAvenv` virtual environment to Git.
* Make sure `.QAvenv/` is included in `.gitignore`.
* Do not commit passwords, credentials, API keys, or other sensitive information.
* Keep Chrome and ChromeDriver versions compatible.
* Generated screenshots and reports should be managed according to the project's `.gitignore` configuration.

---

# 👤 Author

**Masoud Rze**

GitHub:
[masoudrze](https://github.com/masoudrze?utm_source=chatgpt.com)

---

## 📄 License

This project currently does not specify a license.

If this repository is intended to be publicly reused or distributed, consider adding an appropriate open-source license.
