import os 
import cv2
import numpy as np
class  Parcel_Preparation:
    def __init__(self):
        self.folder_name = "Dataset_3rooms"
        self.parcel_folder_name = "final_"+self.folder_name
        self.image_size = 512
        self.list_of_image = os.listdir("ROBIN/"+self.folder_name)
        cv2.namedWindow(winname="Thumbnail")
        cv2.setMouseCallback("Thumbnail",self.get_point)
        self.parcel_points = []
        self.img = None
        if not os.path.isdir("ROBIN/"+self.parcel_folder_name):
            os.makedirs("ROBIN/"+self.parcel_folder_name)

    def get_point(self,event,x,y,flags,param):
        if event == 1:
            # press the left button
            self.parcel_points.append([x,y])
            print(event,x,y,flags,param)


    def start(self):
        for image in self.list_of_image[:5]:
            self.parcel_points = []
            self.img = cv2.imread("ROBIN/"+self.folder_name+"/"+image)
            self.img = cv2.resize(self.img,(self.image_size,self.image_size))
            
            while True:
                corners = np.array(self.parcel_points)
                self.img = cv2.polylines(self.img, [corners],
                           isClosed=False, color=(0,0,0), thickness=9)
                cv2.imshow("Thumbnail",self.img)
                
                if cv2.waitKey(10) & 0xFF == 27:
                    break
            cv2.imwrite("ROBIN/"+self.parcel_folder_name+"/"+image,self.img)
        cv2.destroyAllWindows()


parcel = Parcel_Preparation()
parcel.start()