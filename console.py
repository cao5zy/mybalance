import sys
from budget_management import BudgetManagement

def getBudgetParam():
	return {
		"account": sys.argv[2]
		,"amount": sys.argv[3]
	}

def getConsumptionParam():
	return {
		"account": sys.argv[2]
		,"consumption": sys.argv[3]
		,"desc": "" if len(sys.argv) == 4 else sys.argv[4]
	}

def getIncomeParam():
	return {
		"title": sys.argv[2]
		,"income": sys.argv[3]
		,"desc": "" if len(sys.argv) == 4 else sys.argv[4]
	}

def getAction():
	return sys.argv[2]

def addBudget():
	def add(budgetManagement):
		budgetManagement.addBudget(budgetManagement.currentBalance(), getBudgetParam())

	add(BudgetManagement())

def addConsumption():
	def add(budgetManagement):
		budgetManagement.addConsumption(budgetManagement.currentBalance(), \
			getConsumptionParam().update({"date": datetime.datetime.now()}))

	add(BudgetManagement())

def addIncome():
	def add(budgetManagement):
		budgetManagement.addIncome(budgetManagement.currentBalance(), \
			getIncomeParam().update({"date": datetime.datetime.now()}))

	add(BudgetManagement())

def errorCmd():
	print("error command")

def showBudgetRemaining():
	from present import showBudgetRemaining
	def show(budgetManagement):
		showBudgetRemaining(budgetManagement.toJson(budgetManagement.currentBalance()))

	show(BudgetManagement())

def main():
	def process(action):
		(lambda actionDic:actionDic[(action if action in actionDic else "errorCmd").lower()]())\
		({
			"addbudget": addBudget
			,"addconsumption": addConsumption
			,"addincome": addIncome
			,"errorcmd": errorCmd
			,"showbudgetremaining": showBudgetRemaining
		})

	process(getAction())

if __name__ == '__main__':
	main()