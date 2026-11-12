# WARP.md

Guidance for WARP when working in this repository.

## Purpose and present scope

This is a partial learning companion to _Python Crash Course, Third Edition_ by Eric Matthes, not a self-contained offline environment. See [README.md](README.md) for the authoritative fresh-clone inventory, inferred setup commands, provenance and license-status notes.

Present: chapter index, chapter 1 and 2 guides, Python cheat sheet, activation helper, legacy diagnostic, empty experiment sandbox and dependency pins. Absent: tracked personal exercises, a preinstalled environment, finished game/visualization/Django projects, or an application build configuration.

`book_resources` is a gitlink whose origin is unresolved: no `.gitmodules` URL is tracked. Do not call its unseen contents official, complete or licensed for reuse. Do not guess an upstream URL. `my_work/` is a future local workspace and `venv/` is an ignored local environment, not included packages.

## Suggested local workflow

1. Read the relevant book chapter and one of the existing guides where available.
2. Create a local virtual environment if needed; README documents Bash and PowerShell activation.
3. Create your own exercise files under `my_work/part_1_basics/chapters/chapter_XX/` or `my_work/part_2_projects/chapters/chapter_XX/`.
4. Run the files and tests you wrote. Compare with book resources only after their origin and terms are verified.

Examples, not installation or execution evidence:

```bash
python3 -m venv venv
source venv/bin/activate
# Or source activate_env.sh after venv exists
# Optional for later exercises; normally requires network:
python -m pip install -r requirements.txt
python quick_test.py
python verify_setup.py
```

`quick_test.py` currently runs an empty `pass` body. `verify_setup.py` ignores package-check return values, checks only directory existence, has an outdated version predicate and does not signal failure through process status. Its success output is not proof of readiness. Python 3.7 is not established as compatible with the pins. Installation and offline use require separate verification.

Once real exercise files/tests exist, use `python path/to/your_file.py` or `python -m pytest path/to/your_test_file.py` with pytest installed. Do not offer a repository server, migrations, game entry point or deployment command: none is implemented here.

## Educational and contribution conventions

- Explain concepts for beginners; encourage typing and experimenting with personal code.
- Use four-space indentation, descriptive lowercase filenames and standard Python style.
- Keep book-derived material, upstream reference and personal contributions distinct.
- Preserve Eric Matthes's book credit, recorded JDKristenson history and Warp co-author attribution. The existence of a tool guidance file is not evidence of that tool's authorship.
- Disclose new AI assistance without asserting ownership of older material.
- No blanket repository license is established. Keep license-status language factual and avoid copying additional book prompts without verified permission.
- Keep credentials, personal notes and local account details out of shared material.
