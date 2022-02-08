''' 
def sorting():
    list1 = []
    n = int(input("Enter the number of elements you want in the list :"))
    for i in range(n):
        elements = input("Enter the values one by one: ")
        list1.append(elements)
    print("Elements Entered in the List are:", list1)
    list1.sort()
    print("Elements after sorting are: ", list1)

    
sorting()
''' 

list1 = []    # this list holds all the characters

list2 = []    # this list holds the characters along  with special characters

n = int(input("Enter the number od values you will enter"))

for i in range(n):
    values = input("Enter the values for the List: ")
    list1.append(values)
print("Values entered in the list are: ", list1)
val = input("Enter the Element you want to replace with * :")
for i in range(n):
    if list1[i] != val:
        list2.append("*")
    else:
        list2.append(list1[i])
print("Values in list after replacing the characters are: ", list2)


