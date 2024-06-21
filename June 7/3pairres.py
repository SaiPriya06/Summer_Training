def com(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
    fun([],0)
a=[3,5,1,6,7]
k=3
com(a,k)