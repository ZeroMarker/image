# SVG (Scalable Vector Graphics) 文件格式文档

## 1. 概述

SVG（可缩放矢量图形）是一种基于 XML 的矢量图像格式，用于描述二维图形。SVG 文件是纯文本格式，可以被搜索引擎索引、脚本化、压缩，并且可以无损缩放。

### 1.1 特点
- **矢量图形**：无损缩放，任意分辨率下保持清晰
- **XML 格式**：纯文本，可读性强，易于编辑
- **可交互**：支持 CSS 样式、JavaScript 脚本、动画
- **开放标准**：由 W3C 制定和维护
- **文件小**：相比位图，通常文件体积更小

### 1.2 文件扩展名
- `.svg` - 标准 SVG 文件
- `.svgz` - 压缩的 SVG 文件（gzip 压缩）

---

## 2. 基本结构

### 2.1 文档声明

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

### 2.2 SVG 根元素

```xml
<svg xmlns="http://www.w3.org/2000/svg"
     width="400"
     height="300"
     viewBox="0 0 400 300">
  <!-- 图形内容 -->
</svg>
```

### 2.3 根元素属性

| 属性 | 说明 | 示例 |
|------|------|------|
| `xmlns` | XML 命名空间 | `http://www.w3.org/2000/svg` |
| `width` | 画布宽度 | `400` 或 `400px` |
| `height` | 画布高度 | `300` 或 `300px` |
| `viewBox` | 视口坐标系 | `0 0 400 300` |
| `preserveAspectRatio` | 宽高比保持方式 | `xMidYMid meet` |

---

## 3. 基本图形元素

### 3.1 矩形 `<rect>`

```xml
<rect x="10" y="10" width="100" height="80" rx="10" ry="10"/>
```

| 属性 | 说明 |
|------|------|
| `x` | 左上角 x 坐标 |
| `y` | 左上角 y 坐标 |
| `width` | 宽度 |
| `height` | 高度 |
| `rx` | 水平圆角半径 |
| `ry` | 垂直圆角半径 |

### 3.2 圆形 `<circle>`

```xml
<circle cx="50" cy="50" r="40"/>
```

| 属性 | 说明 |
|------|------|
| `cx` | 圆心 x 坐标 |
| `cy` | 圆心 y 坐标 |
| `r` | 半径 |

### 3.3 椭圆 `<ellipse>`

```xml
<ellipse cx="100" cy="50" rx="80" ry="40"/>
```

| 属性 | 说明 |
|------|------|
| `cx` | 圆心 x 坐标 |
| `cy` | 圆心 y 坐标 |
| `rx` | 水平半径 |
| `ry` | 垂直半径 |

### 3.4 线段 `<line>`

```xml
<line x1="0" y1="0" x2="100" y2="100"/>
```

| 属性 | 说明 |
|------|------|
| `x1` | 起点 x 坐标 |
| `y1` | 起点 y 坐标 |
| `x2` | 终点 x 坐标 |
| `y2` | 终点 y 坐标 |

### 3.5 折线 `<polyline>`

```xml
<polyline points="0,0 50,30 100,0 150,30"/>
```

### 3.6 多边形 `<polygon>`

```xml
<polygon points="50,0 100,50 75,100 25,100 0,50"/>
```

### 3.7 路径 `<path>`

路径是最强大的图形元素，使用 `d` 属性定义复杂形状。

```xml
<path d="M 10 10 L 100 10 L 100 100 Z" fill="blue"/>
```

#### 路径命令

