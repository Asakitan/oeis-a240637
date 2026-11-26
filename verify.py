"""Brute-force first canonical ladder arrays and check the rational identity."""
from itertools import product
def count(n):
    nbr=[[j for j in range(2*n) if abs(i//2-j//2)+abs(i%2-j%2)==1] for i in range(2*n)]
    c=0
    for word in product(range(4),repeat=2*n):
        m=0
        for v in word:
            if v>m: break
            m=max(m,v+1)
        else:
            c+=all(sum(word[j]==word[i] for j in nn)%2==0 for i,nn in enumerate(nbr))
    return c
def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): z[i+j]+=u*v
    return z
if __name__=='__main__':
    values=[count(n) for n in range(1,5)]
    assert values==[1,5,27,193]
    d2=[1,0,-1]; d4=[1,-6,-9]; common=mul(d2,d4)
    out=[0]*7
    for w,pp,dd in [(1,[0,12,16],d2),(6,[0,2,4],d4),(8,[0,0,1],common)]:
        for i,c in enumerate(mul(pp,dd)): out[i]+=w*c
    assert out==[24*u for u in (0,1,-1,-13,-13,2,3)]
    print('Canonical-array counts:',values,'; full Burnside rational identity passed.')
