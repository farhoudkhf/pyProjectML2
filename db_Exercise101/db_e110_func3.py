import sys
sys.path.append('./dbFunction')
import db_e109_func2

from db_e109_func2 import xSQL

sql = '''SELECT * from product'''
print(f"this is External func for xSQL: {xSQL(sql)} endPrint.")
