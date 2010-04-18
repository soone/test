#!/bin/env python
#def calc(seq):
#	maximum = 0
#	max_item = []
#	for i in seq:
#		product = (i[0]*100 + i[1]*10 +i[2]) * (i[3]*10 + i[4])
#		if product > maximum:
#			maximum = product
#			max_item = i
#		elif product == maximum:
#			max_item += ','+i
#	return max_item, maximum
#
#seq = [[5, 6, 7, 8, 9], [5, 6, 7, 9, 8]]
#max_item, maximum = calc(seq)
#print "Maximum at", max_item, ", product", maximum

def calc(seq, where):
	maximum, max_item = 0, []
	for i in seq:
		product = int(i[:where]) * int(i[where:])
		if product > maximum:
			maximum, max_item = product, i
		elif product == maximum:
			max_item += ',' + i
	print "Maximum at", max_item, ",product", maximum

def permute(seq):
	result = []
	for a in seq:
		for b in seq:
			for c in seq:
				for d in seq:
					for e in seq:
						if a!=b and a!=c and a!=d and a!=e and \
							b!=c and b!=d and b!=e and \
							c!=d and c!=e and d!=e:
							result.append(''.join([a,b,c,d,e]))
	return result

def permute1(seq):
	l = len(seq)
	if l == 1:
		return [seq]
	else:
		res = []
		for i in range(len(seq)):
			rest = seq[:i] + seq[i+1:]
			for x in permute1(rest):
				res.append(seq[i:i+1] + x)
		return res

def permute2(seq):
	l = len(seq)
	if l <= 2:
		if l == 2:
			return [ seq, [seq[1], seq[0]] ]
		else:
			return [seq]
		return [seq]
	else:
		res = []
		for i in range(len(seq)):
			rest = seq[:i] + seq[i+1:]
			for x in permute1(rest):
				res.append(seq[i:i+1] + x)
		return res

if __name__ == '__main__':
	import sys
	seq = list(sys.argv[1])
	where = int(sys.argv[2])
	thelist = [ ''.join(x) for x in permute2(seq) ]
	print 'Got', len(thelist), 'items.'
	calc(thelist, where)
