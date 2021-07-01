import os 
import cv2
import numpy as np
from copy import deepcopy, copy
from PIL import ImageColor
# ESC to next 
# c to clear the door image 
class  Parcel_Preparation:
    def __init__(self):
        self.folder_name = "Dataset_4rooms"
        self.final_folder_name = "final_"+self.folder_name
        self.furnished_folder_name = 'furnished_'+self.folder_name
        self.image_size = 512
        self.list_of_image = os.listdir("ROBIN/"+self.final_folder_name)
        cv2.namedWindow(winname="Thumbnail")
        cv2.setMouseCallback("Thumbnail",self.get_point)
        self.armchair = []
        self.bed = []
        self.coffeetable = []
        self.roundtable = []
        self.largesofa = []
        self.smallsofa = []
        self.sink = []
        self.twinsink = []
        self.smallsink = []
        self.largesink = []
        self.tub = []
        self.dinningtable = []
        self.temp = []
        self.possible_state =['armchair','bed','coffeetable','roundtable','largesofa','smallsofa','sink','twinsink','smallsink','largesink','tub','dinningtable']
        self.state = ""
        self.img = None
        if not os.path.isdir("ROBIN/"+self.furnished_folder_name):
            os.makedirs("ROBIN/"+self.furnished_folder_name)

    def get_point(self,event,x,y,flags,param):
        if event == 1:
            # press the left button
            self.temp.append([x,y])

    def change_class(self):
        if self.state == 'armchair':
            self.armchair.append(self.temp)
        elif self.state == 'bed':
            self.bed.append(self.temp)
        elif self.state == 'coffeetable':
            self.coffeetable.append(self.temp)
        elif self.state == 'roundtable':
            self.roundtable.append(self.temp)
        elif self.state == 'largesofa':
            self.largesofa.append(self.temp)
        elif self.state == 'smallsofa':
            self.smallsofa.append(self.temp)
        elif self.state == 'sink':
            self.sink.append(self.temp)
        elif self.state == 'twinsink':
            self.twinsink.append(self.temp)
        elif self.state == 'smallsink':
            self.smallsink.append(self.temp)
        elif self.state == 'largesink':
            self.largesink.append(self.temp)
        elif self.state == 'tub':
            self.tub.append(self.temp)
        elif self.state == 'dinningtable':
            self.dinningtable.append(self.temp)
        self.temp =[]
        

    def create_footprint(self):
        for image in self.list_of_image:
            if not os.path.isfile('ROBIN/'+self.furnished_folder_name+'/'+image):
                self.armchair = []
                self.bed = []
                self.coffeetable = []
                self.roundtable = []
                self.largesofa = []
                self.smallsofa = []
                self.sink = []
                self.twinsink = []
                self.smallsink = []
                self.largesink = []
                self.tub = []
                self.dinningtable = []
                self.temp = []
                self.state = ""
                self.isClear = False
                self.img = cv2.imread("ROBIN/"+self.final_folder_name+"/"+image)
                self.img = cv2.resize(self.img,(self.image_size*2,self.image_size*2))
                while True:
                    self.img_copy=np.copy(self.img)
                    if len(self.temp)>2:
                        corners = np.array(self.temp)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#cccccc','RGB')[::-1])
                    for armchair in self.armchair: 
                        corners = np.array(armchair)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#c8b18b','RGB')[::-1])
                    for bed in self.bed:
                        corners = np.array(bed)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#23eaa5','RGB')[::-1])
                    for coffeetable in self.coffeetable:
                        corners = np.array(coffeetable)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#f483cd','RGB')[::-1])
                    for roundtable in self.roundtable:
                        corners = np.array(roundtable)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#276cbd','RGB')[::-1])
                    for largesofa in self.largesofa:
                        corners = np.array(largesofa)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#f59080','RGB')[::-1])
                    for smallsofa in self.smallsofa:
                        corners = np.array(smallsofa)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#61419c','RGB')[::-1])
                    for sink in self.sink:
                        corners = np.array(sink)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#b83773','RGB')[::-1])
                    for twinsink in self.twinsink:
                        corners = np.array(twinsink)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#ebdd21','RGB')[::-1])
                    for smallsink in self.smallsink:
                        corners = np.array(smallsink)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#8b1c0e','RGB')[::-1])
                    for largesink in self.largesink:
                        corners = np.array(largesink)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#a7dc26','RGB')[::-1])
                    for tub in self.tub:
                        corners = np.array(tub)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#e83b1b','RGB')[::-1])
                    for dinningtable in self.dinningtable:
                        corners = np.array(dinningtable)
                        self.img_copy = cv2.fillPoly(self.img_copy, [corners], color=ImageColor.getcolor('#20340b','RGB')[::-1])

                    cv2.imshow("Thumbnail",self.img_copy)
                    
                    key = cv2.waitKey(10) & 0xFF
                    if key == 27:
                        break
                    if key == ord('a'):
                        self.change_class()
                        self.state = 'armchair'
                        print(self.state)
                    elif key == ord('b'):
                        self.change_class()
                        self.state = 'bed'
                        print(self.state)
                    elif key == ord('c'):
                        self.change_class()
                        self.state = 'coffeetable'
                        print(self.state)
                    elif key == ord('d'):
                        self.change_class()
                        self.state = 'roundtable'
                        print(self.state)
                    elif key == ord('e'):
                        self.change_class()
                        self.state = 'largesofa'
                        print(self.state)
                    elif key == ord('f'):
                        self.change_class()
                        self.state = 'smallsofa'
                        print(self.state)
                    elif key == ord('g'):
                        self.change_class()
                        self.state = 'sink'
                        print(self.state)
                    elif key == ord('h'):
                        self.change_class()
                        self.state = 'twinsink'
                        print(self.state)
                    elif key == ord('i'):
                        self.change_class()
                        self.state = 'smallsink'
                        print(self.state)
                    elif key == ord('j'):
                        self.change_class()
                        self.state = 'largesink'
                        print(self.state)
                    elif key == ord('k'):
                        self.change_class()
                        self.state = 'tub'
                        print(self.state)
                    elif key == ord('l'):
                        self.change_class()
                        self.state = 'dinningtable'
                        print(self.state)
            if len(self.armchair+self.bed+self.coffeetable+self.roundtable+self.largesofa+self.smallsofa+self.sink+self.twinsink+self.smallsink+self.largesink+self.tub+self.dinningtable) != 0:
                self.img_copy = cv2.resize(self.img_copy,(self.image_size,self.image_size))
                cv2.imwrite("ROBIN/"+self.furnished_folder_name+"/"+image,self.img_copy)
                print("saved")
            else:
                print("Roomsplit already created")
        cv2.destroyAllWindows()


parcel = Parcel_Preparation()
parcel.create_footprint()
