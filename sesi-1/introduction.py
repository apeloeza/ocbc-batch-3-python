print(12312379128312)
print(10)
print(type(10))

#floating-point Number
print(4.2)
print(type(4.2))
print(4.)
print(2.)
print(.4e7)
print(4.2e-4)

#strings
print("hactiv8")
print(type("hactiv8"))
print("this string contains a single quote (')character.")
print('this string contains a double quote (")character.')

#boolean
print(type(True))
print(type(False))
print(100>200) #False
print(100 == 200) #False
print(100<200) #True

#variabel assignment
n = 300
print (n)
a=b=c=300
print(a,b,c)

#variable names
name = "Hactiv8"
Age =54
has_laptops=True
print(name, Age, has_laptops)

#operators and expressions
a=10
b=20
print(a+b)
print(a+b-5)

#arithmetic Operators
a=4
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

#comparison Operators
a=10
b=20
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)

#string manipulation
s='foo'
t='bar'
# +and*Operators
print(s+t)
print(s*4)
#case conversion
print(s.capitalize())
print(s.lower())
print(s.swapcase())

#Python lIST
a=['foo','bar','baz','qux']
print(a)
#modifying List Value
a=['foo','bar','baz','qux','quux','colge']
a[2]=10
a[-1]=20
print(a)
#change several contigous
a=['foo','bar','baz','qux','quux','corge']
print(a[1:4])
a[1:4]=[1.1,2.2,3.3,4.4,5.5]
print(a)

#phyton Tuples
t=('foo','bar','baz','qux','quux','corge')
print(t)
print(t[0])
print(t[-1])
#packing and unpacking
(s1,s2,s3,s4)=('foo','bar','baz','qux')
print(s1)

#devining and accessing Dictionary
MLB_team={
    'Colorado': 'Rockies',
    'Boston':'Red Sox',
    'Minnesota':'Twins',
}
print(MLB_team['Minnesota'])
#Adding an entry to an existing dictionary
MLB_team['Kansas City'] = 'Royals'
MLB_team

#building a dictionary incrementally
person={}
person['frame']='hack'
person['lname']='8'
person['age']=51
person['children']=['Ralph','Betty','Joey']
person['pets']={'dog','Fido','cat','Sox'}
print(person)
print(person['children'][1])

