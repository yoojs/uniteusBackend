#!/usr/bin/python
import sys,getopt
def main(argv):
	primesNumber = None
	try:
		opts, args = getopt.getopt(argv,"hi:")
	except getopt.GetoptError:
		print 'test.py -i <number of prime numbers>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i <number of prime numbers>'
			sys.exit()
		elif opt in ("-i"):
			primesNumber = int(arg)
	primes = findPrimes(primesNumber)
	printMultTable(primes)


def findPrimes(numberOfPrimes):
	if numberOfPrimes == 0:
		return primes
	if numberOfPrimes == 1:
		return [2]
	primes = [2]
	num = 3
	numberOfPrimes -= 1
	while numberOfPrimes > 0:

		if isPrime(num):
			primes.append(num)
			numberOfPrimes -= 1
			num += 1
		else:
			num += 1
	return primes

#Used the pseudo code for prime numbers found in the wikipedia page 
def isPrime(num):
	if num <= 3:
		return num > 1
	elif num % 2 == 0 or num%3 == 0:
		return False
	i=5
	while i * i <= num:
		if num % i == 0 or num % (i + 2) == 0:
			return False
		i += 6
	return True

def printMultTable(primesList):
	w, h = len(primesList)+1, len(primesList)+1;
	table = [[0 for x in range(w)] for y in range(h)] 
	for i in range(0,len(primesList)):
		string = ''
		if i == 0:
			header = '\t|'
			for num in primesList:
				header += "	" + str(num)
			print header
			header = ''
			for x in range(len(primesList)+1):
				header += '\t_'
			print header
		for j in range(0,len(primesList)):
			
			if j == 0:
				string += str(primesList[i]) + '\t|'
			string += '	' + str(primesList[i]*primesList[j])
		print string
	
if __name__ == '__main__':
	main(sys.argv[1:])

