'''This code is used to modify my_set, my_dict and global_variable'''

global_variable =100

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(numbers): # add numbers as parameter 
        global global_variable
        local_variable =5
        # numbers = [1, 2, 3, 4, 5] #this number need not to be used

        while local_variable >0 :
                if local_variable % 2 == 0: # if local_variable is even
                        numbers.remove(local_variable) # remove even elements from numbers set
                local_variable -= 1         # decrease local_variable by 1 until local_variable is 0
        return numbers    #return numbers set in which elements are all odd and without even

my_set={1,2,3,4,5,5,4,3,2,1}
result =  process_numbers(numbers=my_set)

def modify_dict():  # used to modify dict and add new element into dict
        local_variable = 10
        my_dict['key4']= local_variable  # add new element 'key4': 10 into my_dict
# modify_dict(5)  #no need to use parameter
modify_dict()  #no need to use parameter, delete parameter 5 from modify_dict(5)      

def update_global():
        global global_variable
        global_variable += 10  #increase global_variable by 10
update_global()  # add update_global() to use function to change global_variable

for i in range(5):
        print(i)
        i+=1        #print i from 0 to 4 

if my_set is not None and my_dict['key4'] == 10:  # it will be true since key4 is added into my_dict
        print("Condition met!")

if 5 not in my_dict:    #my_dict doesn't have 5 in keys, so it will be true, and print "5 not found in the dictionary!"
        print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)