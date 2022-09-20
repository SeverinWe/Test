 
import os
import PyPDF2
import re

keywords = ["female", "cancer", "male","using"]
Directory = '/Users/severinwendelspiess/Documents/Universität/Dissertation/Test/'

for filename in os.listdir(Directory):
    if filename.endswith(".pdf"): 
        print(filename)
        file = PyPDF2.PdfFileReader(filename)
        firstpage = file.getPage(0)
        text = firstpage.extractText()

        summary = re.search(r"(?:summary[:]?[\s]?|background|purpose|)(.*?)(?:objective|background|methods|results|conclusion)", text, flags=re.IGNORECASE | re.MULTILINE)
        summaryGroup = summary.group(1)
        print(summaryGroup)
        #if not summary:
            #print(file, "summary not found")

        background = re.search(r"(?:background[s]?[:]?)(.*?)(?:Method[s]?|Result[s]?|Conclusion[s]?)", text, flags=re.IGNORECASE|re.MULTILINE)
        backgroundGroup = background.group(1)
        print(backgroundGroup)
            #if not background:
                #print(file, "background not found")
            
        methods = re.search(r"(?:method[s]?[:]?)(.*?)(?:Result[s]?|Conclusion[s]?)",text,flags=re.IGNORECASE|re.MULTILINE)
        methodsGroup = methods.group(1)
        print(methodsGroup)
            #if not methods:
                #print(file, "methods not found")
            
        results = re.search(r"(?:result[s]?[:]?)(.*?)(?:Conclusion[s]?)",text, flags=re.IGNORECASE|re.MULTILINE)
        resultsGroup = results.group(1)
        print(resultsGroup)
            #if not results:
                #print(file, "results not found")
    
        conclusion =   re.search(r"(?:conclusion[s]?[:]?)(.*)", text, flags=re.IGNORECASE|re.MULTILINE)
        conclusionGroup = conclusion.group(1)
        print(conclusionGroup)
            #if not conclusion:
                #print(file, "conclusion not found")
     
        
        for keyword in keywords:
            ResSearch = re.search(keyword, summaryGroup)
            if ResSearch:
                print("found Exclusion criteria", "'",keyword,"'", "in summary")
            
        for keyword in keywords:
            ResSearch1 = re.search(keyword, backgroundGroup)
            if ResSearch1:
                print("found Exclusion criteria", "'",keyword,"'", "in background")
        
        
        for keyword in keywords:
            ResSearch2 = re.search(keyword, methodsGroup)
            if ResSearch2:
                print("found Exclusion criteria", "'",keyword,"'", "in methods")

        for keyword in keywords:
            ResSearch3 = re.search(keyword, resultsGroup)
            if ResSearch3:
                print("found Exclusion criteria", "'",keyword,"'", "in results")
                
            
        for keyword in keywords:
            ResSearch4 = re.search(keyword, conclusionGroup)
            if ResSearch4:
                print("found Exclusion criteria", "'",keyword,"'", "in conclusion")
    else:
        continue



 
 

   