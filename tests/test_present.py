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

