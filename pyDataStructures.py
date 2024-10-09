# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:14:43 2024

@author: vaishnavi
"""

           #     PYTHON DATASTRUCTURES:-
                
'''There are 4 inbuilt data structuresin py
They are 1.list
         2.Tuple
         3.set
         4.Dictionary  '''
         
#LIST

li=['ysh',3,7.0,True,5,[2,3]]
print(li)

c=[5,6,"sunny"]
print(c[2])

#slicing

v=[True,'ysh,7,9.0']
print(v[1:2:2])
print(v[0])
v[0]=False
print(v)

#methods in list

c=[]
print(dir(c))

c.append("sunny")
print(c)

c.insert(0,89)
print(c)

c.append(34)
print(c)
print(c[0])
print(len(c))
print((c))

c.clear()
print(c)

a=[4,9,True,"kist",9.8,8]
b=[5,7,8,9,8]
c=b+a
print(c)

print(a)
f=[7,9,0,5,2]
f.sort(reverse=True) #sorting is possible for list
print(f)


                      #TUPLE:-
                       
t=(56,89,0,78,89,"ysh",.9)
print(t)

y=(7,9,6,8)
print(y[2])

u=(9,8,6)

print(u)
print(len(u))  #length method

u=(8,9,7)
v=(4,3,5)
k=u+v  #concatenation/adding 2 tuples
print(k)

 #Tuples won't append and sort


m=("utf",9,0.9,6,9,9,9,6,6,3,3)
print(m.index(9))    #index method
print(m.count(3))    # count of an element
 
                #SETS:-
                
h={1,3,6,8,99,3,5,67,0.9,"string",0.9}
print(h)   #no sorting no indexing no duplicates
print(len(h)) #length method

a=set()
print(dir(a))

a={8,7,5,78,90,45}
a.add(98)                 #add element
print(a)                   
a.remove(7)               # remove element
print(a)
a.update([8,5,"ysh",56])      #update set with multiple values   
print(a)
a.pop()
print(a)


   #set operations

a={8,9,6,5}
b={56,89,98,78,5,8}
print(a|b)   #union operation
print(a.union(b))
print(a&b)     #intersection 
print(a.intersection(b))
print(a-b)
print(b-a)
print(a.difference(b))
print(b.difference(a))




            #DICTIONARIES:-
            
a={1:"sunny",2:"bunny",3:"padma"}
print(a)
b={1:"kist",2:"puram"}
print(b[1])
print(b.get(2))      #get method

g={1:"kit",2:"cat"}   #mutable of dict
g[2]="kat"
print(g)

print(dir(a))

print(g.keys())     #keys method
print(g.values())   #to get values value() is used
print(g.items())     #to get items we use item()
print(len(g))
print(g.pop(2))
print(g)