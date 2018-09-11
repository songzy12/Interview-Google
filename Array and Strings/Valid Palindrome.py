# https://leetcode.com/explore/interview/card/google/59/array-and-strings/435/

class Solution:
	def isPalindrome(self, s):
		i = 0
		j = len(s) - 1 # NOTE: not len(s)
		while i < j:
			import string
			
			if s[i].lower() not in string.ascii_lowercase + string.digits: # NOTE: string.digits
				i += 1
				continue
			if s[j].lower() not in string.ascii_lowercase + string.digits:
				j -= 1
				continue
			if s[i].lower() != s[j].lower():
				return False
			i += 1
			j -= 1
		return True
