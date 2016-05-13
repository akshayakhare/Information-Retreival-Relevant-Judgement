from __future__ import division
from math import log
__author__ = 'Akshaya'


# For Homework 3 use results.eval, for Homework 4 use Query_Result.txt
results_file  = open('results.eval','r')
# results_file  = open('Query_Result.txt','r')

List_result = results_file.readlines()
results_file.close()

######## Used For Debugging ##########- Starts
print "List Results",List_result
######## Used For Debugging ##########- Ends

eval_List = []

for i in List_result:
    t =tuple()
    t = i.split()
    eval_List.append(t[:5])

# eval_List contains the whole result obtained from the search result from BM25 or Lucene
######## Used For Debugging ##########- Starts
print "Eval List",eval_List
######## Used For Debugging ##########- Ends

relevance_judgement_file = open('relevance_judgement.txt','r')

List_relevance = relevance_judgement_file.readlines()
relevance_judgement_file.close()

rel_list = []

counter = 1
temp_value = '12'

for i in List_relevance:
    t = tuple()
    t_ordered = tuple()
    t = i.split()
    if (t[0] == '12' or t[0] == '13' or t[0] == '19'):
        if temp_value <> t[0]:
            counter += 1
            temp_value = t[0]
        t_ordered = (str(counter),t[1:])
        rel_list.append(t_ordered)

# A contains the length of all the relevant docs for all 3 queries
A = [0,0,0]
# A_complement contains the length of all the non-relevant docs for all 3 queries
A_complement = [0,0,0]
# B contains the length of all the retrieved docs for all 3 queries, in this case is 100
B = [0,0,0]
# B_complement contains the length of all the non-retrieved docs for all 3 queries
B_complement = [0,0,0]
# A_set contains the list of all the relevant docs for all 3 queries
A_set = [[],[],[]]
# A_comp_set contains the list of all the non-relevant docs for all 3 queries
A_comp_set =[[],[],[]]
# B_set contains the list of all the retrieved docs for all 3 queries, in this case is 100
B_set = [[],[],[]]
# B_comp_set contains the list of all the non-retrieved docs for all 3 queries
B_comp_set = [[],[],[]]

# rel_list contains the relevant list for the given queries, and the query id is changed to eval_List
######## Used For Debugging ##########- Starts
print "and we have the relevance list",rel_list
######## Used For Debugging ##########- Ends

# Stores respective values A_set
for i in rel_list:
    # print i,'i'
    A[int(i[0])-1] += 1
    st = i[1][1]
    # print str,"str"
    A_set[int(i[0])-1].append(int(st[5:]))

print "A_set",A_set

# Stores respective values in B_set
for i in eval_List:
    B[int(i[0])-1] += 1
    st = i[2]
    B_set[int(i[0])-1].append(int(i[2]))

print "B_set",B_set

ideal_dcg_value = [[],[],[]]
# temp_value = '0'
# Uses the dummy list to calculate idcg values
i_counter = 0
while(i_counter < 3 ):
    j_counter = 0
    i_dcg = 0
    while(j_counter<100):
        if j_counter == 0:
            i_dcg += 1
        elif j_counter >= ((A_set[i_counter]).__len__()):
            i_dcg = i_dcg
        else:
            i_dcg += 1/(log((j_counter+1),2))
        ideal_dcg_value[i_counter].append(i_dcg)
        j_counter += 1
    i_counter += 1

######## Used For Debugging ##########- Starts
print "ideal-stuff",ideal_dcg_value
print "ideal-stuff",ideal_dcg_value[0].__len__(),ideal_dcg_value[1].__len__(),ideal_dcg_value[2].__len__()
print "AAAA",A
print "Acomp",A_complement
print "BBB",B
print "B_compl0",B_complement
# print A_set.__len__()
# print A_comp_set.__len__()
######## Used For Debugging ##########- Ends

recall_count = 0
precision_count = 0
doc_count = 0
rel_level = 0
precision_value = 0
recall_value = 0
avg_precision = 0
mean_avg_precision = 0
temp_value = '0'
cumulative_dcg_value = [0,0,0]

dcg_value = 0

# Use the output file for hw3 or hw4
file_results = open('HW_5_HW_3table.txt','w')
# file_results = open('HW_5_HW_4table.txt','w')

file_results.write("queryno "+"  Rank"+ " Doc".rjust(5)+ " " + "score".rjust(16)
                       +" R"+" "+" Precision".rjust(16)+" "+" Recall".rjust(16)+" "+" NDCG".rjust(16)+"\n")

# Prints the whole file
for i in eval_List:
    current_dcg_value = 0
    dcg_value = 0
    rel_level = 0
    # Resets values everytime query changes
    if temp_value <> i[0]:
        if temp_value <> '0':
            print "avg_precision ",avg_precision/A[int(i[0]) -2]
            mean_avg_precision += avg_precision/A[int(i[0]) -2]
            avg_precision = 0
            # print "CDG",cumulative_dcg_value
        temp_value = i[0]
        recall_count = 0
        precision_count = 0
        doc_count = 1
        n_dcg = 0

    # Increases the count for calculating precision, recall
    if (int(i[2]) in A_set[int(i[0]) -1]):
        recall_count += 1
        precision_count += 1
        rel_level = 1
        avg_precision += precision_count/doc_count
        if i[3] == '1':
            dcg_value = 1
            current_dcg_value += dcg_value
        else:
            dcg_value = 1/(log(int(i[3]),2))
            current_dcg_value += 1/(log(int(i[3]),2))
    cumulative_dcg_value[int(i[0]) -1] += current_dcg_value
    n_dcg = cumulative_dcg_value[int(i[0]) -1]/ideal_dcg_value[(int(i[0])-1)][(int(i[3])-1)]
    recall_value=recall_count/A[int(i[0]) -1]
    precision_value = precision_count/doc_count

    # Prints the data into the file
    file_results.write("query->"+i[0]+" "+i[3].rjust(5)+ " "+ i[2].rjust(4)+ " " + i[4].rjust(16)
                       +" "+str(rel_level)+" "+str(precision_value).rjust(16)+" "+str(recall_value).rjust(16)+" "+str(n_dcg).rjust(16)+"\n")

    doc_count += 1

######## Used For Debugging ##########- Starts
print "avg_precision ",avg_precision/A[2]
# print "CDG",cumulative_dcg_value
######## Used For Debugging ##########- Ends

mean_avg_precision+=avg_precision/A[2]
file_results.close()

######## Used For Debugging ##########- Starts
print "mean_avg_precision",mean_avg_precision/3
######## Used For Debugging ##########- Ends