import gensim
import pickle
model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin',binary=True)


dic={}

for item in model.wv.vocab:
	dic[item]=model[item]



try: 
    testf = open('dictionary', 'wb') 
    pickle.dump(dic, testf) 
    testf.close() 
    print("Done")
  
except: 
    print("Something went wrong")
