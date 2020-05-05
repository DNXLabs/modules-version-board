# modules-version-board

Dashboard that shows all modules, tools and CLIs from DNX.

![Build](https://github.com/DNXLabs/modules-version-board/workflows/Build/badge.svg)
[![LICENSE](https://img.shields.io/github/license/DNXLabs/modules-version-board)](https://github.com/DNXLabs/modules-version-board/blob/master/LICENSE)


## Setup
First go to your GitHub account and create one token with read permission to repositories.

Then export this generated token in your environment.
```bash
export GITHUB_TOKEN=<token>
```


## Dependencies
- Python 3

#### Python Virtual Environment
```bash
# Create environment
python3 -m venv env

# To activate the environment
source env/bin/activate

# When you finish you can exit typing
deactivate
```

#### Install dependencies

```bash
pip3 install -r requirements.txt
```

#### Run
```bash
$ python3 generate-index.py
```

## Author
App managed by DNX Solutions.

## License
Apache 2 Licensed. See LICENSE for full details.