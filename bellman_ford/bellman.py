'''
    Course: EECS 215 Fall 2015

    Name:  chih-wei yang
    Student id: 34564196
    email address: chihwey@uci.edu
    Assignment: hw3
    Filename : bellman.py

    I hereby certify that the contents of this file represent
    my own original individual work. Nowhere herein is there
    code from any outside resources such as another individual,
    a website, or publishings unless specifically designated as
    permissible by the instructor or TA.
'''

from numpy import transpose

temp=[]
in_data=[]
Sour=[]
Dist=[]
W=[]
adj_node=[]

'''
=> read the file and store those information on array
'''

name=raw_input("type the file name:")
handle=open(name)
i=0
for line in handle:
    word=line.rstrip()
    if i==0:
        node=int(line)
        vector=[[float('Inf') for j in range(node)] for j in range(node)]
    else:
        temp.append(word.split(' '))
    i=i+1
edges=(i-1)
in_data=transpose(temp)
Sour=in_data[0]
Dist=in_data[1]
W=in_data[2]
adj_node=[[float('Inf')for i in range(node)]for i in range(node)]

'''
=>initialization the vector table of each node(2D array)
'''

for i in range(node):
    vector[i][i]=0
    for j in range(node):
        adj_node[i][j]=j

for i in range(edges):
    vector[int(Sour[i])][int(Dist[i])]=W[i]

'''
=> start doing bellman-ford(vector-protocal)

'''

for i in range(node):
    for j in range(node):
        for neighbor in range(node):
            if neighbor!=i and (float(vector[neighbor][j])!=float('Inf')):
                if float(vector[i][j]) > float(vector[i][neighbor])+float(vector[neighbor][j]):
                    vector[i][j]=float(vector[i][neighbor])+float(vector[neighbor][j])
                    adj_node[i][j]=neighbor
#print the reuslt
#target=open("output",'w')
'''
=> show the result on screen
'''

for i in range(len(vector)):
    print "node ",i
    for j in range(len(vector)):
        if vector[i][j]!=0:
            print j,adj_node[i][j],vector[i][j]
    #print (vector[i][:])
#target.close

