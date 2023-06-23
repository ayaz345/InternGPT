import os
import sys

from .grit_src.image_dense_captions import image_caption_api, init_demo, dense_pred_to_caption, dense_pred_to_caption_only_name
from detectron2.data.detection_utils import read_image

class DenseCaptioning():
    def __init__(self, device):
        self.device = device
        self.demo =  None


    def initialize_model(self):
        #self.demo = init_demo(self.device)
        self.demo = init_demo("cpu")
    def image_dense_caption_debug(self, image_src):
        return """
        1. the broccoli is green, [0, 0, 333, 325]; 
        2. a piece of broccoli, [0, 147, 143, 324]; 
        3. silver fork on plate, [4, 547, 252, 612];
        """
    
    def image_dense_caption(self, image_src):
        dense_caption = image_caption_api(image_src, self.device)
        print('\033[1;35m' + '*' * 100 + '\033[0m')
        print("Step2, Dense Caption:\n")
        print(dense_caption)
        print('\033[1;35m' + '*' * 100 + '\033[0m')
        return dense_caption
    
    def run_caption_api(self,image_src):
        img = read_image(image_src, format="BGR")
        print(img.shape)
        predictions, visualized_output = self.demo.run_on_image(img,self.device)
        return dense_pred_to_caption_only_name(predictions)

    def run_caption_tensor(self,img):
        # img = read_image(image_src, format="BGR")
        # print(img.shape)
        predictions, visualized_output = self.demo.run_on_image(img,self.device)
        return dense_pred_to_caption_only_name(predictions)
    

