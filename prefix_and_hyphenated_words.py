import win32com.client as win32
import re
word = win32.gencache.EnsureDispatch('Word.Application')
word.Visible = True
doc = word.Documents.Open("C:\\Users\\krupa\\Desktop\\20101.docx")


result = []
result2 = []
for word in doc.Sentences:
    result1 = re.findall(r'\w+(?:-\w+)+', str(word))
    result = result + result1
    result3 = re.findall(i.e, str(word))
    result2 = result2 + result3
print(result)
print(result2)