import csv
data=[]
with open(r"C:\Users\21629\Desktop\Pratique pfe\contiki\dataset\communication.txt", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        data.append(row[2])
c=[]
for i in data:
    x=i[i.find('CH')+3:-1]
    y=i[i.find('ID')+3:i.find('from')-1]
    c.append(y+"-"+x)
cc=list(dict.fromkeys(c))
print(cc)