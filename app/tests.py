import unittest
from models import response

class ResponseTestCase(unittest.TestCase):

	def test_response(self):
		response_final_result = response('javascript', 'california')
		self.assertEqual(response_final_result.status_code, 200)

unittest.main()