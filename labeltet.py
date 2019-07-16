
import cv2

label2 = [[1, 0.454102, 0.422852, 0.111328, 0.07617],
          [2, 0.177734, 0.214844, 0.041992, 0.055665],
          [2, 0.428711, 0.383789, 0.042968, 0.05664],
          [2, 0.734375, 0.496094, 0.060548, 0.046875],
          [2, 0.78125, 0.244141, 0.032228, 0.078125],
          [3, 0.670898, 0.277344, 0.041992, 0.07422],
          [2, 0.472656, 0.40625, 0.047852, 0.052735],
          [3, 0.638672, 0.28418, 0.04004, 0.07324]]

def test_img(m,label):
        """
        将生成的标签在图片中标记显示
        :param m: 第m+1个标签
        :param label: 图片对应的标签
        :return:
        """
        label2=label
        img2=cv2.imread(r'C:\\Users\\zzzZf\Desktop/result/new00hxh0001.jpg',1)

        label2=label2[m]
        x2,y2=int(label2[1] * 1024), int(label2[2] * 1024)
        x1=x2-int(label2[3] * 1024/2)
        y1=y2-int(label2[4] * 1024/2)
        x3=x2+int(label2[3] * 1024/2)
        y3=y2+int(label2[4] * 1024/2)

        ret1=cv2.rectangle(img2,(x1,y1),(x3,y3),(0,0,255),2)
        cv2.imshow('ret', ret1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
def base_img(i):
        label1=[[1,0.454102,0.422852,0.111328,0.07617 ],
                [2,0.764038,0.643262,0.010498,0.011133],
                [2,0.781006,0.651758,0.010742,0.011328],
                [2,0.857666,0.674219,0.015137,0.009375],
                [2,0.869263,0.624023,0.008057,0.015625],
                [3,0.841675,0.630469,0.010498,0.014844],
                [2,0.792114,0.656250,0.011963,0.010547],
                [2,0.619263,0.556152,0.020752,0.003320],
                [3,0.573120,0.547266,0.014893,0.004297],
                [3,0.636719,0.548633,0.012207,0.007422],
                [3,0.618164,0.553809,0.018555,0.004102],
                [3,0.833618,0.631934,0.010010,0.014648],
                [0,0.902466,0.615723,0.035889,0.021680]]
        img1=cv2.imread(r'C:\Users\zzzZf\Desktop\textttt\hxh0001.jpg',1)

        label1=label1[i]
        x0,y0=int(label1[1] * 4096), int(label1[2] * 5120)
        x1=x0+int(label1[3] * 4096)
        y1=y0+int(label1[4] * 5120)
        save_path_img=r'C:\Users\zzzZf\Desktop\hxh0000.jpg'
        ret=cv2.rectangle(img1,(x0,y0),(x1,y1),(0,0,255),2)
        cv2.imshow('ret', ret)
        cv2.imwrite(save_path_img, img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        label1=[1,0.798584,0.674805,0.027832,0.015234]
        x0,y0=int(label1[1] * 4096), int(label1[2] * 5120)
        x1=x0+int(label1[3] * 4096)
        y1=x0+int(label1[4] * 5120)
#base_img(0)
#test_img(0,label2)
