import random
from git import Repo
import os

# Path to your repository
repo = Repo(os.getcwd())

#Get The Date
date = repo.git.log('-1', '--format=%cd', '--date=format:%Y-%m-%d') 

# Git pull
origin = repo.remote(name='origin')
origin.pull()

# Get Random Number for the day
rd = random.randint(1, 10)

for i in range(rd):
    number = 0
    file_path = 'main.txt'
    # Read file
    with open(file_path, 'r') as f:
        lines = f.readlines()
        last_line = lines[-1]
        last_word = last_line.split()[-1]
        try:
            number = int(last_word)
            # Use 'number' in your script
        except ValueError:
            print(f"The last word '{last_word}' is not a number.")

    # Clear file
    with open(file_path, 'w') as file:
        # Write new content to the file
        file.write("")

    # Change File
    with open(file_path, 'a') as f:
        f.write('Hello World! \n')
        f.write('Today is ' + date + 'add I have made a contribution \n')
        f.write('Total number of automatic contributions is: ' + str(number + 1))


    # Add all changes
    repo.git.add(A=True)

    # Commit
    repo.index.commit(date + ' contribution')

    # Push
    origin = repo.remote(name='origin')
    origin.push()
