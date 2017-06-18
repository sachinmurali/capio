# capio

The objective here is to create a Python app/script to process Capio's speech recognition results into a word document. You would need Python 2.7.

[comment]: # (In order to run the app, first create a virtual environment. You can create a virtual environment using the virtualenv library in Python:)

[comment]: # (`pip install virtualenv`)

[comment]: #  (Activate the virtualenv:)
[comment]: #  (`virtualenv venv`)

[comment]: #  (`source venv/bin/activate`)

[comment]: #  (Once you're in the virtualenv, install the requirements file - `pip install -r requirements.txt`)

[comment]: # (Move to the `src` folder and run the flask app using the command `FLASK_APP=app.py flask run`)

In order to run the file, install the latest version of Docker.

Build the docker image with the command - `docker build -t capio-app .`

Run the docker image with the command - `docker run -p 5000:5000 capio-app`

Open the browser on `localhost:5000`, enter a valid key and a transcript id. On clicking the get document button, you should be able to save the processed transcript.
