A="Ram is a God"
print(A)
print(A[4:2])

a=input('Enter a  name')
print(len(a))
print(a.capitalize()) 

a="MADAM"
b=a[-1::-1]
if(a==b):
    print("Palindrome")
else:
    print("Not Palindrom")    

print(a)
print(b)


i=1
while(i<=10):
    i=i+1
print("Hii iam Coder",i)


#list###
a=[10,"Ear",20,"Gun"]
print(a)
print(a[1])
print(a[1:-2])


### Operators List #####
A=[110,33094,7887,"Sural","Joap"]
print(A)
del A[2]
print(A)
A[2]="Anvesh"
print(A)



#list Complasd#####
A = [1, 2, 3, 4, 50, 60, 23438]
print(A)           # Print the original list
print(max(A))      # Find and print the maximum value
print(A)           # Print the list again (remains unchanged)

An = [200,300,400500,503]
print(An)
print(min(An))
print(An)


A = [1, 2, 3]
B = [1, 2, 4]

# Using comparison operators
if A < B:
    print("-1: A is less than B")
elif A > B:
    print("1: A is greater than B")
else:
    print("0: A is equal to B")


An = int(input("Enter a number"))
Bn =int(input("Enter a  number"))

if An > Bn:
    print("An is grater then Bn")

elif An<Bn:
    print("Bn is a grater than An")

else:

    print("dfhyj")



# Create a list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

mylist = [23,34,5,4]
mylist .append(4509)
print(mylist)
mylist.count(23)



mylist = [23, 34, 5, 4, 4509]
mylist.reverse()
print(mylist)  # Output: [4509, 4, 5, 34, 23] 
mylist.pop(3) 
print(mylist)