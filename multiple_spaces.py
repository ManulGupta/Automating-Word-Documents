import win32com.client as win32
import regex as re

wdFindContinue = 1
wdReplaceAll = 2

word = win32.gencache.EnsureDispatch('Word.Application')
word.DisplayAlerts = 0
word.Visible = True
password= input("Please enter the password: ")

doc = word.Documents.Open("C:\\Users\\VAMSI\\Desktop\\as\\te.docx")
# doc.Protect(0, True, password, False, False)
# protecttype = doc.ProtectionType
for sentence in doc.Sentences:
     x = re.findall(r'\w+\s\s+\w+', str(sentence))
     if x:
         print(x)
         for i in x:
            x1 = re.sub(r'\s\s+', " ", str(i))
            word.Selection.Find.Execute(i, False, False, False, False, False, True, wdFindContinue, False,x1,wdReplaceAll)
