import dbhelper
from datetime import date

def test_insert():
	dbhelper.insert({"name":"alan", "date":date.today()})