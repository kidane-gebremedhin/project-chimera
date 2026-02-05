#!/bin/bash
set -e

BRANCH="cursor-autogen"
MESSAGE="chore(cursor): auto-commit generated changes"

# Ensure branch exists
git checkout -B $BRANCH

# Only commit if there are changes
if [[ -n $(git status --porcelain) ]]; then
  git add .
  git commit -m "$MESSAGE"
  git push -u origin $BRANCH
else
  echo "No changes to commit"
fi
