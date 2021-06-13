import os 
import cv2
import numpy as np
from copy import deepcopy, copy

class  Paired_Preparation:
    def __init__(self):
        self.folder_name = "Dataset_3rooms"
        self.final_folder_name_first = "parcel_"+self.folder_name
        self.final_folder_name_second = "footprint_"+self.folder_name
        self.save_folder_name = 'footprint_generation'+self.folder_name
        self.image_size = 512
        self.list_of_image = os.listdir("ROBIN/"+self.final_folder_name_first)
        self.img1 = None
        self.img2 = None
        if not os.path.isdir("ROBIN/"+self.save_folder_name):
            os.makedirs("ROBIN/"+self.save_folder_name)

    def create_paired(self):
        for image in self.list_of_image[:5]:
            self.footprint_points = []
            self.img1 = cv2.imread("ROBIN/"+self.final_folder_name_first+"/"+image)
            self.img1 = cv2.resize(self.img1,(self.image_size,self.image_size))
            self.img2 = cv2.imread("ROBIN/"+self.final_folder_name_second+"/"+image)
            self.img2 = cv2.resize(self.img2,(self.image_size,self.image_size))
            self.img_copy= cv2.hconcat([self.img1, self.img2])
            cv2.imwrite("ROBIN/"+self.save_folder_name+"/"+image,self.img_copy)

paired = Paired_Preparation()
paired.create_paired()