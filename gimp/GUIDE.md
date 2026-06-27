# GIMP Python 脚本图片生成指南

## 目录

1. [简介](#简介)
2. [环境配置](#环境配置)
3. [基础概念](#基础概念)
4. [常用 API](#常用-api)
5. [示例代码](#示例代码)
6. [高级技巧](#高级技巧)
7. [故障排除](#故障排除)

---

## 简介

GIMP 提供了强大的 Python-Fu 脚本接口，允许用户通过 Python 代码自动化图像处理任务。本指南介绍如何使用 GIMP 的 Python 脚本功能生成图片。

### 主要用途

- 批量生成图片
- 自动化图像处理
- 创建模板化设计
- 生成图标、横幅等素材

---

## 环境配置

### 1. 安装 GIMP

下载并安装 GIMP 2.10+：
- 官网：https://www.gimp.org/

### 2. 配置 PATH（可选）

将 GIMP 添加到系统 PATH：

**Windows：**
```
C:\Program Files\GIMP 2\bin
```

**macOS：**
```bash
export PATH="/Applications/GIMP.app/Contents/MacOS:$PATH"
```

**Linux：**
```bash
export PATH="/usr/bin:$PATH"
```

### 3. 验证安装

```bash
gimp --version
```

---

## 基础概念

### GIMP 对象模型

```
Image (图像)
├── Layer (图层)
│   ├── Drawable (可绘制对象)
│   └── ...
├── Channel (通道)
├── Path (路径)
└── Selection (选区)
```

### Python-Fu 控制台

打开 GIMP → 滤镜 → Python-Fu → 控制台

---

## 常用 API

### 图像操作

```python
# 创建图像
image = gimp.Image(width, height, RGB)

# 删除图像
gimp.delete(image)

# 获取活动图层
layer = image.active_layer

# 添加图层
image.add_layer(layer, position)

# 合并图层
image.flatten()
```

### 图层操作

```python
# 创建图层
layer = gimp.Layer(image, name, width, height, type, opacity, mode)

# 图层类型
# - RGB_IMAGE: RGB 图像
# - RGBA_IMAGE: 带透明通道的 RGB 图像
# - GRAY_IMAGE: 灰度图像
# - INDEXED_IMAGE: 索引图像

# 混合模式
# - LAYER_MODE_NORMAL: 正常
# - LAYER_MODE_MULTIPLY: 正片叠底
# - LAYER_MODE_SCREEN: 滤色
# - LAYER_MODE_OVERLAY: 叠加
```

### 颜色设置

```python
# 设置前景色
gimp.set_foreground((r, g, b))  # RGB 0-255

# 设置背景色
gimp.set_background((r, g, b))

# 填充
pdb.gimp_edit_fill(layer, FILL_FOREGROUND)
pdb.gimp_edit_fill(layer, FILL_BACKGROUND)
```

### 选区操作

```python
# 矩形选区
pdb.gimp_image_select_rectangle(image, CHANNEL_OP_REPLACE, x, y, w, h)

# 椭圆选区
pdb.gimp_image_select_ellipse(image, CHANNEL_OP_REPLACE, x, y, w, h)

# 多边形选区
points = [x1, y1, x2, y2, x3, y3, ...]
pdb.gimp_image_select_polygon(image, CHANNEL_OP_REPLACE, num_points, points)

# 取消选区
pdb.gimp_selection_none(image)
```

### 渐变操作

```python
# 应用渐变
pdb.gimp_edit_blend(
    drawable,           # 图层
    blend_mode,         # 渐变模式 (BLEND_FG_BG_RGB)
    paint_mode,         # 绘图模式 (LAYER_MODE_NORMAL)
    gradient_type,      # 渐变类型 (GRADIENT_LINEAR/RADIAL)
    opacity,            # 不透明度
    offset,             # 偏移
    repeat,             # 重复 (REPEAT_NONE)
    supersample,        # 超级采样
    max_depth,          # 最大深度
    threshold,          # 阈值
    x1, y1,             # 起点
    use_dither,         # 使用抖动
    x2, y2              # 终点
)
```

### 文字操作

```python
# 添加文字
text_layer = pdb.gimp_text_fontname(
    image,              # 图像
    drawable,           # 图层 (None 创建新图层)
    x, y,               # 位置
    text,               # 文字内容
    border,             # 边框 (-1 自动)
    antialias,          # 抗锯齿 (TRUE)
    size,               # 字号
    size_type,          # 单位 (UNIT_PIXEL)
    fontname            # 字体名称
)
```

### 文件保存

```python
# 保存为 PNG
pdb.file_png_save(image, layer, filename, raw_filename, 
                  interlace, compression, bkgd, gama, offs, phys, time)

# 保存为 JPEG
pdb.file_jpeg_save(image, layer, filename, raw_filename,
                   quality, smoothing, optimize, progressive,
                   comment, subsmp, baseline, restart, dct)

# 保存为 GIF
pdb.file_gif_save(image, layer, filename, raw_filename,
                  interlace, loop, delay, dispose)
```

---

## 示例代码

### 示例 1：创建纯色图片

```python
from gimpfu import *

def create_solid_color(width, height, color, filename):
    image = gimp.Image(width, height, RGB)
    layer = gimp.Layer(image, "Background", width, height, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(layer, 0)
    
    gimp.set_background(color)
    pdb.gimp_edit_fill(layer, FILL_BACKGROUND)
    
    pdb.file_png_save(image, layer, filename, filename, 0, 9, 1, 1, 1, 1, 1)
    gimp.delete(image)

# 使用
create_solid_color(800, 600, (255, 0, 0), "red.png")
```

### 示例 2：创建渐变背景

```python
def create_gradient_bg(width, height, color1, color2, filename):
    image = gimp.Image(width, height, RGB)
    layer = gimp.Layer(image, "Background", width, height, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(layer, 0)
    
    gimp.set_foreground(color1)
    gimp.set_background(color2)
    pdb.gimp_edit_blend(layer, BLEND_FG_BG_RGB, LAYER_MODE_NORMAL,
                         GRADIENT_LINEAR, 100, 0, REPEAT_NONE, FALSE, FALSE,
                         0, 0, TRUE, 0, 0, width, height)
    
    pdb.file_png_save(image, layer, filename, filename, 0, 9, 1, 1, 1, 1, 1)
    gimp.delete(image)

# 使用
create_gradient_bg(1920, 1080, (66, 133, 244), (234, 67, 53), "gradient.png")
```

### 示例 3：创建带文字的图片

```python
def create_text_image(width, height, text, font_size, filename):
    image = gimp.Image(width, height, RGB)
    
    # 白色背景
    layer = gimp.Layer(image, "Background", width, height, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(layer, 0)
    gimp.set_background((255, 255, 255))
    pdb.gimp_edit_fill(layer, FILL_BACKGROUND)
    
    # 添加文字
    pdb.gimp_text_fontname(image, None, 50, height//3, text, 0, TRUE, 
                            font_size, UNIT_PIXEL, "Sans Bold")
    
    image.flatten()
    pdb.file_png_save(image, image.active_layer, filename, filename, 0, 9, 1, 1, 1, 1, 1)
    gimp.delete(image)

# 使用
create_text_image(800, 400, "Hello World", 72, "text.png")
```

### 示例 4：创建简单 Logo

```python
def create_logo(size, filename):
    image = gimp.Image(size, size, RGB)
    layer = gimp.Layer(image, "Logo", size, size, RGBA_IMAGE, 100, LAYER_MODE_NORMAL)
    image.add_layer(layer, 0)
    
    # 透明背景
    pdb.gimp_edit_clear(layer)
    
    # 外圆
    margin = size // 8
    gimp.set_foreground((66, 133, 244))
    pdb.gimp_image_select_ellipse(image, CHANNEL_OP_REPLACE, 
                                   margin, margin, 
                                   size - 2*margin, size - 2*margin)
    pdb.gimp_edit_fill(layer, FILL_FOREGROUND)
    
    # 内圆
    inner_margin = size // 4
    gimp.set_foreground((255, 255, 255))
    pdb.gimp_image_select_ellipse(image, CHANNEL_OP_REPLACE,
                                   inner_margin, inner_margin,
                                   size - 2*inner_margin, size - 2*inner_margin)
    pdb.gimp_edit_fill(layer, FILL_FOREGROUND)
    
    pdb.gimp_selection_none(image)
    
    pdb.file_png_save(image, layer, filename, filename, 0, 9, 1, 1, 1, 1, 1)
    gimp.delete(image)

# 使用
create_logo(256, "logo.png")
```

### 示例 5：批量生成图标

```python
def batch_create_icons(sizes=[16, 32, 48, 64, 128, 256]):
    for size in sizes:
        create_logo(size, f"icon_{size}x{size}.png")

# 使用
batch_create_icons()
```

---

## 高级技巧

### 1. 使用图层蒙版

```python
# 添加图层蒙版
mask = pdb.gimp_layer_create_mask(layer, ADD_MASK_WHITE)
pdb.gimp_layer_add_mask(layer, mask)

# 用黑色画笔擦除
gimp.set_foreground((0, 0, 0))
pdb.gimp_paintbrush_default(mask, num_points, points)
```

### 2. 应用滤镜

```python
# 高斯模糊
pdb.plug_in_gauss(image, layer, radius_x, radius_y, method)

# 添加噪声
pdb.plug_in_rgb_noise(image, layer, independent, correlated, amount)

# 浮雕效果
pdb.plug_in_emboss(image, layer, azimuth, elevation, depth)
```

### 3. 变换操作

```python
# 缩放图层
pdb.gimp_layer_scale(layer, new_width, new_height, local_origin)

# 旋转图层
pdb.gimp_item_transform_rotate(layer, angle, auto_center, center_x, center_y)

# 翻转图层
pdb.gimp_item_transform_flip_simple(layer, flip_type, auto_center, axis)
```

### 4. 颜色调整

```python
# 色阶调整
pdb.gimp_levels(layer, channel, low_input, high_input, gamma, low_output, high_output)

# 曲线调整
pdb.gimp_curves_spline(channel, num_points, points)

# 色相/饱和度
pdb.gimp_hue_saturation(layer, hue_range, hue_offset, lightness, saturation)
```

---

## 故障排除

### 问题 1：找不到 gimp 模块

**错误信息：**
```
ImportError: No module named gimpfu
```

**解决方案：**
- 确保在 GIMP 的 Python-Fu 控制台中运行
- 或使用 GIMP 批处理模式：`gimp -i -b "..."`

### 问题 2：命令行执行失败

**错误信息：**
```
gimp: command not found
```

**解决方案：**
- 将 GIMP 添加到系统 PATH
- 或使用完整路径：`/Applications/GIMP.app/Contents/MacOS/gimp`

### 问题 3：中文显示乱码

**解决方案：**
- 确保 Python 文件使用 UTF-8 编码
- 在脚本开头添加：`# -*- coding: utf-8 -*-`

### 问题 4：图片质量差

**解决方案：**
- 提高分辨率
- 使用无损格式（PNG）
- 调整压缩参数

### 问题 5：脚本执行缓慢

**解决方案：**
- 减少图层数量
- 简化路径和选区
- 使用更高效的算法

---

## 参考资源

- GIMP 官方文档：https://www.gimp.org/docs/
- GIMP Python-Fu 文档：https://www.gimp.org/docs/python/
- GIMP API 参考：https://developer.gimp.org/api/2.0/

---

*文档版本：1.0*  
*最后更新：2026-06-28*
