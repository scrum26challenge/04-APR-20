# 04-APR-20
TheBoys Cohort


Basic GIT Commands:

1. git status : tells you if you are in a git repo, and what branch

2. you rarely commit to master in a group project, which means you always branch off of master before editing or creating new code
git checkout -b new-branch-name : create a new branch off of the master branch (tested code) and put you into the new branch.

3. to clone: git clone repo-url, then CD into the created directory.

4. to pull the latest code from master, go into the master branch (git checkout master) then git pull origin master (fetches the remote code)

5. edit you code ALWAYS in a new branch, never in master. 

6. to commit: 
  1. git add *
  2. git commit -m "comment"
  3. git push origin branch-name  ***** MAKE SURE THAT YOU PUSH TO THE RIGHT BRANCH

7. create a Pull Request (PR) on github. 

8. 'git branch' shows you what branches are available 
