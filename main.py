import os
from datetime import datetime, timedelta

total_day = 466  # Total days back
commit_frequency = 10  # Commit times per day
repo_link = "https://github.com/anshc022/repo.git"
target_months = {1, 2}  # Specify months as integers (e.g., January = 1, February = 2)

# Set up initial values
tl = total_day
ctr = 1
now = datetime.now()
pointer = 0

# Create and configure the repository
os.system("git config user.name 'Your Name'")
os.system("git config user.email 'your_email@example.com'")
os.system("git init")

while tl > 0:
    ct = commit_frequency
    # Calculate the target date based on pointer offset
    target_date = now - timedelta(days=pointer)
    
    # Check if the target date's month matches the specified target months
    if target_date.month in target_months:
        while ct > 0:
            # Write to file to create a new commit
            with open("commit.txt", "a+") as f:
                format_date = target_date.strftime("%Y-%m-%d")
                f.write(f"Commit number {ctr}: {format_date}\n")
            
            # Stage and commit changes with the specific date
            os.system("git add .")
            os.system(f'git commit --date="{format_date} 12:15:10" -m "Commit number {ctr}"')
            print(f"Commit number {ctr}: {format_date}")
            ct -= 1
            ctr += 1

    # Move to the next day and decrement the total remaining days
    pointer += 1
    tl -= 1

# Push to remote repository
os.system(f"git remote add origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")
