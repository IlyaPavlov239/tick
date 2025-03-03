class passenger:
    def __init__(self, n, surn, arr, dep, t,tr):
        self.arr=arr
        self.dep=dep
        self.t=int(t.split()[0])*60+int(t.split()[1])
        self.n=n
        self.surn=surn
        self.tr=tr