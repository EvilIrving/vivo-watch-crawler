---
title: a
url: https://developers-watch.vivo.com.cn/component/basic/a/
---

# a

# a

更新时间：2025-07-10 10:44:44


超链接（默认不带下划线）。文本内容写在标签内容区，支持转义字符`"\"`


### 子组件


支持[<span>](/component/basic/span)


### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| href | `<string>` | - | 否 | 支持的格式参见[页面路由](/api/system/router)中的 uri 参数。额外的:- href 还可以通过“?param1=value1”的方式添加参数，参数可以在页面中通过`this.param1`的方式使用。
- href 暂不支持加载网页

示例:`<a href="About?param1=value1">关于</a>``<a href="/about?param1=value1">关于</a>`<br/ |


### 样式


支持[<text>样式](/component/basic/text)


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| font-family | `<string>` | - | 否 | 文本字体。可设置一个有先后顺序的，由字体名或者字体族名组成的列表，以逗号分隔。列表中第一个已安装的字体，会被选中作为文本的字体。 |


### 事件


支持[通用事件](/component/common/common-events/)
