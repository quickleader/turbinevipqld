# -*- coding: utf-8 -*-
"""
批量将 static/img 下 JPG/PNG 转为 WebP（保留原图作为 fallback）。
数据隔离：仅本地处理，不上传网络。
"""
import os
from PIL import Image

ROOT = "D:/wbwork/turbinevipqld-work/static/img"
QUALITY = 82
exts = (".jpg", ".jpeg", ".png")

total_src = 0
total_webp = 0
count = 0
skipped = 0

for dirpath, _, files in os.walk(ROOT):
    for fn in files:
        if fn.lower().endswith(exts):
            src = os.path.join(dirpath, fn)
            base, _ = os.path.splitext(src)
            dst = base + ".webp"
            if os.path.exists(dst):
                skipped += 1
                continue
            try:
                im = Image.open(src)
                # PNG 带透明通道保留 RGBA，其余转 RGB
                if im.mode in ("RGBA", "LA", "P"):
                    im = im.convert("RGBA")
                else:
                    im = im.convert("RGB")
                im.save(dst, "WEBP", quality=QUALITY, method=6)
                s_src = os.path.getsize(src)
                s_dst = os.path.getsize(dst)
                total_src += s_src
                total_webp += s_dst
                count += 1
            except Exception as e:
                print(f"  [ERR] {src}: {e}")

print(f"转换完成: {count} 张, 跳过(已存在): {skipped}")
if total_src:
    saved = 100 * (1 - total_webp / total_src)
    print(f"原始: {total_src/1024/1024:.2f} MB -> WebP: {total_webp/1024/1024:.2f} MB (节省 {saved:.1f}%)")
