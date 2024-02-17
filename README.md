# PyWebAutoBot

project_root/
│
├── features/
│   ├── steps/
│   │   ├── __init__.py
│   │   ├── sample_steps.py
│   │
│   ├── sample.feature
│
├── tests/
│   ├── __init__.py
│
└── requirements.txt

Google Chrome Web driver download :
https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/

Generate dependancies file with all requirements
    pip freeze > requirements.txt
    pip install -r requirements.txt
    Notes : 
        - If failed then 
            Remove specified version numbers. Then pip will try to manage and resolve dependancies
            on its own

Install Docker according to playform
    docker pull FROM python:3.9-slim
    docker images
    docker build -t behave-tests .
    docker run behave-tests
    docker rmi -f <ID>
    docker run -it <ID> bash
    docker inspect behave-tests | grep -i os