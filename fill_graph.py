import os, random
from datetime import datetime, timedelta

# 90 dino ke purane commits
for i in range(90):
    if random.random() < 0.4: continue
    date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d 12:00:00")
    with open("contribution.txt", "a") as f: f.write(f"Refactor: {date}\n")
    os.system('git add .')
    os.system(f'GIT_AUTHOR_DATE="{date}" GIT_COMMITTER_DATE="{date}" git commit -m "update"')

os.system('git push')