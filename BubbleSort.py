#Bubble Sort
import random
import datetime

random_num = random.random()
before = datetime.datetime.now()

a=[6,5,3,1,8,7,2,4]
b=[]
random_arr=[]
def bubble_sort(arr):
	for i in range(0,len(arr)):
		for j in range(0,(len(arr)-i)-1):
			if(arr[j] > arr[j+1]):
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
	return arr


for count in range(0,100):
	num = int(round(10000*random.random()))
	random_arr.append(num)

#print random_arr
before = datetime.datetime.now()
b = bubble_sort(random_arr)
after = datetime.datetime.now()
print b

print('The soreting took: ' + str(after-before))
