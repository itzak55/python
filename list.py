lst=['ram','shyam','sita'] #create list
print(lst)
print(lst[1]) #index
lst[2]='geeta' #update
print(lst)
for x in lst:  #travese
    print(x)
print(lst[0:1]) #slice

lst1=[1,2,3]
lst2=[4,5]

c=lst1+lst2 #concate two list

print(c)
lst3=lst2*4 #
print(lst3)

t=['a','b','c','d','e']
t[1:3]=['x','y']
print(t)

t.append('f') #add new element
print(t)

t.sort()
print(t)

t1=['a','b']
t2=['c','d']
t1.extend(t2)
print(t1)

f=t.pop(1)
print(f)
print(t)

#string to list
j='spam'
h=list(j)
print(h)

#string of word
c='hi i am amit kumar'
z=c.split()
print(z)

#delimiter  (can we use more than one delimiter)
s='spam-spam spam'
delimiter='-'

d=s.split(delimiter)
print(d)

k=['pining','for','for','fjrods']
delimiter=' '
l=delimiter.join(k)
print(l)

#parasinf lines







