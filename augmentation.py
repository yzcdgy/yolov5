import albumentations as A
import cv2
import numpy as np
import os
from os import listdir

image_dir = "C:\\Users\\Yz\\Desktop\\199\\EEE 199 DATASET\\tti\\"
label_dir = "C:\\Users\\Yz\\Desktop\\199\\EEE 199 DATASET\\ttl\\"
img_save_path = "C:\\Users\\Yz\\Desktop\\199\\EEE 199 DATASET\\augment images"
label_save_path = "C:\\Users\\Yz\\Desktop\\199\\EEE 199 DATASET\\augment labels"
final_label = []
transform = A.Compose([
    A.RandomSizedCrop(min_max_height=[360,540], height=720, width=1280)
], bbox_params=A.BboxParams(format='yolo', label_fields=['class_labels']))

for filename in os.listdir(label_dir):
    if (filename.endswith(".txt")) and len(open(os.path.join(label_dir, filename), 'r').readlines()) != 1:
        print('Processing image ' + filename.replace('txt', 'JPG'))
        image = cv2.imread(image_dir + filename.replace('txt', 'JPG'))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        label_full = np.loadtxt(label_dir + filename)
        label_coords = label_full.tolist()
        label_class = label_full.tolist()


        for x in range(len(label_class)):
            label_class[x] = label_class[x][0]
        for y in range(len(label_coords)):
            label_coords[y] = label_coords[y][1:]
        transformed = transform(image=image, bboxes=label_coords, class_labels=label_class, min_area=50000)

        new_image = cv2.cvtColor(transformed['image'], cv2.COLOR_RGB2BGR)
        cv2.imwrite(os.path.join(img_save_path, 'aug' + filename.replace('txt', 'JPG')), new_image)

        for z in range(len(transformed['class_labels'])):
            temp = [transformed['class_labels'][z], *transformed['bboxes'][z][:]]
            final_label.append(temp)
        with open(os.path.join(label_save_path, 'aug' + filename), 'w') as output:
            for x, y in zip(transformed['class_labels'], transformed['bboxes']):
                output.write(str(x)[0] + ' ' + str(y[0]) + ' ' + str(y[1]) + ' ' + str(y[2]) + ' ' + str(y[3]) + '\n')
        print('Image ' + filename.replace('txt', 'JPG') + ' done.')

#Rotate
#BBox_Only_TranslateY
