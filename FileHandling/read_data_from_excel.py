import openpyxl
wb = openpyxl.load_workbook("C://Users//sivan//PycharmProjects//Guvi_PythonSelenium//FileHandling//Data.xlsx")
sheet = wb['student']
value = sheet['A5'].value
print(value)

for row in sheet.iter_rows(values_only=True):
    print(f"{row}: type: {type(row)}")
    for r in row:
        print(r)

sheet['A8'] = 'Yamini'
sheet['B8'] = 'Yamini@123'
sheet['A9'] = 'Pooja'
sheet['B9'] = 'Pooja@123'
wb.save("C://Users//sivan//PycharmProjects//Guvi_PythonSelenium//FileHandling//Data1.xlsx")


