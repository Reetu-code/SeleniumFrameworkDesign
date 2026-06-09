@echo off
echo Pushing code to GitHub...

REM Add all changes
git add .

REM Check if there are changes to commit
git diff --cached --quiet
if %errorlevel% neq 0 (
    REM Commit with timestamp
    git commit -m "Auto-commit: %date% %time%"
    echo Changes committed successfully
) else (
    echo No changes to commit
)

REM Push to GitHub
git push origin master
if %errorlevel% equ 0 (
    echo Code pushed to GitHub successfully!
) else (
    echo Failed to push to GitHub
)

pause
