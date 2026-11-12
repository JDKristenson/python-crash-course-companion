# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Repository status

A partial companion to _Python Crash Course, Third Edition_ by Eric Matthes. Read [README.md](README.md) for the fresh-clone inventory, setup caveats and attribution. Only chapter 1 and 2 guides, a chapter index, a cheat sheet, helper scripts and dependency pins are present. There are no tracked student solutions or completed applications.

`venv/` is local and ignored; packages are not preinstalled. `my_work/` is a suggested future student workspace, not tracked content. `book_resources` is an unresolved gitlink with no tracked `.gitmodules` URL; do not describe it as bundled official code or fetch from a guessed origin.

## Working with student code

- Assume a beginner learner; explain concepts clearly and reference book chapters.
- Put new personal exercise files under `my_work/part_1_basics/chapters/chapter_XX/` or `my_work/part_2_projects/chapters/chapter_XX/` as appropriate.
- Use descriptive names such as `exercise_X_Y_descriptive_name.py`, four-space indentation and standard Python conventions.
- Keep personal solutions separate from book/upstream material. Preserve Eric Matthes's book credit, recorded human and Warp co-author credits, and disclose new AI assistance accurately.
- No repository-wide license grant is established; do not invent licensing, upstream provenance or authorship.

## Commands and boundaries

Commands are examples to run only when the relevant local files and environment exist:

```bash
python3 -m venv venv
source venv/bin/activate
# Optional dependencies for later work:
python -m pip install -r requirements.txt
python quick_test.py
python verify_setup.py
```

The sandbox body is currently `pass`. The legacy verifier is informational, not a pass/fail or offline-readiness gate; see README limitations. Dependency compatibility and installation are not verified by these instructions. Do not repeat its Python 3.7 claim as support for the pinned packages.

Run a personal exercise with `python path/to/your_file.py`; after creating actual tests and installing pytest, use `python -m pytest path/to/your_test_file.py`. There is no existing application build/start workflow. Django, Pygame and visualization projects are future book exercises, not present architecture. Do not suggest migrations, servers or deployment until such a project exists and the task authorizes it.
