def binarysearch(sortedlist,len,x):
	first=0
	last=len-1
	while(first<last):
		mid=int((first+last)/2)
		if sortedlist[mid]==x:
			print("found")
			return -1
		elif sortedlist[mid]<x:
			first=mid+1
		elif sortedlist[mid]>x:
			last=mid-1
		
	print("not found")
	return-1
		
alist=[]
size=int(input("enter size\t"))
for i in range(size):
	b=int(input("enter no\t"))
	alist.append(b)
alist.sort()
print(alist)
		
item=int(input("enter item\t"))		
binarysearch(alist,size,item)
