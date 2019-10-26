#pdf轉jpg後擷取畫面

#需要用到模块wand，这是Imagemagick的Python接口。
#我们需要用它来将pdf转换为图片

from wand.image import Image
from PIL import Image as PIL_Image


f = "w001.pdf"
with(Image(filename=f, resolution=1000)) as source: 
    images = source.sequence
    pages = len(images)
    for i in range(pages):
        n = i + 1
        newfilename = f[:-4] + str(n) + '.jpeg'
        Image(images[i]).save(filename=newfilename)

        # -*-coding:utf-8-*-
       

        im = PIL_Image.open(newfilename)
        # 圖片的寬度和高度
        img_size = im.size
        print("圖片寬度和高度分別是{}".format(img_size))

        '''
        裁剪：傳入一個元組作為引數
        元組裡的元素分別是：（距離圖片左邊界距離x， 距離圖片上邊界距離y，
        距離圖片左邊界距離 裁剪框寬度x w，距離圖片上邊界距離 裁剪框高度y h）
        '''
        # 擷取圖片中一塊寬和高都是250的
        x = 0
        y = 0
        w = 1970
        h = 900
        region = im.crop((x, y, w, h))
        region.save(newfilename)


       



# # -*-coding:utf-8-*-
# from PIL import Image
# im = Image.open("w0011.jpeg")
# # 圖片的寬度和高度
# img_size = im.size
# print("圖片寬度和高度分別是{}".format(img_size))

# '''
# 裁剪：傳入一個元組作為引數
# 元組裡的元素分別是：（距離圖片左邊界距離x， 距離圖片上邊界距離y，
# 距離圖片左邊界距離 裁剪框寬度x w，距離圖片上邊界距離 裁剪框高度y h）
# '''
# # 擷取圖片中一塊寬和高都是250的
# x = 0
# y = 0
# w = 1970
# h = 900
# region = im.crop((x, y, w, h))
# region.save("./crop_test1.jpeg")

