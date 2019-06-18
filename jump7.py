i = 1
while i <=100:
 if i%10==7 or i%7==0 or i>70 and i-70<10:
  i+=1
  continue
 else: 
  print(i)
  i+=1
