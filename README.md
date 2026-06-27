# Image Generator

GitHub Actions 自动图片生成项目。

## 目录结构

```
.github/workflows/generate-images.yml  # GitHub Actions 工作流
scripts/generate_images.py              # 图片生成脚本
output/                                 # 生成的图片（gitignore）
```

## 使用方式

### 自动触发

推送到 `main` 分支或创建 Pull Request 时自动运行。

### 手动触发

在 GitHub 仓库页面 Actions → Generate Images → Run workflow，可自定义宽高。

### 本地运行

```bash
pip install Pillow
python scripts/generate_images.py
```

## 生成的图片类型

| 文件 | 说明 |
|------|------|
| gradient.png | RGB 渐变 |
| circles.png | 同心圆图案 |
| checkerboard.png | 棋盘格 |
| dots.png | 圆点图案 |
| waves.png | 波浪线条 |
| stripes.png | 彩色条纹 |
| plasma.png | 等离子效果 |
| noise.png | 随机噪点 |
| icon_*.png | 图标集 (16-256px) |

## 下载图片

运行完成后在 Actions → 对应 run → Artifacts 下载。
