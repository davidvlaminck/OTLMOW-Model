# GitHub Actions Workflow Documentation

This folder contains all GitHub Actions workflows for this repository. Each workflow automates a specific part of the development, testing, or release process.

## Workflows

### 1. auto_update.yml
Automates the update of the class model. Runs daily on a schedule and on manual trigger.
- Checks out the repository
- Installs Python and dependencies
- Runs the automatic update script
- Commits and pushes changes

Note: the schedule is best-effort — GitHub's Actions queue can delay it by several hours. For guaranteed timing, run it manually with `gh workflow run auto_update.yml` or from the Actions tab.

### 2. coverage.yml
Generates a coverage report for the codebase on pushes and pull requests to `master`.
- Checks out the repository
- Installs Python and dependencies
- Runs tests with coverage
- Generates a coverage badge and HTML report
- Commits coverage results

### 3. release.yml
Handles package releases automatically after a successful update or when a tag is pushed.
- Checks out the repository
- Installs Python and build tools
- Builds the package
- Publishes to PyPI

### 4. quality.yml
Runs the quality gate on pushes to `master` and pull requests.
- Checks out the repository
- Installs Python 3.11 and project dependencies
- Runs tests with coverage
- Runs lint, format check, type check, security, and dead-code analysis
- Enforces quality gates (ratchet, security, dead-code) that can block a merge
- Excludes the generated model from checks
- Uploads a QA report artifact

### 5. unittest.yml
Runs the full test suite on multiple OSes and Python versions for every push.
- Checks out the repository
- Installs dependencies for each matrix combination
- Runs unittests and notebook tests

### 6. zip_source.yml
Creates a zip archive of the source code after a release or on demand.
- Checks out the repository
- Zips the source code
- Commits and pushes the zip file

---

For details on each workflow, see the corresponding `.yml` file in this folder.
