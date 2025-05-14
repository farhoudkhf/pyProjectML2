import sys
sys.path.append('./dbFunction')
import dbFuncs

from dbFuncs import xSQL

sql = '''SELECT * from product'''
print(f"this is External func for xSQL: {xSQL(sql)} endPrint.")
