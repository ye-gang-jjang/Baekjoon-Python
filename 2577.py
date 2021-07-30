n1 = int(input())
n2 = int(input())
n3 = int(input())

result = list(str(n1 * n2 * n3))
for own_ten in range(10):
    print(result.count(str(own_ten)))
"""
shot
ex)1
exec('n,m=0,1'+'*int(input())'*3+';print(str(m).count(str(n)));n+=1'*10)

ex)2
i=1;exec('i*=int(input());'*3)
for n in range(10):
    print(str(i).count(str(n)))

ex)3
n=list(str(int(input())*int(input())*int(input())))
for i in range(10):
    print(n.count(str(i)))
"""
