import unittest, sys, StringIO
from backendCode import *

class BackendTests(unittest.TestCase):
	def test_prime_array(self):
		self.assertEqual(findPrimes(10), [2,3,5,7,11,13,17,19,23,29])
	def test_prime(self):
		self.assertEqual(isPrime(19), True);
	def test_mult_output(self):
		capturedOutput = StringIO.StringIO()
		sys.stdout = capturedOutput
		printMultTable([2,3,5,7,11,13,17,19,23,29])   
		sys.stdout = sys.__stdout__          
		self.assertEqual(capturedOutput.getvalue(), '\t|\t2\t3\t5\t7\t11\t13\t17\t19\t23\t29\n\t_\t_\t_\t_\t_\t_\t_\t_\t_\t_\t_\n2\t|\t4\t6\t10\t14\t22\t26\t34\t38\t46\t58\n3\t|\t6\t9\t15\t21\t33\t39\t51\t57\t69\t87\n5\t|\t10\t15\t25\t35\t55\t65\t85\t95\t115\t145\n7\t|\t14\t21\t35\t49\t77\t91\t119\t133\t161\t203\n11\t|\t22\t33\t55\t77\t121\t143\t187\t209\t253\t319\n13\t|\t26\t39\t65\t91\t143\t169\t221\t247\t299\t377\n17\t|\t34\t51\t85\t119\t187\t221\t289\t323\t391\t493\n19\t|\t38\t57\t95\t133\t209\t247\t323\t361\t437\t551\n23\t|\t46\t69\t115\t161\t253\t299\t391\t437\t529\t667\n29\t|\t58\t87\t145\t203\t319\t377\t493\t551\t667\t841\n')
if __name__ == '__main__':
    unittest.main()