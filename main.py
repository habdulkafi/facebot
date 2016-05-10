import pdb
import unittest

import fb


class fbTestCase(unittest.TestCase):
	"""Tests for `fb.py`."""

	def __init__(self, *args, **kwargs):
		super(fbTestCase, self).__init__(*args, **kwargs)
		(browser,fbmsgurl,mbrowser) = fb.login_setup()
		self.browser = browser
		self.fbmsgurl = fbmsgurl
		self.mbrowser = mbrowser


	def test_sending_message(self):
		"""Does the program send messages properly?"""
		self.assertTrue(fb.message("testing 123",self.browser,self.fbmsgurl),'fail message')

	def test_get_joke(self):
		"""Does the program get a joke correctly?"""
		self.assertTrue(fb.get_joke(self.mbrowser)[0] != "")

	def test_image_search(self):
		"""Does the program get images from google images correctly? """
		self.assertTrue(fb.google_image("kitten",self.mbrowser)[4] != "")

	def test_google_search(self):
		"""Does the program get links from google correctly? """
		self.assertTrue(fb.google("kitten",self.mbrowser)[4] != "")



if __name__ == '__main__':
	unittest.main()

