# -*- coding: utf-8 -*-

from django.core.management.utils import get_random_secret_key  

key = get_random_secret_key()
result = f"SECRET_KEY = '{key}'"

file = open("task_management/key.py","w+") 
file.write(result)
file.close()