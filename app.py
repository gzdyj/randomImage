import os
import random
from flask import Flask, send_file, abort

app = Flask(__name__)

# 设置图片路径
IMAGE_FOLDER_1 = r'E:\\path\\to\\output\\folder2'  # 第一个文件夹路径
# IMAGE_FOLDER_2 = r'F:\\photo\\organized_images\\folder_2'  # 第二个文件夹路径
TOTAL_IMAGES_1 = 1489  # folder_1 最大图片数量
TOTAL_IMAGES_2 = 1000    # folder_2 最大图片数量

@app.route('/random_image/folder1')
def random_image_folder1():
    return get_random_image(IMAGE_FOLDER_1, TOTAL_IMAGES_1)

# @app.route('/random_image/folder2')
# def random_image_folder2():
#     return get_random_image(IMAGE_FOLDER_2, TOTAL_IMAGES_2)

def get_random_image(image_folder, total_images):
    try:
        # 生成随机图片索引
        random_index = random.randint(1, total_images) if total_images == 10000 else random.randint(0, total_images)
        print(random_index)
        image_name = f"{random_index}.jpg"
        image_path = os.path.join(image_folder, image_name)

        # 检查文件是否存在
        if not os.path.exists(image_path):
            return "图片不存在", 404

        # 返回图片文件
        return send_file(image_path)
    
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12300)  # 在所有可用的IP地址上运行服务