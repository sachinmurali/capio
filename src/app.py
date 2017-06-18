from word_extractor import WordExtractor 
from flask import Flask, send_from_directory, render_template, request
from flask_bootstrap import Bootstrap
from forms import GetKeyTransactionIdForm

app = Flask(__name__, static_url_path='/files/')
Bootstrap(app)
app.secret_key = 'development key'

@app.route("/")
def index():
    form = GetKeyTransactionIdForm()
    return render_template('index.html', form=form)

# @app.route("/capio/", defaults={'transcript_id' : None})
# @app.route("/capio/<transcript_id>")
# def get_document(transcript_id):
#     pass

@app.route('/get_document/',methods=['POST'])
def get_document():
    key = request.form['key']
    if key:
        wex.set_key(key)
    wex = WordExtractor()        
    transactionId = request.form['transactionId']
    wex.set_transcript_id(transactionId)
    doc = wex.write_transcript()
    doc.save(transactionId + '.docx')
    return send_from_directory('.', transactionId + '.docx', as_attachment=True, attachment_filename=transactionId + '.docx')