# Creating and Merging Branches

<https://www.youtube.com/watch?v=HVsySz-h9r4>

<p>Let's say we want to create a branch named `first_branch`.
We should go to the terminal and do the following commands:</p>

1. `git branch first_branch`
2. `git checkout first_branch`
3. Edit files
4. `git status`
5. `git add -A`
6. `git commit -m "Testing First Branch"`
7. `git push -u origin first_branch`

The `-u` allows us to use `git push` and `git pull` whenever we want to
push and pull from the branch by default.

8. `git branch -a`

Shows all branches, including master. Current branch will be highlighted with *.

### Merging a Branch

8. `git checkout master`
9. `git pull master origin`
10. `git merge first_branch`
11. `git push origin master`

### Deleting a Branch
12. `git branch --merged`
13. `git branch -d first_branch`
14. `git branch -a`

Shows both local and remote branches. We can see that there is only master in
the local repository, but first_branch is still there in the remote repository.

15. `git push origin --delete first_branch`

# Other Useful Information

## Initializing
```
git init
```

## Creating .gitignore
```
$ touch .gitignore
```
Enter files to ignore in `.gitignore`, like the following

```
.DS_Store
.project
*.pyc
```

The `*.pyc` tells Git to ignore all files with the `.pyc` extension.

## Adding and Removing Files from Staging Area
```
git add -A
git reset
git reset somefile.file
```
`git reset` will remove all files in the staging area while
`git reset somefile.file` will remove only `somefile.file` from the
staging area.

## Cloning a Remote Repo
```
git clone <url> <where to clone>
```

## Viewing Info about the Remote Repository
```
git remote -v
git branch -a
```

## Pushing Changes
```
git diff
git status
git add -A
git commit -m "Modified Something"
```
Then push:
```
git pull origin master
git push origin master
```