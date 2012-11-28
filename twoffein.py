#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__doc__ = """Twoffein API

This module is an interface to the Twoffein API.

Copyright (c) 2012, Malte Bublitz
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

	* Redistributions of source code must retain the above copyright
	  notice, this list of conditions and the following disclaimer.

   * Redistributions in binary form must reproduce the above copyright
	  notice, this list of conditions and the following disclaimer in
	  the documentation and/or other materials provided with the
	  distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.
"""

import json
import urllib2
import StringIO

class Twoffein(object):
	_profile = {}
	def __init__(self, auth):
		self._screenname, self._apikey = auth
		response = urllib2.urlopen("http://twoffein.com/api/get/drinks/?screen_name="+self._screenname+"&api_key="+self._apikey+"&encode=json")
		self._drinks = json.load(StringIO.StringIO(response.read()))

	def get_drinks(self):
		return self._drinks

	def get_profile(self, profile=None):
		if not self._profile.has_key(profile):
			if profile==None:
				response = urllib2.urlopen("http://twoffein.com/api/get/profile/?screen_name="+self._screenname+"&api_key="+self._apikey+"&encode=json")
			else:
				response = urllib2.urlopen("http://twoffein.com/api/get/profile/?screen_name="+self._screenname+"&api_key="+self._apikey+"&encode=json&profile="+profile)
			self._profile[profile] = json.load(StringIO.StringIO(response.read()))
		return self._profile[profile]

	def drink(self, drink, target=None):
		pass

	def give_cookie(self, target):
		pass

	def __repr__(self):
		return '<Twoffein API>'

class Drink(object):
	def __init__(self, key):
		self._key = key

	def get_real_name(self, twoffein_instance):
		for d in twoffein_instance._drinks:
			if d["key"] == self._key:
				return d["drink"]
	
	def __repr__(self):
		return '<Drink "'+self._key+'">'

def main():
	api = Twoffein( ("malte70","ABCDEFGHIJK") )
	print api.get_drinks()[1]
	print api.get_profile()
	print api.get_profile('Revengeday')
	drink = Drink("schwarztee")
	print drink.get_real_name(api)

if __name__=="__main__":
	main()
