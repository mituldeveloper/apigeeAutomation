#!/bin/bash
git status
git add .
echo "Enter the commit message"
read commit
git commit -m "$commit"
git push
pause