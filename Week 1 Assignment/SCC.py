from collections import deque
n=875714
t=0
f=[0 for i in range(0,n)]							# for storing finishing time.
v=[0 for i in range(0,n)]							#for checking visited or not, v[i]=1 or 0.
l=[0 for i in range(0,n)]							#for storing leaders of each node.
s=0										#temporary storage for leader's node index.

def dfs_loop(G):
    global s
    global v
    for i in range(n-1,-1,-1):
        if v[i]!=1:
            s=i
            dfs(G,i)


def dfs(G,i):										#iterative dfs function because running recursive one is not possible due to recursion limit in python.
    global t
    global f
    global l
    stk=deque()							                # for storing index whose edges has to be explored.
    stk.append(i)
    stk1=deque()
    v[i]=1
    l[i]=s
    while(len(stk)!=0):
        so=stk.pop()
        stk1.append(so)							        # need to store all the popped vertices to correctly give finishing time. not needed in case of recursive one.
        for j in range(0,len(G[so])):
            if v[G[so][j]]!=1:
                v[G[so][j]]=1
                l[G[so][j]]=s
                stk.append(G[so][j])
                
    while(len(stk1)!=0):                            # using the stack1 to assign correct f[i] value
        i=stk1.pop()
        f[i]=t
        t+=1

fo=open("foo.txt","+r")
list1=fo.readlines()
list2=[[int(i) for i in j.split()] for j in list1]
print("69 mb file of only text phew....reading input completed...")
Grev=[[] for i in range(0,n)]
for i in list2:
    Grev[i[1]-1].append(i[0]-1)
dfs_loop(Grev)
print("First pass over...")    
G=[[] for i in range(0,n)]
for i in range(0,n):
    for j in range(0,len(Grev[i])):
        Grev[i][j]=f[Grev[i][j]]
        G[Grev[i][j]].append(f[i])
v=[0 for i in range(0,n)]
dfs_loop(G)
print("Second Pass completed...")
le=[0 for i in range(0,n)]
for i in l:
    le[i]+=1
le=sorted(le,reverse=True)
print(le[0:5])
