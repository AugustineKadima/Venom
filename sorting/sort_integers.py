'''Given an unsorted array of integers, 
   write a function to sort all
   integers in ascending order
'''

'''
input: nums = [7,4,8]
output:[4,7,8]

------------------------------
input = [7,4,8]
output = [4,7,8]
----------------------------
input: nums = [7,4,8,1]
[4,7,8,1]
[4,1,8,7]
[1,4,8,7]
[1,4,7,8]


pseudocode
-----------
function
loop
create a temp variale
return list of integers

'''

def sort_integers(array_x):
    if len(array_x) < 2: 
        print("Already sorted")
        return array_x

    elif len(array_x) >= 2:
        n = len(array_x)
        for i in range(n):
           for j in range(n):
               if array_x[i] < array_x[j] and i != j:
                   temp = array_x[j]
                   array_x[j] = array_x[i]
                   array_x[i] = temp
        return array_x
        
    else:
        print("Only interger arrays allowed")
        return -1

results = sort_integers([8,6])
print(results)