"""
PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，
又加入了许多新特性，因此，我们可以直接安装使用Pillow。

官方网站: https://pillow.readthedocs.io
"""
import random

from PIL import Image, ImageFont, ImageDraw, ImageFilter

# ================================================
# 图像缩放操作
# ================================================

# 打开图像
img = Image.open("music-life.jpg")
# 获取图像尺寸
w, h = img.size
print("original image size: %d x %d" % (w, h))
# 先复制一份
img1 = img.copy()
# 缩放到50%:
img1.thumbnail((w // 2, h // 2))
print('Resize image to: %sx%s' % (w // 2, h // 2))
# 把缩放后的图像用jpeg格式保存:
img1.save('thumbnail.jpg', 'jpeg')

# 不能放大图片，只能压缩？ValueError: box can't exceed original image size
# img2 = img.copy()
# img2.resize((w * 2, h * 2), box=(0, 0, w * 2, h * 2))
# print('Resize image to: %sx%s' % (w * 2, h * 2))
# # 把缩放后的图像用jpeg格式保存:
# img2.save('resizex2.gif', 'gif')

# ================================================
# 模糊图片
# ================================================

# 应用模糊滤镜
img3 = img.copy()
# 返回新的Image对象
dst = img3.filter(ImageFilter.BLUR)
dst.save('blur.jpg', 'jpeg')


# ================================================
# 生成验证码图片
# ================================================

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 120 x 40:
width = 60 * 2
height = 40
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((20 * t + 5 + random.randint(0, 5), 5), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
