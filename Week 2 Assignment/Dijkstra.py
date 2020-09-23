import datetime
from heapq import heapify,heappush,heappop
size=0
n=200
sp=[-1 for i in range(0,n)]

def getparent(heap,ind):
    pind=(ind-1)//2
    if pind<0:
        return -1
    else:
        return pind

def getrcd(heap,ind):
    rcd=2*ind+2
    if rcd<len(heap):
        return rcd
    else:
        return -1
    
def getlcd(heap,ind):
    lcd=2*ind+1
    if lcd<len(heap):
        return lcd
    else:
        return -1

def swap(heap,pind,ind):
    temp=heap[pind]
    heap[pind]=heap[ind]
    heap[ind]=temp

def heappop2(heap,ele):
    global size
    ind=-1
    for i in range(0,len(heap)):
        if heap[i][1]==ele:
            ind=i
            break
    if ind==-1:
        return ind
    else:
        ele=heap[ind]
        heap[ind]=heap[size-1]
        heap.pop()
        size-=1
        rcd=getrcd(heap,ind)
        lcd=getlcd(heap,ind)
        while rcd!=-1 and lcd!=-1 and (heap[ind][0]>heap[rcd][0] or heap[ind][0]>heap[lcd][0]):
            minm=lcd
            if heap[rcd][0]<heap[minm][0]:
                minm=rcd
            swap(heap,ind,minm)
            ind=minm
            rcd=getrcd(heap,ind)
            lcd=getlcd(heap,ind)
        return ele
    
def dijkstra(alist,a,s):
    heap=[]
    global sp
    global size
    for i in range(0,n):
        if i!=s:
            heap.append((10**5,i))
        else:
            heap.append((0,i))
        size+=1
    heapify(heap)
    for i in range(0,n):
        ele=heappop(heap)
        size-=1
        sp[ele[1]]=ele[0]
        w=ele[1]
        for j in range(0,len(alist[w])):
            dv=alist[w][j]
            if sp[dv]==-1:
                w1=heappop2(heap,dv)
                newval=min(w1[0],sp[w]+a[w][dv])
                heappush(heap,(newval,dv))
                size+=1
        
print(datetime.datetime.now())
fo=open("foo.txt")
list1=fo.readlines()
a=[[0 for i in range(0,n)] for j in range(0,n)]
alist=[[] for j in range(0,n)]

for i in list1:
    ind=i.split()[0]
    for k in i.split():
        j=k.split(",")
        if len(j)>1:
            alist[int(ind)-1].append(int(j[0])-1)
            a[int(ind)-1][int(j[0])-1]=int(j[1])
            
print(datetime.datetime.now())
dijkstra(alist,a,0)
print(datetime.datetime.now())
for i in [7,37,59,82,99,115,133,165,188,197]:
    print(sp[i-1])
        
