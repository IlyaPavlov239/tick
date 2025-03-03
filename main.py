class ticket:
    def __init__(self, tr, n, arr, dep, t):
        self.tr=tr
        self.arr=arr
        self.dep=dep
        self.t=int(t.split(":")[0])*60+int(t.split(":")[1])
        self.n=n

class passenger:
    def __init__(self,surn, name, arr, dep, t,tr=0):
        self.arr=arr
        self.dep=dep
        self.t=int(t.split(":")[0])*60+int(t.split(":")[1])
        self.name=name
        self.surn=surn
        self.tr=tr

def sold(tickets):
    pas = []
    s = input()
    a = []
    while s != "":
        a = s.split(" ")
        k = passenger(a[0], a[1], a[2], a[3], a[4])
        for i in tickets:
            if i.t <= k.t and i.arr == k.arr and i.dep == k.dep and i.n > 0:
                tic.n -= 1
                pas.tr = tic.tr
        s = input()
        pas.append(k)
    return pas
print("Поезда (номер, билеты, отправление, прибытие, время):")
tickets=[]
s=input()
a=[]

while s!="":
    a=s.split(" ")
    tickets.append(ticket(a[0],int(a[1]),a[2],a[3],a[4]))
    s=input()

print("Пассажиры(фамилия, имя, отправление, прибытие, время")
pas=sold(tickets)

print("Номер\tОтправление\tПрибытие\tВремя\tБилеты")
time=""
for i in tickets:
    time="%d:%d" %(i.t//60,i.t%60)
    print("%s\t\t%s\t\t%s\t\t%s\t\t%d" %(i.tr,i.arr,i.dep,time, i.n))

print("Фамилия\tИмя\tОтправление\tПрибытие\tВремя\tНомер")
time=""
for i in pas:
    time="%d:%d" %(i.t//60,i.t%60 if i.t%60!=0 else "00")
    print(time)
    #print("%s\t\t%s\t\t%s\t\t%s\t\t%s" %(i.surn,i.name,i.arr,i.dep,time, i.tr))
