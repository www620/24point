def _try(n, *num):
	num = list(num)
	relist = []

	if not num:
		if not n:
			relist.append('')
	return relist

	for a in range(len(num)):
		one = num[a]
		del num[a]
		relist += getmsg(_try(n - one, *num), '+', one)
		relist += getmsg(_try(n + one, *num), '-', one)
		relist += getmsg(_try(n / one, *num), '*', one)
		relist += getmsg(_try(n * one, *num), '/', one)
		num.insert(a, one)
	return relist

def getmsg(list0, op, n):
	if not list0:
		return list0
	
	for a in range(len(list0)):
		one = list0[a]
		if (one[-2] == '+' or one[-2] == '-') and (op == '*' or op == '/'):
			one = '(' + one + ')'
		one += op + str(n)
		list0[a] = one

	return list0

def printmsg(list0, n):
	if not list0:
		print('没有解')
		return

	print('共' + len(list0) + '个解')
	for one in list0:
		print(one + '=' + str(n))

def main(n=24, *num):
	printmsg(_try(n, *num), n)

if __name__ == '__main__':
	main(1, 2, 3, 4)
