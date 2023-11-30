#!/opt/homebrew/bin/pip3
import random
from git import Repo, GitCommandError
#
import requests

# def check_internet_connection(url='http://www.github.com', timeout=5):
#     try:
#         # Send a request to the specified URL
#         response = requests.get(url, timeout=timeout)
#         # If the request was successful, return True
#         return response.status_code == 200
#     except requests.ConnectionError:
#         # If a connection error occurs, return False
#         return False

if True:
    print("Internet connection is available.")

    try:
        print("Trying to push to GitHub...")
        # Path to your repository
        repo = Repo("/Users/niklashaim/Documents/GitHub_Flex/AutoFlex")

        #Get The Date
        date = repo.git.log('-1', '--format=%cd', '--date=format:%Y-%m-%d') 

        # Git pull
        origin = repo.remote(name='origin')
        origin.pull()

        # Get Random Number for the day
        rd = random.randint(1, 10)

        for i in range(rd):
            number = 0
            file_path = '/Users/niklashaim/Documents/GitHub_Flex/AutoFlex/main.txt'
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
                f.write('Today is ' + date + ' and I have made a contribution \n')
                f.write('Total number of automatic contributions is: ' + str(number + 1))


            # Add all changes
            repo.git.add(A=True)

            # Commit
            repo.index.commit(date + ' contribution')

            # Push
            origin = repo.remote(name='origin')
            origin.push()
            print("Pushed to GitHub successfully.")
    except GitCommandError as e:
        print(f"An error occurred: {e}")    

else:
    print("No internet connection. Please check your connection.")
