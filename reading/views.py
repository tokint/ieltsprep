import os
import re
from django.shortcuts import render
from lib.wstat import UserAnswers
from ieltsprep.settings import BASE_DIR

def index(request):
    filelist = []
    book_dir = os.path.join(BASE_DIR, 'reading/text')
    for root, dirs, files in os.walk(book_dir):
        for filename in files:
            if filename != "license":
                bookroute = filename.replace(".txt","")
                bookname = bookroute.replace("_"," ")
                filelist.append({'bookroute' : bookroute, 'bookname' : bookname})

    return render(request, 'reading/index.html', {'filelist' : filelist})

def read_book(request, file_name):

    def read_file(title_path):
        with open(title_path, "r", encoding ="utf8") as current_file:
            text = current_file.read()

        return text

    def search_title(text):
        ttl = re.search(r'(?<=Title: )(.+)', text)
        return ttl.group(0)

    def search_author(text):
        aut = re.search(r'(?<=Author: )(.+)', text)
        return aut.group(0)

    book_dir = os.path.join(BASE_DIR, 'reading/text/')
    text = read_file(book_dir+file_name+".txt")
    license = read_file(book_dir+"/license")
    title = search_title(text)
    author = search_author(text)
    ua = UserAnswers(text, 250)
    wcount = ua.words_count
    text = text.replace("\n\n","<br>")
    license = license.replace("\n\n","<br>")
    text += license
    ret = {'text':text, 'author': author, 'title': title, 'wc': wcount }

    return render(request, 'reading/readbook.html', ret)
#    return render(request, 'reading/readbook.html')
