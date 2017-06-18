from flask_wtf import Form
from wtforms import TextField
# , [validators.required(), validators.length(max=10)]
class GetKeyTransactionIdForm(Form):
    key = TextField('Key')
    transactionId  = TextField('Transaction Id')