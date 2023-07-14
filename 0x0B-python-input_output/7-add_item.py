#!/usr/bin/python3

"""
    add_item module
"""


import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
arg_len = len(sys.argv)
arg_list = [arg for arg in sys.argv[1:]] if arg_len > 1 else []
file_content = None

try:
    file_content = load_from_json_file(filename)
except FileNotFoundError:
    save_to_json_file(arg_list, filename)

if file_content or file_content == []:
    for arg in arg_list:
        file_content.append(arg)
    save_to_json_file(file_content, filename)
