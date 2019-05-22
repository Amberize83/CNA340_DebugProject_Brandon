def lone_sum(a, b, c):
    if a == b and b == c and a == c: # 0 will be returned if all values are equal0
        return 0
    elif a == b: #IF "a" is equal to "b" then the value of "c" is returned
          return c
    elif a == c: #If "a" is equal to "c" then the value of "b" will be returned
        return b
    elif b == c: #If "b" is equal to "c" then the value of "a" will be returned
        return a
    else: #If  none of the above have been initiatiated, the value of "a", "b", and "c" will be added
        return a + b + c

print (lone_sum(1,2,3)) #check if none are the same
print (lone_sum(7,7,7)) #check if all are the same
print (lone_sum(1,1,3)) #check if "a" and "b" are the same (return "c")
print (lone_sum(1,2,1)) #check if "a" and "c" are the same (return "b")
print (lone_sum(1,2,2)) #check if "b" and "c" are the same (return "a")

#Changes made code works 
