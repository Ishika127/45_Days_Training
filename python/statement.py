##if else statement 
# num = input("Enter your number:-")
# if(num ==0): 
#  print("HEllo")
# else:
#   print("Hey")

# age = int(input("Enter your age :- " ))
# if(age<18):
#   print("Child")
# elif(age<45):
#   print("young")
# else:
#   print("Old man")  

# # num =int(input("Enter a number :-"))
# # if(num <0):
# #   print("Negative number")
# # else:
# #   print("Postive number ")  

# #even old 
# num =int(input("Enter your number:- "))
# if(num % 2==0):
#   print("even")
# else:  
#   print("Odd")

# #nested if else
# marks= 90
# att=70
# if(marks>=33):
#   if(att>=70):
#     print("you are elligable")
#   else:
#     print("low att")
# else:
#   print("low marks")   


  #design system 
amount = float(input("Enter shopping amount: "))

if amount >= 2000:
    discount = amount * 0.10
    final_amount = amount - discount
    print("You got a 10% discount!")
    print("Discount =", discount)
    print("Final amount =", final_amount)
else:
    print("No discount available.")
    print("Amount to pay =", amount)
    
#grade
n =int(input("Enter your grade:-  "))
if(n>=90):
  print("You got A grade")
elif(n>=80):
  print("You got B grade")
elif(n>=70):
  print("You got C garde")
elif(n>=60):
 print("You got D grade")
elif(n>=50):
 print("You got E grade")
else:
  print("you failed") 