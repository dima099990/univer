from openpyxl import Workbook
from config import *

fn = file_name
wb = Workbook()
ws = wb.active

columns=['id','name', 'occupation'])
ws.append(['№ п\п', 'статьи затрат', '2014','2015','отклонения'])
ws.append(['1','2','3'])
ws.append(['1','2','3','4','5','6','7','8','9'])
wb.save(fn)
wb.close()
