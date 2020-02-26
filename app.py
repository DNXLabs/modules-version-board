import json
import requests

BASE_URL = 'https://api.github.com/repos/DNXLabs/'
RELEASES_PATH =  '/releases/latest'
TOKEN = "<github_personal_token>"

input_file = open ('repos.json')
json_obj = json.load(input_file)
repos_array = json_obj['repos']

message = """
# DNX One Modules List

| Name  | Version  | URL  |
|-------|----------|-------|
"""

for item in repos_array:
    print(BASE_URL + item + RELEASES_PATH)
    response = requests.get(BASE_URL + item + RELEASES_PATH, headers={"Authorization": "token " + TOKEN})
    # print(response.text)
    if 'tag_name' in json.loads(response.text):
        repo_json_obj = json.loads(response.text)
        line = "| " + item + " | " + repo_json_obj['tag_name'] + " | " + repo_json_obj['url'] + " | \n"
        message += line
        print(json.loads(response.text)['tag_name'])

f = open('index.md','w')
f.write(message)
f.close()