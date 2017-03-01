import sys
if len(sys.argv) != 3:
    print 'It is used to calculate the score by using a doc file and all LM models.'
    print '$ python', sys.argv[0],'[input-doc-file] [model-path]\n'
    exit()


import kenlm



#import logging
#requests_log = logging.getLogger("kenlm")
#requests_log.addHandler(logging.NullHandler())
#requests_log.propagate = False
#log = logging.getLogger('kenlm')
#log.setLevel(logging.ERROR)

#import os
#print os.path.dirname(kenlm.__file__)

import time
import sys
#time.sleep(2)

print kenlm.Config()._c_config



#model_name = 'lm/Christos_Faloutsos.arpa'
from os import listdir
from os.path import isfile, join

fname = sys.argv[1]
model_path = sys.argv[2]
models_files = [f for f in listdir(model_path) if isfile(join(model_path, f))]

#reading testing doc
with open(fname) as f:
    content = f.read()

model_score_list = dict()
for model_name in models_files:
    try:
        #abc = kenlm.Config()
        #abc.load_method()
        #abc.show_progress = 1
        model = kenlm.Model(model_path+model_name,abc)
        #model.score(content, bos = True, eos = True)
        model_score_list[model_name[:-5]] = model.perplexity(content)
    except:
        pass

sorted_model_list = sorted(model_score_list, key=lambda x: model_score_list[x],reverse=False)


print sorted_model_list[:5]
run = 1
for m_name in sorted_model_list[:5]:
    print "TOP(%d)&Score : %s " % (run,model_score_list[m_name])
    run += 1
#print content
print "Testing Model_path : %s" % model_path
print "Testing Document : %s" % fname
#print "TOP5&Scores : %s " % ()
