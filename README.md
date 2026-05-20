# github-flow-lab

A deliberately tiny Python project. Its only purpose is to give you something real to commit, branch, conflict, review, and release while practicing GitHub Flow.

The "feature" is a calculator module with a CLI. Exercises will have you add operations, introduce bugs, fix bugs, and conflict on the same lines.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
python -m calculator 2 + 3
```

## Project layout

```
sample-repo/
├── pyproject.toml
├── src/calculator/
│   ├── __init__.py
│   ├── __main__.py        # `python -m calculator` entry point
│   └── operations.py      # add / sub / mul / div — where most edits happen
├── tests/
│   └── test_operations.py
├── .github/
│   ├── workflows/ci.yml   # lint + test on every PR
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── ISSUE_TEMPLATE/
├── CODEOWNERS             # auto-request reviews
├── CHANGELOG.md
└── .gitignore
```

## Pushing this as the maintainer's upstream

Once setup Phase 0 is done:

```bash
cd "/Users/tktucker/sandbox/Testing/Github Flow/sample-repo"
git init -b main
git add .
git commit -m "Initial commit: calculator scaffold"

# Create the empty repo on GitHub as tktucker first (UI or `gh repo create`)
git remote add origin git@github-tktucker:tktucker/github-flow-lab.git
git push -u origin main
```

That repo becomes the **upstream** for every exercise. `tktuckerphotos` forks it.
## For contributors
See the lab's `exercises/` directory for the full Github Flow walkthrough.
