import openpyxl


file_path=("C:\Python_Selenium\Selenium\PythonSelenium\WriteData.xlsx")

workbook=openpyxl.load_workbook(file_path)  #workbook
sheet=workbook.active  #sheet, when there is only 1 sheet, can use "active" key



#will write same data in all rows,columns:
for r in range(1,6):
    for c in range(1,4):
        sheet.cell(r,c).value="Rony";

#saving the workbook after entering data:
workbook.save(file_path)

