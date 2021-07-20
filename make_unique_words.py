import os

path = "/home/rezamarefat/rcnn_train_pack/data_generator/normalized_corpus_for_LM.txt"
with open(path, "r") as f:
    
    content = f.readlines()
    words_store = []

    for c in content:
        words = c.split(" ")
        # print(words)

        for w in words:
            words_store.append(w)

    # print(words_store)    
    
from tqdm import tqdm
for w in tqdm(words_store):
    with open("/home/rezamarefat/rcnn_train_pack/data_generator/words.txt", "a+") as f_:

        if not(len(w.strip()) == 0):
            f_.writelines(w)
            f_.writelines("\n")
            f_.seek(0)
    

