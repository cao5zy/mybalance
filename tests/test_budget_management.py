from budget_management import BudgetManagement
from Runner import Run
from assertpy import assert_that

def test_currentBudget():
	Run.command('mkdir ./data/budgetManagement')
	Run.command('touch ./data/budgetManagement/1@2017-12-01.json')
	try:
		budgetManagement = BudgetManagement("./data/budgetManagement")
		assert_that(budgetManagement.currentBudget()).is_equal_to(None)
	finally:
		Run.command("rm ./data/budgetManagement -rf")
	