| 命令 | 说明 | 示例 |
|------|------|------|
| `M` | 移动到（绝对） | `M 10 10` |
| `m` | 移动到（相对） | `m 10 10` |
| `L` | 画线到（绝对） | `L 100 100` |
| `l` | 画线到（相对） | `l 100 100` |
| `H` | 水平线（绝对） | `H 100` |
| `h` | 水平线（相对） | `h 100` |
| `V` | 垂直线（绝对） | `V 100` |
| `v` | 垂直线（相对） | `v 100` |
| `C` | 三次贝塞尔曲线（绝对） | `C 10 10 20 20 30 10` |
| `c` | 三次贝塞尔曲线（相对） | `c 10 10 20 20 30 10` |
| `Q` | 二次贝塞尔曲线（绝对） | `Q 10 10 20 20` |
| `q` | 二次贝塞尔曲线（相对） | `q 10 10 20 20` |
| `A` | 弧线（绝对） | `A 25 25 0 0 1 50 50` |
| `a` | 弧线（相对） | `a 25 25 0 0 1 50 50` |
| `Z` | 闭合路径 | `Z` |

#### 贝塞尔曲线示例

```xml
<!-- 二次贝塞尔曲线 -->
<path d="M 10 80 Q 95 10 180 80" stroke="black" fill="transparent"/>

<!-- 三次贝塞尔曲线 -->
<path d="M 10 80 C 40 10 65 10 95 80" stroke="black" fill="transparent"/>
```

---

## 4. 文本元素

### 4.1 基本文本 `<text>`

```xml
<text x="10" y="20" font-family="Arial" font-size="16" fill="black">
  Hello SVG
</text>
```

### 4.2 文本属性

| 属性 | 说明 |
|------|------|
| `x` | 文本位置 x 坐标 |
| `y` | 文本位置 y 坐标 |
| `font-family` | 字体 |
| `font-size` | 字号 |
| `font-weight` | 字重（bold） |
| `font-style` | 字体样式（italic） |
| `text-anchor` | 对齐方式（start/middle/end） |
| `text-decoration` | 装饰（underline/overline/line-through） |

### 4.3 文本路径 `<textPath>`

```xml
<path id="curve" d="M 10 80 Q 95 10 180 80" fill="none"/>
<text>
  <textPath href="#curve">沿路径的文本</textPath>
</text>
```

---

## 5. 样式属性

### 5.1 填充属性

| 属性 | 说明 | 示例 |
|------|------|------|
| `fill` | 填充颜色 | `red`, `#ff0000`, `rgb(255,0,0)` |
| `fill-opacity` | 填充透明度 | `0.5` |
| `fill-rule` | 填充规则 | `nonzero`, `evenodd` |

### 5.2 描边属性

| 属性 | 说明 | 示例 |
|------|------|------|
| `stroke` | 描边颜色 | `blue` |
| `stroke-width` | 描边宽度 | `2` |
| `stroke-opacity` | 描边透明度 | `0.8` |
| `stroke-linecap` | 线端样式 | `butt`, `round`, `square` |
| `stroke-linejoin` | 连接样式 | `miter`, `round`, `bevel` |
| `stroke-dasharray` | 虚线样式 | `5,3` |
| `stroke-dashoffset` | 虚线偏移 | `10` |

### 5.3 颜色表示

```css
/* 命名颜色 */
fill="red"
fill="blue"

/* 十六进制 */
fill="#ff0000"
fill="#f00"

/* RGB */
fill="rgb(255, 0, 0)"

/* RGBA */
fill="rgba(255, 0, 0, 0.5)"

/* HSL */
fill="hsl(0, 100%, 50%)"
```

### 5.4 内联样式

```xml
<rect style="fill: blue; stroke: black; stroke-width: 2;" 
      x="10" y="10" width="100" height="80"/>
```

### 5.5 CSS 样式表

```xml
<svg xmlns="http://www.w3.org/2000/svg">
  <style>
    .myRect {
      fill: blue;
      stroke: black;
      stroke-width: 2;
    }
  </style>
  <rect class="myRect" x="10" y="10" width="100" height="80"/>
</svg>
```

---

## 6. 变换

### 6.1 变换类型

```xml
<g transform="translate(50, 50)">
  <rect x="0" y="0" width="100" height="80"/>
</g>
```

