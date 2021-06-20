import os 
import cv2
import numpy as np
from copy import deepcopy, copy
from PIL import ImageColor
# ESC to next 
# c to clear the door image 
class  Parcel_Preparation:
    def __init__(self):
        self.folder_name = "Dataset_3rooms"
        self.final_folder_name = "final_"+self.folder_name
        self.roomsplit_folder_name = 'roomsplit_'+self.folder_name
        self.image_size = 512
        self.list_of_image = os.listdir("ROBIN/"+self.final_folder_name)
        cv2.namedWindow(winname="Thumbnail")
        cv2.setMouseCallback("Thumbnail",self.get_point)
        self.bedroom = []
        self.bathroom = []
        self.entry = []
        self.kitchen = []
        self.hall = []
        self.temp = []
        self.possible_state =['bedroom','bathroom','entry','kitchen','hall']
        self.state = ""
        self.img = None
        if not os.path.isdir("ROBIN/"+self.roomsplit_folder_name):
            os.makedirs("ROBIN/"+self.roomsplit_folder_name)

    def get_point(self,event,x,y,flags,param):
        if event == 1:
            # press the left button
            self.temp.append([x,y])
            # if self.state in self.possible_state:
            #     idx = self.possible_state.index(self.state)
            #     if idx == 0: 
            #         self.bedroom.append([x,y])
            #     elif idx == 1:
            #         self.bathroom.append([x,y])
            #     elif idx == 2: 
            #         self.entry.append([x,y])
            #     elif idx == 3:
            #         self.kitchen.append([x,y])
            #     elif idx == 4: 
            #         self.hall.append([x,y])              

    def change_class(self):
        if self.state == 'bedroom':
            self.bedroom.append(self.temp)
        elif self.state == 'bathroom':
            self.bathroom.append(self.temp)
        elif self.state == 'entry':
            self.entry.append(self.temp)
        elif self.state == 'kitchen':
            self.kitchen.append(self.temp)
        elif self.state == 'hall':
            self.hall.append(self.temp)
        self.temp =[]
        

    def create_footprint(self):
        for image in self.list_of_image:
            if not os.path.isfile('ROBIN/'+self.roomsplit_folder_name+'/'+image):
                self.bedroom = []
                self.bathroom = []
                self.entry = []
                self.kitchen = []
                self.hall = []
                self.temp = []
                self.state = ""
                self.isClear = False
                self.img = cv2.imread("ROBIN/"+self.final_folder_name+"/"+image)
                self.img = cv2.resize(self.img,(self.image_size,self.image_size))
                
                while True:
                    self.img_copy=np.copy(self.img)
                    if len(self.temp)>2:
                        corners = np.array(self.temp)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#cccccc','RGB')[::-1])
                    
                    for bedroom in self.bedroom: 
                        corners = np.array(bedroom)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#f1bf15','RGB')[::-1])
                    for bathroom in self.bathroom:
                        corners = np.array(bathroom)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#9352a8','RGB')[::-1])
                    for entry in self.entry:
                        corners = np.array(entry)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#f7760b','RGB')[::-1])
                    for kitchen in self.kitchen:
                        corners = np.array(kitchen)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#99c6f9','RGB')[::-1])
                    for hall in self.hall:
                        corners = np.array(hall)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#d51c3c','RGB')[::-1])
                    cv2.imshow("Thumbnail",self.img_copy)
                    
                    key = cv2.waitKey(10) & 0xFF
                    if key == 27:
                        break
                    if key == ord('a'):
                        self.change_class()
                        self.state = 'bedroom'
                        print(self.state)
                    
                    elif key == ord('b'):
                        self.change_class()
                        self.state = 'bathroom'
                        print(self.state)
                    elif key == ord('c'):
                        self.change_class()
                        self.state = 'entry'
                        print(self.state)
                    elif key == ord('d'):
                        self.change_class()
                        self.state = 'kitchen'
                        print(self.state)
                    elif key == ord('e'):
                        self.change_class()
                        self.state = 'hall'
                        print(self.state)
            if len(self.bedroom+self.bathroom+self.entry+self.kitchen+self.hall) != 0:
                cv2.imwrite("ROBIN/"+self.roomsplit_folder_name+"/"+image,self.img_copy)
                print("saved")
            else:
                print("Roomsplit already created")
        cv2.destroyAllWindows()


parcel = Parcel_Preparation()
parcel.create_footprint()