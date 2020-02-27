import os
import github3


MAIN_BRANCH = 'gh-pages'

with open('index.html') as f:
    index_file = f.read()

# Connect to GitHub API and push the changes.
github = github3.login(token=os.environ['GITHUB_TOKEN'])
repository = github.repository_with_id(os.environ['GITHUB_REPOSITORY_ID'])

github_index = repository.file_contents('/index.html', ref=MAIN_BRANCH)

pushed_change = github_index.update(
    'Bump version',
    index_file.encode('utf-8'),
    branch=MAIN_BRANCH
)

print("Pushed commit {} to {} branch:\n    {}".format(
    pushed_change['commit'].sha,
    MAIN_BRANCH,
    pushed_change['commit'].message,
))