---
title: list-item
url: https://developers-watch.vivo.com.cn/component/container/list-item/
---

# list-item

# list-item

更新时间：2025-06-19 19:54:46


[`<list>`](/component/container/list)的子组件，用来展示列表具体 item，宽度默认充满 list 组件，支持子组件，支持[通用属性](/component/common/common-attributes)，支持[<div>样式](/component/container/div/)，不支持 position 样式，支持[通用样式](/component/common/common-styles)，支持[通用事件](/component/common/common-events)


### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | `<string>` | - | 是 | list-item 类型，值为自定义的字符串，如'loadMore'。**相同的 type 的 list-item 必须具备完全一致的 DOM 结构**。因此，在 list-item 内部需谨慎使用 if 和 for，因为 if 和 for 可能造成相同的 type 的 list-item 的 DOM 结构不一致，从而引发错误 |


### 样式


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| column-span | `<number>` | 1 | 否 | list-item 在 list 中所占列数，一般用于 list 多列显示时。 |


### Slots


| name | 描述 |
| --- | --- |
| right | 左滑后，在右端显示 |
