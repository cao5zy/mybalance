from flask import Flask
import record
import dbHelper

app = Flask(__name__)

@app.route('/<desc>/<amount>')
def recordSingle(desc, amount):
	dbHelper.insert(record.addSimple(desc, amount))

if __name__ == '__main__':
	app.run()