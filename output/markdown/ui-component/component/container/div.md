---
title: div
url: https://developers-watch.vivo.com.cn/component/container/div/
---

# div

# div

更新时间：2023-11-06 14:52:55


基本容器，支持子组件，支持[通用属性](/component/common/common-attributes)，支持[通用样式](/component/common/common-styles)，支持[通用事件](/component/common/common-events)


### 样式


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| flex-direction | column | row | column-reverse | row-reverse | row | 否 | 默认为横向 `row`，父容器为`<div>、<list-item>`时生效 |
| flex-wrap | nowrap | wrap | wrap-reverse | nowrap | 否 | 规定 flex 容器是单行或者多行，同时横轴的方向决定了新行堆叠的方向 |
| justify-content | flex-start | flex-end | center | space-between | space-around | flex-start | 否 | 设置或检索弹性盒子元素在主轴（横轴）方向上的对齐方式 |
| align-items | stretch | flex-start | flex-end | center | stretch | 否 | 定义 flex 子项在 flex 容器的当前行的侧轴（纵轴）方向上的对齐方式 |
| align-content | stretch | flex-start | flex-end | center | space-between | space-around | stretch | 否 | 属性在弹性容器内的各项没有占用交叉轴上所有可用的空间时对齐容器内的各项（垂直），容器内必须有多行的项目，该属性才能渲染出效果 |
