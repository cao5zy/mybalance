import os
import itertools

class BudgetManagement:
	def __init__(self, storePath):

		def newBudget():
			# generate a new balance with name number-date.json
			pass

		def currentBudget():
			print(loadAllBudgetsFileName())
			# if the folder is empty, return None
			pass

		def historyBudgets():
			pass

		def loadAllBudgetsFileName():
			return [y for x in list([\
				list(map(lambda file:file, files)) \
				 for root, dirs, files in os.walk(storePath)]) for y in x]

		self.newBudget = newBudget
		self.currentBudget = currentBudget
		self.historyBudgets = historyBudgets