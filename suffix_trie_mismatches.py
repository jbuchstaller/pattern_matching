import time
import re
import sys
import Levenshtein


class SuffixTrie(object):
    #construct the suffix trie from text and collect branches in a list at the same time
    def constructTreeAndCollectBranches(self, text):
        #add terminator symbol to text
        text += '$' 
        #initialize empty root
        self.root = {}
        ##walk through text (test string) letter by letter and generate different suffixes
        #initailize list to collect branches
        branches = []
        #for each suffix
        for i in range(0,len(text)):
            #reference the root
            currentSuffix = self.root
            # walk through all the characters c in suffix
            for c in text[i:]:
                #check if character is already in the dictionary
                if c not in currentSuffix:
                    #if not, add as a new dictionary with character as its key 
                    currentSuffix[c] = {} 
                #if the character is there, add it to last dictionary without creating an empty one
                currentSuffix = currentSuffix[c]
            branches.append(text[i:])
        return(branches)
        
    
    def checkBranchesforPattern(self,text,pattern,nrmismatches):
        #get all branches of suffixTrie and store in list
        branchList = self.constructTreeAndCollectBranches(text)
        #initialize counter to count pattern occurence
        counter = 0
        #initialize counter to loop over branchList
        i = 0
        #for each branch
        while i < len(branchList):
            #remove $ sign from end of branch
            branch = list(branchList[i])
            branch.pop(-1)
            branch = ''.join(branch)
            #calculate edit distance between pattern and beginning of the branch
            lev = Levenshtein.distance(pattern,branch[0:len(pattern)])
            #allow for given number of mismatches
            if lev <= nrmismatches:
                #increase counter
                counter = counter + 1
                #if match found, move forward in branch list (skip redundant branches)
                i = i + len(pattern)
            else:
                #if no match found just move ahead one branch
                i = i +1
        return (counter)

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
my_trie = SuffixTrie()
bug_count = my_trie.checkBranchesforPattern(test,bug,4)
print("number of bugs in test file: " + str(bug_count))
print("time elapsed: %f seconds" % (time.time() - start_time))