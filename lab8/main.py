from openpyxl import Workbook
from config import *

fn = file_name
wb = Workbook()
ws = wb.active

ws.append(['1', '2', '3'])
ws.append(['1','2','3'])
ws.append(['1','2','3'])
wb.save(fn)
wb.close()
