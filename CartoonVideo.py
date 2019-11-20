'''
Created on 18-Oct-2019

@author: elango
'''

import cv2
import numpy as np
import sys
from tqdm import tqdm

SPEEDUP = 1.1

def cartoonize(video_in, video_out, start_sec=0, end_sec=100000):
    cap = cv2.VideoCapture(video_in)
    
    w, h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = float(cap.get(cv2.CAP_PROP_FPS))
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    

    start_frame, end_frame = start_sec*fps, end_sec*fps

    #min_y,max_y = int(h/4), h
    #min_x,max_x = 0, int(w*3/4)
    
    min_y,max_y = 0, h
    min_x,max_x = 0, w
    out_h = max_y - min_y
    out_w = max_x - min_x

    writer = cv2.VideoWriter(video_out, cv2.VideoWriter_fourcc(*'MP4V'), SPEEDUP*fps, (out_w, out_h))
    
    for i in tqdm(range(length)):
        ret, img = cap.read()
    
        if start_frame <= i <= end_frame: 
            img = img[min_y:max_y, min_x:max_x]
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)
            edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
            color = cv2.bilateralFilter(img, 9, 300, 300)
            cartoon = cv2.bitwise_and(color, color, mask=edges)
            writer.write(cartoon)
    
    writer.release()
    cap.release()

if __name__ == '__main__':
    video_in, video_out = sys.argv[1], sys.argv[2]
    start_sec = int(sys.argv[3])
    end_sec = int(sys.argv[4])
    cartoonize(video_in, video_out, start_sec, end_sec)
