import os, random
from datetime import datetime, timedelta

for i in range(90):
    if random.random() < 0.4: continue
    
    # Date format
    date_str = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d 12:00:00")
    
    # File mein update
    with open("contribution.txt", "a") as f: 
        f.write(f"Refactor: {date_str}\n")
    
    # Windows ke liye command (env variable set karne ki zaroorat nahi)
    os.system('git add .')
    # Windows par date set karne ka tarika
    os.system(f'git commit --date="{date_str}" -m "chore: code cleanup {date_str}"')

# Push final changes
os.system('git push')
print("Automation complete!")