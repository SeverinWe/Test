
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:00:25 2022

@author: severinwendelspiess
"""
#regular expression = re

import PyPDF2 
import re

file = PyPDF2.PdfFileReader("test_paper.pdf") 
NumPages = file.getNumPages()
print("This Paper has", NumPages, "pages")
firstpage = file.getPage(0)
text=firstpage.extractText()

summary = re.search("(summary[:]?[\s]?.*?)(objective|background|methods|results|conclusion)", text, flags=re.IGNORECASE | re.MULTILINE)
summaryGroup = summary.group(1)
print(summaryGroup)

if not summary:
    print(file, "summary not found")


keywords = ["female", "cancer", "male","using"]
for keyword in keywords:
   ResSearch = re.search(keyword, summaryGroup)
   if ResSearch:
       print("found keyword", keyword)













