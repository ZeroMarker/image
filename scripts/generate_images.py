#!/usr/bin/env python3
"""Generate images using Pillow"""

from PIL import Image, ImageDraw
import os
import math
import random

WIDTH = int(os.environ.get('WIDTH', 800))
HEIGHT = int(os.environ.get('HEIGHT', 600))
OUTPUT_DIR = 'output'

os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_gradient():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            r = int(255 * x / WIDTH)
            g = int(255 * y / HEIGHT)
            b = 128
            draw.point((x, y), fill=(r, g, b))
    img.save(os.path.join(OUTPUT_DIR, 'gradient.png'))
    print('Created: gradient.png')


def create_circles():
    img = Image.new('RGB', (WIDTH, HEIGHT), 'white')
    draw = ImageDraw.Draw(img)
    cx, cy = WIDTH // 2, HEIGHT // 2
    for i in range(10, max(WIDTH, HEIGHT) // 2, 30):
        color = (i * 3 % 256, i * 5 % 256, i * 7 % 256)
        draw.ellipse([cx - i, cy - i, cx + i, cy + i], outline=color, width=2)
    img.save(os.path.join(OUTPUT_DIR, 'circles.png'))
    print('Created: circles.png')


def create_checkerboard():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    size = 50
    for y in range(0, HEIGHT, size):
        for x in range(0, WIDTH, size):
            if (x // size + y // size) % 2 == 0:
                color = (240, 240, 240)
            else:
                color = (60, 60, 60)
            draw.rectangle([x, y, x + size, y + size], fill=color)
    img.save(os.path.join(OUTPUT_DIR, 'checkerboard.png'))
    print('Created: checkerboard.png')


def create_dots():
    img = Image.new('RGB', (WIDTH, HEIGHT), 'white')
    draw = ImageDraw.Draw(img)
    spacing, radius = 60, 15
    for y in range(0, HEIGHT, spacing):
        for x in range(0, WIDTH, spacing):
            offset = spacing // 2 if (y // spacing) % 2 else 0
            color = (x * 3 % 256, y * 2 % 256, 150)
            draw.ellipse([x + offset - radius, y - radius, x + offset + radius, y + radius], fill=color)
    img.save(os.path.join(OUTPUT_DIR, 'dots.png'))
    print('Created: dots.png')


def create_waves():
    img = Image.new('RGB', (WIDTH, HEIGHT), 'white')
    draw = ImageDraw.Draw(img)
    for y in range(0, HEIGHT, 30):
        points = [(x, y + int(20 * math.sin(x * 0.02 + y * 0.01))) for x in range(0, WIDTH, 5)]
        if len(points) > 1:
            draw.line(points, fill=(y * 3 % 256, 100, 200 - y % 256), width=3)
    img.save(os.path.join(OUTPUT_DIR, 'waves.png'))
    print('Created: waves.png')


def create_stripes():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    colors = [(231, 76, 60), (52, 152, 219), (46, 204, 113)]
    for x in range(0, WIDTH, 40):
        draw.rectangle([x, 0, x + 40, HEIGHT], fill=colors[(x // 40) % 3])
    img.save(os.path.join(OUTPUT_DIR, 'stripes.png'))
    print('Created: stripes.png')


def create_plasma():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    for y in range(HEIGHT):
        for x in range(WIDTH):
            v1 = math.sin(x * 0.02)
            v2 = math.sin(y * 0.02)
            v3 = math.sin((x + y) * 0.02)
            r = int(128 + 127 * math.sin(v1 + v3))
            g = int(128 + 127 * math.sin(v2))
            b = int(128 + 127 * math.sin(v1 + v2))
            img.putpixel((x, y), (r, g, b))
    img.save(os.path.join(OUTPUT_DIR, 'plasma.png'))
    print('Created: plasma.png')


def create_noise():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            draw.point((x, y), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    img.save(os.path.join(OUTPUT_DIR, 'noise.png'))
    print('Created: noise.png')


def create_icons():
    for size in [16, 32, 48, 64, 128, 256]:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        margin = size // 8
        draw.ellipse([margin, margin, size - margin, size - margin], fill=(66, 133, 244))
        inner = size // 4
        draw.ellipse([inner, inner, size - inner, size - inner], fill=(255, 255, 255))
        img.save(os.path.join(OUTPUT_DIR, f'icon_{size}x{size}.png'))
        print(f'Created: icon_{size}x{size}.png')


if __name__ == '__main__':
    print(f'Generating images ({WIDTH}x{HEIGHT})...')
    create_gradient()
    create_circles()
    create_checkerboard()
    create_dots()
    create_waves()
    create_stripes()
    create_plasma()
    create_noise()
    create_icons()
    print('Done!')
