#pdf轉jpg後擷取畫面

#需要用到模块wand，这是Imagemagick的Python接口。
#我们需要用它来将pdf转换为图片

from wand.image import Image

f = "w001.pdf"
with(Image(filename=f, resolution=600)) as source: 
    images = source.sequence
    pages = len(images)
    for i in range(pages):
        n = i + 1
        newfilename = f[:-4] + str(n) + '.jpeg'
        Image(images[i]).save(filename=newfilename)