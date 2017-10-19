from random import randint
def randlist(r,usedlist,done):
	sum = 0
	alpha = "abcdefghijklmnopqrstuvwkyzABCDEFGHIJKLMNOPQRSTUVWKYZ0123456789'`[]\\;,.!@#$%^&*()_+{}|:\"<>?"
	usedlist[r] = 1
	c = alpha[r]
	
	for i in range (len(usedlist)):
		sum = sum + usedlist[i]
	#print (c,usedlist," sum ",sum)
	if sum == 94:
		done = True
	return c,usedlist,done
	
def main():
	used = [0]*94
	done = False
	while done == False:
		r = randint(0,63)
		c,used,done = randlist(r,used,done)
		print(c,end="")
main()
		
		
		
