---
title: vw-title
url: https://developers-watch.vivo.com.cn/component/global/vw-title/
---

# vw-title

# vw-title

更新时间：2025-04-30 20:56:55


标题显示在页面顶部，作为关键导航信息，用来告知用户当前在哪里。


### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| value | `<string>` | - | 是 | 标题文本内容 |
| is-fixed | `<boolean>` | true | 否 | 标题是否固定顶部 |
| icon-left | `<string>` | - | 否 | 标题左侧图标（仅方表生效） |
| icon-right | `<string>` | - | 否 | 标题右侧图标（仅方表生效） |
| level | Number | 2 | 否 | 值为1:一级标题，值为2:二级标题 |


### 事件


| 名称 | 回调参数 | 说明 |
| --- | --- | --- |
| back | 无 | 点击事件，只在有返回按钮时生效 |
| iconleftclick | 无 | 点击标题左侧icon事件，仅icon-left 配置后生效 |
| iconrightclick | 无 | 点击标题右侧icon事件，仅icon-right配置后生效 |


### vw-title 用法


**标题类型**


```

<vw-title level="1" value="一级标题" onback="handleClick"></vw-title>
<vw-title value="二级标题"" onback="handleClick"></vw-title>

<!--仅方表支持-->
<vw-title
 icon-left="/assets/images/brightness\_on.png"
 icon-right="/assets/images/brightness\_on.png"
 oniconleftclick="onIconLeftClick"
 oniconrightclick="onIconRightClick"
 value="标题+左右按钮"">
</vw-title>


```

复制代码
