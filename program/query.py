#!C:\Users\LSS\AppData\Local\Programs\Python\Python37\python.exe
from buildTree import build
from display import displayTree
from display import displayTable
from remove import removeTree
from remove import removeTable
from relAlg import select


''' root = build('Suppliers', 'sid', 2)
page_name = displayTree(root)
print(root + ":" + page_name)
root = build('Supply', 'pid', 2)
page_name = displayTree(root)
print(root + ":" + page_name)'''

# print(select('Supply', 'sid', '>', "s18"))
removeTable('Temp_ca2a8a303204f9f50a5886601792f0')
