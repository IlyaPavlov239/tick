class ticket:
    def __init__(self, arr, dep, t, n):
        self.arr=arr
        self.dep=dep
        self.t=int(t.split()[0])*60+int(t.split()[1])
        self.n=n