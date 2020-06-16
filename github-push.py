import os
import github3


MAIN_BRANCH          = 'gh-pages'
GITHUB_TOKEN         = os.environ['GITHUB_TOKEN']
GITHUB_REPOSITORY_ID = os.environ['GITHUB_REPOSITORY_ID']

with open('index.html') as f:
    index_file = f.read()

with open('api.json') as f:
    api_file = f.read()

# Connect to GitHub API and push the changes.
github = github3.login(token=GITHUB_TOKEN)
repository = github.repository_with_id(GITHUB_REPOSITORY_ID)

github_index = repository.file_contents('/index.html', ref=MAIN_BRANCH)
github_api = repository.file_contents('/api.json', ref=MAIN_BRANCH)

pushed_index_change = github_index.update(
    'Bump front version',
    index_file.encode('utf-8'),
    branch=MAIN_BRANCH
)

print("Pushed commit {} to {} branch:\n    {}".format(
    pushed_index_change['commit'].sha,
    MAIN_BRANCH,
    pushed_index_change['commit'].message,
))

pushed_api_change = github_api.update(
    'Bump API version',
    api_file.encode('utf-8'),
    branch=MAIN_BRANCH
)

print("Pushed commit {} to {} branch:\n    {}".format(
    pushed_api_change['commit'].sha,
    MAIN_BRANCH,
    pushed_api_change['commit'].message,
))