
import csv

with open('test.csv', 'w') as csvfile:
    csvfile.write('\ufeff')
    spamwriter = csv.writer(csvfile, dialect='excel')
    spamwriter.writerow(['测试'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])