| 变换 | 说明 | 示例 |
|------|------|------|
| `translate` | 平移 | `translate(50, 50)` |
| `scale` | 缩放 | `scale(2)` 或 `scale(2, 3)` |
| `rotate` | 旋转 | `rotate(45)` 或 `rotate(45, 50, 50)` |
| `skewX` | 水平倾斜 | `skewX(20)` |
| `skewY` | 垂直倾斜 | `skewY(20)` |
| `matrix` | 矩阵变换 | `matrix(a,b,c,d,e,f)` |

### 6.2 多重变换

```xml
<g transform="translate(100, 100) rotate(45) scale(0.5)">
  <rect x="-50" y="-50" width="100" height="100"/>
</g>
```

---

## 7. 渐变和图案

### 7.1 线性渐变 `<linearGradient>`

```xml
<defs>
  <linearGradient id="gradient1" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="red"/>
    <stop offset="100%" stop-color="blue"/>
  </linearGradient>
</defs>
<rect fill="url(#gradient1)" x="10" y="10" width="200" height="100"/>
```

### 7.2 径向渐变 `<radialGradient>`

```xml
<defs>
  <radialGradient id="gradient2" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="white"/>
    <stop offset="100%" stop-color="blue"/>
  </radialGradient>
</defs>
<circle fill="url(#gradient2)" cx="100" cy="100" r="80"/>
```

### 7.3 图案 `<pattern>`

```xml
<defs>
  <pattern id="pattern1" x="0" y="0" width="20" height="20" 
           patternUnits="userSpaceOnUse">
    <rect width="10" height="10" fill="lightblue"/>
    <rect x="10" y="10" width="10" height="10" fill="lightblue"/>
  </pattern>
</defs>
<rect fill="url(#pattern1)" x="10" y="10" width="200" height="200"/>
```

---

## 8. 滤镜效果

### 8.1 高斯模糊 `<feGaussianBlur>`

```xml
<defs>
  <filter id="blur">
    <feGaussianBlur in="SourceGraphic" stdDeviation="5"/>
  </filter>
</defs>
<rect filter="url(#blur)" x="10" y="10" width="100" height="80" fill="blue"/>
```

### 8.2 阴影 `<feDropShadow>`

```xml
<defs>
  <filter id="shadow">
    <feDropShadow dx="3" dy="3" stdDeviation="2" flood-color="black" flood-opacity="0.5"/>
  </filter>
</defs>
<rect filter="url(#shadow)" x="10" y="10" width="100" height="80" fill="blue"/>
```

### 8.3 常用滤镜元素

| 元素 | 说明 |
|------|------|
| `feGaussianBlur` | 高斯模糊 |
| `feDropShadow` | 阴影 |
| `feColorMatrix` | 颜色矩阵 |
| `feComponentTransfer` | 组件转换 |
| `feComposite` | 合成 |
| `feConvolveMatrix` | 卷积矩阵 |
| `feDiffuseLighting` | 漫反射光照 |
| `feSpecularLighting` | 镜面反射光照 |
| `feDisplacementMap` | 位移映射 |
| `feFlood` | 填充 |
| `feImage` | 图像 |
| `feMerge` | 合并 |
| `feMorphology` | 形态学 |
| `feOffset` | 偏移 |
| `feTile` | 平铺 |
| `feTurbulence` | 湍流 |

---

## 9. 裁剪和遮罩

### 9.1 裁剪路径 `<clipPath>`

```xml
<defs>
  <clipPath id="clip1">
    <circle cx="50" cy="50" r="40"/>
  </clipPath>
</defs>
<rect clip-path="url(#clip1)" x="0" y="0" width="100" height="100" fill="blue"/>
```

### 9.2 遮罩 `<mask>`

```xml
<defs>
  <mask id="mask1">
    <rect width="100" height="100" fill="white"/>
  </mask>
</defs>
<rect mask="url(#mask1)" x="0" y="0" width="100" height="100" fill="blue"/>
```

---

## 10. 动画

### 10.1 SMIL 动画

