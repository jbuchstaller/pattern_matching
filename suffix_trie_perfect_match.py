import time
import re


def count(d, k):
		return (k in d) + sum(count(v, k) for v in d.values() if isinstance(v, dict))

class SuffixTrie(object):

	#construct the suffix trie from text
	def __init__(self, text):
		#add terminator symbol to text
		text+= '$'
		#initialize empty root
		self.root = {}
		
		#walk through text (test string) letter by letter and generate different suffixes
		
		#for each suffix
		for i in range(0,len(text)): 
			#reference root
			currentSuffix = self.root
			# walk through all the characters in suffix
			for character in text[i:]: 
				#check if character is already in the dictionary
				if character not in currentSuffix:
					#if not, add as a new dictionary with character as its key 
					currentSuffix[character] = {}
				#if there, add to last dictionary, without creating an empty one
				currentSuffix = currentSuffix[character]

	def displayTrie(self):
		print(self.root)

	#take pattern and search for it in trie
	def followPath(self, pattern):
		#follow path of patter in trie
		trie = self.root
		for character in pattern:
			if character not in trie:
				return None
		trie = trie[character]
		return trie

	#def count(d, k):
		#return (k in d) + sum(count(v, k) for v in d.values() if isinstance(v, dict))
	
	def mycount(d, k):
		return (k in d) + sum(count(v, k) for v in d.values() if isinstance(v, dict))

	def countSubstring(self, pattern):
		#count number of endings ($)
		k = '$'
		d = self.followPath(pattern)
		my_count = (k in d) + sum(count(v, k) for v in d.values() if isinstance(v, dict))
		print(my_count)

trainfile = sys.argv[1]
testfile = sys.argv[2]

with open(trainfile) as f1:
	bug = f1.read()
	#remove whitespace and newline
	bug = re.sub(r'\s+', '', bug)
	bug_length = len(bug)


with open(testfile) as f2:
	test = f2.read()
	#remove whitespace and newline
	test = re.sub(r'\s+', '', test)

f1.close()
f2.close()


start_time = time.time()
my_strie = SuffixTrie('||###O||||njsndjwe###Onjkewqnf||||###O||')
my_strie.countSubstring('||###O||')
print("%f seconds" % (time.time() - start_time))