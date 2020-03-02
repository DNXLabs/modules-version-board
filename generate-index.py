import os
import json
import requests

BASE_URL = 'https://api.github.com/repos/DNXLabs/'
RELEASES_PATH =  '/releases/latest'

input_file = open ('repos.json')
json_obj = json.load(input_file)
tools_array = json_obj['tools']
modules_array = json_obj['modules']

tools_cards = ""
modules_cards = ""

for item in tools_array:
    print(BASE_URL + item + RELEASES_PATH)
    response_repo = requests.get(BASE_URL + item, headers={"Authorization": "token " + os.environ['GITHUB_TOKEN']})
    response_release = requests.get(BASE_URL + item + RELEASES_PATH, headers={"Authorization": "token " + os.environ['GITHUB_TOKEN']})

    if 'description' in json.loads(response_repo.text):
        repo_json_obj = json.loads(response_repo.text)

    # print(response_release.text)


    if 'tag_name' in json.loads(response_release.text):
        release_json_obj = json.loads(response_release.text)
        card = """
        <div class="col-md-6 mb-4">
            <div class="card box-shadow shadow-sm h-100">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">%s</h5>
                    <p>
                        <a href="https://github.com/DNXLabs/%s/actions">
                            <img src="https://github.com/DNXLabs/%s/workflows/Security/badge.svg" alt="Security Status">
                        </a>
                        <a href="https://github.com/DNXLabs/%s/actions">
                            <img src="https://github.com/DNXLabs/%s/workflows/Lint/badge.svg" alt="Lint Status">
                        </a>
                        <a href="https://github.com/DNXLabs/%s/blob/master/LICENSE">
                            <img alt="LICENSE" src="https://img.shields.io/github/license/DNXLabs/%s">
                        </a>
                    </p>
                    <div class="card-text">
                        <p><b>Version:</b> <a href="%s">%s</a></p>
                        <p><b>Image:</b> <a href="https://hub.docker.com/repository/docker/dnxsolutions/%s">dnxsolutions/%s:%s</a></p>
                        <p>%s</p>
                    </div>
                    <div class="mt-auto d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                            <a href="%s" class="btn btn-sm btn-outline-primary">.tar</a>
                            <a href="%s" class="btn btn-sm btn-outline-primary">.zip</a>
                        </div>
                        <small class="text-muted">Id: %s</small>
                    </div>
                </div>
            </div>
        </div>
        """ % ( item,
                item,
                item,
                item,
                item,
                item,
                item,
                release_json_obj['html_url'],
                release_json_obj['tag_name'],
                item.split("-")[1],
                item.split("-")[1],
                release_json_obj['tag_name'],
                repo_json_obj['description'],
                release_json_obj['tarball_url'],
                release_json_obj['zipball_url'],
                release_json_obj['id'])
        # print(card)
        tools_cards += card

        print(json.loads(response_release.text)['tag_name'])


for item in modules_array:
    print(BASE_URL + item + RELEASES_PATH)
    response_repo = requests.get(BASE_URL + item, headers={"Authorization": "token " + os.environ['GITHUB_TOKEN']})
    response_release = requests.get(BASE_URL + item + RELEASES_PATH, headers={"Authorization": "token " + os.environ['GITHUB_TOKEN']})

    if 'description' in json.loads(response_repo.text):
        repo_json_obj = json.loads(response_repo.text)

    # print(response_release.text)


    if 'tag_name' in json.loads(response_release.text):
        release_json_obj = json.loads(response_release.text)
        card = """
        <div class="col-md-4 mb-4">
            <div class="card box-shadow shadow-sm h-100">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">%s</h5>
                    <p>
                        <a href="https://github.com/DNXLabs/%s/actions">
                            <img src="https://github.com/DNXLabs/%s/workflows/Lint/badge.svg" alt="Lint Status">
                        </a>
                        <a href="https://github.com/DNXLabs/%s/blob/master/LICENSE">
                            <img alt="LICENSE" src="https://img.shields.io/github/license/DNXLabs/%s">
                        </a>
                    </p>
                    <p class="card-text">
                        <p><b>Version:</b> <a href="%s">%s</a></p>
                        <p>%s</p>
                    </p>
                    <div class="mt-auto d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                            <a href="%s" class="btn btn-sm btn-outline-primary">.tar</a>
                            <a href="%s" class="btn btn-sm btn-outline-primary">.zip</a>
                        </div>
                        <small class="text-muted">Id: %s</small>
                    </div>
                </div>
            </div>
        </div>
        """ % ( item,
                item,
                item,
                item,
                item,
                release_json_obj['html_url'],
                release_json_obj['tag_name'],
                repo_json_obj['description'],
                release_json_obj['tarball_url'],
                release_json_obj['zipball_url'],
                release_json_obj['id'])
        # print(card)
        modules_cards += card

        print(json.loads(response_release.text)['tag_name'])



message = """
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="icon" href="https://github.com/DNXLabs/modules-version-board/raw/master/images/icon.png">

        <title>DNX One</title>

        <link rel="canonical" href="https://getbootstrap.com/docs/4.0/examples/album/">

        <!-- Bootstrap core CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

        <!-- Custom styles for this template -->
        <link href="album.css" rel="stylesheet">
    </head>

  <body>

    <header>
        <div class="navbar navbar-dark bg-dark box-shadow">
            <div class="container d-flex justify-content-between">
            <a href="#" class="navbar-brand d-flex align-items-center">
                <img src="https://github.com/DNXLabs/modules-version-board/raw/master/images/logo.png" width="30" height="30" alt="Italian Trulli">
                <strong>DNX One</strong>
            </a>
            </div>
        </div>
    </header>

    <main role="main">

        <section class="jumbotron text-center mb-0">
            <div class="container">
            <h1 class="jumbotron-heading">DNX One</h1>
            <p class="lead text-muted">At DNX we help your business build better solutions by upgrading how delivery is done, leaving behind manual processes and embracing an automated, cloud-native way of working.</p>
            <p>
                <a href="https://github.com/DNXLabs" class="btn btn-primary my-2">Organization</a>
                <a href="https://www.dnx.solutions/" class="btn btn-secondary my-2">About Us</a>
            </p>
            </div>
        </section>

        <div class="album py-5 bg-light">
            <div class="container">
                <h2>Tools</h2>
                <div class="dropdown-divider pb-3"></div>
                <div class="row">
                    %s
                </div>
                <h2 class="pt-4">Modules</h2>
                <div class="dropdown-divider pb-3"></div>
                <div class="row">
                    %s
                </div>
            </div>
        </div>

    </main>

    <footer class="text-muted">
        <div class="container">
            <p class="float-right">
            <a href="#">Back to top</a>
            </p>
        </div>
    </footer>

    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.slim.js" integrity="sha256-BTlTdQO9/fascB1drekrDVkaKd9PkwBymMlHOiG+qLI=" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>
""" % (tools_cards, modules_cards)

f = open('index.html','w')
f.write(message)
f.close()
