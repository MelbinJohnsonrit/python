list1=input("Enter colors for list 1 (seperated by space):").split()
list2=input("Enter colors for list 2 (seperated by space):").split()
new_list= list(set(list1)-set(list2))
print (new_list)
