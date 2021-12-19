import json

ff = open('yourrealdata.txt', 'a+', encoding='utf-8')
with open('telegramdatabase.txt', 'r', encoding='utf-8') as f:
    for x, i in enumerate(f, start=1):
        if x % 2 == 0:
            ff.write(i)



def makingfunc():
    ff = open('dataset.txt', encoding='utf-8')
    data = [x.replace('\n', '') for x in ff.readlines()]
    global database
    database = []
    for x in data:
        data1 = json.loads(eval(x)['message'])
        database.append([data1['first_name'], data1['last_name'], data1['phone'], data1['id']])
makingfunc()

