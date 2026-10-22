#!/usr/bin/env python3
"""Clean a git repository and re-push it to GitHub.

Implements the 5 steps from git_clean_project.md Task #2:

  1. Delete the local ``.git/`` directory.
  2. Run ``git init`` in the target directory.
  3. Force push to the GitHub repo.
  4. (This file lives at ~/code/python_project/git_clean.py)
  5. Usage directions are in this docstring.

USAGE DIRECTIONS
----------------
- Assume the working directory IS the target repository.
- Run from inside the repo you want to clean::

      cd ~/code/some_repo
      python3 ~/code/python_project/git_clean.py

- The script operates on the current working directory. It does NOT take a
  path argument.
- Requirements:
    * The repo must already have an ``origin`` remote pointing at GitHub
      (the remote URL is captured BEFORE ``.git/`` is deleted, then
      re-added after ``git init``).
    * ``git`` must be installed and SSH/HTTPS auth to GitHub must work.
    * You must confirm the destructive step when prompted (or pass -y).

SAFETY
------
- Only ``.git/`` is removed. No source or other files are touched.
- A confirmation prompt guards the deletion unless ``-y`` is given.
- Repos with no ``origin`` remote are aborted before any deletion.

STEPS PERFORMED
---------------
1. Capture ``origin`` remote URL (abort if missing).
2. Delete ``.git/``.
3. ``git init``.
4. Re-add ``origin`` remote; create an initial commit (``git add -A`` +
   ``git commit --allow-empty``).
5. Force push the current branch to ``origin``.

NOT in scope (see git_clean_project.md open issues): creating remotes for
repos that have none, ``gh`` auth setup, branch protection, etc.
"""

import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd, cwd=None):
    """Run a command, printing it."""
    print("$ " + " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def main():
    target = Path.cwd()
    git_dir = target / ".git"

    print(f"Target repository: {target}")

    if not git_dir.exists():
        print("ERROR: no .git/ found in working directory. Aborting.")
        sys.exit(1)

    # Capture origin remote URL before deletion.
    try:
        remote_url = subprocess.check_output(
            ["git", "remote", "get-url", "origin"], cwd=target, text=True,
            stderr=subprocess.DEVNULL).strip()
    except subprocess.CalledProcessError:
        remote_url = ""
    if not remote_url:
        print("ERROR: no 'origin' remote found. Aborting before deletion "
              "(remote creation is out of scope for this script).")
        sys.exit(1)
    print(f"Captured origin: {remote_url}")

    # Confirmation (safety).
    if "-y" not in sys.argv and "--yes" not in sys.argv:
        answer = input("Delete .git/ and re-init + force push? [yes/NO]: ").strip()
        if answer.lower() not in ("yes", "y"):
            print("Aborted by user. No changes made.")
            sys.exit(0)

    # Step 1: delete .git/
    print("Step 1: deleting .git/ ...")
    if git_dir.is_dir() and not git_dir.is_symlink():
        shutil.rmtree(git_dir)
    else:
        git_dir.unlink()
    print(".git/ removed.")

    # Step 2: git init
    print("Step 2: git init ...")
    run(["git", "init"], cwd=target)

    # Restore origin remote (needed for step 3).
    run(["git", "remote", "add", "origin", remote_url], cwd=target)

    # Ensure a commit exists so we can push.
    run(["git", "add", "-A"], cwd=target)
    try:
        run(["git", "commit", "--allow-empty", "-m",
             "clean re-init via git_clean.py"], cwd=target)
    except subprocess.CalledProcessError:
        print("WARNING: commit failed; continuing to push.")

    # Determine current branch name.
    branch = subprocess.check_output(
        ["git", "branch", "--show-current"], cwd=target, text=True).strip()
    if not branch:
        branch = "main"
        run(["git", "branch", "-M", branch], cwd=target)

    # Step 3: force push
    print(f"Step 3: force push to origin/{branch} ...")
    run(["git", "push", "--force", "origin", branch], cwd=target)

    print("Done.")


if __name__ == "__main__":
    main()
