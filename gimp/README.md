# GIMP Python 图片生成脚本

## 使用方法

### 方法 1: 命令行运行

```bash
# Windows
gimp -i -b "(python-fu-eval RUN-NONINTERACTIVE 0 \"execfile('D:/image/gimp/create_images.py')\")" -b "(gimp-quit 0)"

# macOS / Linux
gimp -i -b '(python-fu-eval RUN-NONINTERACTIVE 0 "execfile(\"/path/to/create_images.py\")")' -b '(gimp-quit 0)'
```

### 方法 2: GIMP 内部运行

1. 打开 GIMP
2. 菜单：滤镜 → Python-Fu → 控制台
3. 输入以下代码：

```python
execfile("D:/image/gimp/create_images.py")
```

### 方法 3: 使用批处理文件 (Windows)

双击运行 `run_generate.bat`

---

## 脚本功能

| 函数 | 说明 | 输出文件 |
|------|------|----------|
| `create_blank_image()` | 创建空白图片 | blank_white.png, blank_black.png |
| `create_gradient_image()` | 创建渐变图片 | gradient_blue_pink.png |
| `create_text_image()` | 创建文字图片 | text_hello.png, text_chinese.png |
| `create_shape_image()` | 创建形状图片 | shapes.png |
| `create_pattern_image()` | 创建图案图片 | pattern_checkerboard.png |
| `create_icon_image()` | 创建图标 | icon_256.png, icon_128.png, icon_64.png |
| `create_banner_image()` | 创建横幅 | banner.png |
| `create_thumbnail_image()` | 创建缩略图 | thumbnail.png |

---

## 自定义参数

### 创建空白图片

```python
create_blank_image(
    width=800,           # 宽度
    height=600,          # 高度
    color=(255, 0, 0),   # RGB 颜色 (红色)
    filename="red.png"   # 文件名
)
```

### 创建渐变图片

```python
create_gradient_image(
    width=1920,              # 宽度
    height=1080,             # 高度
    filename="gradient_hd.png"  # 文件名
)
```

### 创建文字图片

```python
create_text_image(
    text="自定义文字",      # 文字内容
    width=800,              # 宽度
    height=400,             # 高度
    filename="custom.png"   # 文件名
)
```

---

## 输出位置

默认输出目录：`~/gimp_output/`

可在脚本中修改 `OUTPUT_DIR` 变量更改输出位置。

---

## 前置条件

1. 安装 GIMP 2.10+
2. 确保 GIMP 可以通过命令行访问
3. Python 环境已配置

---

## 常见问题

### Q: 找不到 gimp 命令

A: 将 GIMP 安装目录添加到系统 PATH：
- Windows: `C:\Program Files\GIMP 2\bin`
- macOS: `/Applications/GIMP.app/Contents/MacOS`
- Linux: `/usr/bin`

### Q: Python-Fu 脚本不执行

A: 确保使用正确的引号转义，或使用 GIMP 内部控制台运行。

### Q: 输出图片质量不好

A: 修改导出参数，调整压缩级别和 DPI 设置。
