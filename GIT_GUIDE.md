# Git & GitHub Guide — Pushing BrainWave AI to Your Portfolio

This guide assumes **zero prior Git experience**. Follow it top to bottom.

---

## 1. What is Git vs. GitHub?

- **Git** is a *version control system* — software installed on your computer that tracks changes to your files over time, letting you save "snapshots" (commits) and go back to any previous snapshot.
- **GitHub** is a *website/cloud service* that hosts your Git repositories online, so others (like recruiters) can view your code, and so you have a backup off your own machine.

Think of Git as "Save Game" checkpoints, and GitHub as the cloud server where those checkpoints are backed up and shown off.

---

## 2. Installing Git

- **Windows:** Download from https://git-scm.com/downloads and run the installer (defaults are fine).
- **macOS:** Run `git --version` in Terminal — macOS will prompt you to install Developer Tools if needed.
- **Linux:** `sudo apt install git` (Debian/Ubuntu) or your distro's package manager.

Verify installation:
```bash
git --version
```

---

## 3. One-Time Git Configuration

Tell Git who you are (this gets attached to every commit you make):
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 4. Initializing the Repository

Navigate to your project folder and turn it into a Git repository:
```bash
cd BrainWave-AI-EEG-Classification
git init
```
`git init` creates a hidden `.git/` folder — this is where Git stores all your history. You won't need to touch it directly.

---

## 5. Understanding the Git Workflow (3 Stages)

```
Working Directory  --->  Staging Area  --->  Repository (committed history)
   (your files)          (git add)              (git commit)
```

- **Working Directory:** the actual files on your disk, as you're editing them.
- **Staging Area:** a "waiting room" for changes you're about to save. You choose exactly what goes into the next commit.
- **Repository:** the permanent, saved history of commits.

---

## 6. Core Git Commands Explained

| Command | What it does |
|---|---|
| `git status` | Shows which files are changed, staged, or untracked. Run this often! |
| `git add <file>` | Moves a specific file into the staging area. |
| `git add .` | Stages ALL changed files in the current folder. |
| `git commit -m "message"` | Saves a permanent snapshot of everything staged, with a description. |
| `git log` | Shows the history of all commits. |
| `git branch` | Lists branches / creates a new one. |
| `git checkout -b <branch-name>` | Creates AND switches to a new branch. |
| `git push` | Uploads your local commits to GitHub. |
| `git pull` | Downloads new commits from GitHub into your local copy. |
| `git clone <url>` | Downloads an entire existing repository from GitHub. |

---

## 7. Making Your First Commit

```bash
# Check what Git sees as changed/untracked
git status

# Stage everything (respecting .gitignore rules)
git add .

# Commit with a clear, descriptive message
git commit -m "Initial commit: BrainWave AI EEG classification pipeline"
```

**Good commit message habits:**
- Use present tense: "Add feature engineering module" not "Added..."
- Keep the first line under ~50 characters; add detail below if needed.
- One logical change per commit (don't cram unrelated changes together).

---

## 8. Creating the GitHub Repository

1. Go to https://github.com and log in (create a free account if needed).
2. Click the **+** icon (top right) → **New repository**.
3. Name it exactly: `BrainWave-AI-EEG-Classification`
4. Add a short description (e.g., "EEG signal classification for BCI using classical ML").
5. Choose **Public** (so it's visible in your portfolio).
6. **Do NOT** initialize with a README, .gitignore, or license — we already have those locally, and adding them on GitHub too will cause a conflict.
7. Click **Create repository**. GitHub will show you a page with commands — we'll use the "push an existing repository" section below.

---

## 9. Connecting Your Local Repo to GitHub & Pushing

```bash
# Link your local repo to the GitHub repo you just created
git remote add origin https://github.com/<your-username>/BrainWave-AI-EEG-Classification.git

# Rename your default branch to "main" (modern GitHub convention)
git branch -M main

# Push your commits up to GitHub for the first time
git push -u origin main
```

`-u origin main` sets `origin/main` as the default upstream branch, so future pushes can simply be `git push`.

After this, refresh your GitHub repository page — your entire project should now be visible online!

---

## 10. Branching (For Future Feature Work)

**Why branch?** A branch is an independent line of development. Instead of editing `main` directly (which should always stay stable/working), you create a branch for new work, and only merge it back once it's tested.

```bash
# Create and switch to a new branch for a new feature
git checkout -b feature/add-deep-learning-model

# ... make your changes, then stage and commit as usual ...
git add .
git commit -m "Add CNN-based model for Version 2"

# Push this branch to GitHub
git push -u origin feature/add-deep-learning-model
```

On GitHub, you can then open a **Pull Request** to merge this branch into `main` — this is standard practice in professional software teams and shows interviewers you understand collaborative workflows.

---

## 11. Everyday Workflow Going Forward

Whenever you make changes to the project:

```bash
git status                      # see what changed
git add .                       # stage changes
git commit -m "describe change" # save a snapshot
git push                        # upload to GitHub
```

---

## 12. Quick Troubleshooting

| Problem | Fix |
|---|---|
| `fatal: not a git repository` | Run `git init` first, or `cd` into the correct folder. |
| Large file rejected by GitHub | Make sure large datasets are listed in `.gitignore` (they already are here). |
| Merge conflicts | Happens when the same lines were changed in two places. Git will mark the conflicting section in the file — edit it manually to resolve, then `git add` and `git commit`. |
| Forgot to `.gitignore` something already committed | Run `git rm --cached <file>`, add it to `.gitignore`, then commit again. |

---

You're now ready to maintain this project like a professional software engineer. 🎉
