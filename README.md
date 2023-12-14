## Setup :

Install Docker  : https://docs.docker.com/engine/install/

Install Poetry : https://python-poetry.org/docs/#installation

Install wireshark : https://www.wireshark.org/download.html

- check if docker is already on from the previous step if not switch it on by the command `docker-compose up`
- clone the application : `https://github.com/vishrutkohli/pycon-workshop/tree/main`
- install potery  on your local machine if not already
- setup and run the application :
    - `poetry install --only main`
    - `poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload`
