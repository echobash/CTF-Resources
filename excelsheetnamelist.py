import xlrd
import pprint
list_of_filenames=["backhoe.xlsx","compactor.xlsx","telehandler.xlsx"]
a=[]
#If we want to print all the sheetnames of excelworkbook then uncomment the following

for filename in list_of_filenames:
        xls = xlrd.open_workbook(filename, on_demand=True)
        a.append(xls.sheet_names()) # <- remeber: xlrd sheet_names is a function,it's a property
# pprint.pprint(a)
# print(len(a))
for items in a:
        for item in items:
                print(item)
