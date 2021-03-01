PROJECT_NAME := book_store
PYTHON_VERSION := 3.8.8
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

code-convention:
	flake8
	pycodestyle

makemessages:
	python3 manage.py makemessages -l pt_BR --no-wrap --no-location

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

setup:
	pip3 install -r requirements.txt

setup-dev:
	pip3 install -r requirements-dev.txt

.create-venv:
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup-dev

test:
	py.test -v
