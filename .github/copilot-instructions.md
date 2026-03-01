## Purpose
Short, actionable guidance for AI coding agents working on this repository.

## Repo snapshot
- Single top-level script: `new.py` (root).
- No tests, packages, or build system detected.

## How this project runs (developer workflows)
- Run locally (PowerShell):
  - `python new.py`  # or `py -3 new.py` if multiple Python installs
- The script is interactive: it prints the first two Fibonacci numbers and then waits for an integer from stdin.
  - Key lines in `new.py`:
    - `a,b=0,1`
    - `print('the fiboacci series are :',a,b)`  # note the exact output string (typo "fiboacci")
    - `n=int(input())`  # reads an integer; current code does not use `n`

## What to expect when changing code
- Preserve the script's interactive I/O semantics when making small edits. Many automated runs will call `python new.py` and expect a prompt/read behavior.
- If you convert the script into functions for testing, keep a thin CLI wrapper that preserves the same stdout lines and input prompt text unless intentionally changing behavior.

## Project-specific patterns and conventions
- Very small, single-file codebase. Expect any change to affect the entire project behavior. There are no modules, packages, or CI configs to follow.
- There is an explicit stdout string that external scripts or graders may match: `the fiboacci series are :` (includes a trailing space and the misspelling). Do not change this text without verifying downstream consumers.

## Integration points & dependencies
- No external dependencies detected. Use standard CPython (3.7+) to run.

## Examples for AI edits
- Safe small change (preserve behavior): wrap interactive logic in a main guard but keep identical prints and input:
  - update `new.py` to call a `main()` from `if __name__ == '__main__':` while keeping the printed string and input call unchanged.
- If adding tests: provide a non-interactive entrypoint (e.g., `def run(n):`) and a small CLI wrapper that still calls `input()` so normal `python new.py` runs unchanged.

## When to ask for human guidance
- If you plan to change any user-visible text (print/input) or transform the script into a package/module structure, confirm intended downstream consumers (grading scripts, CI, or instructors).

## Quick checklist for PRs
- Verify `python new.py` still runs and accepts an integer from stdin.
- Keep or explicitly update the exact printed string if external matchers exist.
- Add a short note in the PR description if you change the CLI behaviour or the interactive prompt.

If any of the repository's scope expands (new files, tests, CI), update this document to list new entrypoints and commands.
