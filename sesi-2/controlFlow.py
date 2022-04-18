
x=0
y=3
if x<y: print('yes')   #true
if y<x: print('yes')   #false not tampil
if x: print('yes')     #false not tampil
if y: print('yes')      #true
if 'aul' in 'grault': print('yes')              #true
if 'quux' in ['foo','bar','baz']: print('yes')  #false not tampil

#grouping statements: identation and blocks
if 'foo' in ['bar','baz','qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')

print('After Conditional')

#does line execute?
if 'foo' in ['foo','bar','baz']:            #yes
    print('Outer condition is true')        #yes

    if 10>20: print('inner condition 1')    #no

    print('Between inner conditions')       #yes

    if 10<20: print ('inner condition 2')   #yes

    print('End of outer condition')         #yes
    print('Apter outer condition')          #yes

#the else and elif clauses
x=20
if x<50: 
    print('(first suite)')  #true
    print('x is small')     #false
else:
    print('(secoond suite)')    #true
    print('x is large')         #false

x=120
if x<50: 
    print('(first suite)')  #true
    print('x is small')     #false
else:
    print('(secoond suite)')    #true
    print('x is large')         #false    

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup")


hargaBuku = 20000
hargaMajalah= 50009
uang = 2000

if uang>hargaBuku: print("beli buku")
elif uang>hargaMajalah: print("beli majalah")
else: print("uang tidak cukup")

name = 'Fred'
if name == 'Fred': print ("hello Fred")
elif name == 'Xnder': print ("hello Xander")
elif name == 'Hactiv8': print("Hello Hactiv8")
elif name == 'Arnold': print("Hello Arnold")
else: print("I don't know who you are!")

if 'a' in 'bar': print('foo')
elif 1/10: print ("this won't happen")
elif var: print("this won't either")

#One-line Statements
if 'a' in'foo': print('1');print('2'); print('3')
# multiple statement
x=2
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

x=3
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')
#while all of this work
x=3
if x == 1: print('foo'), print('bar'), print('baz')
elif x == 2: print('qux'), print('quux')
else: print('corge'), print('grault')

#conditional expressions (Python's ternary Operator)
raining = False
print("Let's go to the", 'beach' if not raining else ' library')

raining = True
print("Let's go to the", 'beach' if not raining else ' library')

age=12
s='teen' if age < 21 else 'adult'
print(s)

'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'

#the python pass statement
if True: print ('foo')

if True:
    pass

    print('foo')