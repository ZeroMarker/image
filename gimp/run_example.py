#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GIMP 命令行图片生成示例
使用 GIMP 的批处理模式生成图片
"""

import subprocess
import os
import sys


def run_gimp_script(script_path, args=None):
    """运行 GIMP Python-Fu 脚本"""
    # GIMP 可执行文件路径
    gimp_cmd = "gimp"
    
    # 构建命令
    cmd = [
        gimp_cmd,
        "-i",  # 非交互模式
        "-b", f"(python-fu-eval RUN-NONINTERACTIVE 0 \"execfile('{script_path}')\")",
        "-b", "(gimp-quit 0)"
    ]
    
    print(f"运行命令: {' '.join(cmd)}")
    
    # 执行命令
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("输出:")
        print(result.stdout)
        if result.stderr:
            print("错误:")
            print(result.stderr)
        return result.returncode == 0
    except FileNotFoundError:
        print("错误: 未找到 GIMP 命令")
        print("请确保 GIMP 已安装并添加到系统 PATH")
        return False


def generate_script_content():
    """生成 GIMP Python-Fu 脚本内容"""
    script = '''
import os
from gimpfu import *

OUTPUT_DIR = os.path.expanduser("~/gimp_output")
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def create_simple_image():
    # 创建 800x600 图片
    image = gimp.Image(800, 600, RGB)
    
    # 创建背景图层
    layer = gimp.Layer(image, "Background", 800, 600, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(layer, 0)
    
    # 渐变背景
    gimp.set_foreground((41, 128, 185))
    gimp.set_background((52, 152, 219))
    pdb.gimp_edit_blend(layer, BLEND_FG_BG_RGB, LAYER_MODE_NORMAL,
                         GRADIENT_LINEAR, 100, 0, REPEAT_NONE, FALSE, FALSE,
                         0, 0, TRUE, 0, 0, 800, 600)
    
    # 添加圆形
    gimp.set_foreground((255, 255, 255))
    pdb.gimp_image_select_ellipse(image, CHANNEL_OP_REPLACE, 300, 200, 200, 200)
    pdb.gimp_edit_fill(layer, FILL_FOREGROUND)
    pdb.gimp_selection_none(image)
    
    # 添加文字
    pdb.gimp_text_fontname(image, None, 250, 450, "GIMP", 0, TRUE, 72, UNIT_PIXEL, "Sans Bold")
    
    # 合并图层
    image.flatten()
    
    # 导出
    full_path = os.path.join(OUTPUT_DIR, "gimp_example.png")
    pdb.file_png_save(image, image.active_layer, full_path, full_path, 0, 9, 1, 1, 1, 1, 1)
    print("已创建: " + full_path)
    
    gimp.delete(image)

create_simple_image()
'''
    return script


def main():
    print("=" * 50)
    print("GIMP 命令行图片生成示例")
    print("=" * 50)
    print()
    
    # 创建临时脚本文件
    script_content = generate_script_content()
    script_path = os.path.join(os.path.dirname(__file__), "_temp_gimp_script.py")
    
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print(f"临时脚本: {script_path}")
    print()
    
    # 运行 GIMP 脚本
    success = run_gimp_script(script_path)
    
    # 清理临时文件
    try:
        os.remove(script_path)
    except:
        pass
    
    if success:
        print()
        print("=" * 50)
        print("图片生成成功！")
        print(f"输出目录: {os.path.expanduser('~/gimp_output')}")
        print("=" * 50)
    else:
        print()
        print("图片生成失败，请检查 GIMP 安装")


if __name__ == "__main__":
    main()
