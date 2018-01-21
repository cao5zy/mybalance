from budget_management import BudgetManagement
from assertpy import assert_that

def test_currentBudget():
		budgetManagement = BudgetManagement()
		budgetManagement.newBalance()

def test_currentKey():
	budgetManagement = BudgetManagement()

	result = budgetManagement.currentKey()

	assert_that(budgetManagement.setCurrentKey(result["order"] + 1)["order"]).is_equal_to(result["order"] + 1)
