import subprocess
from os.path import join, expanduser

import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = 'https://github.com/salah93?tab=repositories'
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    clone_url = 'https://github.com/salah93'
    all_sources = soup.find_all(class_='source')
    repos = [repo.find('a').text.strip() for repo in all_sources]
    clone_urls = [join(clone_url, repo) for repo in repos]
    [subprocess.Popen(['git', 'clone', i], cwd=expanduser('~/Projects')) for i in clone_urls]
