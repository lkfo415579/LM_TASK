import sys
if len(sys.argv) != 3:
    print 'It is used to calculate the score from a doc file.'
    print '$ python', sys.argv[0],'[input-doc-file] [model-file]\n'
    exit()


import kenlm
#model_name = 'lm/Christos_Faloutsos.arpa'
fname = sys.argv[1]
model_name = sys.argv[2]
model = kenlm.Model(model_name)

with open(fname) as f:
    content = f.read()
#print content
print "Testing Model : %s" % model_name
print "Testing Document : %s" % fname
print "Score : %s " % (model.score(content, bos = True, eos = True))
