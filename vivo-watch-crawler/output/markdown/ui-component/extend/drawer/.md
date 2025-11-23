---
title: drawer
url: https://developers-watch.vivo.com.cn/component/extend/drawer/
---

# drawer

# drawer

更新时间：2023-10-20 10:02:06


抽屉容器，抽屉默认隐藏。可通过边缘滑动，支持 flex 布局。


### 子组件


支持,包括 [<drawer-navigation>](/component/extend/drawer-navigation/) 子组件


### 属性


支持[通用属性](/component/common/common-attributes/)


### 样式


支持[通用样式](/component/common/common-styles/)


### 事件


支持[通用事件](/component/common/common-events/)


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | {direction:directionValue, state: stateValue} | 抽屉打开关闭时回调。direction：抽屉的位置，值为 start 或 end 或 up 或 down。 start：左边，end：右边，up：上边，down：下边。state:打开或者关闭状态。0：关闭，1：打开 |


### 方法


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| openDrawer | Object | 打开指定方向的抽屉 |
| closeDrawer | Object | 关闭指定方向的抽屉 |


openDrawer 的参数说明:


| 属性 | 类型 | 是否必选 | 描述 |
| --- | --- | --- | --- |
| direction | start | end | up | down | 否 | 可选参数 direction 可指定为 start | end | up | down。 如果未设置 direction 的值，且只存在一个 drawer-navigation 时，默认打开这个 drawer-navigation；如果多个 drawer-navigation 都存在，则按照左、右、上、下的次序打开。当指定的 direction 与实际的 drawer-navigation 的 direction 的值不匹配时不生效。 |


closeDrawer 的参数说明:


| 属性 | 类型 | 是否必选 | 描述 |
| --- | --- | --- | --- |
| direction | start | end | up | down | 否 | 可选参数 direction 可指定为 start | end | up | down。如果未设置 direction 的值，且只存在一个 drawer-navigation 时，默认关闭这个 drawer-navigation；如果多个 drawer-navigation 都存在，则按照左、右、上、下的次序关闭。当指定的 direction 与实际的 drawer-navigation 的 direction 的值不匹配时不生效。 |
