import cv2
import pyzbar.pyzbar as pyzbar
import requests

def decode_qr_code(image_path):
    # 读取图像
    frame = cv2.imread(image_path)

    # 转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 二维码检测
    decoded_objects = pyzbar.decode(gray)

    # 提取二维码内容
    for obj in decoded_objects:
        video_url = obj.data.decode('utf-8')
        print("Video URL:", video_url)
        return video_url

    return None

def download_video(video_url, output_path):
    # 发送GET请求
    response = requests.get(video_url, stream=True)

    # 确保请求成功
    if response.status_code == 200:
        # 打开一个本地文件用于写入
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:  # 过滤掉保持连接的chunk
                    f.write(chunk)
        print(f"Video downloaded and saved to {output_path}")
    else:
        print("Failed to download video")

# 图片路径
image_path = '"C:\\Users\\86183\\Desktop\\微信图片_20241206172718.jpg"'
# 视频保存路径
output_path = 'C:\\Users\\86183\\Downloads.mp4'

# 解码二维码
video_url = decode_qr_code(image_path)

if video_url:
    # 下载并保存视频
    download_video(video_url, output_path)
else:
    print("No QR code found in the image")