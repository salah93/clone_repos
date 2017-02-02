# clone all your repos

useful if working on updating current projects


```
# step 1: get personal access token from github settings
# step 2: check off boxes for repos access
# step 3: save personal access token in .bashrc as 'GITHUB_TOKEN'
$ echo "export GITHUB_TOKEN='your-token'" >> ~/.bashrc
$ . ~/.bashrc
$ python clone_repos.py
```
