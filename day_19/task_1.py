import subprocess

PROJECT_PATH = r"C:\Users\Hanith Salian\OneDrive\Documents\GitHub\DS_AI_Internship"

def run_git(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True,
            cwd=PROJECT_PATH   # 👈 VERY IMPORTANT
        )
        print(f"Success: {command}")
        if result.stdout:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Note/Error on '{command}': {e.stderr.strip()}")

run_git("git init")
run_git("git add .")
run_git('git commit -m "Initial commit"')

run_git("git checkout -b feature-viz")
run_git('echo # New Plot File > plots.py')
run_git("git add plots.py")
run_git('git commit -m "Add experimental visualization script"')

run_git("git checkout main")
run_git("git checkout feature-viz")