# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:23:15 2019

@author: Sylwek Szewczyk
"""

import requests

url = 'http://localhost:3000'

r = requests.post(url,json={'text': 'this is an animal'})
print(r.json())