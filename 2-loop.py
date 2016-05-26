######################  Loop: while  ##############################
# Set password
actual_password = input("Set your password: ")
password = input("Enter your password angain: ")
while password != actual_password:
	print("Two inputs do not match!\n") 
	actual_password = input("Set your password: ")
	password = input("Enter your password angain: ")
else:
	print("Password is set!\n") 

#######################  Loop: for  ###############################
# Dict: no order!!!
print("For dictionary")                
profile_dict = {"Name": "Alex", "Age": 24, "Gender": "Male"} 
for elem in profile_dict:              
    print(elem, ":", profile_dict[elem])
#>>> For dictionary
#>>> Gender : Male
#>>> Name : Alex
#>>> Age : 24
 
# List: has order!!!
print("\nFor list")                    
profile_list = ["Alex", "24", "Male"]  
for index in range(len(profile_list)):
    if not index-0:
        print("Name:",profile_list[0])
    elif not index-1:
        print("Age:",profile_list[1])
    else:
        print("Gender:",profile_list[2])
#>>> For list
#>>> Name: Alex
#>>> Age: 24
#>>> Gender: Male
 
# Set: no order!!!
print("\nFor set")                     
profile_set = {"Alex", 24, "Male"}     
for elem in profile_set:
    print(elem)
#>>> For set
#>>> 24
#>>> Alex
#>>> Male
 
# String: has order!!!
print("\nFor string")                  
profile_str = "Name: Alex,Gender: Male,Age: 24."
fromindex=0
index = 0
for elem in profile_str:
    if elem == "," or elem == ".":       # eliminate the "," and ".".
        print(profile_str[fromindex:index])
        fromindex = index+1
    else:
        pass                             # use "pass" temporarily
    index += 1
#>>> For string
#>>> Name: Alex
#>>> Gender: Male
#>>> Age: 24
 
# String: has order!!!
print("\nFor string (split)")           
profile_str = "Name: Alex,Gender: Male,Age: 24."
profile_list = profile_str.split(",")
for index in range(len(profile_list)):
    if index<(len(profile_list)-1):       # eliminate the "." at the end
        print(profile_list[index])
    else:
        print(profile_list[index][:-1])
#>>> For string (split)
#>>> Name: Alex
#>>> Gender: Male
#>>> Age: 24
