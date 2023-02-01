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
	#python3 -m pytest -vv --cov=mylib test_logic.py
build:
	#build the docker image
	docker build -t deploy-fastapi .
run:
	#running the docker contianer from docker image
	docker run -p 127.0.0.1:8080:8080 492094906798.dkr.ecr.us-east-1.amazonaws.com/fastapi-wikipedia:latest
deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 492094906798.dkr.ecr.us-east-1.amazonaws.com
	docker build -t fastapi-wikipedia .
	docker tag fastapi-wikipedia:latest 492094906798.dkr.ecr.us-east-1.amazonaws.com/fastapi-wikipedia:latest
	docker push 492094906798.dkr.ecr.us-east-1.amazonaws.com/fastapi-wikipedia:latest
all: install format lint deploy run