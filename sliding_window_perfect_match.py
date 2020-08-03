import re
import Levenshtein
import time

# at the beginning:
start_time = time.time()

testfile = "landscape_complex.txt"
trainfile = "bug.txt"

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

#walk thorugh string
string_index = 0
match_counter = 0 

#slide over test string and calculate the levenshtein distance between the bug and the substring of the same length in the text.
while string_index < len(test):
	lev = Levenshtein.distance(bug,test[string_index:string_index+(bug_length)])
	#if there is a perfect match, count it skip it and go to new search start
	if lev == 0:
		match_counter = match_counter+1
		string_index = string_index + bug_length
	#if no match, walk ahead 1 letter in the test string
	elif lev != 0:
		string_index = string_index+1

print("nr of bugs in test file: " + str(match_counter))

# at the end of the program:
print("time elapsed: %f seconds" % (time.time() - start_time))