```xml
<circle cx="50" cy="50" r="20" fill="blue">
  <animate attributeName="cx" from="50" to="200" dur="2s" repeatCount="indefinite"/>
  <animate attributeName="fill" from="blue" to="red" dur="2s" repeatCount="indefinite"/>
</circle>
```

### 10.2 动画元素

| 元素 | 说明 |
|------|------|
| `<animate>` | 属性动画 |
| `<animateTransform>` | 变换动画 |
| `<animateMotion>` | 运动路径动画 |
| `<set>` | 属性设置 |

### 10.3 CSS 动画

```xml
<style>
  @keyframes move {
    from { transform: translateX(0); }
    to { transform: translateX(200px); }
  }
  .animated {
    animation: move 2s infinite;
  }
</style>
<rect class="animated" x="0" y="0" width="50" height="50" fill="blue"/>
```

---

## 11. 交互和脚本

### 11.1 事件处理

```xml
<rect x="10" y="10" width="100" height="80" fill="blue"
      onclick="alert('Clicked!')"
      onmouseover="this.setAttribute('fill', 'red')"
      onmouseout="this.setAttribute('fill', 'blue')"/>
```

### 11.2 JavaScript 操作

```xml
<svg xmlns="http://www.w3.org/2000/svg" onload="init()">
  <script>
    function init() {
      var rect = document.getElementById('myRect');
      rect.addEventListener('click', function() {
        this.setAttribute('fill', 'green');
      });
    }
  </script>
  <rect id="myRect" x="10" y="10" width="100" height="80" fill="blue"/>
</svg>
```

---

## 12. 嵌入方式

### 12.1 内联 SVG

```html
<html>
<body>
  <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
    <circle cx="50" cy="50" r="40" fill="blue"/>
  </svg>
</body>
</html>
```

### 12.2 `<img>` 标签

```html
<img src="image.svg" alt="SVG Image" width="100" height="100">
```

### 12.3 `<object>` 标签

```html
<object data="image.svg" type="image/svg+xml" width="100" height="100">
  浏览器不支持 SVG
</object>
```

### 12.4 `<embed>` 标签

```html
<embed src="image.svg" type="image/svg+xml" width="100" height="100">
```

### 12.5 `<iframe>` 标签

```html
<iframe src="image.svg" width="100" height="100"></iframe>
```

### 12.6 CSS 背景

```css
.element {
  background-image: url('image.svg');
  background-size: cover;
}
```

---

## 13. 响应式 SVG

### 13.1 使用 viewBox

```xml
<svg xmlns="http://www.w3.org/2000/svg" 
     viewBox="0 0 100 100" 
     width="100%" 
     height="100%">
  <circle cx="50" cy="50" r="40" fill="blue"/>
</svg>
```

### 13.2 preserveAspectRatio

```xml
<svg viewBox="0 0 200 100" preserveAspectRatio="xMidYMid meet">
  <!-- 内容会保持宽高比，居中显示 -->
</svg>
```

| 值 | 说明 |
|------|------|
| `xMinYMin meet` | 左上角对齐，保持宽高比 |
| `xMidYMid meet` | 居中对齐，保持宽高比（默认） |
| `xMaxYMax meet` | 右下角对齐，保持宽高比 |
| `none` | 拉伸填充，不保持宽高比 |

---

## 14. 符号和复用

### 14.1 符号 `<symbol>`

```xml
<svg xmlns="http://www.w3.org/2000/svg">
  <defs>
    <symbol id="icon" viewBox="0 0 24 24">
      <path d="M12 2L2 22h20L12 2z"/>
    </symbol>
  </defs>
  <use href="#icon" x="10" y="10" width="50" height="50"/>
  <use href="#icon" x="70" y="10" width="50" height="50"/>
</svg>
```

### 14.2 复用元素 `<use>`

```xml
<defs>
  <circle id="myCircle" cx="0" cy="0" r="20" fill="blue"/>
</defs>
<use href="#myCircle" x="50" y="50"/>
<use href="#myCircle" x="150" y="50"/>
```

