# pattern_matching

GOAL: find the pattern in the bug.txt file in the landscape.txt file

APPROACH:

sliding_window_perfect_match.py:  

It reads the files with the bug and the landscape as strings then slides over the landscape string and checks for perfect matches between the bug and the pieces of the landscape.
Please run with: ‘python sliding_window_perfect_match.py bug.text landscape.txt’ from the command line. Output is the number of bugs and time it takes for the program to run.

suffix_trie_perfect_match.py:
	
It reads the files with the bug and the landscape as strings then constructs a suffix trie of the landscape string. Finally it counts the matches of the pattern from the bug,txt file in the suffix trie.
Please run with: ‘python suffix_trie_perfect_match.py bug.text landscape.txt’ from the command line. Output is the number of bugs and time it takes for the program to run.

sliding_window_mismatches.py:  

It reads the files with the bug and the landscape as strings then slides over the landscape string and checks for partial matches between the bug and the pieces of the landscape, allowing for 4 mismatches.
Please run with: ‘python sliding_window_mismatches.py bug.text landscape_complex.txt’ from the command line. Output is the number of bugs and time it takes for the program to run.

suffix_trie_mismatches.py:
	
It reads the files with the bug and the landscape as strings then constructs a suffix trie of the landscape string, store individual branches in a list. It then loops over the branches and matches the pattern with the beginning of each branch, allowing for 4 mismatches and skipping the redundant branches containing the pattern after a match has been found.
Please run with: ‘python suffix_trie_mismatche.py bug.text landscape_complex.txt’ from the command line. Output is the number of bugs and time it takes for the program to run.

