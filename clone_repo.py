import argparse
import subprocess
from os.path import join, expanduser

import requests


def clone_repos(user):
    user_url = 'https://api.github.com/users/{user}/repos'.format(user=user)
    page = requests.get(user_url)
    if page.status_code >= 400:
        raise Exception
    repos = filter(lambda x: not x['fork'], page.json())
    return repos

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory',
                        type=str, default='~/Projects')
    parser.add_argument('--user',
                        type=str, default=salah93)
    args = parser.parse_args()
    repos = clone_repos(args.user)
    gh_url = 'git@github.com:'
    for r in repos:
        command = ['git', 'clone', gh_url + r['full_name']]
        subprocess.Popen(command, cwd=expanduser(args.directory))
)
