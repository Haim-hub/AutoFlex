from git import Repo
import os

# Path to your repository
repo = Repo(os.getcwd())

#Get The Date
date = repo.git.log('-1', '--format=%cd', '--date=format:%Y-%m-%d')

number = 0
# Read file
with open('main.txt', 'r') as f:
    lines = f.readlines()
    last_line = lines[-1]
    number = int(last_line.split()[-1])

# Change File
with open('main.txt', 'a') as f:
    f.write('Hello World! \n')
    f.write('Today is ' + date + 'add I have made a contribution')
    f.write('Total number of automatic contributions is:' + str(number + 1))


# Add all changes
repo.git.add(A=True)

# Commit
repo.index.commit(date + 'contribution')

# Push
origin = repo.remote(name='origin')
origin.push()
