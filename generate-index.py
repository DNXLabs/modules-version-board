import os
import json
import requests
from jinja2 import Environment, FileSystemLoader

BASE_URL      = 'https://api.github.com/repos/DNXLabs/'
RELEASES_PATH =  '/releases/latest'

input_file    = open ('repos.json')
json_obj      = json.load(input_file)
tools_array   = json_obj['tools']
modules_array = json_obj['modules']

tools   = []
modules = []


for item in tools_array:
    print(BASE_URL + item + RELEASES_PATH)
    response_repo    = requests.get(BASE_URL + item, headers={"Authorization": "token " + os.environ['GITHUB_TOKEN']})
    response_release = requests.get(BASE_URL + item + RELEASES_PATH, headers={"Authorization": "token " + os.environ['GITHUB_TOKEN']})

    if 'description' in json.loads(response_repo.text):
        repo_json_obj = json.loads(response_repo.text)

    if 'tag_name' in json.loads(response_release.text):
        release_json_obj = json.loads(response_release.text)
        tool = {
            "name":        item,
            "description": repo_json_obj['description'],
            "short_name":  item.split("-")[1],
            "html_url":    release_json_obj['html_url'],
            "tag_name":    release_json_obj['tag_name'],
            "tarball_url": release_json_obj['tarball_url'],
            "zipball_url": release_json_obj['zipball_url'],
            "id":          release_json_obj['id']
        }

        tools.append(tool)
        print(json.loads(response_release.text)['tag_name'])


for item in modules_array:
    print(BASE_URL + item + RELEASES_PATH)
    response_repo    = requests.get(BASE_URL + item, headers={"Authorization": "token " + os.environ['GITHUB_TOKEN']})
    response_release = requests.get(BASE_URL + item + RELEASES_PATH, headers={"Authorization": "token " + os.environ['GITHUB_TOKEN']})

    if 'description' in json.loads(response_repo.text):
        repo_json_obj = json.loads(response_repo.text)

    if 'tag_name' in json.loads(response_release.text):
        release_json_obj = json.loads(response_release.text)
        module = {
            "name":        item,
            "description": repo_json_obj['description'],
            "short_name":  item.split("-")[1],
            "html_url":    release_json_obj['html_url'],
            "tag_name":    release_json_obj['tag_name'],
            "tarball_url": release_json_obj['tarball_url'],
            "zipball_url": release_json_obj['zipball_url'],
            "id":          release_json_obj['id']
        }

        modules.append(module)
        print(json.loads(response_release.text)['tag_name'])


root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('modules.html')


filename = os.path.join(root, 'index.html')
with open(filename, 'w') as fh:
    fh.write(template.render(
        tools = tools,
        modules = modules
    ))