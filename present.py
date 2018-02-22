

def genBudgetList(budgets):
	from itertools import groupby

	return [{"account": key, \
			"amount": sum(map(lambda n:n["amount"], group))
			} \
		for key, group in groupby(budgets, lambda n:n["account"])]

def genConsumptionList(consumptions):
	pass
def genResultList(budgets, consumptions):
	pass
def printResult(resultList):
	pass
def showBudgetRemaining(balance):
	printResult(\
		genResultList(\
			genBudgetList(balance["budgets"]), \
			genConsumptionList(balance["consumptions"]))\
		)
