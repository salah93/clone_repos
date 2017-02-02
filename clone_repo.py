import argparse
import json
import subprocess
from os import environ
from os.path import join, expanduser

import requests


def clone_repos(affiliation):
    user_url = 'https://api.github.com/user/repos'
    page = requests.get(user_url, dict(affiliation=','.join(affiliation), access_token=environ['GITHUB_TOKEN']))
    if page.status_code >= 400:
        raise Exception
    repos = filter(lambda x: not x['fork'], page.json())
    return repos


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory',
                        type=str, default='~/Projects')
    # you can also add 'collaborator', 'organization_member'
    parser.add_argument('--affiliation',
                        type=str, nargs='+', 
                        default=['owner'])
    args = parser.parse_args()
    repos = clone_repos(args.affiliation)
    gh_url = 'git@github.com:'
    for r in repos:
        command = ['git', 'clone', gh_url + r['full_name']]
        subprocess.Popen(command, cwd=expanduser(args.directory))
