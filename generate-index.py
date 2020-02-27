import os
import json
import requests

BASE_URL = 'https://api.github.com/repos/DNXLabs/'
RELEASES_PATH =  '/releases/latest'

input_file = open ('repos.json')
json_obj = json.load(input_file)
repos_array = json_obj['repos']

cards = ""

for item in repos_array:
    print(BASE_URL + item + RELEASES_PATH)
    response = requests.get(BASE_URL + item + RELEASES_PATH, headers={"Authorization": "token " + os.environ['GITHUB_TOKEN']})
    # print(response.text)
    if 'tag_name' in json.loads(response.text):
        repo_json_obj = json.loads(response.text)
        # line = "| %s | [%s](%s)  | %s |\n"% (item, repo_json_obj['tag_name'], repo_json_obj['html_url'], repo_json_obj['id'])
        card = """
        <div class="col-md-4">
            <div class="card mb-4 box-shadow shadow-sm">
                <div class="card-body">
                <h5 class="card-title">%s</h5>
                <p class="card-text">
                    <p>Version: <a href="%s">%s</a></p>
                </p>
                <div class="d-flex justify-content-between align-items-center">
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
                repo_json_obj['html_url'],
                repo_json_obj['tag_name'],
                repo_json_obj['tarball_url'],
                repo_json_obj['zipball_url'],
                repo_json_obj['id'])
        # print(card)
        cards += card
        
        print(json.loads(response.text)['tag_name'])



message = """
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="icon" href="https://github.com/DNXLabs/modules-version-board/raw/master/images/icon.png">

        <title>Modules DNX One</title>

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
                <strong>DNX One Modules</strong>
            </a>
            </div>
        </div>
    </header>

    <main role="main">

        <section class="jumbotron text-center mb-0">
            <div class="container">
            <h1 class="jumbotron-heading">Modules DNX One</h1>
            <p class="lead text-muted">At DNX we help your business build better solutions by upgrading how delivery is done, leaving behind manual processes and embracing an automated, cloud-native way of working.</p>
            <p>
                <a href="https://github.com/DNXLabs" class="btn btn-primary my-2">Organization</a>
                <a href="https://www.dnx.solutions/" class="btn btn-secondary my-2">About Us</a>
            </p>
            </div>
        </section>

        <div class="album py-5 bg-light">
            <div class="container">
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
""" % (cards)

f = open('index.html','w')
f.write(message)
f.close()