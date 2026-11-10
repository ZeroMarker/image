# 微信封面设计

[设计规范](https://cover.weixin.qq.com/cgi-bin/mmcover-bin/readtemplate?t=page/index#/doc?page=design&index=-1)

## 圣诞节（2026）

| 素材 | 源文件 | 尺寸 | 导出 |
| --- | --- | --- | --- |
| 封面图 | `christmas-cover.html` | 957×1278 | `christmas/cover.png` |
| 挂件（透明底） | `christmas-pendant.html` | 1053×354 | `christmas/pendant.png` |
| 气泡挂件（透明底） | `christmas-bubble.html` | 480×384 | `christmas/bubble.png` |

导出命令（挂件 / 气泡需透明底；URL 加 `?preview` 可在红底上预览）：

```bash
chromium-browser --headless --hide-scrollbars --default-background-color=00000000 \
  --window-size=957,1278 --screenshot=$PWD/christmas/cover.png file://$PWD/christmas-cover.html
```
