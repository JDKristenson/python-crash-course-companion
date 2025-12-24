# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is an offline learning companion for "Python Crash Course, Third Edition" by Eric Matthes. It's a self-contained educational environment designed for learners working through the book without internet access. The repository contains:
- Official book resources (example code, solutions)
- Structured workspace for student exercises
- Exercise guides with detailed instructions
- Helper scripts for environment management and testing
- All required Python packages pre-installed

## Common Development Commands

### Environment Management
```bash
# Activate the virtual environment
source activate_env.sh

# Or manually activate
source venv/bin/activate

# Verify setup is complete
python verify_setup.py

# Deactivate environment
deactivate
```

### Running Code
```bash
# Run any Python file directly
python path/to/file.py

# Quick test sandbox (for experimenting)
python quick_test.py

# Interactive Python REPL
python
```

### Testing
```bash
# Run pytest tests (used from Chapter 11 onwards)
pytest test_file.py

# Run tests with verbose output
pytest -v test_file.py

# Run specific test function
pytest test_file.py::test_function_name
```

### Django Commands (Chapters 18-20)
```bash
# Start Django development server
python manage.py runserver

# Run Django migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Create new Django app
python manage.py startapp app_name
```

### Pygame Commands (Chapters 12-14)
```bash
# Run Pygame projects directly
python game_file.py
```

## Repository Structure

### Key Directories
- **`my_work/`** - Student workspace, organized by book parts (part_1_basics, part_2_projects)
  - Create all your code here in the appropriate chapter subdirectories
  - Structure: `my_work/part_X/chapters/chapter_XX/`
  
- **`book_resources/`** - Official code examples from the book (read-only reference)
  - Organized by chapter (chapter_01/ through chapter_20+)
  - Contains author's solutions and example code
  
- **`exercises/`** - Detailed exercise guides for each chapter
  - Start here: `CHAPTERS_OVERVIEW.md` provides a complete chapter index
  - Each guide includes: learning objectives, key concepts, exercises, quick reference, common mistakes
  
- **`quick_reference/`** - Cheat sheets and quick syntax guides
  
- **`venv/`** - Python virtual environment with all dependencies

### Important Files
- **`activate_env.sh`** - Quick environment activation script
- **`verify_setup.py`** - Validates that environment is ready for offline use
- **`quick_test.py`** - Sandbox for quick code experiments
- **`requirements.txt`** - All installed packages for the learning path

## Architecture and Design Principles

### Learning-Focused Structure
This repository follows the book's two-part structure:
1. **Part I (Chapters 1-11)**: Fundamentals - variables, data structures, functions, classes, files, testing
2. **Part II (Chapters 12-20)**: Three major projects:
   - Alien Invasion game (Pygame)
   - Data Visualization (matplotlib, plotly)
   - Web Application (Django)

### Workspace Organization
- Students work in `my_work/` - never modify `book_resources/`
- Each chapter has a dedicated directory for exercises
- Naming convention for exercise files: `exercise_X_Y_descriptive_name.py`

### Helper Scripts Philosophy
- All scripts include error handling and clear user feedback
- Scripts print formatted output with emojis (✅ ❌) for visual clarity
- `verify_setup.py` checks Python version, packages, and directory structure
- `quick_test.py` provides a safe sandbox with exception handling

## Installed Packages and Usage

All packages are pre-installed in the virtual environment:
- **pygame** (2.6.1) - Game development framework
- **matplotlib** (3.10.7) - Data visualization and plotting
- **plotly** (6.4.0) - Interactive visualizations
- **Django** (5.2.8) - Web framework
- **requests** (2.32.5) - HTTP library for API calls
- **beautifulsoup4** (4.14.2) - HTML/XML parsing
- **pytest** (8.4.2) - Testing framework

## Working with Student Code

### When Creating New Files
- Place student exercises in appropriate `my_work/part_X/chapters/chapter_XX/` directories
- Use descriptive filenames that include exercise numbers
- Follow Python naming conventions (lowercase with underscores)

### When Debugging Student Code
- Check that virtual environment is activated (look for `(venv)` in prompt)
- Common beginner issues: indentation, missing colons, unmatched quotes/parentheses
- Direct students to compare with `book_resources/` solutions when stuck
- Use `quick_test.py` for isolated testing of problematic code

### When Working with Projects
- **Game project** (ch 12-14): Files go in `my_work/part_2_projects/chapters/chapter_12/`
- **Data viz** (ch 15-17): Use matplotlib/plotly from `my_work/part_2_projects/chapters/chapter_15/`
- **Django project** (ch 18-20): Create Django project in `my_work/part_2_projects/chapters/chapter_18/`

## Code Style Guidelines

This repository follows standard Python conventions appropriate for beginners:
- 4 spaces for indentation (never tabs)
- Descriptive variable names (student-friendly)
- Comments explaining what code does (educational context)
- Docstrings for functions and modules
- Follow PEP 8 where appropriate for learning level

## Educational Context

When assisting with code in this repository:
- Assume the user is a beginner learning Python
- Explain concepts clearly without jargon when possible
- Encourage typing code rather than copy-pasting (builds muscle memory)
- Reference specific chapter content when relevant
- Point to appropriate exercise guides in `exercises/` directory
- Suggest checking `book_resources/` for comparison with author's solutions

## Development Workflow

Typical learning workflow:
1. Read chapter in the book
2. Open corresponding exercise guide (`exercises/chapter_XX_name.md`)
3. Create Python files in `my_work/part_X/chapters/chapter_XX/`
4. Test code frequently with `python filename.py`
5. Use `quick_test.py` for quick experiments
6. Compare with solutions in `book_resources/` if needed
7. Move to next chapter when comfortable

## Environment Notes

- Virtual environment must be activated before running code
- All dependencies are pre-installed for offline use
- Python 3.7+ required (verified by `verify_setup.py`)
- No internet connection needed for learning
- Django development server runs on default port 8000
