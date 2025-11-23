---
title: picker
url: https://developers-watch.vivo.com.cn/component/table/picker/
---

# picker

# picker

更新时间：2025-03-31 12:03:25


滚动选择器，支持四种选择器，普通选择器，日期选择器，时间选择器，索引栏选择器。


### 子组件


不支持


### 属性


支持[通用属性](/component/common/common-attributes/)


**普通选择器**


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | text | - | 是 | 不支持动态修改 |
| range | `<array>` | - | 否 | 选择器的取值范围 |
| selected | `<string>` | 0 | 否 | 选择器的默认取值，取值为 range 的索引 |
| loop | `<boolean>` | false | 是 | 是否开启循环模式，选项数量大于 2 时生效 |


**日期选择器**


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | date | - | 是 | 不支持动态修改 |
| start | `<time>` | 1970-1-1 | 否 | 起始时间，格式为 yyyy-MM-dd |
| end | `<time>` | 2100-12-31 | 否 | 结束时间，格式为 yyyy-MM-dd |
| selected | `<string>` | 当前时间 | 否 | 选择器的默认取值，格式为 yyyy-MM-dd |
| loop | `<boolean>` | false | 是 | 是否开启循环模式，选项数量大于 2 时生效 |


**时间选择器**


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | time | - | 是 | 不支持动态修改 |
| selected | `<string>` | 当前时间 | 否 | 选择器的默认取值，格式为 "HH:mm:ss" |
| format | `<string>` | HH:mm:ss | 否 | 展示的时间格式，默认 24 小时制，12 小时制目前支持"h:mm A"，不支持"h:mm:ss A" |
| loop | `<boolean>` | false | 是 | 是否开启循环模式，选项数量大于 2 时生效 |
| snap-interval | `<number>` | 1 | 否 | 用户快速滑动分/秒选择器时，惯性滚动可能导致停止在非标值（如 `23秒`、`58秒`）。通过改属性可以对齐到固定间隔（如 `5秒`），能保证数据规则性（如计时器、运动记录等场景） |


**索引栏选择器**


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | `index-bar` | - | 是 | 不支持动态修改 |
| range | `<array>` | - | 否 | 选择器的取值范围。建议每个选项内容为 1 个字符。 |
| selected | `<string>` | 0 | 否 | 选择器的默认取值，取值为 range 的索引 |


### 样式


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| font-size | `<length>` | 40px | 否 | 未选中项文本尺寸 |
| selected-font-size | `<length>` | 56px | 否 | 选中项文本尺寸 |
| color | `<color>` | #ffffffff | 否 | 未选中项文本颜色 |
| selected-color | `<color>` | #ffffffff | 否 | 选中项文本颜色 |
| selected-background-color | `<color>` | #ff415fff | 否 | 选中项背景颜色 |
| linecolor | `<color>` | - | 否 | 下划线的颜色 |


### 事件


不支持 click 事件，支持[通用事件](/component/common/common-events/)


**普通选择器**


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | {newValue:newValue, newSelected:newSelected} | 滚动选择器选择值后触发（newSelected 为索引） |


**日期选择器**


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | {year:year, month:month, day:day} | 滚动选择器选择值后触发 |


**时间选择器**


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | {hour:hour, minute:minute,second:second} | 滚动选择器选择值后触发 |


**索引栏选择器**


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | {newValue:newValue, newSelected:newSelected} | 滚动选择器选择值后触发（newSelected 为索引） |


### 方法


**索引栏选择器**


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| scrollTo | { index: number } | 索引栏选择器平滑的滚动到 index 位置，index 为选项值的序号(从 0 开始)，调用后会触发 change 事件。scrollTo 和赋值属性 selected 的区别：selected 赋值是瞬间到达索引位置，scrollTo 方法是平滑的到索引位置 |
