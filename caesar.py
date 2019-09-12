d={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',
12:'l',13:'m',14:'n',15:'o',16:'p',
17:'q',18:'r',19:'s',20:'t',21:'u',
22:'v',23:'w',24:'x',25:'y',26:'z'}
#Caesar cipher
def cipher(n):
	nd={}
	for k in d.keys():
		if (k+n)>26:
			nk=(k+n-26)
			nd[d[k]]=d[nk]
		else:
			nd[d[k]]=d[k+n]	
	return nd		
n=input('輸入1~25:')	
print(cipher(int(n)))
print('Hello!')