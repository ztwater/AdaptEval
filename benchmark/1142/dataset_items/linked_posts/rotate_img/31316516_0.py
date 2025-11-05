im = dbimg[i]
bb = boxes[i]  
m = im.transpose((1, 2, 0)).astype(np.uint8).copy() 
pt1 = (bb[0],bb[1])
pt2 = (bb[0]+bb[2],bb[1]+bb[3])  
cv2.rectangle(m,pt1,pt2,(0,255,0),2)  
