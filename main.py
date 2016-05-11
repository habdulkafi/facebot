#
# Husam Abdul-Kafi
# 05/11/16
#

import pdb
import unittest
import sys
import os

import fb


class fbTestCase(unittest.TestCase):
	"""Tests for `fb.py`."""

	@classmethod
	def setUpClass(self):
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

	def test_image_search_one_word(self):
		"""Does the program get images from google images correctly? """
		self.assertTrue(fb.google_image("kitten",self.mbrowser)[4] != "")

	def test_image_search_two_words(self):
		"""Does the program get images from google images correctly? """
		self.assertTrue(fb.google_image("Grado Labs",self.mbrowser)[4] != "")

	def test_image_search_three_words(self):
		"""Does the program get images from google images correctly? """
		self.assertTrue(fb.google_image("Flying spaghetti monster",self.mbrowser)[4] != "")		

	def test_image_search_many_words(self):
		"""Does the program get images from google images correctly? """
		self.assertTrue(fb.google_image("htc 10 vs lgg5 vs samsung galaxy s7",self.mbrowser)[4] != "")

	def test_image_search_misspelling(self):
		"""Does the program get images from google images correctly? """
		self.assertTrue(fb.google_image("fiv guyes",self.mbrowser)[4] != "")

	def test_google_search_single_word(self):
		"""Does the program get links from google correctly? """
		self.assertTrue(fb.google("kitten",self.mbrowser)[4] != "")

	def test_google_search_two_words(self):
		"""Does the program get links from google correctly? """
		self.assertTrue(fb.google("mersenne primes",self.mbrowser)[4] != "")

	def test_google_search_three_words(self):
		"""Does the program get links from google correctly? """
		self.assertTrue(fb.google("columbia academic calendar",self.mbrowser)[4] != "")

	def test_google_search_many_words(self):
		"""Does the program get links from google correctly? """
		self.assertTrue(fb.google("Rick Astley - Never Gonna Give You Up",self.mbrowser)[4] != "")

	def test_google_search_ishan(self):
		"""Does the program get links from google correctly? """
		self.assertTrue(fb.google("Ishan Guru Columbia University",self.mbrowser)[4] != "")

	def test_google_search_misspelling(self):
		"""Does the program get links from google correctly? """
		self.assertTrue(fb.google("fiv guyes",self.mbrowser)[4] != "")

	@classmethod
	def tearDownClass(self):
		fb.logout(self.browser)


if __name__ == '__main__':
	if len(sys.argv) == 1:
		os.system(sys.executable + ' setup.py')
		os.system(sys.executable + ' fb.py')
	elif sys.argv[1] == "run_tests":
		del sys.argv[1:]
		unittest.main()
	elif sys.argv[1] == "debug":
		os.system(sys.executable + ' setup.py')
		os.system(sys.executable + ' fb.py debug')
	elif sys.argv[1] == "help":
		print "To understand how the entire program works, please visit:\n"\
		"      https://github.com/habdulkafi/facebook-bot/blob/master/README.md"
		print "Usage:\n   python main.py help      -- prints this help and exits \n"\
				"   python main.py run_tests -- runs the tests \n" \
				"   python main.py debug     -- runs setup.py then runs fb.py with debug \n"\
				"   python main.py run       -- runs the whole program (setup.py and fb.py)"


