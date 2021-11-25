Fib=[1, 2]
EndSeq = True #limit the sequence up to 4m
while EndSeq:
  for n in range (2,):
    Fib.append (Fib[-1]+Fib[-2])
  
  if Fib[-1]>=4000000:
    EndSeq = False #it still gives couple numbers beyond 4m, but I'll get rid of extra numbers later on
#print ("Fibonacci sequence (not precise length", Fib)
evFib=[]
for n in Fib:
  if n%2==0 and n<=4000000:
    evFib.append(n)
print ("Even elements of Fib seq", evFib)
a=sum(evFib)
print("The sum of even element of Fibonacci up to 4m is ", a)

