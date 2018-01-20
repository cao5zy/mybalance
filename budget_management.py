import os
import itertools
from pymongo import MongoClient


class BudgetManagement:
	def __enter__(self):
		return self

	def __exit__(self, e_t, e_v, t_b):
		self.conn.close()

	def __init__(self):
		self.conn = MongoClient("mongodb://localhost", 27017)
		self.db = self.conn.testdb

		def newBalance():
			self.db["Balances"].insert_many([{"number": 1, "data": {"bds":[{"name": "KFC"}]}}])

			# generate a new balance with name number-date.json
			pass

		def currentBalance():
			print(loadAllBalancesFileName())
			# if the folder is empty, return None
			pass

		def historyBalances():
			pass

		def loadAllBalancesFileName():
			pass

		def getFileNameParts(fileName):
			def processName(exp):
				if not re.search(exp, fileName):
					raise Error("invalid file name:%s" % fileName)
				
		def getNumberOfFileName(fileName):
			pass

		def getDateOfFileName(fileName):
			pass

		self.newBalance = newBalance
		self.currentBalance = currentBalance
		self.historyBalances = historyBalances