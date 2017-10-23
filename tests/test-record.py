# -*- coding: utf-8 -*- 
import record
from assertpy import assert_that
from datetime import date
import demjson
def test_addSimple():
	result = record.addSimple("have lunch", 30)
	
	assert_that(result).contains_entry({"amount": 30})
	assert_that(result).contains_entry({"desc": 'have lunch'})
	assert_that(result["date"]).is_equal_to(date.today())
	assert_that(result["id"]).is_not_empty()

def test_getDefaultCategory():
	cat = record.getDefaultCategory('吃麦当劳')
	assert_that(cat).is_equal_to('吃')

def test_getDefaultCategory_default():
	cat = record.getDefaultCategory('seredsfdfsdf sdf')
	assert_that(cat).is_equal_to('其它')

def test_reportCategory():
	json = demjson.decode('''
		[
			{
			"desc":"吃肯德基",
			"amount":80,
			"date": "2017-10-23"
			}
		]''')
	result = list(record.reportCategory(json))
	assert_that(result).is_length(1)
	assert_that(result[0]).contains_entry({"category":"吃"})
