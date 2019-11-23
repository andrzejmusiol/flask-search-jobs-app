# Add parent path to project
import sys
sys.path.append('..')
#imports
import unittest
from application.scripts import getResponseFromApi, saveToJson, readFromJson

class scriptsTestCase(unittest.TestCase):

	def test_saveToJson(self):
		response_final_result = getResponseFromApi('javascript', 'california')
		self.assertEqual(response_final_result.status_code, 200)

	def test_readFromJon(self):
		jobs_file = readFromJson()
		self.assertEqual(jobs_file, [{'test':'test'}])

if __name__ == '__main__':
	unittest.main()