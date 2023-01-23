'''
There is an array ob the size of the array 
is 10, now put the value in the array
(ob[0]=6, ob[1]=11, ob[2]=2, ob[3]=0, ob[4]=1, 
ob[5]=6, ob[6]=16, ob[7]=6, ob[8]=6,
ob[9]=3). Find out the average of the value 
which contains in the array. * Must use loop
'''


ob = [6, 11, 2, 0, 1, 6, 16, 6, 6, 3]
sum = 0
count = 0
for i in ob:
 sum += i
 count += 1
average = sum / count
print(average)
