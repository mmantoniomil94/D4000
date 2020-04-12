# In this file write your unit tests.
# I have set up the est class for you.
import unittest
import Cipher as target

class TestCipherTools(unittest.TestCase):


#Test 1
text = "THISisaTEST"
s = 5
print "Text  : " + text 
print "Shift : " + str(s) 
print "Cipher: " + encrypt(text,s)
