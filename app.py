from flask import Flask, request
import record
import dbhelper
import chardet
import codecs

app = Flask(__name__)

@app.route('/<desc>/<amount>')
def recordSingle(desc, amount):
	dbhelper.insert(record.addSimple(desc, amount))
	return "OK"


if __name__ == '__main__':
	app.run(debug=True)
