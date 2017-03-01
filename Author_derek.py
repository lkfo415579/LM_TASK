print "Derek Version"
fname = "paper2authors.txt"
with open(fname) as f:
    content = f.readlines()

Authors = dict()
for x in range(0,len(content),3):
    #print x
    splited = content[x + 2].split('\t')
    splited[-1] = splited[-1][:-1]
    for author in splited:
        try:
            Authors[author].append(content[x].strip())
        except:
            Authors[author] = [content[x].strip()]

Sorted_NameList = sorted(Authors, key=lambda x: len(Authors[x]),reverse=True)


#print Authors
'''
run = 0
for node in Authors:
    print Authors[node]
    run += 1
    if run > 50: break'''
print "TOTAL AUTHORS : %s" % len(Authors)
print "TOP num_paper author: %s " % len(Authors[Sorted_NameList[0]])
print "Starting Create Authors own training doc"


print "Reading Required list"
with open("new_data/test_list.txt") as f:
    test_list = [x.strip() for x in f.readlines()]
with open("new_data/train_list.txt") as f:
    train_list = [x.strip() for x in f.readlines()]
with open("new_data/author_list.txt") as f:
    author_list = [x.strip() for x in f.readlines()]

import sys
import uniout

#sys.exit()

for x in range(0,len(Sorted_NameList)):
    #check whether the author is in the author list
    if Sorted_NameList[x] in author_list:
        train_content = []
        test_content = []
        for paper_id in Authors[Sorted_NameList[x]]:
            if paper_id in test_list:
                #test_set
                with open("pdfTxt-parsed/" + paper_id + ".raw") as f:
                    test_content += [t.strip()+"\n" for t in f.readlines()]
            elif paper_id in train_list:
                #not last two paper
                with open("pdfTxt-parsed/"+paper_id+".raw") as f:
                    train_content += [t.strip()+"\n" for t in f.readlines()]

        with open("train_derek/"+Sorted_NameList[x].replace(" ","_"), 'w') as outfile:
            outfile.writelines(train_content)
        with open("test_derek/" + Sorted_NameList[x].replace(" ", "_"), 'w') as outfile:
            outfile.writelines(test_content)


    #print len(Authors[Sorted_NameList[x]])