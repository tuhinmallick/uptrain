# Contributing to the UpTrain Framework


If you're interested in contributing to the UpTrain repository, we'd love to have you! Here's a more detailed guide on how to get started:

1. First, fork the repository to your own GitHub account. This will create a copy of the repository that you can make changes to.

2. Next, navigate to the repository on your own account. This is where you'll make your changes and additions. But first you need to clone the repository to your local system using (replacing "YOUR_GITHUB_USERNAME" with your actual GitHub username)
```console
git clone https://github.com/YOUR_GITHUB_USERNAME/uptrain
```

3. Run `cd uptrain` to change your current working directory and run the following command to create a new branch: 
```console
git checkout -b YOUR_GITHUB_USERNAME/somefeature
```

4. Now it's time to make changes! You can add new files, modify existing files, or delete files that are no longer needed. To reinstall the UpTrain package with your local changes, run the following in the `uptrain` repository home folder: 
```console
pip install .
```

5. Before you add your changes, run [Black](https://github.com/psf/black) on your source files or directory. It is an automated code formatting tool that makes your code compliant to standard Python style guides. Read the documentation for detailed information.
```console
# Install Black
pip install black black[jupyter]

# Format your source changes
black {source_file_or_directory}

# or
python -m black {source_file_or_directory}
```

6. Once you've made the changes you want, you'll need to add them to a commit. You can do this by running the command `git add filename` for each file name you want to add/update. This will add all changes to the next commit.

7. Now you're ready to commit your changes. You'll need to provide a commit message that briefly describes the changes you've made. You can do this by running the command (replacing "Add something" with a brief description of your changes)
```console
git commit -m 'Add something'
```

8. Finally, you'll need to push your changes to the branch you created in step 3. You can do this by running the command (using `HEAD` will prevent you from accidentally pushing to the wrong remote branch. ) 
```console
git push origin HEAD
```

9. Once your changes are pushed, you can go back to the UpTrain repository on GitHub and make a pull request. This is where you'll describe your changes and ask for them to be reviewed and merged into the main repository.

Thank you for your interest in contributing to UpTrain! We look forward to reviewing your pull request and incorporating your changes ❤️
