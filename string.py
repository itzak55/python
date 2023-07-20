fruits='banana'
#index of string
print(fruits[2])

#slice of string
print(fruits[0:4])  #lenght is final index- intial index
print(fruits[:4])
print(fruits[0:])
print(fruits[:])

#string are immutable so we can not changestring
newstrng='B'+fruits[1:6]
print(newstrng)

#while loop in string
index=0
while index< len(fruits):
    letter=fruits[index]
    print(letter)
    index=index+1

#counting a letter in string
count=0
for x  in fruits:
    if x=='a':
        count=count+1
    
print(count)


for x in fruits:
    print(x)

#in operatotr
x='a' in fruits
print(x)

y='c' not in fruits
print(y)

#string method
print(dir(fruits))
    
newword=fruits.upper()
print(newword)

up=fruits.capitalize()
print(up)

z=fruits.find('a')
print(z)

line=' HI I AM AMIT KUMAR '
Q=line.strip()
print(Q)

w=line.startswith('')
print(w)


#parsing a string(find substring)
str='Often, we want to look into a string and find a substring. For example if we were presented a series of lines formatted as follows'


r=str.find('look')
print(r)

t=str.find('.')
print(t)

print(str[18:57])


#format string



