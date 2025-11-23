---
title: 数据绑定
url: https://developers-watch.vivo.com.cn/reference/app-service/data-binding/
---

# 数据绑定

# 数据绑定

更新时间：2024-03-08 15:34:54


蓝河应用提供了数据绑定 UI 组件的方式，当数据发生变化时，会自动触发 UI 组件的更新。


## 绑定方法


用法上，开发者可以在组件上使用 **"{{varname}}"** ，即双大括号内放置变量的形式，即可将变量绑定在 UI 组件上。


### 示例如下


```

<template>
  <div>
    <text>{{title}}</text>
    <input type="button" value="changeTitle" onclick="changeTitle" />
  </div>
</template>

<script>
 export default {
 data: {
 title: 'Hello World!',
 },
 changeTitle() {
 this.title = 'Hello 蓝河应用'
 },
 }
</script>
```

复制代码
## 注意事项


响应式数据必须先在 data 上静态声明或者使用 `this.$set` 动态添加，不能直接使用 `this.title = 'hello'` 添加。


### 错误示例


```

<script>
 export default {
 data: {},
 onInit() {
 this.title = 'Hello 蓝河应用'
 },
 }
</script>
```

复制代码
