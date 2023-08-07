import cv2
import os


path= "./data/缺陷识别yolo/设备部件识别"
classes = ['cysb_qyb', 'ddjt', 'cysb_sgz', 'SF6ylb', 'drq', 'ecjxh', 'drqgd', 'cysb_tg', 'cysb_lqq', 'cysb_qtjdq', 'xldlb', 'yx', 'sly_dmyw', 'ywj', 'ywb', 'jdyxx', 'fhz_f', 'bmwh', 'xmbhzc', 'pzq', 'jyh', 'ywc', 'cysb_cyg', 'bjzc']

imgpath = os.path.join(path, "images/train")
labelpath = os.path.join(path, "labels/train")

imglist = os.listdir(imgpath)

for imgname in imglist:
    if(imgname.split(".")[1] != "jpg" and imgname.split(".")[1] != "JPG"):
        continue

    img = cv2.imread(os.path.join(imgpath, imgname))
    labels = open(os.path.join(labelpath, imgname.split(".")[0]+".txt"), "r")
    for label in labels:
        label = label.split(" ")
        x = int(float(label[1]) * img.shape[1])
        y = int(float(label[2]) * img.shape[0])
        w = int(float(label[3]) * img.shape[1])
        h = int(float(label[4]) * img.shape[0])
        x1 = int(x - w/2)
        y1 = int(y - h/2)
        x2 = int(x + w/2)
        y2 = int(y + h/2)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, classes[int(label[0])], (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2)
    cv2.imshow(imgname,img)
    cv2.waitKey(0)
    cv2.destroyWindow(imgname)
    cv2.waitKey(1) 


