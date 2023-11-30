from git import Repo
import os

# Path to your repository
repo = Repo(os.getcwd())

# Add all changes
repo.git.add(A=True)

# Commit
repo.index.commit('Test Commit')

# Push
origin = repo.remote(name='origin')
origin.push()
