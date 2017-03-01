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
for x in range(0,1500):
    content = []
    test_content = []
    for paper_id in Authors[Sorted_NameList[x]]:
        if paper_id == Authors[Sorted_NameList[x]][-1] or paper_id == Authors[Sorted_NameList[x]][-2]:
            #test_set
            with open("pdfTxt-parsed/" + paper_id + ".raw") as f:
                test_content += f.readlines()
        else:
            #not last two paper
            with open("pdfTxt-parsed/"+paper_id+".raw") as f:
                content += f.readlines()
    with open("train/"+Sorted_NameList[x].replace(" ","_"), 'w') as outfile:
        outfile.writelines(content)
    with open("test/" + Sorted_NameList[x].replace(" ", "_"), 'w') as outfile:
        outfile.writelines(test_content)


    #print len(Authors[Sorted_NameList[x]])