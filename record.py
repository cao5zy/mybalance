# -*- coding: utf-8 -*-
from datetime import date
import uuid
import re

def addSimple(desc, amount):
	return {
	"desc": desc,
	"amount": amount,
	"date": date.today(),
	"id": str(uuid.uuid1())
	}

def reportCategory(json):
	def setCat(dic):
		dic["category"] = getDefaultCategory(dic["desc"])
		return dic
	return map(lambda n:setCat(n), json)

def getDefaultCategory(desc):
	dic = {
	"吃":[
	r".*吃.*"
	],
	"学习":[
	r".*书.*",
	r".*学.*",
	r".*笔.*"
	],
	"住":[
	r".*房.*"
	],
	"生活":[
	]
	}
	
	isMatch = lambda pattern:re.search(pattern, desc) != None

	isMatchArray = lambda patterns:any(filter(lambda pattern:isMatch(pattern), patterns))

	return ((lambda keys:keys[0] if len(keys) > 0 else "其它")\
		(list(filter(lambda key:isMatchArray(dic[key]), dic.keys()))))
	