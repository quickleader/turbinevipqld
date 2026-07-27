# -*- coding: utf-8 -*-
"""
从现有 logo 无损生成移动端图标 (apple-touch-icon / android-chrome)。
数据隔离：仅本地处理，不上传网络。
"""
import os
from PIL import Image

SRC = "D:/wbwork/turbinevipqld-work/static/img/logo/mark.jpg"
OUT_DIR = "D:/wbwork/turbinevipqld-work/static/img/favicon"
os.makedirs(OUT_DIR, exist_ok=True)

# 目标图标规格 (尺寸, 文件名)
TARGETS = [
    (180, "apple-touch-icon.png"),      # iOS 主屏图标
    (192, "android-chrome-192x192.png"),# Android/PWA
    (512, "android-chrome-512x512.png"),# PWA 高清
    (32,  "favicon-32x32.png"),         # 桌面标签页
    (16,  "favicon-16x16.png"),         # 桌面标签页小图
]

def make_square(im):
    """居中裁切为正方形，避免拉伸变形。"""
    w, h = im.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    return im.crop((left, top, left + side, top + side))

def main():
    im = Image.open(SRC).convert("RGB")
    print(f"源图: {SRC} 尺寸={im.size}")
    sq = make_square(im)
    print(f"居中裁切正方形: {sq.size}")
    for size, name in TARGETS:
        resized = sq.resize((size, size), Image.LANCZOS)
        out_path = os.path.join(OUT_DIR, name)
        resized.save(out_path, "PNG", optimize=True)
        print(f"  生成 {name}: {size}x{size} -> {os.path.getsize(out_path)} bytes")

    # 生成 site.webmanifest (PWA)
    manifest = '''{
  "name": "Qingdao Quickleader - Power Plant 4S Service Center",
  "short_name": "Quickleader",
  "icons": [
    {"src": "/img/favicon/android-chrome-192x192.png", "sizes": "192x192", "type": "image/png"},
    {"src": "/img/favicon/android-chrome-512x512.png", "sizes": "512x512", "type": "image/png"}
  ],
  "theme_color": "#ffffff",
  "background_color": "#ffffff",
  "display": "standalone"
}
'''
    manifest_path = os.path.join("D:/wbwork/turbinevipqld-work/static", "site.webmanifest")
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(manifest)
    print(f"  生成 site.webmanifest")
    print("完成。")

if __name__ == "__main__":
    main()
