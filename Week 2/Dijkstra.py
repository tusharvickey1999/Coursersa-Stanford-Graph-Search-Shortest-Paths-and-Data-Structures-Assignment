import datetime
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

def heap_swap(heap,pind,ind):
    temp=heap[pind]
    heap[pind]=heap[ind]
    heap[ind]=temp

def heappush(heap, ele):
    global size
    heap.append(ele)
    size+=1
    ind=size-1
    if ind==0:
        return 0
    else:
        pind=getparent(heap,ind)
        while pind>=0 and heap[pind][1]>heap[ind][1]:
            heap_swap(heap,pind,ind)
            ind=pind
            pind=getparent(heap,ind)
        
def heappop(heap):
    global size
    ele=heap[0]
    heap[0]=heap[size-1]
    heap.pop()
    size-=1
    ind=0
    rcd=getrcd(heap,ind)
    lcd=getlcd(heap,ind)
    while rcd!=-1 and lcd!=-1 and (heap[ind][1]>heap[rcd][1] or heap[ind][1]>heap[lcd][1]):
        minm=lcd
        if heap[rcd][1]<heap[minm][1]:
            minm=rcd
        heap_swap(heap,ind,minm)
        ind=minm
        rcd=getrcd(heap,ind)
        lcd=getlcd(heap,ind)
    return ele

def heappop2(heap,ele):
    global size
    ind=-1
    for i in range(0,len(heap)):
        if heap[i][0]==ele:
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
        while rcd!=-1 and lcd!=-1 and (heap[ind][1]>heap[rcd][1] or heap[ind][1]>heap[lcd][1]):
            minm=lcd
            if heap[rcd][1]<heap[minm][1]:
                minm=rcd
            heap_swap(heap,ind,minm)
            ind=minm
            rcd=getrcd(heap,ind)
            lcd=getlcd(heap,ind)
        return ele
    
def dijkstra(alist,a,s):
    heap=[]
    global sp
    for i in range(0,n):
        if i!=s:
            heappush(heap,[i,10**5])
        else:
            heappush(heap,[i,0])
    for i in range(0,n):
        ele=heappop(heap)
        sp[ele[0]]=ele[1]
        w=ele[0]
        for j in range(0,len(alist[w])):
            dv=alist[w][j]
            if sp[dv]==-1:
                w1=heappop2(heap,dv)
                newval=min(w1[1],sp[w]+a[w][dv])
                heappush(heap,[dv,newval])
        
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
