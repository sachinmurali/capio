from word_extractor import WordExtractor 
from flask import Flask, send_from_directory
app = Flask(__name__, static_url_path='/files/')

@app.route("/")
def path_to_get_file():
	return "The path to download the transcript would be http://127.0.0.1:5000/capio/[transcript_id]"

@app.route("/capio/", defaults={'transcript_id' : None})
@app.route("/capio/<transcript_id>")
def get_document(transcript_id):
	wex = WordExtractor()
	wex.set_transcript_id(transcript_id)
	doc = wex.write_transcript()
	doc.save(transcript_id + '.docx')
	return send_from_directory('.', transcript_id + '.docx', as_attachment=True, attachment_filename=transcript_id + '.docx')
	