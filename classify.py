import sys
if len(sys.argv) != 3:
    print "I hate hate hate the log so so so much"
    print 'It is used to calculate the score by using a doc file and all LM models.'
    print '$ python', sys.argv[0],'[input-doc-path] [model-path]\n'
    exit()


import time
start = time.time()
print "starting : %s " % start


import kenlm

#model_name = 'lm/Christos_Faloutsos.arpa'
from os import listdir
from os.path import isfile, join

fname_path = sys.argv[1]
model_path = sys.argv[2]
models_files = [f for f in listdir(model_path) if isfile(join(model_path, f))]
doc_files = [f for f in listdir(fname_path) if isfile(join(fname_path, f))]
#reading testing docs
test_set = dict()
for fname in doc_files:
    with open(fname_path+fname) as f:
        test_set[fname] = f.read()
print "Reading Docs Completed"
#reading models
model_set = dict()
for model_name in models_files:
    try:
        model = kenlm.Model(model_path+model_name)
        model_set[model_name[:-5]] = model
        #model.score(content, bos = True, eos = True)
        #model_score_list[model_name[:-5]] = model.perplexity(content)
    except:
        pass
print "Reading Models Completed"
#sorted_model_list = sorted(model_score_list, key=lambda x: model_score_list[x],reverse=False)

print "Calculating each doc match Model TOP5"
Top_record = [0]*5
def displayTOP():
    tmp = 0
    for top in Top_record:
        tmp += 1
        print "Top(%s):" % tmp,
        print top

def calculation(test_set,model_set):
    bango = 0
    runner = 0

    for doc in test_set:
        score_list = dict()
        for model_name in model_set:
            score_list[model_name] = model_set[model_name].score(test_set[doc], bos = True, eos = True)
        #comparing TOP5
        #reverse=true for score , false for perplexity
        sorted_model_list = sorted(score_list, key=lambda x: score_list[x], reverse=True)

        Top = -1
        for m_name in sorted_model_list[:5]:
            Top += 1
            if doc == m_name:
                #match
                bango += 1
                Top_record[Top] += 1
        ##infomation
        print doc
        print "Bango : %s" % bango,
        runner += 1
        print "     Current Doc number : %s" % runner
        displayTOP()


calculation(test_set,model_set)


'''print sorted_model_list[:5]
run = 1
for m_name in sorted_model_list[:5]:
    print "TOP(%d)&Score : %s " % (run,model_score_list[m_name])
    run += 1'''
#print content
print "Testing Model_path : %s" % model_path
print "Testing Document : %s" % fname_path
runner = 1

displayTOP()

print "it took", time.time() - start, "seconds."


#print "TOP5&Scores : %s " % ()
