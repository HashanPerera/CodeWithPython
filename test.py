class Test1:
   name = ''
   color = ''
   weight = ''
   height = ''

   def Pet(self):
      Pet_name = input("Tell me your Pet's name: ")
      Pet_color = input("Tell me your Pet's color: ")
      Pet_weight = input("Tell me your Pet's weight: ")
      Pet_height = input("Tell me your Pet's height: ")
      
      return f'My pet name is {Pet_name}. Color is {Pet_color}. And weight and height in order are {Pet_weight}, {Pet_height}'
      
   def human(self):
      human_type = input('Are male or female? ')
      
      if human_type == 'male' or human_type == 'Male' or human_type == 'MALE':
         return 'Please go to the Floor No : 01'
      elif human_type == 'Female' or human_type == 'female' or human_type == 'FEMALE':
         return 'Please go to the Floor No : 02'
      else:
         return 'Please go to the Floor No : 03'
      
# user input getting for a list

   def Inputarray():
      
      arr1 = []
      list_length = input('How many numbers are you going to input? ')

      for i in range(int(list_length)):
         list = input(f"Give your integer {i+1} : ")
         arr1.append(int(list))
      print(arr1, type(arr1))

      return arr1

# use bubble sort for input number sorting

 
   def BubbleSort(arr):
      r = len(arr)
      for i in range(1,r): 
         for j in range(1,r):
            t = arr[j-1]
            if arr[j-1] > arr[j]:
               arr[j-1] = arr[j]
               arr[j] = t            

      print(f'Your sorted list : {arr}')

   # def BubbleSort(arr):
      
   #    #arr = [2,4,2,5,1]

   #    r = len(arr)
   #    for i in range(1,r): 
   #       for j in range(1,r):
   #          s = j-1
   #          p = arr[s]
   #          q = arr[j]
   #          t = q
   #        # print(p,q)

   #          if p>q or p==q :
   #             arr[j] = p
   #             arr[s] = q
   #           # print(arr[s], arr[j])
   #           # print(arr)

   #    print(f'Your sorted list : {arr}') 


   
""" def set_variable():
    my_variable = "Hello from Python"
    return my_variable

def use_variable(variable):
    print(variable)

my_variable = set_variable()
use_variable(my_variable) """