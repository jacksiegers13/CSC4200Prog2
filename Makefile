build:
	@echo "Nothing to build for Python"

run-server:
	python3 server.py

run-client:
	python3 client.py

clean:
	rm -f *.pyc
	rm -rf __pycache__
