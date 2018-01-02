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

		def newBudget():
			self.db["budgets"].insert_many([{"number": 1, "data": {"bds":[{"name": "KFC"}]}}])

			# generate a new balance with name number-date.json
			pass

		def currentBudget():
			print(loadAllBudgetsFileName())
			# if the folder is empty, return None
			pass

		def historyBudgets():
			pass

		def loadAllBudgetsFileName():
			pass

		def getFileNameParts(fileName):
			def processName(exp):
				if not re.search(exp, fileName):
					raise Error("invalid file name:%s" % fileName)
				
		def getNumberOfFileName(fileName):
			pass

		def getDateOfFileName(fileName):
			pass

		self.newBudget = newBudget
		self.currentBudget = currentBudget
		self.historyBudgets = historyBudgets