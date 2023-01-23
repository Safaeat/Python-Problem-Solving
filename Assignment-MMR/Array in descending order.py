#Write a Python program that contains an Array and show the value in descending order. [In the Array keep any ten values]

arr = [1,2,3,4,5,6,7,8,9,10]; 
temp = 0; 
 
print("Elements of original array: "); 
for i in range(0, len(arr)): 
 print(arr[i]), 
for i in range(0, len(arr)): 
 for j in range(i+1, len(arr)): 
  if(arr[i] < arr[j]): 
    temp = arr[i]; 
    arr[i] = arr[j]; 
    arr[j] = temp; 
print(); 
print("Elements of array sorted in descending order: "); 
for i in range(0, len(arr)): 
 print(arr[i]) 