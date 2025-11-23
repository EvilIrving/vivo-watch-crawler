---
title: slider
url: https://developers-watch.vivo.com.cn/component/table/slider/
---

# slider

# slider

更新时间：2024-02-28 14:20:00


滑动型输入器


### 子组件


不支持


### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| min | `<number>` | 0 | 否 | - |
| max | `<number>` | 100 | 否 | - |
| value | `<number>` | 0 | 否 | - |
| type | `<string>` | 无 | 否 | type = `vertical` 为垂直方向，不设置为水平 |
| show-block | `<boolean>` | true | 否 | 配置滑块是否展示，默认为 true 展示滑块，值为 false 隐藏滑块 |


### 样式


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | `<color>` | #f0f0f0 | 否 | 背景条颜色 |
| selected-color | `<color>` | #009688 | 否 | 已选择颜色 |
| block-color | `<color>` | - | 否 | 滑块的颜色 |
| padding-[left|right] | `<length>` | 32px | 否 | 左右边距 |


### 事件


支持[通用事件](/component/common/common-events/)


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | {progress:progressValue, isFromUser:isFromUserValue } | 拖动过程中触发的事件  isFromUser 说明:  该事件是否由于用户拖动触发 |
