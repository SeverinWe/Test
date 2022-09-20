
import os
import PyPDF2
import re

keywords = ["female", "cancer", "male", "using"]
current_directory = os.path.dirname(os.path.realpath(__file__))
pdf_directory = current_directory + "/pdfs"

summary_regex = r"(?:summary[:]?[\s]?|background|purpose|)(.*?)(?:objective|background|methods|results|conclusion)"
background_regex = r"(?:background[s]?[:]?)(.*?)(?:Method[s]?|Result[s]?|Conclusion[s]?)"
methods_regex = r"(?:method[s]?[:]?)(.*?)(?:Result[s]?|Conclusion[s]?)"
results_regex = r"(?:result[s]?[:]?)(.*?)(?:Conclusion[s]?)"
conclusion_regex = r"(?:conclusion[s]?[:]?)(.*)"


def searchTextAndPrint(regex, text, section_name):
    searchResult = re.search(regex, text, flags=re.IGNORECASE | re.MULTILINE)
    # only read .group(1) if summary is not None, otherwise we'll get an error
    if searchResult:
        print(searchResult.group(0))
        for keyword in keywords:
            exclusionResult = re.search(keyword, searchResult.group(
                1), flags=re.IGNORECASE | re.MULTILINE)
            if exclusionResult:
                print(f"Keyword '{keyword}' found in {section_name} section")


for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        print(filename)
        full_file_name = os.path.join(pdf_directory, filename)
        file_obj = open(full_file_name, "rb")  # rb => read binray
        pdf_file = PyPDF2.PdfFileReader(file_obj, strict=False)
        first_page = pdf_file.getPage(0)
        first_page_text = first_page.extractText()

        searchTextAndPrint(regex=summary_regex,
                           text=first_page_text, section_name="Summary")
        searchTextAndPrint(regex=background_regex,
                           text=first_page_text, section_name="Background")
        searchTextAndPrint(regex=methods_regex,
                           text=first_page_text, section_name="Methods")
        searchTextAndPrint(regex=results_regex,
                           text=first_page_text, section_name="Results")
        searchTextAndPrint(regex=conclusion_regex,
                           text=first_page_text, section_name="Conclusion")
    else:
        continue
