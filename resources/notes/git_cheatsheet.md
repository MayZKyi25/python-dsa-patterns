# Git Cheat Sheet 

https://medium.com/double-pointer/essential-git-cheatsheet-a-developers-companion-5dd8dc480a9f


Beginner-friendly Git commands for your coding practice repo.

---

## 1. Check where you are

```bash
pwd
# Shows your current folder path
# Example: /Users/may/Desktop/Practice Coding
```

```bash
ls
# Lists files and folders in the current directory
```

---

## 2. Start Git in a folder

```bash
git init
# Turns the current folder into a Git repository
# Creates a hidden .git folder
# You only do this once per project
```

---

## 3. Check Git status

```bash
git status
# Shows which files are changed, new, staged, or committed
# Use this command often
```

Common status meanings:

```text
Untracked files
# New files Git sees, but Git is not tracking yet

Changes not staged for commit
# Files changed, but not added to the next commit yet

Changes to be committed
# Files are staged and ready to commit

nothing to commit, working tree clean
# Everything is saved in Git
```

---

## 4. Add files to staging

```bash
git add .
# Adds all changed and new files to staging
# Staging means: "I want these changes included in my next commit"
```

```bash
git add README.md
# Adds only README.md
```

```bash
git add dsa/arrays_hashing/0001_two_sum.py
# Adds one specific file
```

---

## 5. Commit changes

```bash
git commit -m "Add two sum solution"
# Saves a snapshot of your staged changes
# The message should explain what changed
```

Good commit messages:

```text
Add Python count words practice
Add Two Sum solution
Organize DSA folder structure
Update README with LeetCode section
Add ML interview notes
```

Bad commit messages:

```text
update
stuff
fix
asdf
```

---

## 6. Connect local repo to GitHub

```bash
git remote add origin https://github.com/USERNAME/REPO-NAME.git
# Connects your local project to a GitHub repository
# You usually do this once
```

Example:

```bash
git remote add origin https://github.com/MayZKyi25/practice-coding.git
```

Check your remote:

```bash
git remote -v
# Shows which GitHub repo your local project is connected to
```

If remote already exists:

```bash
git remote set-url origin https://github.com/USERNAME/REPO-NAME.git
# Changes the GitHub repo URL
```

---

## 7. Rename branch to main

```bash
git branch -M main
# Renames your current branch to main
# GitHub commonly uses main as the default branch
```

---

## 8. Push code to GitHub

```bash
git push -u origin main
# Uploads your local commits to GitHub
# -u remembers origin main for next time
```

After the first push, you can usually use:

```bash
git push
# Pushes new commits to GitHub
```

---

## 9. Daily workflow

Use this every time you make changes:

```bash
git status
# Check what changed
```

```bash
git add .
# Stage all changes
```

```bash
git commit -m "Write a clear message"
# Save the changes locally
```

```bash
git push
# Upload changes to GitHub
```

Full example:

```bash
git status
git add .
git commit -m "Add count words practice"
git push
```

---

## 10. See commit history

```bash
git log
# Shows past commits
```

```bash
git log --oneline
# Shows shorter commit history
```

Example output:

```text
a1b2c3d Add count words practice
e4f5g6h Update README
```

---

## 11. See what changed

```bash
git diff
# Shows changes that are not staged yet
```

```bash
git diff --staged
# Shows changes that are staged and ready to commit
```

---

## 12. Undo staging

```bash
git restore --staged README.md
# Removes README.md from staging
# Does NOT delete your actual changes
```

```bash
git restore --staged .
# Removes all files from staging
# Does NOT delete your actual changes
```

---

## 13. Undo local file changes

Be careful with this.

```bash
git restore README.md
# Cancels your local changes to README.md
# Goes back to the last committed version
```

```bash
git restore .
# Cancels all local changes
# Be careful: this can remove work you have not committed
```

---

## 14. Delete files with Git

```bash
git rm old_file.py
# Deletes the file and stages the deletion
```

Then commit:

```bash
git commit -m "Remove old file"
```

---

## 15. Move or rename files with Git

