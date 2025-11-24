---
title: list
url: https://developers-watch.vivo.com.cn/component/container/list/
---

# list

# list

更新时间：2025-06-19 19:54:46


列表视图容器，仅支持[`<list-item>`](/component/container/list-item)子组件，支持[通用属性](/component/common/common-attributes)，支持[通用样式](/component/common/common-styles)


### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | normal|fisheye|grid | normal | 否 | 设置列表的的布局方式，默认为普通的 list 布局；fisheye 是类似鱼眼镜头效果布局；grid 是网格布局。该属性不可动态变更 |
| scrollbar | `<boolean>` | false | 否 | 是否启用滚动条 |
| title | `<boolean>` | false | 否 | 值为 true <list-item> 的第一个元素将会作为 list 的标题，标题位置固定在 list 开头，向上滑动时标题会渐渐消失（透明度逐渐变为完全透明) |
| circular | `<boolean>` | false | 否 | 是否循环展示 <list-item>, 值为 true 时部分滚动事件不可用。 |
| alignmentnum | `<number>` | 3 | 否 | 鱼眼 list 一屏幕 <list-item> 对齐数量，type 为 fisheye 时生效，设置范围：3-7，超出范围则自动设置为默认值 |
| bounces | `<boolean>` | true | 否 | 是否启用回弹 |


### 样式


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| flex-direction | column | row | column | 否 | - |
| columns | `<number>` | 1 | 否 | list 显示列数 |


### 事件


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| scrollbottom | - | 列表滑动到底部 |
| scrolltop | - | 列表滑到到顶部 |
| scrollindex | {first, last} | 返回 list 可视范围的索引范围。first:可视范围第一个 item 的索引；last:可视范围最后一个 item 的索引。 |


### 方法


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| scrollTo | Object | list 滚动到指定 item 位置 |


**scrollTo 的参数说明:**


| 名称 | 类型 | 是否必选 | 默认值 | 备注 |
| --- | --- | --- | --- | --- |
| index | number | 是 | 无 | list 滚动的目标 item 位置 |
| behavior | smooth|instant|auto | 否 | auto | 是否平滑滑动，支持参数 smooth (平滑滚动)，instant (瞬间滚动)，默认值 auto，效果等同于 instant |
