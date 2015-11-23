'''
    Course: EECS 215 Fall 2015

    Name:  chih-wei yang
    Student id: 34564196
    email address: chihwey@uci.edu
    Assignment: hw3
    Filename : knapsack.py

    I hereby certify that the contents of this file represent
    my own original individual work. Nowhere herein is there
    code from any outside resources such as another individual,
    a website, or publishings unless specifically designated as
    permissible by the instructor or TA.
'''

from numpy import transpose
name=raw_input("type the file name:")
handle=open(name)

temp=[]
in_data=[]
items=[]
items_recoder=[]
items_report=[]
items_result=[]
weight=[]
value=[]
flag=[]

'''
=> read file and store it in array
'''

i=0
for line in handle:
    word=line.rstrip()
    if i ==0:
        W=int(line)
    else:
        temp.append(word.split(' '))
    i=i+1

in_data=transpose(temp)
items=in_data[0]
weight=in_data[1]
value=in_data[2]

k=[0 for i in range(W+1)]

'''
=> do the Dynamic Programming
'''

for w in range(0,W+1,1):
    j=0
    for i in range(0,len(weight)):
        if(int(weight[i])<=w):
            k[w]=k[(w-int(weight[i]))]+int(value[i])
            flag.append(k[w])
            items_recoder.append(int(items[i]))
    # record the items in every Iteration
    for index in range(0,len(flag)):
        if ((flag[index] == max(flag)) and  j==0):
            j=j+1
            items_report.append(int(items_recoder[index]))
    if (len(flag)<=0):
        items_report.append(0)
        k[w]=0
    else:
        k[w]=max(flag)
'''
=> trace the optimal subset by existing table
'''

items_result.append(items_report[W])
cur_weight=W

while(1):
    if (cur_weight<=0):
        break
    item_w=int(weight[int(items_report[cur_weight]-1)])
    cur_weight=cur_weight-item_w
    x=int(items_report[cur_weight])
    items_result.append(x)

items_result.remove(0)

'''
=>give the result

'''

print (k[len(k)-1])
print(items_result)



