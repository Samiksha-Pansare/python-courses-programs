# Search for lines that start with From and have an at sign
import re
sum=0
c=0
fname=input('Enter:')
hand = open(fname)
for line in hand:
	line = line.rstrip('.')
	x = re.findall('([0-9]+)', line)
	if len(x) > 0:
		print(x)
		i=0
		for intg in x:
			n=int(x[i])
			sum=sum+n
			i=i+1
			c=c+1
print('Sum:',sum)
print('Values:',c)
		
    
        
    

    