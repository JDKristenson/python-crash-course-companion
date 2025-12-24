# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Offline learning companion for "Python Crash Course, Third Edition" by Eric Matthes. Self-contained educational environment with all packages pre-installed for learning without internet access.

## Common Commands

```bash
# Environment
source activate_env.sh          # Activate virtual environment
source venv/bin/activate        # Manual activation
python verify_setup.py          # Verify environment is ready
deactivate                      # Exit virtual environment

# Running code
python path/to/file.py          # Run any Python file
python quick_test.py            # Sandbox for experiments
python                          # Interactive REPL

# Testing (Chapter 11+)
pytest test_file.py             # Run tests
pytest -v test_file.py          # Verbose output
pytest test_file.py::test_name  # Run specific test

# Django (Chapters 18-20)
python manage.py runserver      # Start dev server
python manage.py migrate        # Run migrations
python manage.py createsuperuser
python manage.py startapp app_name

# Pygame (Chapters 12-14)
python game_file.py             # Run directly
```

## Architecture

### Directory Structure

- **`my_work/`** - Student workspace (all student code goes here)
  - `part_1_basics/chapters/chapter_XX/` - Chapters 1-11
  - `part_2_projects/chapters/chapter_XX/` - Chapters 12-20

- **`book_resources/`** - Author's official code (read-only reference)
  - Contains solutions and examples for all chapters

- **`exercises/`** - Exercise guides with instructions
  - Start with `CHAPTERS_OVERVIEW.md`

- **`quick_reference/`** - Cheat sheets (`python_basics_cheatsheet.md`)

### Helper Scripts

- `activate_env.sh` - Environment activation with helpful output
- `verify_setup.py` - Checks Python version, packages, directory structure
- `quick_test.py` - Sandbox with exception handling for quick experiments

### Installed Packages

Pre-installed in venv for offline use:
- pygame (2.6.1) - Game development
- matplotlib (3.10.7) - Data visualization
- plotly (6.4.0) - Interactive charts
- Django (5.2.8) - Web framework
- requests (2.32.5) - HTTP library
- beautifulsoup4 (4.14.2) - HTML parsing
- pytest (8.4.2) - Testing framework

## Educational Context

Assume the user is a beginner learning Python. When assisting:

- Place new exercise files in `my_work/part_X/chapters/chapter_XX/`
- File naming: `exercise_X_Y_descriptive_name.py`
- Reference `book_resources/` solutions when comparing or debugging
- Check virtual environment is active (look for `(venv)` prompt)
- Common beginner issues: indentation, missing colons, unmatched quotes

## Book Structure

**Part I (Chapters 1-11):** Fundamentals
- Variables, strings, numbers
- Lists, dictionaries, tuples
- Loops, conditionals, functions
- Classes, files, exceptions, testing

**Part II (Chapters 12-20):** Three projects
- Alien Invasion game (12-14): Pygame
- Data Visualization (15-17): matplotlib, plotly, APIs
- Learning Log web app (18-20): Django
