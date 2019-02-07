#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
author:
    raja

source: (if any)
   https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list 
'''

import requests

def print_file(filename):

    writer = open("public_projects.txt", "a")
    missing_writer = open("missing_projects.txt", "a")

    with open(filename) as f:
        content = f.readlines()
        
    counter = 0

    # you may also want to remove whitespace characters like `\n` at the end of each line
    for x in content:

        counter = counter + 1

        if(len(x.strip()) == 0):
            continue

        items = x.split(" ")

        #if(counter > 30):
        #    break

        #print(len(items))

        if(len(items) != 5):
            continue

        g_link = 'https://github.com' + items[2]

        if(is_page_alive(g_link) == False):
            print('Not Available : ', g_link)
            missing_writer.write(g_link)
            missing_writer.write('\n')    
            continue

        writer.write(g_link)
        writer.write('\n')

        #print(x)    
    
    print('Done!')

def is_page_alive(url):
    r = requests.get(url)
    #print(r.status_code)

    if(r.status_code == 200):
        return True
    else:
        return False    
            
print_file("public_projects_from_hits_dwyl.txt")