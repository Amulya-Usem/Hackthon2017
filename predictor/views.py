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
