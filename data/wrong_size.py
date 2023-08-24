#detect jpg images which have wrong size label
import cv2
import os
import xml.etree.ElementTree as ET

path= "./data/缺陷识别raw/设备部件识别"
classes = ['cysb_qyb', 'ddjt', 'cysb_sgz', 'SF6ylb', 'drq', 'ecjxh', 'drqgd', 'cysb_tg', 'cysb_lqq', 'cysb_qtjdq', 'xldlb', 'yx', 'sly_dmyw', 'ywj', 'ywb', 'jdyxx', 'fhz_f', 'bmwh', 'xmbhzc', 'pzq', 'jyh', 'ywc', 'cysb_cyg', 'bjzc']

def get_label_size(imagename):
    in_file = open(os.path.join(path, "labels", imagename + ".xml"))
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)
    return width, height

imgpath = os.path.join(path, "images")
labelpath = os.path.join(path, "labels")

imglist = os.listdir(imgpath)
wrong = open(os.path.join(path,"wrong_size.txt"), 'w')
for imgname in imglist:
    if(imgname.split(".")[1] != "jpg" and imgname.split(".")[1] != "JPG"):
        continue
    img = cv2.imread(os.path.join(imgpath, imgname))
    width, height = img.shape[1], img.shape[0]
    label_width, label_height = get_label_size(imgname.split(".")[0])
    if(width != label_width or height != label_height):
        print(imgname)
        wrong.write(imgname + "\n")
        wrong.write(imgname.strip(".jpg").strip(".JPG") + ".xml\n")

wrong.close()


