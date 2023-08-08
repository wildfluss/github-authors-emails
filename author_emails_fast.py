#!/usr/bin/env python

import pandas as pd
import os
# from dotenv import load_dotenv
import sys
import subprocess
from pygit2 import Repository
from pygit2 import GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE
import shutil


def real_main(repo_str):
    # load_dotenv()

    GIT = '/opt/homebrew/bin/git'  # '/usr/bin/git' # GCP
    REPO = f"/tmp/{repo_str.replace('/','-')}.git"

    # TODO: pub/sub message
    # repo_str = sys.argv[1]  # 'jrzaurin/pytorch-widedeep'

    git_cmd = [GIT, 'clone', '--bare',
                    '--filter=blob:none', f"git@github.com:{repo_str}.git", REPO]
    print(git_cmd)
    subprocess.call(git_cmd)

    repo = Repository(REPO)

    commits = []
    for commit in repo.walk(repo.head.target, GIT_SORT_TOPOLOGICAL | GIT_SORT_REVERSE):
        commits.append(commit)

    ae = pd.DataFrame(data=[{'sha': c.hex,
                             'author_email': c.author.email} for c in commits])
    ae['repo'] = repo_str

    ae.to_csv(f"{repo_str.replace('/','-')}.csv", index=False)

    print(f"Wrote {len(commits)} commits.")

    shutil.rmtree(REPO)


if __name__ == "__main__":
    real_main(sys.argv[1])
