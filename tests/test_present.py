from assertpy import assert_that

def test_genBudgetList():
	from present import genBudgetList

	lst = [{
	"account": "play"
	,"amount": 30
	}
	,{
	"account": "play"
	,"amount": 40
	}]

	result = genBudgetList(lst)
	assert_that(result).is_length(1)
	assert_that(result[0]["amount"]).is_equal_to(70)
	assert_that(result[0]["account"]).is_equal_to("play")

def test_genBudgetListMulti():
	from present import genBudgetList

	lst = [{
	"account": "play"
	,"amount": 30
	}
	,{
	"account": "play"
	,"amount": 40
	}
	,{
	"account": "other"
	,"amount": 50
	}]

	result = genBudgetList(lst)
	assert_that(result).is_length(2)
	assert_that(result).contains({"account": "play", "amount": 70})
	assert_that(result).contains({"account": "other", "amount": 50})

def test_genConsumptionList():
	from present import genConsumptionList

	lst = [{
	"account": "play"
	,"consumption": 30
	}
	,{
	"account": "play"
	,"consumption": 40
	}
	,{
	"account": "other"
	,"consumption": 50
	}]

	result = genConsumptionList(lst)
	assert_that(result).is_length(2)
	assert_that(result).contains({"account": "play", "consumption": 70})
	assert_that(result).contains({"account": "other", "consumption": 50})

def test_genResultList_empty():
	from present import genResultList

	budgets = []
	consumptions = []

	result = genResultList(budgets, consumptions)

	assert_that(result).is_length(0)

def test_genResultList_empty():
	from present import genResultList

	budgets = [{
		"account": "play"
		,"amount": 50
	}
	,{
		"account": "other"
		,"amount": 60
	}]
	consumptions = [{
		"account": "play"
		,"consumption": 30
	}
	,{
		"account": "other"
		,"consumption": 70
	}]

	result = genResultList(budgets, consumptions)

	assert_that(result).is_length(2)
	assert_that(result).contains({"account": "play", "amount": 20})
	assert_that(result).contains({"account": "other", "amount": -10})

def test_printResult():
	from present import printResult

	printResult([{"account": "play", "amount": 30}])