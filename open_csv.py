import os
import csv


def read_csv(filename, location=None, poprows=None, delimiter=None):
    if location==0:
        filepath = filename
    elif location!= None and location!=0:
        filepath = str(location) + str(filename)
    else:
        filepath = str(os.getcwd()) + str('\\') + str(filename)

    if delimiter=='\t':
        delim = '\t'
    else:
        delim = ','

    with open(filepath, 'r') as infile:
        data = csv.reader(infile, delimiter=delim)
        datalist, rows = [], []
        for row in data:
            datalist.append(row)
        if poprows!=None:
            for i in range(poprows):
                datalist.pop(0)
        for j in range(len(datalist[0])):
            globals()['string%s' % j] = []
            for k in datalist:
                globals()['string%s' % j].append(float(k[j]))
            rows.append(globals()['string%s' % j])
        infile.close()

    return rows



