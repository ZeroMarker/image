#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GIMP Python-Fu 图片生成脚本集合
用法: gimp -i -b '(python-fu-eval RUN-NONINTERACTIVE 0 "execfile(\"create_images.py\")")' -b '(gimp-quit 0)'
"""

from gimpfu import *
import os

# 输出目录
OUTPUT_DIR = os.path.expanduser("~/gimp_output")
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def create_blank_image(width=800, height=600, color=(255, 255, 255), filename="blank.png"):
    """创建空白图片"""
    image = gimp.Image(width, height, RGB)
    
    # 创建背景图层
    layer = gimp.Layer(image, "Background", width, height, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(layer, 0)
    
    # 填充颜色
    gimp.set_background(color)
    pdb.gimp_edit_fill(layer, FILL_BACKGROUND)
    
    # 导出
    full_path = os.path.join(OUTPUT_DIR, filename)
    pdb.file_png_save(image, layer, full_path, full_path, 0, 9, 1, 1, 1, 1, 1)
    print(f"已创建: {full_path}")
    
    gimp.delete(image)


def create_gradient_image(width=800, height=600, filename="gradient.png"):
    """创建渐变图片"""
    image = gimp.Image(width, height, RGB)
    
    # 创建背景图层
    layer = gimp.Layer(image, "Background", width, height, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(layer, 0)
    
    # 设置渐变颜色
    gimp.set_foreground((0, 102, 255))  # 蓝色
    gimp.set_background((255, 51, 102))  # 粉色
    
    # 应用渐变
    pdb.gimp_edit_blend(layer, BLEND_FG_BG_RGB, LAYER_MODE_NORMAL, 
                         GRADIENT_LINEAR, 100, 0, REPEAT_NONE, FALSE, FALSE, 
                         0, 0, TRUE, 0, 0, width, height)
    
    # 导出
    full_path = os.path.join(OUTPUT_DIR, filename)
    pdb.file_png_save(image, layer, full_path, full_path, 0, 9, 1, 1, 1, 1, 1)
    print(f"已创建: {full_path}")
    
    gimp.delete(image)


def create_text_image(text="Hello GIMP", width=800, height=400, filename="text.png"):
    """创建文字图片"""
    image = gimp.Image(width, height, RGB)
    
    # 创建背景图层
    bg_layer = gimp.Layer(image, "Background", width, height, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(bg_layer, 0)
    
    # 填充白色背景
    gimp.set_background((255, 255, 255))
    pdb.gimp_edit_fill(bg_layer, FILL_BACKGROUND)
    
    # 创建文字图层
    text_layer = gimp.Layer(image, "Text", width, height, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(text_layer, 0)
    
    # 添加文字
    text_drawable = pdb.gimp_text_fontname(image, None, width//4, height//3, 
                                            text, 0, TRUE, 72, UNIT_PIXEL, "Sans Bold")
    
    # 合并图层
    image.flatten()
    
    # 导出
    full_path = os.path.join(OUTPUT_DIR, filename)
    pdb.file_png_save(image, image.active_layer, full_path, full_path, 0, 9, 1, 1, 1, 1, 1)
    print(f"已创建: {full_path}")
    
    gimp.delete(image)


def create_shape_image(width=800, height=600, filename="shapes.png"):
    """创建包含基本形状的图片"""
    image = gimp.Image(width, height, RGB)
    
    # 创建背景图层
    bg_layer = gimp.Layer(image, "Background", width, height, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(bg_layer, 0)
    
    # 填充白色背景
    gimp.set_background((255, 255, 255))
    pdb.gimp_edit_fill(bg_layer, FILL_BACKGROUND)
    
    # 绘制矩形
    rect_layer = gimp.Layer(image, "Rectangle", width, height, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(rect_layer, 0)
    gimp.set_foreground((255, 0, 0))  # 红色
    pdb.gimp_image_select_rectangle(image, CHANNEL_OP_REPLACE, 50, 50, 200, 150)
    pdb.gimp_edit_fill(rect_layer, FILL_FOREGROUND)
    pdb.gimp_selection_none(image)
    
    # 绘制圆形
    circle_layer = gimp.Layer(image, "Circle", width, height, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(circle_layer, 0)
    gimp.set_foreground((0, 200, 0))  # 绿色
    pdb.gimp_image_select_ellipse(image, CHANNEL_OP_REPLACE, 300, 100, 200, 200)
    pdb.gimp_edit_fill(circle_layer, FILL_FOREGROUND)
    pdb.gimp_selection_none(image)
    
    # 绘制三角形（使用路径）
    tri_layer = gimp.Layer(image, "Triangle", width, height, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(tri_layer, 0)
    gimp.set_foreground((0, 100, 255))  # 蓝色
    
    # 创建三角形路径
    points = [
        600, 50,   # 顶点1
        500, 250,  # 顶点2
        700, 250,  # 顶点3
    ]
    pdb.gimp_image_select_polygon(image, CHANNEL_OP_REPLACE, 6, points)
    pdb.gimp_edit_fill(tri_layer, FILL_FOREGROUND)
    pdb.gimp_selection_none(image)
    
    # 合并图层
    image.flatten()
    
    # 导出
    full_path = os.path.join(OUTPUT_DIR, filename)
    pdb.file_png_save(image, image.active_layer, full_path, full_path, 0, 9, 1, 1, 1, 1, 1)
    print(f"已创建: {full_path}")
    
    gimp.delete(image)


def create_pattern_image(width=800, height=600, filename="pattern.png"):
    """创建图案背景图片"""
    image = gimp.Image(width, height, RGB)
    
    # 创建背景图层
    layer = gimp.Layer(image, "Background", width, height, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(layer, 0)
    
    # 设置颜色并创建棋盘图案
    for y in range(0, height, 50):
        for x in range(0, width, 50):
            if (x // 50 + y // 50) % 2 == 0:
                gimp.set_foreground((240, 240, 240))
            else:
                gimp.set_foreground((200, 200, 200))
            pdb.gimp_image_select_rectangle(image, CHANNEL_OP_REPLACE, x, y, 50, 50)
            pdb.gimp_edit_fill(layer, FILL_FOREGROUND)
    
    pdb.gimp_selection_none(image)
    
    # 导出
    full_path = os.path.join(OUTPUT_DIR, filename)
    pdb.file_png_save(image, layer, full_path, full_path, 0, 9, 1, 1, 1, 1, 1)
    print(f"已创建: {full_path}")
    
    gimp.delete(image)


def create_icon_image(size=256, filename="icon.png"):
    """创建简单图标"""
    image = gimp.Image(size, size, RGB)
    
    # 创建背景图层
    layer = gimp.Layer(image, "Icon", size, size, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(layer, 0)
    
    # 透明背景
    pdb.gimp_edit_clear(layer)
    
    # 绘制圆形图标背景
    margin = size // 8
    gimp.set_foreground((66, 133, 244))  # Google 蓝
    pdb.gimp_image_select_ellipse(image, CHANNEL_OP_REPLACE, 
                                   margin, margin, 
                                   size - 2*margin, size - 2*margin)
    pdb.gimp_edit_fill(layer, FILL_FOREGROUND)
    
    # 添加内圆
    inner_margin = size // 4
    gimp.set_foreground((255, 255, 255))
    pdb.gimp_image_select_ellipse(image, CHANNEL_OP_REPLACE,
                                   inner_margin, inner_margin,
                                   size - 2*inner_margin, size - 2*inner_margin)
    pdb.gimp_edit_fill(layer, FILL_FOREGROUND)
    
    pdb.gimp_selection_none(image)
    
    # 导出
    full_path = os.path.join(OUTPUT_DIR, filename)
    pdb.file_png_save(image, layer, full_path, full_path, 0, 9, 1, 1, 1, 1, 1)
    print(f"已创建: {full_path}")
    
    gimp.delete(image)


def create_banner_image(width=1200, height=400, filename="banner.png"):
    """创建横幅图片"""
    image = gimp.Image(width, height, RGB)
    
    # 创建背景图层
    bg_layer = gimp.Layer(image, "Background", width, height, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(bg_layer, 0)
    
    # 渐变背景
    gimp.set_foreground((41, 128, 185))  # 深蓝
    gimp.set_background((52, 152, 219))  # 浅蓝
    pdb.gimp_edit_blend(bg_layer, BLEND_FG_BG_RGB, LAYER_MODE_NORMAL,
                         GRADIENT_LINEAR, 100, 0, REPEAT_NONE, FALSE, FALSE,
                         0, 0, TRUE, 0, 0, width, height)
    
    # 添加装饰圆点
    for i in range(20):
        x = (i * 137) % width
        y = (i * 89) % height
        r = 10 + (i % 3) * 10
        
        dot_layer = gimp.Layer(image, f"Dot{i}", width, height, RGBA_IMAGE, 30, LAYER_MODE_NORMAL)
        image.add_layer(dot_layer, 0)
        
        gimp.set_foreground((255, 255, 255))
        pdb.gimp_image_select_ellipse(image, CHANNEL_OP_REPLACE, x-r, y-r, 2*r, 2*r)
        pdb.gimp_edit_fill(dot_layer, FILL_FOREGROUND)
        pdb.gimp_selection_none(image)
    
    # 添加标题文字
    text_layer = pdb.gimp_text_fontname(image, None, width//6, height//3,
                                         "Welcome to GIMP", 0, TRUE, 64, UNIT_PIXEL, "Sans Bold")
    
    # 合并图层
    image.flatten()
    
    # 导出
    full_path = os.path.join(OUTPUT_DIR, filename)
    pdb.file_png_save(image, image.active_layer, full_path, full_path, 0, 9, 1, 1, 1, 1, 1)
    print(f"已创建: {full_path}")
    
    gimp.delete(image)


def create_thumbnail_image(width=300, height=300, filename="thumbnail.png"):
    """创建缩略图"""
    image = gimp.Image(width, height, RGB)
    
    # 创建背景图层
    layer = gimp.Layer(image, "Thumbnail", width, height, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(layer, 0)
    
    # 渐变背景
    gimp.set_foreground((231, 76, 60))   # 红色
    gimp.set_background((192, 57, 43))   # 深红
    pdb.gimp_edit_blend(layer, BLEND_FG_BG_RGB, LAYER_MODE_NORMAL,
                         GRADIENT_RADIAL, 100, 0, REPEAT_NONE, FALSE, FALSE,
                         0, 0, TRUE, width//2, height//2, width, height)
    
    # 添加播放按钮图标
    gimp.set_foreground((255, 255, 255))
    
    # 三角形播放按钮
    points = [
        width//2 - 30, height//2 - 40,
        width//2 - 30, height//2 + 40,
        width//2 + 40, height//2
    ]
    pdb.gimp_image_select_polygon(image, CHANNEL_OP_REPLACE, 6, points)
    pdb.gimp_edit_fill(layer, FILL_FOREGROUND)
    pdb.gimp_selection_none(image)
    
    # 导出
    full_path = os.path.join(OUTPUT_DIR, filename)
    pdb.file_png_save(image, layer, full_path, full_path, 0, 9, 1, 1, 1, 1, 1)
    print(f"已创建: {full_path}")
    
    gimp.delete(image)


# 主程序：生成所有示例图片
if __name__ == "__main__":
    print("=" * 50)
    print("GIMP 图片生成脚本")
    print("=" * 50)
    print(f"输出目录: {OUTPUT_DIR}")
    print()
    
    # 生成各种图片
    create_blank_image(800, 600, (240, 240, 240), "blank_white.png")
    create_blank_image(800, 600, (0, 0, 0), "blank_black.png")
    
    create_gradient_image(800, 600, "gradient_blue_pink.png")
    
    create_text_image("Hello GIMP!", 800, 400, "text_hello.png")
    create_text_image("图片生成", 800, 400, "text_chinese.png")
    
    create_shape_image(800, 600, "shapes.png")
    
    create_pattern_image(400, 400, "pattern_checkerboard.png")
    
    create_icon_image(256, "icon_256.png")
    create_icon_image(128, "icon_128.png")
    create_icon_image(64, "icon_64.png")
    
    create_banner_image(1200, 400, "banner.png")
    
    create_thumbnail_image(300, 300, "thumbnail.png")
    
    print()
    print("=" * 50)
    print("所有图片生成完成！")
    print("=" * 50)
