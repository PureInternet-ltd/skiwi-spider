
import csv
import io

with io.open('test.csv', 'w', encoding="utf-8") as csvfile:
    csvfile.write('\ufeff')
    spamwriter = csv.writer(csvfile, dialect='excel')
    spamwriter.writerow(['测试'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])