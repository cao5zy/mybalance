# -*- coding: utf-8 -*-
from datetime import date
import uuid

def addSimple(desc, amount):
	return {
	"desc": desc,
	"amount": amount,
	"date": date.today(),
	"id": str(uuid.uuid1())
	}

def getDefaultCategory(desc):
	dic = {
	"吃":[],
	"学习":[],
	"住":[],
	"生活":[]
	}
	return "other"
	