# FP-Datasets
Datasets for FP generation using GAN 
This is a repo to generate datsets for FP generation Using GAN. Here, we are going to use ROBIN well furnished datasets and create previous datasets following which we can reach up to the furnished datasets. Here we are to generate 5 different types of datasets which are:
1. Augmented Datasets with better spacing in all 4 sides of images with same image size of all images and few other datasets with 30 degree rotation of the current sets.
2. Then we create final raw datasets, i.e datasets with augmented and space outside plan and also with the land area i.e boundary of the oner's land.
3. Then we create parcel using the augmented datasets, i.e remove the building and create datasets with parcel only.
4. Then using the same final datasets, we create footprint of the floor.
5. Then using the same final datasets, we create room split plan of the floor using the color representation of rooms.
6. Then using same final datasets, we create well furnished dataset of the floor using the color representation of furniture.

Overall steps to be followed to create different types of datasets:
1. Clone the git repo in local using command : git clone https://github.com/banmala/FP-Datasets.git 

2. Download ROBIN FloorPlan datasets from _____ and paste the ROBIN folder inside the main repo.

3. First of all, augmentation of the datas  to create extra space around the plans so as to make all the datasets of same size, and to create extra space around to draw some parcel in the datasets: python3 create_augmented_datset.py

4. Create final raw datas for further processing by drawing some parcel around augmented datas and create final data for datasets creation: python3 create_Final_Data.py

5. Create parcels by clearing the plans from final data. It can be done by placing corresponding points of corner inside the parcel and outside the plan: same as is donw to craeate parcel: python3 create_parcel.py

6. Create footprint by using same polylines method and pinpoint corresponding corners of the house and get the foorprint: python3 create_footprint.py

7. Create roomsplit: python3 create_roomsplit.py

8. Create furnished rooms: create_furnished.py

9. Now Creating paired images of the datasets for corresponding transformation, i.e Parcel-Footprint, Footprint-RoomSplit, RoomSplit-Furnished and Furnished-FurnitureMapped  : set the folders first and second from which paired datasets are to be created and also choose the folder name to save the dataset then run: python3 create_paired_images.py