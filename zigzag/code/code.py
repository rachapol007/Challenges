def zigzag(a):
  temp = []
  Array_t = []  
  count = 0
  if len(a) == 1 or len(a) == 2:
    return 1
  
  for i in range(1,len(a)-1):
    if (a[i-1] < a[i] and a[i+1] < a[i]) or (a[i-1] > a[i] and a[i+1] > a[i]):
      count +=1 

    else:
      Array_t.append(count)
      count = 0
   
  
  Max = max(Array_t)
  return Max+2

