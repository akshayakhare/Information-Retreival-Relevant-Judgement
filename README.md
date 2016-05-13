# Relevant-Judgement
After getting the relevant documents from BM25 or Lucene, we judge the accuray of the results.

	Steps for running the program:
---------------------------------------------------------------------------------------------------------------------------
1. Install Python if not already installed from https://www.python.org/downloads/  version 2.7.10
2. The file 'HW_5.py' is the main file which contains the source code to find precision, recall and NDCG values
3. The file 'HW_5.py' takes no arguments, and expects 2 files to be available within the same directory as the 'HW_5.py'

	 i) One is the "relevance_judgement.txt" which contains the relevance judgement score of all the queries
		Line 29 in the code can be used to manipulate the location of this file
		
	ii) Second is either of the input file from HW_3("results.eval") or HW_4("Query_Result.txt")
		Line 7 or Line 8 can be used to manipulate the location of this file
		
4. The folder "HW3 related" contains all the files for running the result for input from HW_3 and
	The folder "HW4 related" contains all the files for running the result for input from HW_4
5. The two "HW_5.py" files in different folders have just one line changes for getting the input
6. The main file in the outside folder uses HW_4 as an input.

References:
----------------------------------------------------------------------------------------------------------------------------
http://stackoverflow.com/-> Helping out for various logic and syntax issues in python

https://www.python.org/doc/

----------------------------------------------------------------------------------------------------------------------------
The below files are present in both "HW3_related" and "HW4_related" folders

----------------------------------------------------------------------------------------------------------------------------
A table with the following columns and values for all 3 queries:

Rank
Document ID
Document score
Relevance level
Precision
Recall
NDCG

"portable operating systems _12.txt"

"code optimization for space efficiency_13.txt"

"parallel algorithms_19.txt"

******************************************************************************************************
The values of P@20 and MAP for the search engine

"P@k_and_MAP_values"
