from math import comb, factorial
from itertools import permutations, product, combinations
from fractions import Fraction as F
checks=0
def check(a,b):
 global checks
 assert a==b,(a,b)
 checks+=1
# Explicitly enumerate restriction and overcounting cases.
p=list(permutations('ABCDEFG'))
check(sum(abs(x.index('A')-x.index('B'))==1 for x in p),2*factorial(6))
check(sum(x.index('A')<x.index('B')<x.index('C') for x in p),factorial(7)//factorial(3))
check(sum(x.index('A')<x.index('B') and x.index('C')<x.index('D') for x in p),factorial(7)//4)
check(len(set(permutations('BANANA'))),factorial(6)//(factorial(3)*factorial(2)))
check(sum(1 for x,y,z in product(range(13),repeat=3) if x+y+z==12 and x<=4),comb(14,2)-comb(9,2))
check(sum(1 for x,y,z in product(range(13),repeat=3) if x+y+z==12 and x<=4 and y<=3),comb(14,2)-comb(9,2)-comb(10,2)+comb(5,2))
check(sum(1 for x,y,z in product(range(13),repeat=3) if x+y+z<=12),comb(15,3))
check(sum(1 for x,y,z,w in product(range(17),repeat=4) if x+y+z+w==16 and x>=2 and y>=1 and w>=1 and z<=5),comb(15,3)-comb(9,3))
# Both poker straight conventions form complete, nonoverlapping partitions.
for s in [9,10]:
 high=(comb(13,5)-s)*(4**5-4)
 pair=13*comb(4,2)*comb(12,3)*4**3
 two=comb(13,2)*comb(4,2)**2*11*4
 triple=13*comb(4,3)*comb(12,2)*4**2
 straight=s*(4**5-4)
 flush=4*(comb(13,5)-s)
 full=13*comb(4,3)*12*comb(4,2)
 four=13*12*4
 sf=s*4
 check(sum([high,pair,two,triple,straight,flush,full,four,sf]),comb(52,5))
# Occupancy and run counts.
check(sum(len(set(x))==3 for x in product(range(4),repeat=9)),comb(4,3)*(3**9-3*2**9+3))
check(sum(len(set(x))==4 for x in product(range(4),repeat=6)),4**6-4*3**6+6*2**6-4)
for n,m,r in [(8,5,3),(7,4,2)]:
 count=0
 for inds in combinations(range(n+m),n):
  z=set(inds)
  runs=sum(i in z and (i==0 or i-1 not in z) for i in range(n+m))
  count+=runs==r
 check(count,comb(n-1,r-1)*comb(m+1,r))
# Derangements and combinatorial identities.
for n in range(1,8):
 d=sum(all(i!=x[i] for i in range(n)) for x in permutations(range(n)))
 check(F(d,factorial(n)),sum((F((-1)**j,factorial(j)) for j in range(n+1)),F(0)))
 check(sum(k*comb(n,k) for k in range(1,n+1)),n*2**(n-1))
 if n>=2:check(sum(k*k*comb(n,k) for k in range(1,n+1)),n*(n+1)*2**(n-2))
# Equivalent probability models and conditional samples.
check(F(comb(5,2)*4,comb(9,3)),3*F(5,9)*F(4,8)*F(4,7))
pairs=list(product(range(1,7),repeat=2))
check(F(sum(sum(x)%2==0 and 6 in x for x in pairs),sum(sum(x)%2==0 for x in pairs)),F(5,18))
for p in [F(1,2),F(2,3),F(1,4)]:
 check(sum(comb(k-1,3)*p**4*(1-p)**(k-4) for k in range(4,8)),sum(comb(7,j)*p**j*(1-p)**(7-j) for j in range(4,8)))
print(str(checks)+' independent mathematical checks passed.')