### 14.3 组 `<g>`

```xml
<g id="group1" transform="translate(50, 50)">
  <rect x="0" y="0" width="100" height="80" fill="blue"/>
  <circle cx="50" cy="40" r="20" fill="red"/>
</g>
```

---

## 15. 完整示例

### 15.1 简单图标

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     viewBox="0 0 100 100" 
     width="100" 
     height="100">
  
  <!-- 背景圆 -->
  <circle cx="50" cy="50" r="45" fill="#4CAF50"/>
  
  <!-- 勾号 -->
  <path d="M 30 50 L 45 65 L 70 35" 
        stroke="white" 
        stroke-width="8" 
        stroke-linecap="round" 
        stroke-linejoin="round" 
        fill="none"/>
  
</svg>
```

### 15.2 渐变背景

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     viewBox="0 0 400 200" 
     width="400" 
     height="200">
  
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#667eea"/>
      <stop offset="100%" stop-color="#764ba2"/>
    </linearGradient>
  </defs>
  
  <!-- 渐变背景 -->
  <rect width="400" height="200" fill="url(#bg)" rx="20"/>
  
  <!-- 文本 -->
  <text x="200" y="110" 
        text-anchor="middle" 
        font-family="Arial, sans-serif" 
        font-size="36" 
        font-weight="bold" 
        fill="white">
    Hello SVG
  </text>
  
</svg>
```

### 15.3 复杂图形

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     viewBox="0 0 300 300" 
     width="300" 
     height="300">
  
  <defs>
    <!-- 径向渐变 -->
    <radialGradient id="sphere" cx="40%" cy="40%">
      <stop offset="0%" stop-color="#fff"/>
      <stop offset="100%" stop-color="#0066cc"/>
    </radialGradient>
    
    <!-- 阴影滤镜 -->
    <filter id="shadow">
      <feDropShadow dx="5" dy="5" stdDeviation="5" flood-opacity="0.3"/>
    </filter>
  </defs>
  
  <!-- 球体 -->
  <circle cx="150" cy="150" r="100" 
          fill="url(#sphere)" 
          filter="url(#shadow)"/>
  
  <!-- 高光 -->
  <ellipse cx="120" cy="120" rx="30" ry="20" 
           fill="white" 
           opacity="0.5" 
           transform="rotate(-30, 120, 120)"/>
  
</svg>
```

---

## 16. 最佳实践

### 16.1 文件优化
- 移除不必要的空格和换行
- 使用简化的路径命令
- 合并相同的元素
- 使用 `<symbol>` 和 `<use>` 复用元素

### 16.2 可访问性
- 添加 `role="img"` 属性
- 提供 `aria-label` 或 `<title>` 描述
- 确保足够的颜色对比度
- 支持键盘导航

### 16.3 浏览器兼容性
- 所有现代浏览器都支持 SVG
- 旧版 IE 需要 polyfill
- 测试不同浏览器的渲染差异

### 16.4 性能
- 避免过于复杂的路径
- 使用 CSS 动画代替 SMIL
- 压缩 SVG 文件（SVGZ）
- 使用适当的 viewBox 尺寸

---

## 17. 工具推荐

### 17.1 编辑器
- Adobe Illustrator
- Inkscape（免费）
- Figma
- Sketch

### 17.2 优化工具
- SVGO（SVG Optimizer）
- SVGOMG（在线工具）
- Jake Archibald's SVG Editor

### 17.3 代码编辑
- VS Code + SVG 插件
- 任意文本编辑器

---

## 18. 参考资源

- [W3C SVG 规范](https://www.w3.org/TR/SVG/)
- [MDN SVG 文档](https://developer.mozilla.org/zh-CN/docs/Web/SVG)
- [SVG 教程](https://www.runoob.com/svg/svg-tutorial.html)
- [Can I Use - SVG](https://caniuse.com/svg)

---

*文档版本：1.0*  
*最后更新：2026-06-28*
