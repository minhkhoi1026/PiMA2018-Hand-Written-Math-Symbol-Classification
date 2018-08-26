from sklearn.neural_network import MLPClassifier
from PIL import Image
import numpy as np
import os
import random

#input()
directory_list = []
std_output_data= []
training_data= []
# create a list of folder ( alpha,beta,...)

directory_list = []
foldername="D:/Khoi/[PiMA] Nguyen_Nhat_Minh_Khoi/SymbolRegconitionDataset3"
for root, dirs, files in os.walk(foldername, topdown=False):
    for name in dirs:
        directory_list.append(os.path.join(root, name))

num_symbol = 0
# iterate through all folder
for directory in directory_list:
    # create standard output of symbol i

    std_output = np.zeros(5)
    std_output[num_symbol] = 1
    num_symbol = num_symbol + 1

    # print(std_output)
    # iterate through all file in folder
    for file in os.listdir(directory):

        filename = os.fsdecode(file)

        if filename.endswith(".jpg"):

            # image to vector
            img = Image.open(os.path.join(directory, filename)).convert('')
            arr = np.array(img)
            flat_arr = np.ravel(arr)
            training_data.append(flat_arr)
            std_output_data.append(std_output)


def shuf(a,b):
    for i in range(n):
        a.append(b[id[i]])

#neural network

clf = MLPClassifier(hidden_layer_sizes=(50,50))

#shuffle data

n=len(training_data)
id= [ i for i in range(n) ]
random.shuffle(id)
r_training_data=[]
r_std_output_data=[]
shuf(r_training_data,training_data)
shuf(r_std_output_data,std_output_data)

#train network

n=(4*n)/5
clf.fit( np.matrix( r_training_data[:int(n)] ) , np.matrix( r_std_output_data[:int(n)]) )

#score network
print( (clf.score( np.matrix(r_training_data[int(n):]), np.matrix(r_std_output_data[int(n):]) )) )
