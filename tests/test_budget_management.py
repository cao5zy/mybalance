from budget_management import BudgetManagement
from assertpy import assert_that

def test_currentBudget():
	try:
		with BudgetManagement() as budgetManagement:
			budgetManagement.newBalance()
	finally:
		pass	
