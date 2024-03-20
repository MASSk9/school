'''
1. Add students
2. Show all students
3. Delete students
4. Exit
'''

print("1. Add students\n2. Show all students\n3. Delete students\n4. Exit")

a = int(input("=> "))

if a == 1:
   print("1.Add student to new class\n2.Add student to existing class") 
   b = int(input("=> "))
   if b == 1:
       list_name = input("Enter list name => ")
       added_students = input("Enter student => ")
       student_list = []
       student_list.append(added_students)
       print(f"file name {list_name}\n Students added to new list {student_list}")
       #print("file name",list_name,"\n Students added are",student_list)
    
   elif b == 2:
       list1=["ram","manjot","raju","sham"]
       list2= ["a","b","c"]
       list3= [1,2,3,4]
       print(f"1. {list1}\n2. {list2}\n3. {list3}")
       x =int(input("select_list_number=> "))
       if x == 1:
           print(f"selected list{list1}")
           new_students_list=input("enter_student_names_to_be_added=>[]")
           list1.append(new_students_list)
           print (f"edited_list {list1}")
       
       elif x == 2:
           print(f"selected_list {list2}")
           new_students_list=input("enter_student_names_to_be_added=>[]")
           list2.append(new_students_list)
           print(f"edited_list {list2}")

       elif x == 3:
           print(f"selected list{list3}")
           new_students_list=input("new_student_names_to_be_added=>[]")
           list3.append(new_students_list)
           print(f"edited_list {list3}")

elif a == 2:
    list1=["ram","manjot","raju","sham"]
    list2= ["a","b","c"]
    list3= [1,2,3,4]
    
    print({f"list of all students {list1},{list2},{list3}"})


    

         
         
         
        
           
             

           
          


    