```bash
git mv old_name.py new_name.py
# Renames or moves a file
```

Example:

```bash
git mv Python_review python_review
# Rename folder using Git
```

Then commit:

```bash
git commit -m "Rename Python review folder"
```

---

## 16. Pull latest changes from GitHub

```bash
git pull
# Downloads latest changes from GitHub into your local repo
```

Use this if you changed something on GitHub directly.

---

## 17. Clone a repo

```bash
git clone https://github.com/USERNAME/REPO-NAME.git
# Downloads a GitHub repo to your computer
```

Example:

```bash
git clone https://github.com/MayZKyi25/practice-coding.git
```

---

## 18. Branch basics

```bash
git branch
# Shows your branches
```

```bash
git checkout -b new-branch-name
# Creates and switches to a new branch
```

Example:

```bash
git checkout -b add-two-sum
```

```bash
git checkout main
# Switches back to main branch
```

Newer Git command:

```bash
git switch main
# Also switches to main branch
```

---

## 19. Merge a branch

```bash
git checkout main
# Go to main branch first
```

```bash
git merge add-two-sum
# Merges changes from add-two-sum into main
```

---

## 20. Delete a branch

```bash
git branch -d add-two-sum
# Deletes the branch locally after merging
```

---

## 21. Good .gitignore for Python

Create a file called `.gitignore` and add:

```text
__pycache__/
*.py[cod]
.venv/
venv/
.env
.DS_Store
.vscode/
.ipynb_checkpoints/
```

Meaning:

```text
__pycache__/
# Python auto-generated files

.venv/ or venv/
# Virtual environment folder

.env
# Secret environment variables

.DS_Store
# Mac system file

.vscode/
# VS Code settings
```

---

## 22. Recommended workflow for your practice-coding repo

When you finish one practice problem:

```bash
git status
git add dsa/arrays_hashing/0001_two_sum.py
git commit -m "Add LeetCode 1 Two Sum solution"
git push
```

When you update notes:

```bash
git status
git add notes/mistakes_log.md
git commit -m "Update mistakes log"
git push
```

When you organize folders:

```bash
git status
git add .
git commit -m "Organize Python DSA and ML interview folders"
git push
```

---

## 23. Most important commands to memorize first

```bash
git status
# Check what is happening
```

```bash
git add .
# Stage all changes
```

```bash
git commit -m "message"
# Save changes locally
```

```bash
git push
# Upload to GitHub
```

```bash
git pull
# Download latest changes from GitHub
```

---

## 24. Simple mental model

```text
Working folder
# Your actual files on your computer

Staging area
# Files you selected for the next save

Commit
# Saved snapshot of your work

GitHub
# Online backup / portfolio
```

Flow:

```text
edit files -> git add -> git commit -> git push
```

---

## 25. Emergency commands

Check current status:

```bash
git status
```

See remote GitHub link:

```bash
git remote -v
```

See recent commits:

```bash
git log --oneline
```

Cancel staged files:

```bash
git restore --staged .
```

Stop tracking a file but keep it on your computer:

```bash
git rm --cached filename
```

Example:

```bash
git rm --cached .env
# Good for accidentally staged secret files
```

---

## 26. Common beginner mistakes

### Mistake 1: Using mkdir to create a Python file

Wrong:

```bash
mkdir 0001_two_sum.py
# This creates a folder, not a file
```

Correct:

```bash
touch 0001_two_sum.py
# This creates a file
```

### Mistake 2: Forgetting to commit before pushing

Wrong:

```bash
git add .
git push
# Nothing may push if you did not commit
```

Correct:

```bash
git add .
git commit -m "Add new practice problem"
git push
```

### Mistake 3: Being in the wrong folder

Check first:

```bash
pwd
# Make sure you are inside your project folder
```

---

## 27. For your current repo

Your normal command sequence should be:

```bash
cd "/Users/may/Desktop/Practice Coding"
git status
git add .
git commit -m "Update practice coding repo"
git push
```

Remember:

```text
Do not worry about being perfect.
Commit small progress often.
GitHub is your learning journal and portfolio.
```
