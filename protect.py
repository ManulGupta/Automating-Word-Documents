import win32com.client as win32

word = win32.gencache.EnsureDispatch('Word.Application')
word.Visible = False
doc = word.Documents.Open("fullpathofyourdoc.docx")

password= input("Please enter the password: ")

doc.Protect(0, True, password, False, False)                     
protecttype = doc.ProtectionType 
print("Protection Added!")

doc.SaveAs("fullpathofyourdoc.docx")
