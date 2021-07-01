import os 
import cv2
import numpy as np
from copy import deepcopy, copy

# ESC to next 
# c to clear the door image 
class  Parcel_Preparation:
    def __init__(self):
        self.folder_name = "Dataset_4rooms"
        self.final_folder_name = "final_"+self.folder_name
        self.footprint_folder_name = 'footprint_'+self.folder_name
        self.image_size = 512
        self.list_of_image = os.listdir("ROBIN/"+self.final_folder_name)
        cv2.namedWindow(winname="Thumbnail")
        cv2.setMouseCallback("Thumbnail",self.get_point)
        self.footprint_points = []
        self.footprint_points_clear = []
        self.img = None
        self.isClear = False
        if not os.path.isdir("ROBIN/"+self.footprint_folder_name):
            os.makedirs("ROBIN/"+self.footprint_folder_name)

    def get_point(self,event,x,y,flags,param):
        if event == 1:
            # press the left button
            if not self.isClear:
                self.footprint_points.append([x,y])
            else:
                self.footprint_points_clear.append([x,y])                


    def create_footprint(self):
        for image in self.list_of_image:
            if not os.path.isfile('ROBIN/'+self.footprint_folder_name+'/'+image):
                self.footprint_points = []
                self.footprint_points_clear = []
                self.isClear = False
                self.img = cv2.imread("ROBIN/"+self.final_folder_name+"/"+image)
                self.img = cv2.resize(self.img,(self.image_size,self.image_size))
                
                while True:
                    self.img_copy=np.copy(self.img)
                    if len(self.footprint_points)>2:
                        corners = np.array(self.footprint_points)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=(0, 0, 0))
                    if len(self.footprint_points_clear)>2 and self.isClear:
                        corners = np.array(self.footprint_points_clear)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=(255, 255, 255))
                    cv2.imshow("Thumbnail",self.img_copy)
                    
                    if cv2.waitKey(10) & 0xFF == 27:
                        break
                    if cv2.waitKey(10) & 0xFF == ord('c'):
                        self.isClear = True
                        print(self.isClear)
                if len(self.footprint_points) != 0:  
                    cv2.imwrite("ROBIN/"+self.footprint_folder_name+"/"+image,self.img_copy)
            else:
                print("Footprint already created.")
        cv2.destroyAllWindows()


parcel = Parcel_Preparation()
parcel.create_footprint()