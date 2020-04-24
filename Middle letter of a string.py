#Program to find middle letter of a string

#program 1 when string is odd
a="mycomputers"
l=len(a)
print(a[(l//2)])

#program 1 when string is even
a="mycomputer"
l=len(a)
print(a[(l//2)])


#another way of finding middle letter in string
a="mycomputer"
length=int(len(a)/2)
print(a[length])
i=(a[length])
print(len(i))

a="mycomputer"
l=len(a)
print(a[(l-1)//2])

a="mycomputers"
l=len(a)
print(a[(l-1)//2])

#output
#p
#p
#p
#1
#m
#p
