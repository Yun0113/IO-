import json

fr=open("C:/Users/Administrator/Documents/student.csv","r",encoding='utf-8')
ls=[]
for line in fr:
    line=line.replace("\n","")
    ls.append(line.split(","))
fr.close()
fw=open("C:/Users/Administrator/Documents/student.json","w",encoding='utf-8')
for i in range(1,len(ls)):
    ls[i]=dict(zip(ls[0],ls[i]))
b = json.dumps(ls[1:],sort_keys=True,indent=5,ensure_ascii=False)
print(b)
fw.write(b)
fw.close()
