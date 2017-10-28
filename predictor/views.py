# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.utils import simplejson

import json

from django.shortcuts import render

from django.http import HttpResponse

from . config import initiateDb

# Create your views here.


def fetchData(request):
	db = initiateDb()
	records = list(db.users.find({},{'_id':0}))
	res = json.dumps({"data": records})
	return HttpResponse(res)


def fetchEachYearData(request):
	"""
	Getting data according to a year
	"""
	year = request.GET.get('year')
	db = initiateDb()
	records = list(db.users.find({"year":int(year)},{'_id':0}))
	res = json.dumps({"data": records})
	return HttpResponse(res)

def fetchYearDelta(request):
	"""
	Getting delta of a year
	"""
	year = request.GET.get('year')
	db = initiateDb()
	distinct_disease = db.users.find({"year":int(year)},{'diseaseType':1}).distinct("diseaseType")
	disease_delta_list = []
	if len(distinct_disease):
		for i in distinct_disease:
			disease_type_obj = {}	
			current_year_cnt = db.users.find({"diseaseType":i,"year":int(year)},{'_id':0}).count()
			previous_year_cnt = db.users.find({"diseaseType":i,"year": int(year)-1},{'_id':0}).count()
			disease_type_obj.update({"delta":current_year_cnt - previous_year_cnt,"disease_type":i})
			disease_delta_list.append(disease_type_obj)

	res = json.dumps({"data": disease_delta_list})
	return HttpResponse(res)
