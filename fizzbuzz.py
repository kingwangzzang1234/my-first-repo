def do_fizzbuzz():
	for i in range(1,15+1):
		if i%3==0 or i%5==0:
			print('fizz'*(i%3==0)+'buzz'*(i%5==0))
		else:
			print(f'{i}')


if __name__=='__main__':
	do_fizzbuzz()
