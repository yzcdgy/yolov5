import numpy as np
import os
from os import listdir

label_dir = "C:\\Users\\Yz\\Desktop\\199\\EEE 199 DATASET\\ttl\\"
label_save_path = "C:\\Users\\Yz\\Desktop\\199\\EEE 199 DATASET\\adjusted_labels"

for filename in os.listdir(label_dir):
    if (filename.endswith(".txt")) and len(open(os.path.join(label_dir, filename), 'r').readlines()) != 1:
        label_full = np.loadtxt(label_dir + filename)
        for x in label_full:
            if x[0] == 0:
                x[0] = 1
            elif x[0] == 1:
                x[0] = 2
            elif x[0] == 2:
                x[0] = 3
            elif x[0] == 3:
                x[0] = 5
            elif x[0] == 4:
                x[0] = 7
            elif x[0] == 5:
                x[0] = 3
        np.savetxt(filename, x, delimiter=' ')
    elif (filename.endswith(".txt")) and len(open(os.path.join(label_dir, filename), 'r').readlines()) == 1:
        label_full = np.loadtxt(label_dir + filename)
        if x[0] == 0:
            x[0] = 1
        elif x[0] == 1:
            x[0] = 2
        elif x[0] == 2:
            x[0] = 3
        elif x[0] == 3:
            x[0] = 5
        elif x[0] == 4:
            x[0] = 7
        elif x[0] == 5:
            x[0] = 3
        np.savetxt(filename, x, delimiter=' ')


#bike 0 -> 1
#car 1 -> 2
#motorcycle 2 -> 3
#bus 3 -> 5
#truck 4 -> 7
#other 5 -> 3
