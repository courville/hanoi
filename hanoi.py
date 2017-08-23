#!/usr/local/bin/python3

def hanoi(n):
    towers=[[], [], []]
    N=n
    for i in range(n,0,-1):
        towers[0].append(i)
    # n source buffer destination
    def hanoib(n,s,b,d):
        if n<=0:
            return
        else:
            # n-1 s->b with d as b
            hanoib(n-1,s,d,b)
            # s top -> d
            top=towers[s].pop(-1)
            print("Next move: disk",top,"from tower",s+1,"to tower",d+1)
            input("Press Enter to continue...")
            towers[d].append(top)
            atowers(N)
            # n-1 b->d with s as b
            hanoib(n-1,b,s,d)
    def adisk(k,n):
        # find closest round up odd integer to have a middle for | when there is a number of disk that is leading to str of even chars
        s=(len(str(n)) & (-2))+1
        # this is the padding on each side
        p=(int)(s/2)
        if k==0:
            return((n+1+p)*" "+"|"+(n+1+p)*" ")
        elif k>n:
            return((2*n+2+2*p+1)*"-")
        else:
            return((n-k)*" "+"<"+k*"-"+str(k).zfill(s)+k*"-"+">"+(n-k)*" ")
    def atowers(n):
        d="   "
        for i in range(n,0,-1):
            res=""
            for j in range(3):
                l=len(towers[j])
                if (i>l):
                    res=res+adisk(0,n)+d
                else:
                    res=res+adisk(towers[j][i-1],n)+d
            print(res)
        plateau=adisk(n+1,n);
        print(3*(plateau+d))
    atowers(N)
    hanoib(n,0,1,2)
    print("Task complete: this is the end...")

hanoi(5)
