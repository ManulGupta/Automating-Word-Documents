import win32com.client as win32
import re

word = win32.gencache.EnsureDispatch('Word.Application')
word.Visible = True
doc = word.Documents.Open("C:\\Users\\VAMSI\\Desktop\\as\\oof.docx")
words = []

for word in doc.Words:
    ele = str(word)
    ele = ele.strip()
    ele = ele.lower()
    if str(word) == "United" or str(word) == "States" or str(word) == "US" or ele == "usa" or ele == "u" or ele == "s":
        word.HighlightColorIndex = 7
