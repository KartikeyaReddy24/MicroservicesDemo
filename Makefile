install:
	# installing commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py mylib/*.py
lint:
	#pylint or flake8
	pylint --disable=R,C *.py mylib/*.py

test:
	#testing
	python3 -m pytest -vv --cov=mylib test_logic.py
build:
	#build container


deploy:

all: install format lint test deploy