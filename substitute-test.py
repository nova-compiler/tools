import unittest, substitute

class TestSubstitution(unittest.TestCase):
	def test_equal(self):
		output = substitute.substitute_text('what output this should be?', {}, True)
		self.assertEqual(output, 'what output this should be?')

	def test_percent_token(self):
		output = substitute.substitute_text('what output %% should be?', {}, True)
		self.assertEqual(output, 'what output % should be?')

	def test_variable(self):
		output = substitute.substitute_text('what output %var% should be?', { 'var' : 'aloha' }, True)
		self.assertEqual(output, 'what output aloha should be?')

	def test_unmatched_percent(self):
		self.assertRaises(substitute.SubstituteError, substitute.substitute_text, 'what output % should be?', {}, True)

	def test_not_found_variable(self):
		self.assertRaises(substitute.SubstituteError, substitute.substitute_text, 'what output %var% should be?', {}, True)

if __name__ == '__main__':
	unittest.main()
