import os
import cv2
import csv
import pandas as pd
import numpy as np
import os.path

folder="Dataset_4rooms"
list_of_image=os.listdir("ROBIN/"+folder)
# print(list_of_image)
#to get the size of all images 
with open(folder+'.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "image", "breadth", "height", "channel"])
    for index,image in enumerate(list_of_image):
        img=cv2.imread("ROBIN/"+folder+"/"+image)
        # print(img)
        # print(img.shape)
        writer.writerow([index+1, image, img.shape[0],img.shape[1],img.shape[2]])

#to get the max value of the breadh/height
df=pd.read_csv(folder+'.csv')
p=df['breadth'].max()
q=df['height'].max()
max_size=max(p,q)
print(max_size)


#to get new image of required size and place datasets at center

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR, borderValue=(255,255,255))
  return result


# load background image as grayscale
new_folder="augmented_"+folder
if not os.path.isdir("ROBIN/"+new_folder):
    os.makedirs("ROBIN/"+new_folder)
# os.mkdir(new_folder)
max_size+=int(max_size/4)
back = np.ones((max_size,max_size,1),np.uint8)*255
cv2.imwrite("background.jpg", back)

back = cv2.imread('background.jpg', cv2.IMREAD_GRAYSCALE)
hh, ww = back.shape
# print(hh,ww)
for index,image in enumerate(list_of_image):
    # load resized image as grayscale
    img=cv2.imread("ROBIN/"+folder+"/"+image,cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    # compute xoff and yoff for placement of upper left corner of resized image   
    yoff = round((hh-h)/2)
    xoff = round((ww-w)/2)
    # print(yoff,xoff)

    # use numpy indexing to place the resized image in the center of background image
    result = back.copy()
    result[yoff:yoff+h, xoff:xoff+w] = img
    # result=rotate_image(result,30)
    # view result
    # cv2.imshow('CENTERED', result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # # save resulting centered image
    # result = cv2.resize(result, (512,512))

    #For space expanded datasets
    cv2.imwrite('ROBIN/'+new_folder+'/'+image, result)

    #For space expanded and then 30 degree rotated datsets:
    result=rotate_image(result,30)
    cv2.imwrite('ROBIN/'+new_folder+'/'+os.path.splitext(image)[0]+'_r.jpg', result)

    