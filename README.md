# AutoFlex

For those of us who wants to flex our GitHub contributions without actually having contributed much.

## What is this?

This is a simple script that will automatically create commits on your GitHub account. It will create a commit for each day of the year, and each commit will have a random number of files, each with a random number of lines.

## Why?

Because I wanted to flex my GitHub contributions without actually having contributed much. And also to see if it was poopible.

## How to use?

To use this script, you need to have Python 3 installed. You can install it by running `pip3 install requests` in your terminal.
You also need to have Git installed. You can install it by running `pip3 install GitPython` in your terminal.

1. Fork this repository.
2. Clone your forked repository.
3. Run `python3 autoflex.py` in the cloned repository.

### Auto Run

If you want to run this script automatically, there a a lot of ways to do so, and I will not go into detail on how to do it. But here are some suggestions:

#### Windows

If you are on Windows, you can use Task Scheduler to run the script daily. I don't use Windows myself, so this might be wrong, feel free to correct me.

1. Open Task Scheduler and create a new task.
2. Set the trigger to run daily at your preferred time.
3. For the action, start a program, and browse to your Python executable (python.exe), usually located in the Python installation directory.
4. In the arguments, enter the path to your Python script.

#### Linux/MacOS

For Linux and MacOS, you can use cron jobs to run the script daily.

1. Open your terminal.
2. Type crontab -e to edit the cron jobs.
3. Add a line like this to execute the script daily at a specific time (e.g., 3 AM):

```ruby
0 3 * * * /usr/bin/python /path/to/your/example.py
```

4. Save and exit the editor.
