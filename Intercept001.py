#coding=utf-8
import cv2
import numpy as np
import os
import os.path
#input_dir1=r'C:\Users\zzzZf\Desktop/text'
#output_dir1=r'C:\Users\zzzZf\Desktop\result'
input_dir=r"C:\Users\zzzZf\Desktop\min\3"
output_dir=r"C:\Users\zzzZf\Desktop\save\min\3"
def intercept_img(input_dir,output_dir):
    '''
    样本扩充及处理：将带有目标标签的4096*5120的图片截取成1024*1024并输出在新图片中目标的标签（x,y,w,h）
    :param input_dir: 存储4096*5120图片及其标签的路径（英文）
    :param output_dir: 存储处理后1024*1024图片及其标签的路径（英文）
    :return:
    '''
    # 获得图片和标签的名称列表
    file_list=os.listdir(input_dir)
    img_list=[]
    label_list=[]
    for filename in file_list:
        pos=filename.rfind(".")
        if filename[pos+1:]=="jpg":
            img_list.append(filename)
        elif filename[pos+1:]=="txt":
            label_list.append(filename)
    print('打印图片和标签的名称列表:',img_list,label_list)#打印图片和标签的名称列表
    # 设置获得图片标签路径
    for i in range(len(img_list)):
        img=img_list[i]
        print(img)
        label_name=label_list[i]
        work_path_img = input_dir + '/' + img
        work_path_img = work_path_img.replace('\ ', "/")
        work_path_label = input_dir + '/' + label_name
        work_path_label = work_path_label.replace('\ ', "/")

        label = []
        with open(work_path_label, "r") as f:
            label1 = f.readlines()
            #print(label1, len(label1))
            for m in range(len(label1)):
                label2 = label1[m]
                label3 = label2.split()
                label.append(label3[0:5])
        print('打印标签列表',label)
    # 裁剪图片
        img1 = cv2.imread(work_path_img, 1)
        for m in range(len(label)):
            new_label=label[m]
            new_label = list(map(float,new_label))
            print('中心目标船只标签',new_label)
            #图片中心坐标
            x0, y0 = int(new_label[1] * 4096), int(new_label[2] * 5120)
            a = np.random.randint(-206, 206, 2)#生成随机数
            xb, yb = a[0], a[1]
            x0=x0+xb
            y0=y0+yb

            #图片原点坐标
            x1, y1 = x0 - 511, y0 - 511
            x2, y2 = x0 + 513, y0 + 513
            if x1<0 :
                x1=0
                x2=1024
            if  y1<0:
                y1=0
                y2=1024
            if x2>4096:
                x1 = 3072
                x2 = 4096
            if y2 > 5120:
                y1 = 4096
                y2 = 5120
            cutimg1 = img1[y1:y2,x1:x2]

            #cv2.imshow('image', cutimg)
            #cv2.imwrite('cut.jpg', cutimg)
            #cv2.waitKey(0)

            sum_label = []
            #判断图片里是否有其他船只
            for n in range(len(label)):
                text_label = label[n]
                text_label = list(map(float, text_label))

                xt, yt = int(text_label[1] * 4096), int(text_label[2] * 5120)
                if 0<=xt-x1<=1024 and 0<=yt-y1<=1024:
                    #text_label = [str(i) + ' ' for i in text_label]
                    text_label[0] = int(text_label[0])
                    x_t, y_t = xt-x1,yt-y1
                    text_label[1] = x_t/ 1024
                    text_label[2] = y_t/ 1024
                    text_label[1] = float('%.6f' % text_label[1])
                    text_label[2] = float('%.6f' % text_label[2])
                    text_label[3] = text_label[3] * 4096 / 1024
                    text_label[4] = text_label[4] * 5120 / 1024
                    text_label[3] = float('%.6f' % text_label[3])
                    text_label[4] = float('%.6f' % text_label[4])
                    # cv2.imshow('origin', img)
                    for k in text_label:
                        a=str(k)+" "
                        sum_label.append(a)
                    sum_label.append('\n')
            print('所有船只标签：',sum_label)
            # 储存图片及标签
            a='new{}{}'.format(i,m)
            save_path_img = output_dir + '/' + a+img
            save_path_img = save_path_img.replace('\ ', "/")
            save_path_label = output_dir + '/' + a + label_name
            save_path_label = save_path_label.replace('\ ', "/")

            cv2.imwrite(save_path_img, cutimg1)
            with open(save_path_label,"w") as f:
                f.writelines(sum_label)





intercept_img(input_dir,output_dir)

