# book store

## Instalação


### Instalação do pyenv

 1. pyenv (https://github.com/pyenv/pyenv | https://github.com/pyenv/pyenv/wiki)
    - Instalação (debian / ubuntu): 
    ```bash
    $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
    $ exec "$SHELL"
    ```

 2. Python 3.8.8
    - Instalação via pyenv:
    ```bash
    $ pyenv install 3.8.8
    ```

A automatização das tarefas é realizada via Makefile. Se todos os requisitos foram contemplados, o ambiente virtual 
deve ser criado através do seguinte comando:

```bash
$ make create-venv
```

- Talvez seja necessário instalar:
  - python3 -m pip install djangorestframework
  - python3 -m pip install djangorestframework
  - python3 -m pip install django-filter
  - python3 -m pip install drf-yasg
  - python3 -m pip install PyMySQ

### Rodando o banco de dados no docker

1. Ter o docker instalado na maquina ou instalar de acordo com tutorial contido em:
https://docs.docker.com/get-docker/
   
2. Baixar o projeto git: https://github.com/getonini/book_store-config

3. Acessar a pasta book_store-config e rodar docker-compose build e em seguida: docker-compose up


### PyCharm

1. Acessar menu File -> Settings

    1.1. Acessar opções Project -> Project -> Interpreter

    1.2. Acessar Settings (icone de engrenagem) -> Add

    1.3. Selecionar "Existing Environment" e clicar em 'OK'

2. Acesssar 'Run Configurations' -> New

    2.1. Aba Configuration:

        2.1.1. Script path: inserir/o/path/para/manage.py (Dentro do projeto)

        2.1.2. Parameters: runserver

        2.1.3. Environment variables: PYTHONUNBUFFERED=1

        2.1.4. Python interpreter: selecionar interpreter recém criado

3. Antes de rodar o projeto no pycharm, necessário rodar o migrate, para criar as tabelas no mysql rodando no docker.

    