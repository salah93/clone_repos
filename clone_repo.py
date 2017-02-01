import subprocess
from os.path import join, expanduser

import requests
from bs4 import BeautifulSoup


def clone_repos(user, directory):
    gh_url = 'https://github.com/'
    user_url = 'https://api.github.com/users/{user}/repos'.format(user=user)
    page = requests.get(user_url)
    if page.status_code >= 400:
        raise Exception
    repos = filter(lambda x: not x['fork'], page.json())
    [subprocess.Popen(['git', 'clone', join(gh_url, i['full_name'])], cwd=expanduser(directory)) for i in repos]


if __name__ == '__main__':
    clone_repos('salah93', '~/Projects')
