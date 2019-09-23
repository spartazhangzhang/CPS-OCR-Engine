import pickle
import os

# os.mknod('labels')

text = {1:'一', 2:'丁'}
with open('chinese_labels','wb') as f:
    i = pickle.dump(text,f,0)
print(i)