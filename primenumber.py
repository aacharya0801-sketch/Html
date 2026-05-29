num=int(input("Enter a number: "))
if num >1:
  for i in range(2,int(num 0.5)+1):
    if num %i==0:
      print("The number is not a prime number")
      break
    else:
      print("The number is prime number")
else:
  print("please enter number greater than 1")