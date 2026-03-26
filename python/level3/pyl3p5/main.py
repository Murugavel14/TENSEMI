def find_number_of_zeros(number):
  count=0
  while number>0:
    a=int(number%10)#1's
    if(a==0):
      count=count+1;
    number=int(number/10)
  return count
number = int(input("?"))  
result = find_number_of_zeros(number)
print(result)