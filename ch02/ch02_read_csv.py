# -*- coding -*-：utf-8
# filename: ch02_read_csv.py
#

import csv

filename = 'ch02-data.csv'

data = []

try:
    with open(filename) as f:
        reader = csv.reader(f)
        #原代码为
        #header = reader.next()
        #python3.5的csv.reader没有next方法,若一定要用
        #则可使用 reader.__next__()代替        
        allRows = [row for row in reader]
        header = allRows[0]
        data = allRows[1:]        
except csv.Error as e:
    print("Error reading CSV file at line %s: %s" % (reader.line_num, e))
    sys.exit(-1)

if header:
    print(header)
    print("==============")

for datarow in data:
    print(datarow)



##原书python2.7代码
##import csv
##
##filename = 'ch02-data.csv'
##
##data = []
##
##try:
##    with open(filename) as f:
##        reader = csv.reader(f)
##        header = reader.next()
##        data = [row for row in reader]
##except csv.Error as e:
##    print "Error reading CSV file at line %s: %s" % (reader.line_num, e)
##    sys.exit(-1)
##
##if header:
##    print header
##    print "=============="
##
##for datarow in data:
##    print datarow
