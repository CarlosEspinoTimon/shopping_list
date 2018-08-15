# FLASK Server
## How to start it
### First time
The first time you clone the project you need to create a virtualenv
`virtualenv venv`
Activate the virtualenv
`source venv/bin/activate`
And install the requirements
`pip install -r requirements.txt`

### The rest of the times
The rest of the times you just activate the virtualenv

## Configure some variables
You need to configure some variables from the terminal
`export FLASK_APP=server.py && export FLASK_DEBUG=1`

## Start the server
From the rest-server directory:
`flask run`

## Requirements
You need to have MySQL installed (or use the Docker that I share in the project) and configure the connection in the config.py file.