import os 
import cv2
import numpy as np
from copy import deepcopy, copy

class  Parcel_Preparation:
    def __init__(self):
        self.folder_name = "Dataset_3rooms"
        self.final_folder_name = "final_"+self.folder_name
        self.parcel_folder_name = 'parcel_'+self.folder_name
        self.image_size = 512
        self.list_of_image = os.listdir("ROBIN/"+self.final_folder_name)
        cv2.namedWindow(winname="Thumbnail")
        cv2.setMouseCallback("Thumbnail",self.get_point)
        self.footprint_points = []
        self.img = None
        if not os.path.isdir("ROBIN/"+self.parcel_folder_name):
            os.makedirs("ROBIN/"+self.parcel_folder_name)

    def get_point(self,event,x,y,flags,param):
        if event == 1:
            # press the left button
            self.footprint_points.append([x,y])
            print(event,x,y,flags,param)


    def create_footprint(self):
        for image in self.list_of_image[:5]:
            self.footprint_points = []
            self.img = cv2.imread("ROBIN/"+self.final_folder_name+"/"+image)
            self.img = cv2.resize(self.img,(self.image_size,self.image_size))
            
            while True:
                self.img_copy=np.copy(self.img)
                if len(self.footprint_points)>2:
                    corners = np.array(self.footprint_points)
                    self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=(255, 255, 255))
                if self.img is self.img_copy:
                    print("True")
                cv2.imshow("Thumbnail",self.img_copy)
                
                if cv2.waitKey(10) & 0xFF == 27:
                    break
            cv2.imwrite("ROBIN/"+self.parcel_folder_name+"/"+image,self.img_copy)
        cv2.destroyAllWindows()


parcel = Parcel_Preparation()
parcel.create_footprint()