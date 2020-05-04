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

print(_try(24, 1, 2, 3, 4))