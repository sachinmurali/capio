# capio

The objective here is to create a Python app/script to process Capio's speech recognition results into a word document. You would need Python 2.7.

[comment]: # (In order to run the app, first create a virtual environment. You can create a virtual environment using the virtualenv library in Python:)

In order to run the file, install the latest version of Docker. Clone the repo and run the following docker commands.

Build the docker image with the command - `docker build -t capio-app .`

Run the docker image with the command - `docker run -p 5000:5000 capio-app`

Open the browser on `localhost:5000`, enter a valid key and a transcript id. On clicking the get document button, you should be able to save the processed transcript.

You can also run in standalone mode by following the below commands, in case you are not using docker.

`pip install virtualenv`

Activate the virtualenv
`virtualenv venv`
`source venv/bin/activate`

Once you're in the virtualenv, install the requirements file - `pip install -r requirements.txt`

`cd` to the `src` folder and run the flask app using the command `FLASK_APP=app.py flask run`

Additionally, you can just run the `word_extractor.py` file. `cd` into `src` folder and run `python word_extractor.py`
