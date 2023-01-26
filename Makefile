install:
	# installing commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	#pylint or flake8

test:

deploy:

all: install format lint test deploy