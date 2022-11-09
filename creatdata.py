import json

twowords=set()
stopwords=set()

for line in open("vietdict.txt", 'r'):
    a=json.loads(line)
    t_str=a["text"]
    tmp=str.split(t_str)
    if (len(tmp)==2):
        set.add(twowords,t_str)

for line in open("vietnamese-stopwords.txt", 'r'):
    set.add(stopwords,line[:-1])
