# https://leetcode.com/explore/interview/card/google/59/array-and-strings/337/

class Solution:
	def addBoldTag(self, s, dict):
		def find_indices_word(s, word):
			results = []
			def check(index):
				for t in range(index, index + len(word)):
					if s[t]  != word[t - index]:
						return False
				return True
			for index in range(len(s) - len(word) + 1):
				if check(index):
					results.append([index, index + len(word)])			
			return results
			
		def find_indices_dict(s, dict):
			results = []
			for word in dict:
				results += find_indices_word(s, word)
			return results

		def merge(indices):
			result = []
			stack = []
			for left, right in indices:
				if not stack:					
					stack.append([left, right])
				else:
					if left > stack[-1][-1]:
						result.append(stack.pop(-1))
						stack.append([left, right])
					else:
						stack[-1][-1] = max(right, stack[-1][-1]) # NOTE: the max one rather than replace by default
			while stack:
				result.append(stack.pop(-1))
			return result
		
		indices = find_indices_dict(s, dict)
		# print(indices)
		indices.sort()
		indices = merge(indices)
		# print(indices)

		# for now the indices have been merged with no overlap
		result = ""
		last = 0
		for left, right in indices:
			result += s[last:left]
			result += "<b>"
			result += s[left:right]
			result += "</b>"
			last = right
		result += s[last:] # NOTE: do not forget to add the residue
		return result

s = "aaabbcc"
dict = ["aaa","aab","bc","aaabbcc"]
print(Solution().addBoldTag(s, dict))

# 当然可以用 KMP
# 第一步是标出所有的 left, right 序列
# 然后 sort 这个序列
# 然后从前往后过一遍

# 但是我觉得类似前缀树是不是会更快一点