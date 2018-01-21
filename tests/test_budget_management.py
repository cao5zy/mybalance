from budget_management import BudgetManagement
from assertpy import assert_that

def test_currentBudget():
		budgetManagement = BudgetManagement()
		budgetManagement.newBalance()

def test_currentKey():
	budgetManagement = BudgetManagement()

	assert_that(budgetManagement.currentKey()).is_equal_to(0)