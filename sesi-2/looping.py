#python while" Loops
n=5
while n>0: 
    n-=1
    print(n)
print("===============================")
i = 1
while i<6:
    print(i)
    i +=1
print("===============================")
# The python break and continue Statements
n=5
while n>0: 
    n-=1
    if n==2:
        break #break Statement
    print(n)
print('Loop ended.')
print("===============================")
#the else clause
n=5
while n > 0:
    n -=1
    print(n)
else:
    print('loop done.')
    print("===============================")
#was exhausted
n=5
while n>0:
    n-=1
    print(n)
    if n == 2:
        break
    else:
        print('Loop done.')
# infinite Loops
# while True: print('foo')
#nested while oops
#similarly
a=['foo','bar']
while len(a):
    print(a.pop(0))
    b=['baz','qux']
    while len(b):
        print('>',b.pop(0))
#one-line while loops
print("------------------")
n=5 
while n>0 : n -=1; print(n)
print("------------------")
#the Pyhon for loop
a=['foo','bar','baz']
for i in a: print(i)
print("------------------")
d = {'foo':1,'bar':2,'baz':3} 
for k in d: print(k)
print("------------------")
for k in d: print(d[k])
print("------------------")
for k in d.values(): print(k)
for k, v in d.items(): print (k, ":", v)
print("-------------")
for i in ['foo','bar','baz','qux']: 
    if 'b' in i:
        break
    print(i)
#continue
for i in ['foo','bar','baz','qux']:
    if 'b' in i:
        print(i)

for i in ['foo','bar','baz','qux']:
    if i == 'bar':
        break
    print(i)
else:
    print('done.')
