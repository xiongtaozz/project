from bs4 import  BeautifulSoup
import lxml
import re

markup = '''"<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a><a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>"'''
soup = BeautifulSoup(markup)
print soup.get_text()
print soup.i.get_text()
# print soup.original_encoding
# params=soup.find_all('b')
# s = BeautifulSoup(str(params),'lxml')
# print s.original_encoding
# print s.get_text()