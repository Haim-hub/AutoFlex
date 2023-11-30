from git import Repo
import os

# Path to your repository
repo = Repo(os.getcwd())

#Get The Date
date = repo.git.log('-1', '--format=%cd')


# Change File
with open('main.txt', 'a') as f:
    f.write('Hello World! \n')
    f.write('Today is ' + date + 'add I have made a contribution')


# Add all changes
repo.git.add(A=True)

# Commit
repo.index.commit(date + 'contribution')

# Push
origin = repo.remote(name='origin')
origin.push()
