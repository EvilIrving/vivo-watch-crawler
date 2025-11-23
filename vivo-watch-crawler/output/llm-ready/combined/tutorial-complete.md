# vivo BlueOS 手表开发文档 - 教程文档

> 本文档由爬虫自动生成，包含 39 个页面的内容

## 目录

- [数据绑定](#数据绑定)
- [概述](#概述)
- [列表渲染](#列表渲染)
- [条件渲染](#条件渲染)
- [页面布局](#页面布局)
- [自定义组件](#自定义组件)
- [props](#props)
- [页面路由](#页面路由)
- [文件组织](#文件组织)
- [框架简介](#框架简介)
- [manifest 文件](#manifest-文件)
- [javascript 代码](#javascript-代码)
- [style 样式](#style-样式)
- [UX 文件](#ux-文件)
- [页面启动模式](#页面启动模式)
- [屏幕适配](#屏幕适配)
- [后台运行](#后台运行)
- [表盘](#表盘)
- [快捷卡片](#快捷卡片)
- [概述](#概述)
- [避免高耗性能操作](#避免高耗性能操作)
- [响应式数据优化](#响应式数据优化)
- [帧率优化指引](#帧率优化指引)
- [减少初始化开销](#减少初始化开销)
- [长列表性能优化](#长列表性能优化)
- [js 内存泄漏排查](#js-内存泄漏排查)
- [运行时性能优化](#运行时性能优化)
- [图片资源优化](#图片资源优化)
- [退出页面释放监听](#退出页面释放监听)
- [减少代码体积](#减少代码体积)
- [编译环境变量](#编译环境变量)
- [国际化](#国际化)
- [概述](#概述)
- [构建首个蓝河应用](#构建首个蓝河应用)
- [标准卡开发](#标准卡开发)
- [轻卡开发](#轻卡开发)
- [概述](#概述)
- [卡片配置](#卡片配置)
- [widgetProvider 开发](#widgetprovider-开发)

---


<!-- 文档 1: tutorial/app-service/data-binding/.md -->


## 数据绑定

## 数据绑定

更新时间：2024-03-08 15:34:54


蓝河应用提供了数据绑定 UI 组件的方式，当数据发生变化时，会自动触发 UI 组件的更新。


### 绑定方法


用法上，开发者可以在组件上使用 **"{{varname}}"** ，即双大括号内放置变量的形式，即可将变量绑定在 UI 组件上。


#### 示例如下


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
### 注意事项


响应式数据必须先在 data 上静态声明或者使用 `this.$set` 动态添加，不能直接使用 `this.title = 'hello'` 添加。


#### 错误示例


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


---


<!-- 文档 2: tutorial/app-service/event-on/.md -->


## 概述

## 概述

更新时间：2025-08-13 20:11:57


通过在 UI 组件上绑定事件，开发者可以实现蓝河应用与用户之间的交互。


### 绑定事件


用法上，开发者可以使用 on (可以用@简写代替) 来绑定事件，如：onclick,onchange 可简写成 @click,@change，并在事件触发时执行对应的 JavaScript 业务代码。


#### 示例如下


```

<template>
  <div class="tutorial-page">
    <text id="elNode1" class="{{ elClassName + 1 }}" disabled="false" onclick="onClickHandler"
 >组件节点1</text
 >
    <text
 id="elNode2"
 class="class-static-1 {{ elClassName + 2 }}"
 onclick="onClickHandler2('参数1', argName)"
 >组件节点2</text
 >
  </div>
</template>

<style lang="less">
 .tutorial-page {
 flex-direction: column;
 }
</style>

<script>
 export default {
 data: {
 elClassName: 'class-dynamic',
 argName: '动态参数',
 },
 onClickHandler(evt) {
 console.info(`触发事件`)
 },
 onClickHandler2(arg1, arg2, evt) {
 console.info(`触发事件，参数： ${arg1}, ${arg2}`)
 },
 }
</script>
```

复制代码
#### 事件传参


UI 组件可以向绑定的事件方法传递自定义参数。


##### 示例如下


```

<template>
  <div class="demo-page">
    <text for="{{list}}" key="{{$idx}}" onclick="handle($idx,$item,total)">{{$item}}</text>
  </div>
</template>

<script>
 export default {
 data: {
 list: [1, 2, 3, 4, 5],
 total: 0,
 },
 handle(idx, item, total, $evt) {
 console.log(idx)
 console.log(item)
 console.log(total)
 console.log($evt)
 },
 }
</script>
```

复制代码
回调函数被调用时，会在参数列表末尾自动添加一个 evt 参数，通过 evt 参数开发者可以访问回调事件相关上下文数据。


  

UI 组件还支持许多其他的事件绑定，如果您想进一步了解，请移步[通用事件](/component/common/common-events/)。


---


<!-- 文档 3: tutorial/app-service/for/.md -->


## 列表渲染

## 列表渲染

更新时间：2025-06-17 15:55:14


使用 `for` 指令可循环渲染数组数据。其语法支持多种形式（`{{}}` 可省略）：


### 基础写法


```

for="{{list}}"
```

复制代码
- `list` 是数组类型数据。
- 默认数组元素变量为 `$item`，索引为 `$idx`。


### 自定义变量名


```

for="{{value in list}}"
```

复制代码
- `value` 是自定义的数组元素变量名。
- 索引仍默认为 `$idx`。


### 自定义索引和元素变量名


```

for="{{(index, value) in list}}"
```

复制代码
- `index` 是索引变量名，`value` 是元素变量名。


### 使用常数作为循环次数


你还可以使用一个常数作为数据源，表示循环执行的次数。等价于遍历从 `0` 到 `n - 1` 的索引。


```

for="{{value in 10}}"
for="{{(index, value) in 5}}"
```

复制代码
- 等价于遍历 `[0, 1, 2, ..., n - 1]`。
- 可以搭配 `index` 和 `value` 使用。


### tid 属性


用于指定每个循环项的唯一 ID，用于 DOM 节点复用和性能优化。若未指定，默认使用 `$idx`。


```

<div for="value in list" tid="uniqueId">
  <text>{{$idx}}.{{value.name}}</text>
</div>
<script>
  export default {
    data: {
      list: [
        { name: 'aa', uniqueId: 1 },
        { name: 'bb', uniqueId: 2 },
        { name: 'cc', uniqueId: 3 },
      ],
    },
    onInit() {
      console.log('指令for')
    },
  }
</script>
```

复制代码
### 示例


```

<template>
  <div class="tutorial-page">
    <!-- 方式1：默认$item代表数组中的元素, $idx代表数组中的索引 -->
    <div class="tutorial-row" for="{{list}}" tid="uniqueId">
      <text>{{$idx}}.{{$item.name}}</text>
    </div>
    <!-- 方式2：自定义元素变量名称 -->
    <div class="tutorial-row" for="value in list" tid="uniqueId">
      <text>{{$idx}}.{{value.name}}</text>
    </div>
    <!-- 方式3：自定义元素、索引的变量名称 -->
    <div class="tutorial-row" for="(personIndex, personItem) in list" tid="uniqueId">
      <text>{{personIndex}}.{{personItem.name}}</text>
    </div>
  </div>
</template>

<style lang="less">
 .tutorial-page {
 flex-direction: column;
 .tutorial-row {
 width: 85%;
 margin-top: 10px;
 margin-bottom: 10px;
 }
 }
</style>

<script>
 export default {
 data: {
 list: [
 { name: 'aa', uniqueId: 1 },
 { name: 'bb', uniqueId: 2 },
 { name: 'cc', uniqueId: 3 },
 ],
 },
 onInit() {
 console.log('指令for')
 },
 }
</script>
```

复制代码
示例代码中，在渲染页面时，`div.tutorial-row`的结构，会根据 script 中的数据 list 的定义，被循环的生成多个。tid="uniqueId"，数组元素的某个属性名，不一定叫 uniqueId。 它类似于 React 的 key={item.uniqueId}或 vue 的 track-by={ uniqueId }, 用于优化渲染速度。当数据修改时，数据不改变的 dom 不会被重新渲染，已经改变的数据所在的 dom 才会被重新渲染， 因此我们必须保证 uniqueId 这个属性值在每个数组元素都不一样。


### 注意事项


> 
> for 指令只能循环数组，不能循环对象。当 for 指令与 if 指令共存于一个标签时， if 指令的优先级优于 for 指令。为了方便未看文档的新人快速上手项目，不建议这两个指令共存于同一个标签。自定义变量表示 for 指令的数组索引和数组元素时，变量名不可以用`$`或`_`开头；使用`tid属性`时应注意：
> 
> 
> 


- `tid属性`指定的数据属性必须存在，否则可能导致运行异常
- `tid属性`指定的数据属性要保证唯一，否则可能导致性能问题
- `tid属性`目前不支持表达式。


---


<!-- 文档 4: tutorial/app-service/if-show/.md -->


## 条件渲染

## 条件渲染

更新时间：2023-10-31 15:05:28


> 
> 条件渲染有 2 种：if/elif/else 和 show。它们的区别在于：if 为 false 时，组件会从 DOM 中移除，而 show 仅仅是渲染时不可见，组件依然存在于 DOM 中;
> 
> 
> 


### if 指令


if 条件渲染，是指 if/elif/else 这 3 个相关指令，用于控制是否增加或者删除组件；


if/elif/else 节点必须是相邻的兄弟节点


```

<template>
  <div>
    <text if="{{display}}">Hello-1</text>
    <text elif="{{display}}">Hello-2</text>
    <text else>Hello-3</text>
  </div>
</template>

<script>
 export default {
 data: {
 display: false,
 },
 }
</script>
```

复制代码
### show 指令


show 指令，是指是否显示组件，用于控制组件的显示状态，并不会从 DOM 结构中删除;


show 等同于 visible=none, 主要用于在原生组件上声明；


show 指令开始支持在自定义组件上进行声明，当这样使用时，等同于在该自定义子组件的根节点上使用 show 指令；


对于之前版本，自定义组件不支持 show 指令的需求，可以通过 props 传入参数，在自己内部使用 show 来控制是否可见；


```

<template>
  <text show="{{visible}}">Hello</text>
</template>

<script>
 export default {
 data: {
 visible: false,
 },
 }
</script>
```

复制代码
### if 与 show 区别


- 当 if/elif 指令的值为 false 时，节点会从页面中移除，当 if/elif 指令值为 true，组件会动态插入节点中；
- 当 show 指令的值为 true 时，节点可见， 当其值为 false 时，组件不可见，但节点仍会保留在页面 DOM 结构中


---


<!-- 文档 5: tutorial/app-service/page-style-and-layout/.md -->


## 页面布局

## 页面布局

更新时间：2024-01-10 16:04:30


蓝河应用使用的是 Flex 布局方式。


### 盒模型


蓝河应用布局框架使用 border-box 模型，具体表现与宽高边距计算可参考 MDN 文档 [box-sizing](https://developer.mozilla.org/zh-CN/docs/Web/CSS/box-sizing)， 暂不支持 content-box 模型与手动指定 box-sizing 属性。


布局所占宽度 Width：


`Width = width(包含padding-left + padding-right + border-left + border-right)`


布局所占高度 Height:


`Height = height(包含padding-top + padding-bottom + border-top + border-bottom)`


### 长度单位


#### px


与传统 web 页面不同，`px`是相对于`项目配置基准宽度`的单位，已经适配了移动端屏幕，其原理类似于`rem`


开发者只需按照设计稿确定框架样式中的 px 值即可。


首先，我们需要定义`项目配置基准宽度`，它是项目的配置文件（`<ProjectName>/src/manifest.json`）中`config.designWidth`的值


然后， `设计稿1px`与`框架样式1px`转换公式如下：


```

设计稿1px / 设计稿基准宽度 = 框架样式1px / 项目配置基准宽度
```

复制代码
**示例如下：**


若设计稿宽度为 640px，元素 A 在设计稿上的宽度为 100px，实现的两种方案如下：


**方案一：**


修改`项目配置基准宽度`：将`项目配置基准宽度`设置为`设计稿基准宽度`，则`框架样式1px`等于`设计稿1px`


- 设置`项目配置基准宽度`，在项目的配置文件（`<ProjectName>/src/manifest.json`）中，修改`config.designWidth`：


```

{
  "config": {
    "designWidth": 640
  }
}
```

复制代码
- 设置元素 A 对应的框架样式：


```

width: 100px;
```

复制代码
**方案二：**


不修改`项目配置基准宽度`：若当前项目配置的`项目配置基准宽度`为 466，设元素 A 的框架样式 x`px`，由转换公式得：`100 / 640 = x / 466`


- 设置元素 A 对应的框架样式：


```

width: 73px;
```

复制代码
### 设置定位


position 将支持三种属性值：relative、absolute 和 fixed，并且默认值为 relative，入门可以参考[MDN 文档](https://developer.mozilla.org/zh-CN/docs/Web/CSS/position)


### 设置样式


开发者可以使用`内联样式`、`tag选择器`、`class选择器`、`id选择器`来为组件设置样式


同时也可以使用`并列选择`、`后代选择器`设置样式


详细的文档可以查看[此处](/component/common/common-styles)


**注意:** template 的样式读取范围，只包括内联样式与当前 ux 文件的`<style>`标签内的样式与引入的 css/less/scss，如果一个 ux 文件被包装成自定义组件并被其他父组件引用，其样式并不能响应父组件的样式。


**示例如下：**


```

<template>
  <div class="tutorial-page">
    <text style="color: #FF0000;">内联样式</text>
    <text id="title">ID选择器</text>
    <text class="title">class选择器</text>
    <text>tag选择器</text>
  </div>
</template>

<style>
 .tutorial-page {
 flex-direction: column;
 }
 /\* tag选择器 \*/
 text {
 color: #0000ff;
 }
 /\* class选择器（推荐） \*/
 .title {
 color: #00ff00;
 }
 /\* ID选择器 \*/
 #title {
 color: #00a000;
 }
 /\* 并列选择 \*/
 .title,
 #title {
 font-weight: bold;
 }
 /\* 后代选择器 \*/
 .tutorial-page text {
 font-size: 42px;
 }
 /\* 直接后代选择器 \*/
 .tutorial-page > text {
 text-decoration: underline;
 }
</style>
```

复制代码
### 通用样式


通用样式如 margin,padding 等属性可以点击[此处](/component/common/common-styles)


### Flex 布局示例


框架使用`Flex布局`，关于`Flex布局`可以参考外部文档[A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)


flex 布局的支持也可以在官网文档的[通用样式](/component/common/common-styles)查询


div 组件为最常用的 Flex 容器组件，具有 Flex 布局的特性；text、a、span、label 组件为文本容器组件，**其它组件不能直接放置文本内容**


**示例如下：**


```

<template>
  <div class="tutorial-page">
    <div class="item">
      <text>item1</text>
    </div>
    <div class="item">
      <text>item2</text>
    </div>
  </div>
</template>

<style>
 .tutorial-page {
 /\* 交叉轴居中 \*/
 align-items: center;
 /\* 纵向排列 \*/
 flex-direction: column;
 }
 .tutorial-page > .item {
 /\* 有剩余空间时，允许被拉伸 \*/
 /\*flex-grow: 1;\*/
 /\* 空间不够用时，不允许被压缩 \*/
 flex-shrink: 0;
 /\* 主轴居中 \*/
 justify-content: center;
 width: 200px;
 height: 100px;
 margin: 10px;
 background-color: #ff0000;
 }
</style>
```

复制代码


---


<!-- 文档 6: tutorial/app-service/parent-child-component-communication/.md -->


## 自定义组件

## 自定义组件

更新时间：2025-06-23 10:14:39


> 
> 熟悉自定义组件的开发，了解父子组件之间的通信方式，如：props，data。
> 
> 
> 


### 组件自定义


开发页面时开发者必须用到各种 UI 组件，如：`text`、`div`，这些组件是由蓝河系统提供的；如果开发一个复杂的页面，开发者把所有的 UI 部分写在一个文件的`<template>`，那代码的可维护性将会很低，并且模块之间容易产生不必要的耦合关系。


为了更好的组织逻辑与代码，可以把页面按照功能拆成多个模块，每个模块负责其中的一个功能部分，最后页面将这些模块引入管理起来，传递业务与配置数据完成代码分离，那么这就是`自定义组件`的意义。


自定义组件是开发者使用 `.ux` 文件编写的 UI 组件，可以对数据、事件、方法进行个性化管理。


**示例如下：**


```

<template>
  <div class="tutorial-page">
    <text class="tutorial-title">自定义组件:</text>
    <text>{{ say }}</text>
    <text>{{ obj.name }}</text>
  </div>
</template>

<style lang="less">
 .tutorial-page {
 flex-direction: column;
 padding-top: 20px;

 .tutorial-title {
 font-weight: bold;
 }
 }
</style>

<script>
 // 子组件
 export default {
 data: {
 say: 'hello',
 obj: {
 name: '蓝河应用',
 },
 },
 /\*
 data（）{
 return {
 say:'hello',
 obj:{
 name:'vivo手表应用'
 }
 }
 },
 \*/
 onInit() {
 console.log('我是子组件')
 },
 }
</script>
```

复制代码
自定义组件中数据模型只能使用**data 属性**，data 类型可以是 Object 或 Function。如果是函数，返回结果必须是对象。


### 组件使用


#### 组件引入


蓝河应用中是通过`<import>标签`引入组件,如下面代码所示


```

<import name="XXX" src="XXX"></import>
```

复制代码
`<import>标签`中的的`src`属性指定自定义组件的地址，`name`属性指定在父组件中引用该组件时使用的**标签名称**


**示例如下：**


```

<import name="comp-part1" src="./part1"></import>

<template>
  <div class="tutorial-page">
    <text class="tutorial-title">引入组件：</text>
    <comp-part1></comp-part1>
  </div>
</template>

<style lang="less">
 .tutorial-page {
 flex-direction: column;
 padding: 20px 10px;

 .tutorial-title {
 font-weight: bold;
 }
 }
</style>

<script>
 // 父组件
 export default {
 data: {},
 onInit() {
 console.log('引入组件')
 },
 }
</script>
```

复制代码

### 自定义组件的生命周期


| 属性 | 类型 | 参数 | 返回值 | 描述 | 触发时机 |
| --- | --- | --- | --- | --- | --- |
| onInit | Function | 无 | 无 | 监听初始化 | 当数据驱动化完成时触发 |
| onReady | Function | 无 | 无 | 监听模板创建完成 | 当模板创建完成时触发 |
| onDestroy | Function | 无 | 无 | 监听组件销毁 | 当销毁时触发 |


### 父子组件通信


#### 父组件通过 Prop 向子组件传递数据


父组件向子组件传递数据，通过在子组件的`props`属性中声明对外暴露的属性名称，然后在`组件引用标签`上声明传递的父组件数据，详见[Props](/reference/app-service/props)


**示例如下：**


```

<!-- 子组件 -->
<template>
  <div class="child-demo">
    <text class="title">子组件:</text>
    <text>{{ say }}</text>
    <text>{{ propObject.name }}</text>
  </div>
</template>
<script>
 export default {
 props: {
 say:{},
 propObject:{}
 }

 onInit() {
 console.info(`外部传递的数据：`, this.say, this.propObject)
 },
 }
</script>
```

复制代码

```

<!-- 父组件 -->
<import name="comp" src="./comp"></import>
<template>
  <div class="parent-demo">
    <comp say="{{say}}" prop-object="{{obj}}"></comp>
  </div>
</template>
<script>
 export default {
 data: {
 say:'hello'
 obj:{
 name:'child-demo'
 }
 }
 }
</script>
```

复制代码
#### 子组件对父组件通信


当子组件对数据进行改造后，把最终数据交给父组件甚至往上，往往有以下办法


- 父组件传递的数据本身就是对象，子组件**直接修改对象中的属性**，父组件的值也会发生改变，不推荐这种;
- 子组件通过`$emit()`触发在 UI 组件上绑定的自定义事件来执行父组件的方法


##### emit 示例如下


父组件监听子组件事件


```

<import name="comp" src="./comp.ux"></import>
<template>
  <div class="parent-demo">
    <text>我是父组件count:{{count}}</text>
    <comp count="{{count}}" @child-evt="emitEvt"></comp>
  </div>
</template>

<script>
 export default {
 data: {
 count: 20,
 },
 emitEvt(evt) {
 this.count = evt.count
 },
 }
</script>
```

复制代码
子组件触发事件


```

<template>
  <div class="child-demo">
    <text>我是子组件一count:{{compCount}}</text>
    <input type="button" @click='addHandler' value='add'></input>
  </div>
</template>
<script>
 export default {
 props: {
 count:{}
 },
 data(){
 return{
 compCount:this.count
 }
 },
 addHandler(){
 this.compCount ++
 this.$emit('childEvt',{
 count:this.compCount
 })
 },
 }
</script>
```

复制代码


---


<!-- 文档 7: tutorial/app-service/props/.md -->


## props

## props

更新时间：2025-07-10 10:44:44


### Prop 写法


Prop 属性名称使用 camelCase(驼峰命名法)命名法，在外部传递数据时请转化为以 kebab-case (短横线分隔命名) propObject 转换为 prop-object。


```

<!-- 子组件 -->
<template>
  <div class="child-demo">
    <text>{{ propObject.name }}</text>
  </div>
</template>
<script>
 export default {
 props: {
 propObject: {},
 },
 }
</script>
```

复制代码

```

<!-- 父组件 -->
<import name="comp" src="./comp"></import>
<template>
  <div class="parent-demo">
    <comp prop-object="{{obj}}"></comp>
  </div>
</template>
<script>
 export default {
 data: {
 obj: {
 name: 'child-demo',
 },
 },
 }
</script>
```

复制代码
### 属性默认值


子组件声明属性时，可以设置默认值。当调用子组件没有传入该数据时，将会自动设为默认值。


如果需要设置默认值，`props` 属性的写法必须要要写成 Object 形式，**不能**写成 Array 形式。


**示例如下：**


```

<script>
 // 子组件
 export default {
 props: {
 prop1: {
 default: 'Hello', //默认值
 },
 prop2Object: {}, //不设置默认值
 },
 onInit() {
 console.info(`外部传递的数据：`, this.prop1, this.prop2Object)
 },
 }
</script>
```

复制代码
### 数据单向性


父子间的数据传输是单向性的，父组件 prop 数据更新，子组件的数据会刷新为最新值;子组件的 prop 值发生改变，并不会改变父组件中值。


但是**prop 类型事数组或者对象，自组件变化会影响到父组件的值**，这意味着你不应该在一个子组件内部改变 prop 的值，这是危险性操作。


常见的三种操作 prop 值的方法：


**1.将 prop 传入的值作为初始值，用 data 接收**


```

<script>
 export default {
 props: {
 say: {},
 propObject: {},
 },
 data() {
 return {
 obj: this.propObject.count,
 }
 },
 onInit() {
 console.info(`外部传递的数据：`, this.say, this.propObject)
 },
 }
</script>
```

复制代码
**提示：**


- 如果你想用 data 直接接收 propObject 这个对象，可以采用**JSON.parse(JSON.stringify(propObject))**，将 prop 深度克隆。


**2.$watch 监控数据改变**


如果是监听对象中的属性，参数请使用`.`分割，如：`this.$watch('propSay.name', 'watchPropsChange') 才能生效`


**注意使用$watch,一般用于处理 data 里面的数据监听**


```

<script>
 export default {
 data() {
 return {
 propSay: {
 name: 'app',
 },
 }
 },
 onInit() {
 // 监听数据变化
 this.$watch('propSay.name', 'watchPropsChange')
 },
 /\*\*
 \* 监听数据变化，你可以对数据处理后，设置值到data上
 \* @param newV
 \* @param oldV
 \*/
 watchPropsChange(newV, oldV) {
 console.info(`监听数据变化：`, newV, oldV)
 this.propSay = newV && newV.toUpperCase()
 },
 }
</script>
```

复制代码


---


<!-- 文档 8: tutorial/app-service/switching-pages/.md -->


## 页面路由

## 页面路由

更新时间：2025-10-09 11:25:10


> 
> 了解如何打开页面、回退，并传递参数
> 
> 
> 


### 组件 a 切换页面


#### 切换页面


组件 a 可通过配置 href 属性跳转到应用内的页面


**示例如下：**


```

<template>
  <div class="tutorial-page">
    <!-- 以'/'开头的应用内页面的路径 -->
    <a href="/PageParams/receiveparams">跳转到接收参数页面</a>
    <!-- 以非'/'开头的应用内页面的名称 -->
    <a href="PageParams/receiveparams">跳转到接收参数页面</a>
    <!-- 特殊的,如果uri的值是'/',则跳转到path为'/'的页,没有则跳转到首页-->
    <a href="/">跳转到首页</a>
  </div>
</template>
```

复制代码


#### 传递参数


通过组件 a 实现页面切换时，可以通过'?key=value'的方式添加参数，支持参数为变量


**示例如下：**


```

<script>
 export default {
 data: {
 title: 'Hello, world!',
 },
 onInit() {
 console.log('组件a切换页面并传递参数')
 },
 }
</script>

<template>
  <div class="flex flex-col justify-center items-center">
    <!-- 添加参数 -->
    <a href="/PageParams/receiveparams?key=Hello, world!" class="mt-[75px] text-[30px] text-[#09ba07] underline">携带参数key1跳转</a>
    <!-- 添加变量参数 -->
    <a href="/PageParams/receiveparams?key={{title}}" class="mt-[75px] text-[30px] text-[#09ba07] underline">携带参数key2跳转</a>
  </div>
</template>

<style>
@tailwind utilities;
</style>
```

复制代码
### 接口 router 切换页面


#### 切换页面


router 接口在使用前，需要先导入模块


`router.push(OBJECT)` / `router.replace(OBJECT)` 支持的参数 uri 与组件 a 的 href 属性完全一致


**示例如下：**


```

<script>
 // 导入模块
 import router from '@blueos.app.router'

 export default {
 onInit () {
 console.log('接口router切换页面')
 },
 routePagePush () {
 // 跳转到应用内的某个页面
 router.push({
 uri: '/PageParams/receiveparams'
 })
 },
 routePageReplace () {
 // 跳转到应用内的某个页面，当前页面无法返回
 router.replace({
 uri: '/PageParams/receiveparams'
 })
 },
 routePageBack () {
 // 返回上一页面
 router.back()
 },
 routePageClear () {
 // 清空所有历史页面记录，仅保留当前页面
 router.clear()
 }
 }
</script>

<template>
  <div class="flex flex-col justify-center items-center">
    <input class="w-[550px] h-[86px] mt-[75px] rounded-[43px] bg-[#09ba07] text-[30px] text-white" type="button" value="跳转到接收参数页面" onclick="routePagePush"></input>
    <input class="w-[550px] h-[86px] mt-[75px] rounded-[43px] bg-[#09ba07] text-[30px] text-white" type="button" value="跳转到接收参数页面，当前页面无法返回" onclick="routePageReplace"></input>
    <input class="w-[550px] h-[86px] mt-[75px] rounded-[43px] bg-[#09ba07] text-[30px] text-white" type="button" value="返回上一页" onclick="routePageBack"></input>
    <input class="w-[550px] h-[86px] mt-[75px] rounded-[43px] bg-[#09ba07] text-[30px] text-white" type="button" value="清空页面记录，仅保留当前页面" onclick="routePageClear"></input>
  </div>
</template>

<style>
@tailwind utilities;
</style>
```

复制代码
#### 传递参数


router 接口的参数 params 可配置页面跳转时需要传递的参数


**示例如下：**


```

<script>
 // 导入模块
 import router from '@blueos.app.router'

 export default {
 data: {
 title: 'Hello, world!'
 },
 onInit () {
 console.log('接口router切换页面并传递参数')
 },
 routePagePushWithParams () {
 // 跳转到应用内的某个页面
 router.push({
 uri: '/PageParams/receiveparams',
 params: { key: this.title }
 })
 },
 routePageReplaceWithParams () {
 // 跳转到应用内的某个页面，当前页面无法返回
 router.replace({
 uri: '/PageParams/receiveparams',
 params: { key: this.title }
 })
 }
 }
</script>

<template>
  <div class="flex flex-col justify-center items-center">
    <input class="w-[550px] h-[86px] mt-[75px] rounded-[43px] bg-[#09ba07] text-[30px] text-white" type="button" value="携带参数跳转页面" onclick="routePagePushWithParams"></input>
    <input class="w-[550px] h-[86px] mt-[75px] rounded-[43px] bg-[#09ba07] text-[30px] text-white" type="button" value="携带参数跳转页面，当前页面无法返回" onclick="routePageReplaceWithParams"></input>
  </div>
</template>

<style>
@tailwind utilities;
</style>
```

复制代码
### 接收参数


现在，开发者已经掌握了通过组件 a 和接口 router 在页面之间传递参数的方法，如何接收参数呢？


其实很简单，组件 a 和接口 router 传递的参数的接收方法完全一致：在页面的 ViewModel 的`data属性`中声明使用的属性


**示例如下：**


```

<script>
 export default {
 data: {
 key: '',
 },
 onInit() {
 console.log('接收参数')

 // js中输出页面传递的参数
 console.info('key: ' + this.key)
 },
 }
</script>

<template>
  <div class="flex flex-col justify-center items-center">
    <text>page</text>
    <!-- template中显示页面传递的参数 -->
    <text>{{key}}</text>
  </div>
</template>

<style>
@tailwind utilities;
</style>
```

复制代码


---


<!-- 文档 9: tutorial/configuration/file-organization/.md -->


## 文件组织

## 文件组织

更新时间：2024-01-10 16:04:30


> 
> 本文对项目的文件目录及相关内容进行了介绍，包括蓝河应用文件结构讲解，配置信息、新增页面等
> 
> 
> 


### 项目介绍


通过 BlueOS Studio 新建一个项目，这个项目已经包含了**项目配置**与**示例页面**的初始代码，项目根目录主要结构如下：


```

├── scripts                   工具脚本文件
├── src
│   ├── assets                公用资源
│   │   ├── images            图片资源
│   │   └── styles            应用样式
│   ├── pages                 页面目录
│   │   ├── Demo              应用首页
│   │   └── DemoDetail        应用详情页
│   ├── app.ux                app.ux文件。
│   └── manifest.json         项目配置文件，配置应用图标、页面路由等
└── jsconfig.json             js 配置文件，用于语法校验
└── package.json              定义项目需要的各种模块及配置信息
```

复制代码
#### 目录的简要说明如下：


- **src**：项目源文件夹
- **app.ux** 文件用于全局 JavaScript 逻辑和应用生命周期管理，[详见](/api/extend/lifecycle/)


### 配置信息


每个应用都要有专属的名称，图标等，这些信息都需要在`manifest.json`文件中配置。详见文档[manifest 文件](/reference/configuration/manifest)


#### 应用包名（package）


应用包名，是区别于其他应用的唯一标识


推荐采用 com.company.module 的格式，示例如下：


```

{
  "package": "com.example.demo"
}
```

复制代码
#### 应用名称（name）


应用名称，6 个汉字以内，与应用商店保存的名称一致；框架提供保存到桌面的功能，桌面上显示的应用名即为此属性


示例如下：


```

{
  "name": "发票小助手"
}
```

复制代码
#### 应用图标（icon）


规则为正方形（不能是圆角），且务必无白边


```

{
  "icon": "/assets/images/logo.png"
}
```

复制代码
#### 应用版本名称、版本号（versionName、versionCode）


应用版本名称、版本号为开发者的应用包维护的版本信息


应用版本名称为`主版本.次版本`格式


应用版本号为整数，从`1`开始，每次更新上架请自增 1


示例如下：


```

{
  "versionName": "1.0",
  "versionCode": 1
}
```

复制代码
#### 配置接口列表（features）


在使用接口时，需要先在 manifest 中声明接口。在每个接口文档的顶部，都附有声明接口的配置代码


以 fetch 网络请求为例，示例如下：


```

{
  "features": [{ "name": "blueos.communication.network.fetch" }]
}
```

复制代码
### 新增页面


新增及配置页面，需要依赖`manifest.json`中`router`配置


#### router


`router`，路由，用于定义页面的实际地址、跳转地址。如果 ux 页面没有配置路由，则不参与项目编译。一个目录下最多只能存在一个主页面文件（不包括组件文件）


##### 首页 (router.entry)


首页，即应用平台启动时默认打开的页面。首页需配置为应用中某页面的名称，即在`<ProjectName>/src`目录下，**页面目录的相对路径**


假设工程根目录如下所示


```

└── src
    └── Demo                  页面目录，存放各自页面私有的资源文件和组件文件
        └── index.ux          页面文件，文件名不必与父文件夹相同（推荐index.ux）
```

复制代码
假设首页为 Demo 目录下的 index.ux 文件，则首页对应的页面名称为`Demo`


```

{
  "router": {
    "entry": "Demo"
  }
}
```

复制代码
##### 页面路由对象（router.pages）


页面路由对象，key 为页面名称（`<ProjectName>/src`目录下，**页面目录的相对路径**），value 为页面具体路由配置，key 不要重复


页面具体路由配置（router.pages 的 value）包括以下属性：


- **component**：页面对应的 ux 文件名
- **path**：页面路径，不填则默认为页面名称（`<ProjectName>/src`目录下，页面目录的**相对路径**）


示例如下：


假设工程根目录如下所示


```

└── src
    |── Demo                  页面目录，存放各自页面私有的资源文件和组件文件
    |   └── index.ux          页面文件，文件名不必与父文件夹相同（推荐index.ux）
    └── Doc
        └── Layout            页面目录，存放各自页面私有的资源文件和组件文件
            └── index.ux      页面文件，文件名不必与父文件夹相同（推荐index.ux）
```

复制代码
当页面名称（router.pages 的 key）为`Demo`时，对应的页面配置（router.pages 的 value）包括：


- **component**：页面对应的 ux 文件名`index`
- **path**：页面路径，默认为页面名称`Demo`


```

{
  "router": {
    "pages": {
      "Demo": {
        "component": "index"
      },
      "Doc/Layout": {
        "component": "index"
      }
    }
  }
}
```

复制代码
现在，开发者就可以通过`/Demo`访问到 Demo 目录下的 index.ux 页面了


---


<!-- 文档 10: tutorial/configuration/intro/.md -->


## 框架简介

## 框架简介

更新时间：2025-07-09 21:34:57


蓝河应用框架采用了类 web 开发范式，具有学习成本低，开发效率高的特点。框架提供了丰富的 UI 组件与样式，开发者可以因此高效搭建界面。同时框架提供了两套 API 接口，开发者可以按需选择。


### 数据绑定


数据绑定可以让数据与视图非常简单地保持同步。当做数据修改的时候，只需要在逻辑层修改数据，视图层就会做相应的更新。数据绑定的具体使用参看[数据绑定](/reference/app-service/data-binding/) 。


### 路由管理


框架负责管理整个应用的页面路由，实现页面间的无缝切换，管理每个页面的完整生命周期。开发者需要将页面在 manifest.json 中进行注册，在代码中通过框架提供的接口方法实现页面的切换。具体使用参看[manifest 文件](/reference/configuration/manifest)、[页面路由](/api/system/router)和[页面启动模式](/reference/extend/launch-mode)。


### UI 组件


提供了基础、表单，布局/容器、画布、导航、动画、系统风格等类型的一系列组件。通过参看[UI 组件](/component/common/rule/)，您可以了 UI 组件解更详细的信息。


### API 接口


蓝河应用提供了 JS API 和 Native API 两种接口，以支撑高效和高性能的开发场景。如果您需要了解更多关于这些开放能力的信息，请移步[JS 功能接口](/api/system/app/)与[Native API](/native/quickstart/introduction/)进行了解。


### 生命周期


生命周期是指在程序运行的过程中，程序从创建、运行到销毁的整个过程。在这个过程中，程序会经历多个状态和阶段，每个阶段都会触发一些特定的回调函数，用于执行相应的操作和处理，这些回调函数被称为生命周期函数。


  

蓝河应用提供了自定义组件、页面与应用的生命周期函数，让开发者有机会在特定阶段运行相应的代码。如果您需要了解更多关于生命周期的信息，请移步[生命周期](/api/extend/lifecycle/)


---


<!-- 文档 11: tutorial/configuration/manifest/.md -->


## manifest 文件

## manifest 文件

更新时间：2025-10-09 11:25:10


manifest.json 文件中包含了应用描述、接口声明、页面路由信息


### manifest


| 属性 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| package | string | - | 是 | 应用包名，**确认与原生应用的包名不一致**，推荐采用 com.company.module 的格式，如：com.example.demo |
| name | string | - | 是 | 应用名称，**6 个汉字以内，与应用商店保存的名称一致**，用于在桌面图标、弹窗等处显示应用名称 |
| icon | string | - | 是 | 应用图标，提供 114x114 大小的即可 |
| versionName | string | - | 否 | 应用版本名称，如：`"1.0"` |
| versionCode | number | - | 是 | 应用版本号，从`1`自增，**推荐每次重新上传包时`versionCode`+1** |
| features | [FeatureInfo](#featureinfo)[] | - | 否 | 接口列表，绝大部分接口都需要在这里声明，否则不能调用，详见每个接口的文档说明 |
| config | [Config](#config) | - | 是 | 系统配置信息，详见下面说明 |
| router | [Router](#router) | - | 是 | 路由信息，详见下面说明 |
| deviceTypeList | Array<string> | watch | 否 | 可选值有：`watch`, `watch-square`, `watch-round`, `tv` , `car`, `phone` |
| display | [Display](#display) | - | 否 | UI 显示相关配置，详见下面说明 |
| permissions | [PermissionInfo](#permissioninfo)[] | - | 否 | 权限申请示例:[{ "name": "watch.permission.LOCATION" }] |
| appCategory | [AppCategory](#appcategory)[] | - | 是 | 应用类别,可选值详见下文应用类别说明,最多 2 个分类 |
| customData | Record<string, string> | - | 否 | 开发者自定义字段，限定不超过 30 个字符，可通过 `packageManager.getCustomData()`方法读取 |
| distrubuteRules | [DistrubuteRules](#distrubuterules) | - | 否 | 表示分发规则，定义包对应的细分设备规格的分发策略，以便在应用市场进行云端分发应用包时做精准匹配。该标签可配置的分发策略维度包括 minAPILevel |
| widgetProvider | [WidgetProvider](#widgetprovider)[] | - | 否 | 注册和生命 widgetProvider，为蓝河智慧服务卡片提供数据 |


#### AppCategory


appCategory 要求开发者必填，如有开发者未填，系统将设置为 ['other']。


| 取值 | 说明 |
| --- | --- |
| business | 商业类应用 |
| education | 教育类应用 |
| pastime | 娱乐类应用 |
| finance | 财务类应用 |
| games | 游戏类应用 |
| lifestyle | 生活方式类应用 |
| medical | 医疗类应用 |
| music | 音乐类应用 |
| news | 新闻类应用 |
| photography | 摄影类应用 |
| reference | 参考资料类应用 |
| social | 社交类应用 |
| sports | 体育类应用 |
| travel | 旅游类应用 |
| utilities | 实用工具类应用 |
| video | 视频类应用 |
| weather | 天气类应用 |
| navigation | 导航类应用 |
| book | 书籍类应用 |
| shopping | 购物类应用 |
| podcasts | 播客类应用 |
| audiobooks | 音频书籍类应用 |
| radio | 电台类应用 |
| other | 其它类应用 |


#### FeatureInfo


声明应用需要使用的 feature


| 属性 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| name | string | - | feature 名称，可在具体 feature 的说明文档中查阅 |


**示例：**


```

{
  "name": "blueos.storage.file"
}
```

复制代码
#### Config


用于定义系统配置和全局数据。


| 属性 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| designWidth | number | - | 页面设计基准宽度，根据实际设备宽度来缩放元素大小，建议使用 466 |


**示例：**


```

{
  "designWidth": 466
}
```

复制代码
#### Router


用于定义页面的组成和相关配置信息，如果页面没有配置路由信息，则在编译打包时跳过。


| 属性 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| entry | string | - | 是 | 首页名称 |
| pages | Record<string, [Page](#page)> | - | 是 | 页面配置列表，key 值为页面名称（对应页面目录名，例如 Hello 对应'Hello'目录），value 为页面详细配置 page，详见下面说明 |


**示例：**


```

{
  "entry": "Demo",
  "pages": {
    "Demo1": {
      "component": "index"
    },
    "Demo2": {
      "component": "index"
    }
  }
}
```

复制代码
#### Page


用于定义单个页面路由信息。


| 属性 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| component | string | - | 是 | 页面对应的组件名，与 ux 文件名保持一致，例如'hello' 对应 'hello.ux'，目前仅支持 index.ux |
| path | string | /<页面名称> | 否 | 页面路径，例如“/user”,不填则默认为/<页面名称>。path 必须唯一,不能和其他 page 的 path 相同。下面 page 的 path 因为缺失,会被设置为“/Index”：`"Index": {"component": "index"}` |
| launchMode | [LaunchMode](#launchmode) | standard | 否 | 声明页面的启动模式 |
| followHand | string | enable | 否 | 配置页面是否支持右滑跟手，disable：不支持；enable：支持 |


#### LaunchMode


页面的启动模式


| 取值 | 说明 |
| --- | --- |
| singleTask | 每次打开目标页面都会打开已有的目标页面并回调 onRefresh 生命周期函数，清除该页面上打开的其他页面，没有打开过此页面时会创建新的目标页面实例。 |
| standard | 每次打开新的目标页面（多次打开目标页面地址时会存在多个相同页面） |


#### Display


用于定义与 UI 显示相关的配置。


如果在 display 对象下定义以下属性值，则生效范围为此蓝河应用全部页面；


| 属性 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| backgroundColor | string | #000 | 窗口背景颜色 |


**示例：**


```

{
  "backgroundColor": "#ffffff"
}
```

复制代码
#### PermissionInfo


权限配置信息


| 属性 | 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| name | [PermissionName](#permissionname) | - | 权限名 |


**示例：**


```

{
  "name": "watch.permission.LOCATION"
}
```

复制代码
#### DistrubuteRules


分发规则详细信息


| 属性 | 类型 | 默认值 | 含义 |
| --- | --- | --- | --- |
| minAPILevel | number | 1 | 表示最低的 APILevel 要求，只有支持该 APILevel 的系统版本，才能被分发。 |


**示例：**


```

{
  "minAPILevel": 2
}
```

复制代码
#### WidgetProvider


widgetProvider 详细配置信息


| 属性 | 类型 | 必填 | 默认值 | 含义 |
| --- | --- | --- | --- | --- |
| name | string | 是 | - | widgetProvider 名称 |
| path | string | 是 | - | widgetProvider 的 js 文件路径 |


**示例：**


```

{
  "name": "music",
  "path": "/widgetProvider/index.js"
}
```

复制代码
#### PermissionName


权限名及模块接口信息，该信息也可以在具体的模块文档中查看。


| 权限名 | 模块 | 说明 | 权限错误码 |
| --- | --- | --- | --- |
| watch.permission.LOCATION | @blueos.hardware.geolocation | 位置信息 | 400 : 拒绝授予权限, 402: 权限错误（未声明该权限） |
| watch.permission.STEP\_COUNTER | @blueos.hardware.sensor | 计步传感器 | 400 : 拒绝授予权限, 402: 权限错误（未声明该权限） |
| watch.permission.DEVICE\_INFO | @blueos.hardware.device | 设备信息 | 400: 拒绝授予权限 , 402: 权限错误（未声明该权限） |
| watch.permission.RECORD | @blueos.multimedia.record | 录音 | 400: 拒绝授予权限, 401: 敏感权限不能在后台运行, 402: 权限错误（未声明该权限） |
| watch.permission.BLUETOOTH | @blueos.communication.bluetooth.bluetooth@vivo.bluetooth | 允许使用设备蓝牙 | 400 : 拒绝授予权限, 402: 权限错误（未声明该权限） |
| watch.permission.READ\_HEALTH\_DATA | @blueos.health.health@vivo.health | 读取健康数据 | 400 : 拒绝授予权限, 402: 权限错误（未声明该权限） |


---


<!-- 文档 12: tutorial/configuration/script/.md -->


## javascript 代码

## javascript 代码

更新时间：2025-05-20 14:21:12


用来定义页面数据和实现生命周期接口


### 语法


支持 ES6 语法


#### 模块声明


蓝河应用中支持`ES6`的`module`标准，使用`import`引入 js 依赖，同时支持 CommonJs 规范，使用`require`引入 js 依赖（具体参看功能接口部分文档说明）


```

// 首先在 `manifest.json` 中配置 `fetch` 接口

// require引入
const fetch = require('@blueos.communication.network.fetch')

// import引入
import fetch from '@blueos.communication.network.fetch'
```

复制代码
#### 代码引用


JS 代码引用推荐使用 import 来导入, 例如：


```

import utils from '../Common/utils.js'
```

复制代码
**注意**： 蓝河应用环境不是 node 环境，不要引用 node 原生模块，如 `import fs from 'fs'`


### 对象


蓝河应用的组件对象提供了一些属性和方法，用于控制组件的渲染、数据处理、组件逻辑等方面


#### 页面级组件对象


| 属性 | 类型 | 描述 |
| --- | --- | --- |
| data | Object | Function | 页面级组件的数据模型，能够转换为 JSON 对象；属性名不能以$或\_开头, 不要使用 for, if, show, tid 等保留字如果是函数，返回结果必须是对象，在组件初始化时会执行函数获取结果作为 data 的值使用 data 方式声明的属性会被外部数据覆盖，因此存在一定安全风险。 |


##### 示例


```

<template>
  <div class="wrapper">
    <text>{{title}]</text>
  </div>
</template>

<script>
export default {
  data: {
    title: 'Hello Word'
  },
}
</script>
```

复制代码
#### 自定义组件对象


| 属性 | 类型 | 描述 |
| --- | --- | --- |
| data | Object | Function | 自定义组件的数据模型，能够转换为 JSON 对象；属性名不能以$或\_开头, 不要使用 for, if, show, tid 等保留字如果是函数，返回结果必须是对象，在组件初始化时会执行函数获取结果作为 data 的值 |
| props | Array | Object | 定义组件外部可传入的所有属性；属性名不能以$或\_开头, 不要使用 for, if, show, tid 等保留字在模板代码中，请使用短横线分隔命名代替驼峰命名。如，属性定义 props: ['propA']，可通过`<tag prop-a='xx'>`方式传递到组件内部 |


##### 示例


```

<template>
  <div class="wrapper">
    <text>{{title}]</text>
    <text>{{name}]</text>
  </div>
</template>

<script>
export default {
  data: {
    title: 'child component'
  },
  props: ['name']
}
</script>
```

复制代码
想了解更多信息可以参考[自定义组件](/reference/app-service/parent-child-component-communication/)


#### 公共对象


| 属性 | 类型 | 描述 |
| --- | --- | --- |
| $app | Object | 应用对象 |
| $page | Object | 页面对象 |
| $valid | Boolean | 页面对象是否有效 |
| $device | { deviceType: string } | 获取当前设备类型。`watch-square`：方形手表，`watch-round`：圆形手表 |


#### 应用对象


可通过`$app`访问


| 属性 | 类型 | 描述 |
| --- | --- | --- |
| $def | Object | 使用`this.$app.$def`获取在`app.ux`中暴露的对象 |


### 方法


#### 公共方法


| 属性 | 类型 | 参数 | 描述 |
| --- | --- | --- | --- |
| $element | Function | id: String 组件 id | 获取指定 id 的组件调用来对应的组件方法 |
| $set | Function | key: String 属性名称  value: Any | 添加数据属性，用法：`this.$set('key',value)` |


#### 事件方法


| 属性 | 类型 | 参数 | 描述 |
| --- | --- | --- | --- |
| $watch | Function | data: String 属性名, 支持'a.b.c'格式，不支持数组索引  handler: String 事件句柄函数名, 函数的第一个参数为新的属性值，第二个参数为旧的属性值 | 动态添加属性/事件绑定，属性必须在 data 中定义，handler 函数必须在`<script>`定义；当属性值发生变化时事件才被触发用法：`this.$watch('a','handler')` |


#### 应用方法


可通过`$app`访问


| 属性 | 类型 | 参数 | 描述 |
| --- | --- | --- | --- |
| exit | Function | 无 | 退出蓝河应用，结束应用生命周期。调用方法：`this.$app.exit()` |


该 feature 依赖 `blueos.app.app`, 请确保在 `manifest.json` 中引入


#### 页面方法


可通过`$page`访问


| 属性 | 类型 | 参数 | 描述 |
| --- | --- | --- | --- |
| setStopGestureQuit | Function | Number | 是否屏蔽手势返回，1 - 屏蔽。0 - 不屏蔽。调用方法：`this.$page.setStopGestureQuit(1)` |


该 feature 依赖 `blueos.app.router`, 请确保在 `manifest.json` 中引入


---


<!-- 文档 13: tutorial/configuration/style-sheet/.md -->


## style 样式

## style 样式

更新时间：2024-10-11 11:55:18


用于描述 template 模板的组件样式，决定组件应该如何显示


样式布局采用 CSS Flexbox（弹性盒）样式，针对部分原生组件，对 CSS 进行了少量的扩充以及修改


为了解决屏幕适配问题，所有与大小相关的样式（例如 width、font-size）均以基准宽度（默认 750px）为基础，根据实际屏幕宽度进行缩放


### 文件导入


支持@import 导入外部文件


```

<style>
 @import './style.css';
 .a {
 }
</style>
```

复制代码
### 模板内部样式


支持使用 style、class 属性来控制组件的样式


```

<!-- 内联inline -->
<div style="color: #f00; margin: 10px;" />
<!-- class声明 -->
<div class="normal append" />
```

复制代码
### 伪类


css 伪类是选择器中的关键字，用于指定要选择元素的特殊状态。


| 名称 | 支持组件 | 描述 |
| --- | --- | --- |
| :active | 通用 | 表示被用户激活的元素，如：被用户按下的按钮。 |


### 选择器


支持的选择器有：


| 选择器 | 样例 | 样例描述 |
| --- | --- | --- |
| .class | .intro | 选择所有拥有 class="intro" 的组件 |
| #id | #firstname | 选择拥有 id="firstname" 的组件 |
| tag | div | 选择所有 div 组件 |
| , | .a, .b | 选择所有 class=“.a” 以及 class=“.b”的组件 |
| #id .class tag | .page .body text | 支持 id,class,tag 的后代选择器，也可以使用">"表示直接后代 |


```

<style>
 /\* 单个选择器 \*/
 text {
 }
 .class-abc {
 }
 #idAbc {
 }
 /\* 后代选择 \*/
 .doc-page #testTag div text {
 }
 .doc-page #test-class .class1 {
 }
 .doc-page #testId #testIdId1 {
 }
 /\* 直接后代选择 \*/
 .doc-page #testTag .flex-column > text {
 }
 /\* 同一样式适应多个选择器 \*/
 .font-text,
 .font-comma {
 }
</style>
```

复制代码
注意，选择器声明的变化可能会导致元素重新绘制。为了减少选择器变化引起的 DOM 更新数量，**当前只支持：CSS 声明的多个选择器中最后一个规则的变更对 DOM 的更新**


```

<template>
  <div class="{{docBody}}">
    <text class="{{rowDesc}}">描述内容</text>
  </div>
</template>

<style>
 .doc-body .row-desc1 {
 color: #ff0000;
 }
 .doc-body .row-desc2 {
 color: #0000ff;
 }
 .doc-body2 .row-desc1 {
 color: #00ff00;
 }
</style>

<script>
 export default {
 // 页面级组件的数据模型
 data: {
 rowDesc: 'row-desc1',
 docBody: 'doc-body',
 },
 }
</script>
```

复制代码
以上的代码示例，当我们把`rowDesc变量`从`row-desc1`变为`row-desc2`时是通知 Native 更新节点样式，但是如果把`docBody变量`从`doc-body`变为`doc-body2`，是不会通知 DOM 更新的。


因为`doc-body`不是最后一个选择器，非末尾的选择器变更有可能影响很多 DOM 元素，从而影响到渲染性能


### 选择器优先级


当前样式的选择器的优先级计算保持与浏览器一致，是浏览器 CSS 渲染的一个子集（仅支持：inline, id, class, tag, 后代，直接后代）


多条 CSS 声明可以匹配到同一个元素 如 div，应用在该元素上的 CSS 声明总体优先级是：inline > #id > .class > tag，这四大类匹配到该元素的多个 CSS 声明，如：`#page .class-div`和`.page .class-div`，其优先级按照各选择器的权值高低之和来比较


- `ID选择器`（例如: #hello）的权值为 10000
- `类选择器`（例如: .example）的权值为 100
- `类型选择器`（例如: h1）的权值为 1


css 的优先级计算文档也可以查看 [MDN 文档](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Specificity) 入门


那么以下 CSS 声明计算的权值为：


- `#page`的权值为：10000
- `#page .class-div`的权值为：10100
- `#page .class-div text`的权值为 10101
- `#page #body .container div text`的权值为：20102


因此：


- `#page .class-div`和`.page .class-div`比较，权值不一样，权值高优先级高；如果权值相同，则按照声明顺序：后者覆盖前者


### 样式预编译


目前蓝河应用支持`less`与`sass`的预编译，具体教程也可以参考[[这里]](https://less.bootcss.com/)


```

<!--导入外部文件, 代替style内部样式-->
<style lang="less" src="./lessFile.less"></style>

<!--合并外部文件-->
<style lang="less">
 @import './lessFile.less';
 .page-less {
 #testTag {
 .less-font-text,
 .less-font-comma {
 font-size: 60px;
 }
 }
 }
</style>
```

复制代码
### 媒体查询


媒体查询（Media Query）在移动设备上应用十分广泛，开发者经常需要根据设备的大致类型或者特定的特征和设备参数（例如屏幕分辨率）来修改应用的样式。为此媒体查询提供了如下功能：


1.针对设备和应用的属性信息，可以设计出相匹配的布局样式。 2.当屏幕发生动态改变时（比如分屏、横竖屏切换），应用页面布局同步更新。


### CSS 语法规则


使用@media 来引入查询语句，具体规则如下：


```

@media [media-type] [and|not|only] [(media-feature)] {
  CSS-Code;
}
```

复制代码
### 举例：


```

/\* level3的写法, 表示：宽度小于30dp时生效 \*/
@media (max-width: 30) {  .box {
    background-color: red;
  }
}
/\* level4的写法，比level3更清晰简洁，表示：宽度小于30dp时生效 \*/
@media (width <= 30) {  .box {
    background-color: red;
  }
}
/\* 多条件写法，表示：宽度大于400dp且小于700dp时生效 \*/
@media screen and (min-width: 400) and (max-width: 700) {  .box {
    background-color: red;
  }
}
/\* 多条件level4写法，表示：宽度大于400dp且小于700dp时生效 \*/
@media (400 <= width <= 700) {  .box {
    background-color: red;
  }
}
/\* 多条件写法，表示：方表和手机上生效 \*/
@media screen and (device: watch-square) or screen and (device: phone) {  .box {
    background-color: red;
  }
}
```

复制代码
### 页面中引用资源


通过@import 方式引入媒体查询，具体使用方法如下：


```

@import url [media-type] [and|not|only] [(media-feature) ];
```

复制代码
例如：


```

@import '../common/style.css' screen and (min-width: 600) and (max-width: 1200);
```

复制代码
### 动态修改样式


动态修改样式有多种方式，包括但不限于以下：


- **修改 class**：更新组件的 class 属性中使用的变量的值
- **修改内联 style**：更新组件的 style 属性中的某个 CSS 的值
- **修改绑定的对象**：通过绑定的对象控制元素的样式
- **修改绑定的样式字符串**：通过样式字符串控制元素的样式


**示例如下：**


```

<template>
  <div style="flex-direction: column;">
    <!-- 修改 class -->
    <text class="normal-text {{ className }}" onclick="changeClassName">点击我修改文字颜色</text>
    <!-- 修改内联 style -->
    <text style="color: {{ textColor }}" onclick="changeInlineStyle">点击我修改文字颜色</text>
    <!-- 修改绑定的对象 -->
    <text style="{{ styleObj }}" onclick="changeStyleObj">点击我修改文字颜色</text>
    <!-- 修改绑定的样式字符串 -->
    <text style="{{ styleText }}" onclick="changeStyleText">点击我修改文字颜色</text>
  </div>
</template>

<style>
 .normal-text {
 font-weight: bold;
 }
 .text-blue {
 color: #0faeff;
 }
 .text-red {
 color: #f76160;
 }
</style>

<script>
 export default {
 data: {
 className: 'text-blue',
 textColor: '#0faeff',
 styleObj: {
 color: '#f00',
 },
 styleText: 'color: #0f0',
 },
 changeClassName() {
 this.className = 'text-red'
 },
 changeInlineStyle() {
 this.textColor = '#f76160'
 },
 changeStyleObj() {
 this.styleObj = {
 color: '#00f',
 }
 },
 changeStyleText() {
 this.styleText = 'color: #0f0'
 },
 }
</script>
```

复制代码
### 引入 less/scss 预编译


#### less 篇


less 语法入门请参考[less 中文官网](https://less.bootcss.com/) 学习


使用 less 请先安装相应的类库：`less`、`less-loader`，


```

npm i less less-loader
```

复制代码
在`<style>`标签上添加属性`lang="less"`


```

<template>
  <div class="tutorial-page">
    <text id="title">less示例!</text>
  </div>
</template>
<style lang="less">
 /\* 引入外部less文件 \*/
 @import './style.less';
 /\* 使用less \*/
</style>
```

复制代码
#### scss 篇


scss 语法入门请参考 [[scss 中文官网]](https://www.sasscss.com/)学习


使用 scss 请在蓝河应用项目下执行以下命令安装相应的类库：`node-sass`、`sass-loader`，


```

npm i node-sass sass-loader
```

复制代码
在`<style>`标签上添加属性`lang="scss"` **示例如下：**


```

<template>
  <div class="tutorial-page">
    <text id="title">less示例!</text>
  </div>
</template>

<style lang="scss">
 /\* 引入外部scss文件 \*/
 @import './style.scss';
 /\* 使用scss \*/
</style>
```

复制代码
### 媒体类型


| 类型 | 说明 |
| --- | --- |
| screen | 按屏幕相关参数进行媒体查询。 |


### 媒体逻辑操作


开发者可以使用逻辑操作符组合多个媒体特性的查询条件，编写复杂的媒体查询。


| 类型 | 说明 |
| --- | --- |
| and | and 运算符用于将多个媒体特性组合到一个单独的媒体查询中，要求每个链接的特性返回 true，则此时查询为真。 |
| not | not 运算符用于否定媒体查询，如果查询不返回 false，则返回 true。如果出现在逗号分隔的列表中，它只会否定应用它的特定查询。如果使用 not 运算符，则必须指定显式媒体类型。例如：not screen and (min-width: 400) and (max-width: 700)注：not 关键字不能用于否定单个功能表达式，它会作用于整个媒体查询。 |
| only | only 运算符仅用于整个查询匹配应用样式,蓝河应用处理以 only 开头的关键词时将会忽略 only。如果使用 only 运算符，必须指定媒体类型。例如：only screen and (min-width: 400) and (max-width: 700) |
| ,(逗号) | 逗号分隔效果等同于 or 逻辑操作符。当使用逗号分隔的媒体查询时，如果任何一个媒体查询返回真，样式就是有效的。例如：(orientation: landscape), (height >= 690)。 |
| or | or 运算符用于将多个媒体特性比较语句组合到一个媒体查询语句中，只要有其中一条媒体特性比较语句返回 true，查询成立。例如：(min-width: 400) or (max-width: 700) |
| <= | 小于等于。例如： (400 <= width)。 |
| >= | 大于等于。例如： (500 >= height)。 |
| < | 小于。例如： (400 < width)。 |
| > | 大于。例如： (500 > height)。 |


### 媒体特性


| 类型 | 说明 | 查询时是否带单位 | 支持单位 |
| --- | --- | --- | --- |
| height | 定义输出设备中的页面可视区域高度。 | 否 | dp |
| min-height | 定义输出设备中的页面可视区域最小高度。 | 否 | dp |
| max-height | 定义输出设备中的页面可视区域最大高度。 | 否 | dp |
| width | 定义输出设备中的页面可视区域宽度。 | 否 | dp |
| min-width | 定义输出设备中的页面可视区域最小宽度。 | 否 | dp |
| max-width | 定义输出设备中的页面可视区域最大宽度。 | 否 | dp |
| orientation | 定义屏幕处于横屏模式还是竖屏模式，支持属性：portrait（竖屏）、landscape（横屏）。 | 否 | 无 |
| aspect-ratio | 定义输出设备中的页面可见区域宽高比，比例值需要按照 x / y 的格式，例如 1 / 2。 | 否 | 无 |
| min-aspect-ratio | 定义输出设备中的页面可见区域最小宽高比，参数要求同上。 | 否 | 无 |
| max-aspect-ratio | 定义输出设备中的页面可见区域最大宽高比，参数要求同上。 | 否 | 无 |
| device | device 的可选值为:`phone`、`watch`、`car`、`tv`、`pad`、`watch-square`、`watch-round`，`watch` 默认 `watch-square` | 否 | 无 |


---


<!-- 文档 14: tutorial/configuration/ux-file/.md -->


## UX 文件

## UX 文件

更新时间：2025-10-09 11:25:10


APP、页面和自定义组件均通过 ux 后缀文件编写，ux 后缀文件由 [javascript 代码](/reference/configuration/script)、template 模板和[style 样式](/reference/configuration/style-sheet) 3 个部分组成，一个典型的页面 ux 后缀文件示例如下：


```

<script>
 import router from '@blueos.app.router'

 export default {
 // 页面级组件的数据模型
 data: {
 title: '示例页面',
 },
 routeDetail() {
 // 跳转到应用内的某个页面，router用法详见：文档->接口->页面路由
 router.push({
 uri: '/DemoDetail',
 })
 },
 }
</script>

<template>
  <!-- template里只能有一个根节点 -->
  <div class="flex flex-col justify-center items-center">
    <text class="text-4xl text-center">欢迎打开{{title}}</text>
    <!-- 点击跳转详情页 -->
    <input class="w-[550px] h-[86px] mt-[75px] rounded-[43px] bg-[#09ba07] text-3xl text-white" type="button" value="跳转到详情页" onclick="routeDetail" />
  </div>
</template>

<style>
@tailwind utilities;
</style>
```

复制代码
### app.ux


当前`app.ux`编译后会包含`manifest配置信息`，所以请不要删除`/**manifest**/`的注释内容标识。


您可以在`<script>`中引入一些公共的脚本，并暴露在当前 app 的对象上，如下所示，然后就可以在页面 ux 文件的 ViewModel 中，通过`this.$app.$def.util`访问。


```

<script>
 /\*\*
 \* 应用级别的配置，供所有页面公用
 \*/
 import util from './util'

 export default {
 showMenu: util.showMenu,
 createShortcut: util.createShortcut,
 util,
 }
</script>
```

复制代码


---


<!-- 文档 15: tutorial/extend/launch-mode/.md -->


## 页面启动模式

## 页面启动模式

更新时间：2023-10-21 10:15:58


用于定义页面的启动行为


### 静态声明


在 manifest 文件中页面路由信息 router.page 可增加启动模式字段 launchMode，用于声明该页面的启动模式


#### 页面启动模式参数：


| 属性 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| launchMode | String | standard | 否 | 声明页面的启动模式，支持"singleTask"，"standard"两种页面启动模式。标识为"singleTask"模式时每次打开目标页面都会打开已有的目标页面并回调 onRefresh 生命周期函数，清除该页面上打开的其他页面，没有打开过此页面时会创建新的目标页面实例。标识为"standard"模式时会每次打开新的目标页面（多次打开目标页面地址时会存在多个相同页面） |


#### 示例：


```

{
  "router": {
    "entry": "PageA",
    "pages": {
      "PageA": {
        "launchMode": "singleTask",
        "component": "index"
      },
      "PageB": {
        "launchMode": "standard",
        "component": "index"
      },
      "PageC": {
        "launchMode": "singleTask",
        "component": "index"
      }
    }
  }
}
```

复制代码
打开页面的行为逻辑：


若按顺序启动 PageA -> PageB -> PageC -> PageB -> PageC -> PageA


- 打开 PageA，首次打开时页面栈为空 `页面栈为PageA`
- 打开 PageB，PageB 的启动模式为 standard，即在 PageA 之上新建 PageB 的页面实例并显示 `页面栈为PageA,PageB`
- 打开 PageC，首次打开 PageC，即在 PageB 之上新建 PageC 的页面实例并显示 `页面栈为PageA,PageB,PageC`
- 打开 PageB，PageB 的启动模式为 standard，即在 PageC 之上新建 PageB 的页面实例并显示 `页面栈为PageA,PageB,PageC,PageB`
- 打开 PageC，PageC 页面实例已存在，即销毁 PageC 之上的页面实例 PageB，回到之前打开的 PageC 的页面实例并回调此页面生命周期的 onRefresh 函数 `页面栈为PageA,PageB,PageC`
- 打开 PageA，PageA 页面实例已存在，即销毁 PageA 之上的页面实例 PageB 和 PageC，回到之前打开的 PageA 的页面实例并回调此页面生命周期的 onRefresh 函数 `页面栈为PageA`


---


<!-- 文档 16: tutorial/extend/mulit/.md -->


## 屏幕适配

## 屏幕适配

更新时间：2024-10-11 11:55:18


蓝河操作系统支持对不同尺寸和不同形状的屏幕的适配能力。


### 1.等比放缩


在 manifest 文件中配置`designWidth`字段的设计基准宽度，蓝河应用便可以自动完成等比缩放。


```

// manifest.json
{
  "config": {
    "designWidth": 466
  }
}
```

复制代码
如上示例中`designWidth`配置为 466px，那么所有的 px 单位使用都会按照 466px 的基准宽度换算。如下示例中显示为宽高都是屏幕宽度一半。


```

.box {
  width: 233px;
  height: 233px;
}
```

复制代码
### 2.非等比屏幕


在非等比屏幕下，使用等比缩放或许不是开发想要的效果，这里蓝河应用提供了使用绝对宽度的方案来实现您想要的布局。


#### dp 单位


px 会使布局产生等比缩放效果，而 dp 为绝对的屏幕尺寸。


以宽度为示例，设备 dp 的计算方法如下：


```

屏幕宽度dp值 = 设备屏幕分辨率的宽度 / DPR
```

复制代码
上述公式中 DPR 的取值可以查如下表格得到


| 规格 | 取值 | 说明 |
| --- | --- | --- |
| ldpi | 0.75 | 低密度屏幕(~120dpi) |
| mdpi | 1 | 中密度屏幕(~160dpi)(基准密度) |
| hdpi | 1.5 | 高密度屏幕(~240dpi) |
| xhdpi | 2.0 | 加高密度屏幕(~320dpi) |
| xxhdpi | 3.0 | 超超高密度屏幕(~480dpi) |
| xxxhdpi | 4.0 | 超超超高密度屏幕(~640dpi) |


引入 DP 单位，开发者可以解决 `非等比例的屏幕适配` ;比如:在 DPR 为 3 的小屏幕上希望内容显示较少，设置元素 的宽度 dp 较小，在 DPR 为 3 的大屏幕上希望内容显示较多，设置元素的宽度 dp 较大;该单位可以像 px 单位 一样，用于常⻅的 DOM 元素的宽度、高度上。如下示例


```

.box {
  width: 50dp;
  height: 50dp;
}
```

复制代码
### 3.媒体查询


结合 dp 值，设备类型，开发者可以针对不同屏幕和设备写不同样式。如下示例：


```

/\* 方表和手机上生效 \*/
@media screen and (device: watch-square) or screen and (device: phone) {
  .box {
    background-color: red;
  }
}
```

复制代码
更多内容参考[媒体查询](/reference/configuration/style-sheet/#%E5%AA%92%E4%BD%93%E6%9F%A5%E8%AF%A2)


### 4.获取设备类型


在 template 或者 js 中，如果我们想差异性处理组件和逻辑，可以判断当前的设备类型。


如下示例，在布局中判断设备类型


```

<div>
  <header-of-square if="$device.deviceType == 'watch-square'">
  <header-of-round elif="$device.deviceType == 'watch-round'">
</div>
```

复制代码
$device 的详细文档异步[公共对象](/reference/configuration/script/#%E5%85%AC%E5%85%B1%E5%AF%B9%E8%B1%A1)


### 5. 资源管理


资源是与您的应用程序捆绑和部署的文件，它们可以在运行时被访问。常见的资源类型包括静态数据（例如 JSON 文件）、配置文件、以及各种格式的图标和图像（JPEG、WebP、GIF、动画 WebP/GIF、PNG、BMP 和 WBMP）。考虑到您的程序将在各种不同类型和屏幕分辨率的设备上运行，为了追求最佳的用户体验，您需要针对不同的场景、设备和分辨率匹配合适的资源。因此，这里提供了一套匹配规则，使得您的应用可以轻松地适配不同的设备状态。


在项目的根目录下的 `resources` 文件夹中，您可以根据需要创建 JSON 格式的配置文件。这些文件的命名规则为：前缀“res”开头，用连字符“-”连接，再根据需要添加限定词。默认的配置文件命名为 `res-defaults.json`。


```

├── resources
  │── res-pad.json
  │── res-watch.json
  └── res-defaults.json
```

复制代码
#### 5.1 resources 规则


1、res-watch-分辨率-手表形状-屏幕密度.json，短线连接的为限定词，限定词顺序为：分辨率 > 表盘形状 > 屏幕密度。


2、其中分辨率、手表形状和屏幕密度如无需要可以不用写


3、分辨率使用 宽 x 高的形式，x 为英文字母 X 的小写


4、 屏幕密度的枚举为：`ldpi`/`mdpi`/`hdpi`/`xhdpi`/`xxhdpi`/`xxxhdpi`


5、手表形状枚举值为：`square` 和 `round`


6、 默认资源名为：res-defaults.json


7、 资源的命中权重大小为：分辨率 (1000) > 表盘形状 (100) > 屏幕密度 (10)


为方便理解资源的生效顺序，我们可以假设下权重: 分辨率 = 1000, 表盘形状 = 100, 屏幕密度 = 10，以下权重越高则越会优先命中并生效。


```

// 匹配402x402，方形手表，屏幕密度120
// 权重：1110
res-watch-402x402-square-ldpi.json

// 匹配402x402，圆形手表
// 权重：1100
res-watch-402x402-round.json

// 匹配方形手表
// 权重：100
res-watch-square.json

// 匹配402x402的手表
// 权重：1000
res-watch-402x402.json

// 匹配手表密度为120dpi
// 权重：10
res-watch-ldpi.json

// 匹配手表
res-watch.json

// 匹配所有资源作为兜底
res-defaults.json
```

复制代码
#### 5.2 resources 配置


下面示例演示了如何配置 pad 和 watch 两种设备的资源的配置


```

// resources/res-pad.json
{
  "image": {
    "logo": "/common/pad/logo.png",
    "banner": "/common/pad/banner.png"
  },
  "colors": {
    "headerBackGround": "#ffffff"
  }
}
```

复制代码

```

// resources/res-watch.json
{
  "image": {
    "logo": "/common/watch/logo.png",
    "banner": "/common/watch/banner.png"
  },
  "colors": {
    "headerBackGround": "#fff000"
  }
}
```

复制代码
#### 5.3 $res 方法


配置完 resources 后就可以使用$res 在 template 和 script 中使用了


| 属性 | 类型 | 参数 | 描述 |
| --- | --- | --- | --- |
| $res | Function | path: String 资源路径 | 根据开发者配置的 resources 和当前系统的参数返回对应的资源 |


示例：


```

<template>
  <div style="background-color: {{ $res('colors.headerBackGround') }}">
    <image src="{{ $res('image.banner') }}"></image>
  </div>
</template>
<script>
 export default {
 onInit() {
 console.log(this.$res('image.banner'))
 },
 }
</script>
```

复制代码


---


<!-- 文档 17: tutorial/extend/resident/.md -->


## 后台运行

## 后台运行

更新时间：2025-05-16 10:47:50


### 概述


为了节省系统资源，通常情况下，应用切换到后台后将会暂停运行，等到再次切换回前台时继续运行。但音乐/运动等类型的应用， 退到后台后可能仍然需要继续运行，为满足此类需求，加入了对后台运行的支持。


#### 后台运行模式的工作原理如下:


在应用切换到后台时，系统将会检查是否满足后台运行的条件，如果满足，应用将继续运行，否则将被暂停。此条件包括：


- manifest.json 中声明了后台运行接口
- 当前至少有一个（已在 manifest.json 中声明的）后台运行接口正在运行


处于后台运行中的应用，如果所有后台运行接口均运行结束，系统将会启动倒计时。倒计时结束后，如果仍未有后台运行接口被调用， 应用将会退出后台运行模式，暂停运行。


#### 实践建议:


- 后台运行需要消耗较多的系统资源，应用需要根据自身需求审慎使用。针对申请后台运行的应用，上线审核时将会审核其后台运行的需求是否合理。
- 后台运行接口的导入和后台执行的工作放到 app.ux 中，而不是放到页面中，以免避免页面切换和销毁的影响。


#### 配置方法


manifest.json 中声明所需的后台运行接口。后台运行接口及后台运行条件包括：


| 模块 | 后台运行条件 |
| --- | --- |
| blueos.multimedia.audio | 音频播放 |
| blueos.multimedia.record | 录音 |
| blueos.multimedia.media | 音频播放/录音 |
| blueos.communication.network.request | 上传下载 |
| blueos.hardware.geolocation | 定位 |
| blueos.bluetooth.ble | 蓝牙连接 |


**使用示例：**


```

{
  "package": "com.demo.sample",
  "config": {
    "logLevel": "trace",
    "background": {
      "features": [
        "blueos.multimedia.audio",
        "blueos.multimedia.media",
        "blueos.multimedia.record",
        "blueos.communication.network.request",
        "blueos.hardware.geolocation"
      ]
    }
  }
}
```

复制代码


---


<!-- 文档 18: tutorial/extend/watchface/.md -->


## 表盘

## 表盘

更新时间：2025-10-09 11:25:10


### 概述


表盘指默认开机首屏的界面，可分为指针表盘和数字表盘，除了查看时间，表盘还可以给用户提供展示计步、心率、电量、天气等关键信息。


系统会内置一些表盘，同时也支持第三方开发，用户可以根据喜好通过长按切换选择表盘。


### 表盘项目结构


一个表盘项目包含：描述项目配置信息的[manifest 文件](/reference/configuration/manifest)，一个描述表盘界面的[ux 文件](/reference/configuration/ux-file)，以及引用的图片资源文件，典型示例如下：


应用根目录


```

.
├── README.md
├── package.json
├── sign
│   ├── certificate.pem
│   └── private.pem
└── src
    ├── app.ux
    ├── manifest.json
    └── watch3000
        ├── assets
        │   ├── aaa.png
        │   └── bg.png
        ├── edit.ux
        └── index.ux
```

复制代码
### manifest 文件


manifest.json 文件中包含了表盘信息描述、接口声明等


#### manifest


| 属性 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| package | String | - | 是 | 表盘包名，**确认与原生应用的包名不一致**，包名须保证唯一，推荐采用 com.company.watch 的格式，如：com.company.watch.demo |
| versionName | String | - | 否 | 表盘版本名称，如：`"1.0"` |
| versionCode | Integer | - | 是 | 表盘版本号，从`1`自增，**推荐每次重新上传包时`versionCode`+1** |
| config | Object | - | 是 | 系统配置信息，详见下面说明 |
| router | Object | - | 是 | 路由信息，详见下面说明 |
| deviceTypeList | Array<String> | watch | 否 | 可选值有：`watch`, `watch-square`, `watch-round`, `tv` , `car`, `phone` |
| customData | Record<string, string> | - | 否 | 开发者自定义字段，限定不超过 30 个字符，可通过 `packageManager.getCustomData()`方法读取 |


#### config


用于定义系统配置和全局数据。


| 属性 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| designWidth | Integer | 466 | 页面设计基准宽度，根据实际设备宽度来缩放元素大小 |


#### router


用于定义页面的组成和相关配置信息，如果页面没有配置路由信息，则在编译打包时跳过。


| 属性 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| watchfaces | Object | - | 是 | 页面配置列表，key 值为表盘目录（命名为**watch+表盘 id**，对应表盘目录名，例如表盘 id 为 3000，则 key 为 `watch3000`， 对应 `watch3000` 目录），value 为该表盘详细配置 ，详见下面说明 |


##### router.watchfaces[watchPath]


用于定义单个表盘页面信息。


| 属性 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | Integer | - | 是 | 表盘唯一标识，由服务端生成 |
| name | String | - | 是 | 表盘名称，用于在表盘商店、切换选择等显示的名称 |
| component | String | - | 是 | 表盘对应组件名，与 ux 文件名保持一致，例如'index' 对应 'index.ux' |
| edit | String | '' | 否 | 为空字符串 `''` 时，表盘为不可编辑表盘；为非空字符串值时，代表表盘目录下编辑表盘页面的路由名称 |
| features | Array | - | 否 | 表盘用到的 features 全部在此配置，注意与蓝河应用的配置区别 |
| params | Object | - | 是 | 表盘参数，详见下面说明 |


###### params


表盘特有参数，用于表盘框架加载表盘和展示列表。


| 属性 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| previewImage | [String] | - | 是 | 字符串数组，数组每一项代表预览图片路径，用于在表盘商店、切换选择等显示的预览图，预览图片的路径格式为：`local://包名/path` |
| hpw | Integer | - | 否 | 高功耗提醒，0-无高功耗提醒，1-需要高功耗提醒，默认为 0 |


示例:


```

{
  "package": "com.vivo.watch.sample",
  "versionName": "1.0.0",
  "versionCode": 1,
  "config": {
    "designWidth": 466
  },
  "router": {
    "watchfaces": {
      "watch3000": {
        "id": 3000,
        "name": "表盘示例",
        "component": "index",
        "edit": "edit",
        "features": [
          {
            "name": "blueos.app.router"
          }
        ],
        "params": {
          "previewImage": ["assets/aaa.png"],
          "hpw": 0
        }
      }
    }
  },
  "customData": { "key1": "value1", "key2": "value2" }
}
```

复制代码
### ux 文件


index.ux 文件中包含了表盘界面描述、样式定义和业务逻辑代码，最终会编译为 js 文件，在运行时中以挂件组件的形式进行加载


#### 生命周期


##### onInit


监听表盘初始化。当表盘数据完成初始化时调用，只触发一次


##### onReady


监听表盘界面创建完成。当表盘界面完成创建可以显示时触发，只触发一次


##### onDestroy


监听表盘退出。当表盘即将退出销毁时触发


##### onShow()


监听表盘返回前台,表盘返回前台时调用


##### onHide()


监听表盘退到后台,表盘退到后台时调用


```

<template>
  <div class="wrap">
    <!-- 表盘界面 -->
  </div>
</template>
<script>
 // 业务逻辑代码
 export default {
 // 初始化数据
 data() {
 return {}
 },
 // 生命周期
 onInit() {},
 onShow() {},
 onHide() {}
 // 自定义方法
 refreshTime() {}
 }
</script>
<style>
 /\* 样式描述 \*/
</style>
```

复制代码


---


<!-- 文档 19: tutorial/extend/widget/.md -->


## 快捷卡片

## 快捷卡片

更新时间：2025-10-09 11:25:10


> 
> ⚠ 快捷卡片已经弃用，请使用 [智慧服务卡片](/reference/widget/overview/)
> 
> 
> 


#### 概述


快捷卡片是应用的特殊页面，配置为快捷卡片的页面可以被其他宿主应用作为组件引入。此特性可以使得其能跟随主应用更新，而宿主应用无需更新。


一个应用可以配置多个快捷卡片，一个快捷卡片也可以被多个宿主应用所引用。


#### manifest.json 文件


快捷卡片在 manifest.json 中的 widgets 对象里进行定义，参考下面定义简例：


```

{
  "package": "com.example.demo",
  "router": {
    "entry": "pages/Home",
    "pages": {
      "pages/Home": {
        "component": "index"
      },
      "pages/Music": {
        "component": "index"
      }
    },
    // 快捷卡片定义
    "widgets": {
      // 音乐快捷卡片
      "pages/Music": {
        "id": "music2008",
        // 快捷卡片名（必填）
        "name": "音乐服务",
        // 快捷卡片组件名（必填）
        "component": "index",
        // 可编辑路径
        "params": {
          // 快捷卡片缩略图 (必填)
          "previewImage": ["./music.png"],
          "hpw": 0
        }
      }
    }
  }
}
```

复制代码
##### router.widgets[widgetPath]


用于定义单个快捷卡片页面信息。


| 属性 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | Integer | - | 是 | 快捷卡片唯一标识 |
| name | String | - | 是 | 快捷卡片中文名称，用于在切换选择等显示的名称 |
| component | String | - | 是 | 表盘对应组件名，与 ux 文件名保持一致，例如'index' 对应 'index.ux' |
| params | Object | - | 是 | 快捷卡片参数，详见下面说明 |


##### params


快捷卡片特有参数，用于快捷卡片框架加载快捷卡片和展示列表。


| 属性 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| previewImage | String | - | 是 | 字符串数组，数组每一项代表预览图片路径，用于在快捷卡片商店、切换选择等显示的预览图 |
| hpw | Integer | - | 否 | 高功耗提醒，0-无高功耗提醒，1-需要高功耗提醒，默认为 0 |


#### 快捷卡片生命周期


1、宿主页面的生命周期触发，同时也会触发快捷卡片的生命周期。


2、对快捷卡片使用`if指令`移除时会触发`onDestroy`, `if指令`再显示等同于重新创建。


3、对快捷卡片使用`show指令`控制显示隐藏时会触发`onShow`和`onHide`。


#### 注意


快捷卡片为单页面操作，不能使用路由跳转


---


<!-- 文档 20: tutorial/perf-guide/overview/.md -->


## 概述

## 概述

更新时间：2025-04-28 19:30:44


### 1 前言


本章节聚焦手表应用的性能优化，结合可穿戴设备资源受限、低功耗需求和小屏幕交互特点，提出切实可行的优化策略。我们将重点关注电池续航、显示功耗和交互流畅度，帮助开发者在蓝河应用框架下构建高效、稳定的智能穿戴产品。


### 2 使用说明


文中示例提供了「正例」和「反例」，便于读者直观对比两种方案的优劣，迅速掌握规范要点。示例仅供说明，不代表可直接运行的完整项目代码。


### 3 推荐级别


【强烈】必须遵守的核心规范


【建议】除特殊场景外应优先采用的最佳实践


【鼓励】可选但有助于提升体验的优化手段


### 4 章节指引


在深入阅读各章节前，您可参照下表快速定位所需内容：


| 章节 | 说明 |
| --- | --- |
| 响应式数据优化 | 针对响应式声明与使用进行精简与性能调优 |
| 减少代码体积 | 利用 Tree-shaking、按需加载等技术精简打包体积 |
| 减少初始化开销 | 通过 app.ux 优化和长页面分段渲染，提升首屏加载速度 |
| 运行时性能优化 | 优化模板结构与指令组合，降低运行时计算开销 |
| 避免高耗性能操作 | 规避常见高耗操作，提升应用响应与功耗效率 |
| 退出页面释放监听 | 规范页面销毁时的资源清理流程，防止内存泄漏 |
| 图片资源优化 | 合理选择与加载图片资源，提高渲染效率并压缩安装包大小 |
| 长列表性能优化 | 针对大规模列表渲染场景的方案 |
| 帧率优化指引 | 提升动画与滚动流畅度的实用方法 |


---


<!-- 文档 21: tutorial/perf-guide/perf-dangerous/.md -->


## 避免高耗性能操作

## 避免高耗性能操作

更新时间：2025-04-27 09:58:15


在蓝河应用开发中，需特别注意以下高消耗性能操作，合理规避可显著提升渲染效率与运行时性能。


### 避免使用后代选择器


**推荐级别：强烈**


后代选择器在传统 Web 开发中能有效规避样式污染，但蓝河应用的页面与组件采用**天然样式隔离机制**，嵌套选择器会触发冗余的样式计算，导致渲染性能下降。


直接使用类名选择器，避免多级嵌套结构。


**反例**


```

.list .item {
  color: red;
}
```

复制代码
**正例**


```

.item {
  color: red;
}
```

复制代码
### 精简打印日志


**推荐级别：强烈**


高频次、冗余的日志输出会引发以下问题：


1. 增加运行时内存开销
2. 干扰开发者调试关键信息


**优化方案**


- 仅记录核心调试信息
- 避免全量序列化复杂对象


**反例**


```

/\* 反例：全量序列化大对象产生性能损耗 \*/
console.log(`sportInfo = ${JSON.stringify(sportInfo)}`)
```

复制代码
**正例**


```

/\* 正例：选择性输出关键字段 \*/
console.log(`运动ID: ${sportInfo.id}, 类型: ${sportInfo.type}`)
```

复制代码
### 避免后台渲染指令堆积


常驻后台的应用频繁更新 UI 会导致：


1. 渲染指令队列堆积
2. 内存占用持续增长
3. 应用恢复前台时出现 UI 抖动


**优化方案**


- 使用状态标志位控制渲染时机
- 结合生命周期管理数据更新


```

// 临时变量暂存后台刷新数据
let tempData
export default {
  data: {
    bgData: [1, 2],
    showing: false,
  },
  onInit() {
    const evtId = event.subscribe({
      eventName: 'new\_data',
      callback: (res) => {
        if (!this.showing) {
          tempData = res.data
        } else {
          this.bgData = res.data
        }
      },
    })
  },
  onShow() {
    this.showing = true
    if (tempData) {
      this.bgData = tempData
    }
  },
  onHide() {
    this.showing = false
  },
}
```

复制代码


---


<!-- 文档 22: tutorial/perf-guide/perf-data/.md -->


## 响应式数据优化

## 响应式数据优化

更新时间：2025-04-27 11:06:02


蓝河框架基于 Proxy 实现响应式追踪机制，data 对象中的每个属性都会创建监听代理。优化数据层可显著降低内存消耗，提升渲染速度。


### 消除冗余响应式数据


**推荐级别：强烈**


未使用的响应式数据仍会触发依赖收集，导致内存占用增加。


**优化方案**


- 采用普遍变量声明非响应式数据


**反例 1**


```

<template>
  <text>{{a}}</text>
</template>

<script>
 export default {
 data: {
 a: 'hello',
 b: 'world',
 },
 onInit() {
 this.a = this.a + this.b
 },
 }
</script>
```

复制代码
**正例 1**


```

<template>
  <text>{{a}}</text>
</template>

<script>
 const b = 'world'
 export default {
 data: {
 a: 'hello',
 },
 onInit() {
 this.a = this.a + b
 },
 }
</script>
```

复制代码
**反例 2**


```

<template>
  <list>
    <list-item for="{{list}}">
      <text>{{ $item.name }}</text>
      <image src="{{ $item.icon }}"></image>
    </list-item>
  </list>
</template>

<script>
 const getSportsList = () => {
 return [
 {
 name: 'Football',
 description: 'A team sport played with ...',
 category: 'Team Sports',
 icon: 'football.png',
 },
 {
 name: 'Basketball',
 description: 'A team sport in which two teams, ...',
 category: 'Team Sports',
 icon: 'basketball.png',
 },
 {
 name: 'Tennis',
 description: 'A racket sport that can be ...',
 category: 'Individual Sports',
 icon: 'tennis.png',
 },
 ]
 }
 export default {
 data: {
 sports: [],
 },
 onInit() {
 this.sports = getSportsList()
 },
 }
</script>
```

复制代码
**正例 2**


```

<template>
  <list>
    <list-item for="{{list}}">
      <text>{{ $item.name }}</text>
      <image src="{{ $item.icon }}"></image>
    </list-item>
  </list>
</template>

<script>
 const getSportsList = () => {
 return [
 {
 name: 'Football',
 description: 'A team sport played with ...',
 category: 'Team Sports',
 icon: 'football.png',
 },
 {
 name: 'Basketball',
 description: 'A team sport in which two teams, ...',
 category: 'Team Sports',
 icon: 'basketball.png',
 },
 {
 name: 'Tennis',
 description: 'A racket sport that can be ...',
 category: 'Individual Sports',
 icon: 'tennis.png',
 },
 ]
 }
 export default {
 data: {
 sports: [],
 },
 onInit() {
 this.sports = getSportsList().map((item) => ({
 name: item.name,
 icon: item.icon,
 }))
 },
 }
</script>
```

复制代码
### 静态属性访问规范


**推荐级别：强烈**


**编译优化:** 动态属性访问会导致，阻碍编译时的优化分析。


**反例**


```

<template>
  <div>
    <text>{{person.name}}</text>
    <text>{{person.location}}</text>
  </div>
</template>

<script>
 export default {
 data: {
 person: {
 name: 'Vance',
 location: 'shenzhen',
 },
 },
 onInit() {
 const location = 'location'
 this.person[location] = 'beijing'
 },
 }
</script>
```

复制代码
**正例**


```

<template>
  <div>
    <text>{{person.name}}</text>
    <text>{{person.location}}</text>
  </div>
</template>

<script>
 export default {
 data: {
 person: {
 name: 'Vance',
 location: 'shenzhen',
 },
 },
 onInit() {
 this.person.location = 'beijing'
 },
 }
</script>
```

复制代码
### 数据结构层级优化


**推荐级别：鼓励**


对于动态绑定的数据，不宜嵌套层级过深，建议不超过 3 层。


**反例**


```

<template>
  <div>
    <text>{{obj.a.name}}</text>
    <text>{{obj.b.name}}</text>
  </div>
</template>

<script>
 export default {
 data: {
 obj: {
 a: {
 name: 'name a',
 },
 b: {
 name: 'name b',
 },
 },
 },
 }
</script>
```

复制代码
**正例**


```

<template>
  <div>
    <text>{{obj.a}}</text>
    <text>{{obj.b}}</text>
  </div>
</template>

<script>
 export default {
 data: {
 obj: {
 a: 'name a',
 b: 'name b',
 },
 },
 }
</script>
```

复制代码


---


<!-- 文档 23: tutorial/perf-guide/perf-frame-rate/.md -->


## 帧率优化指引

## 帧率优化指引

更新时间：2025-04-25 20:12:10


本节介绍提升帧率的有效方法。


### 避免冗余背景声明


- 如背景色为黑色，则不需要另外设置黑色（默认背景色为黑色）
- 如父容器已经有背景颜色，则不需要单独给页面的容器设置一样的背景色


### 给 div 组件设置宽高


- 横向布局至少设置高度
- 纵向布局至少设置宽度


### 使用图片的原始尺寸


- image 组件上的宽高使用图片的原始尺寸
- background-image 上使用图片的原始尺寸


---


<!-- 文档 24: tutorial/perf-guide/perf-init/.md -->


## 减少初始化开销

## 减少初始化开销

更新时间：2025-04-28 19:30:44


应用初始化阶段的代码复杂度直接影响应用/页面实例的创建耗时，优化该阶段的执行效率能显著改善首屏渲染性能。


### 避免引入耗时自执行模块


**推荐级别：强烈**


模块中的自执行逻辑会在导入时立即执行，导致页面加载阻塞。应将初始化逻辑移至生命周期钩子中按需执行。


**反例**


```

// init.js 中的自执行逻辑会立即执行，延长加载时间
import './init.js' // 包含立即执行的复杂初始化逻辑
export default {}
```

复制代码
**正例**


```

export default {
  onInit() {
    // 将初始化逻辑移至生命周期钩子中按需执行
    this.performInitialization()
  },
  performInitialization() {
    // 具体的初始化操作
  },
}
```

复制代码
### 优化 app.ux 数据管理


**推荐级别：建议**


过度加载的全局数据会延长应用启动时间，建议遵循以下原则：


1. 仅将全局共享状态存储在 app.ux
2. 工具类方法按需在各页面独立引入


**反例**


```

// app.ux
import utils from './utils' // 引入可能包含复杂逻辑的工具库

export default {
  utils, // 全局挂载非必要工具方法
  // ...其他全局配置
}
```

复制代码
### 长页面分段加载


**推荐级别：建议**


对复杂长页面实施分阶段加载策略：


1. 首屏优先加载关键数据/视图
2. 可视区域外内容延迟加载


**正例 1**


```

<template>
  <div>
    <div for="{{visibleItems}}">
      <text>{{$item}}</text>
    </div>
  </div>
</template>
<script>
 const fullDataset = [.../\* 完整数据集 \*/]
 export default {
 data: {
 visibleItems: [],
 },
 onInit() {
 // 首屏加载前6条
 this.visibleItems = fullDataset.slice(0, 6)
 },
 onShow() {
 // onShow 后显示所有数据
 this.visibleItems = fullDataset
 },
 }
</script>
```

复制代码
**正例 2**


```

<template>
  <div>
    <!-- 首屏核心模块 -->
    <critical-module />

    <!-- 次要模块延迟加载 -->
    <secondary-module if="{{isSecondaryLoaded}}" />
  </div>
</template>
<script>
 export default {
 data: {
 isSecondaryLoaded: false,
 },
 onShow() {
 // 首屏渲染完成后加载次要模块
 this.isSecondaryLoaded = true
 },
 }
</script>
```

复制代码


---


<!-- 文档 25: tutorial/perf-guide/perf-longlist/.md -->


## 长列表性能优化

## 长列表性能优化

更新时间：2025-10-09 11:25:10


本文阐述了长列表场景下的性能优化方案，在开发过程中遇到长列表性能问题时，可参考下面优化方案。


### 分离固定标题与列表容器


当`<list>`组件滚动时，内部元素复杂度直接影响滚动性能。建议将固定标题等静态元素移出列表容器，采用绝对定位等方式处理。


**推荐级别：强烈**


**反例**


标题内嵌于列表容器，影响滚动性能：


```

<template>
  <list title="true">
    <list-item type="title">
      <vw-title value="蔬菜列表" is-fixed="true"></vw-title>
    </list-item>
    <!-- 列表内容 -->
  </list>
</template>
```

复制代码
**正例**


通过外层容器实现布局分离：


```

<template>
  <div class="list-container">
    <vw-title value="蔬菜列表" is-fixed="true"></vw-title>
    <list>
      <!-- 列表内容 -->
    </list>
  </div>
</template>
```

复制代码
### 避免模板内表达式


模板中的复杂表达式会频繁触发 JS 引擎执行，建议通过数据预处理替代模板运算。


**推荐级别：强烈**


**反例**


模板中使用条件表达式：


```

<div for="{{foodList}}">
  <text>{{$item.vegetarian ? 'Vegetarian' : 'Non-Vegetarian'}}</text>
</div>
```

复制代码
**正例**


预处理数据格式：


```

// Script部分
data: {
  foodList: foodList.map((item) => ({
    ...item,
    vegetarianStatus: item.vegetarian ? 'Vegetarian' : 'Non-Vegetarian',
  }))
}
```

复制代码
### 规避列表循环中的自定义组件


**推荐级别：强烈**


列表项内使用自定义组件会创建大量 vm 实例，建议优先使用原生组件。


### 保持列表数据独立性


**推荐级别：强烈**


确保列表项仅依赖自身数据，避免引入外部响应式变量。


**反例**


依赖外部变量：


```

<div for="{{list}}">
  <text class="{{$item.num > count ? 'red' : 'blue'}}">{{$item.num}}</text>
</div>
```

复制代码
**正例**


预处理样式状态：


```

// 预处理时添加状态字段
list.map((item) => ({
  ...item,
  className: item.num > threshold ? 'red' : 'blue',
}))
```

复制代码
### 分段懒加载实现


**推荐级别：强烈**


结合滚动监听实现动态加载，分页大小控制在一屏可见就可以。


**正例**


```

let currentPage = 0;

async loadMore() {
  const newData = await fetchPageData(++currentPage);
  this.list = this.list.push(...newData);
}
```

复制代码
### 关注 onInit 的执行时间


**推荐级别：建议**


使用性能分析工具监控关键生命周期。


---


<!-- 文档 26: tutorial/perf-guide/perf-memory-leak/.md -->


## js 内存泄漏排查

## js 内存泄漏排查

更新时间：2025-05-20 10:54:23


在需要排查的场景先后进行两次 dump, 比如排查页面泄漏，在进入页面前 dump 一次，进入页面退出后再 dump 一次


导出泄漏可以分为两种情况


- 如果应用不需要底层能力支撑


比如不需要 `blueos.multimedia.audio`这些底层能力，可以直接在 BlueOS Studio 测试，在下图场景前后分别点击 `位置 4` 进行 dump
- 如果应用需要底层能力支持


​ 先安装具有能 dump js heap 的固件， `dump_js_heap /sdcard` , 然后拷贝到主机，来到 BlueOS Studio 的面板进行 `位置3`加载


下图为 js heap 分析和导出的在 BlueOS Studio 中位置`Devtool->Snapshot->Profile`


![sample_eg25](/9e5f013430e1f98818f8fc0642438567/sample_eg25.png)


### 分析泄漏


比如我们构造一个常见的泄漏，event 订阅了但没有取消 （npm 类库 [[eventEmitter3]](https://www.npmjs.com/package/eventemitter3)有类似的问题）


```

  import event from '@blueos.app.event'
  onReady() {
    const that = this
    const evtId = event.subscribe({
      eventName: 'myEventName',
      callback: function MyEvent(res) {
        console.log(res.params)
        that.hello()
      },
    })
```

复制代码
进入退出页面后，导出两份 snapshot，选中第二份 snapshot (标号 1), 在 `标号2` 处切换到 `comparison`试图，然后重点关注`标号3`的 Delta 部分， 增量即为泄漏


可以重点关注以下对象


- App, 每个应用有一个，如果新增，代表应用泄漏
- Page，对应一个页面或者表盘，有新增代表相关泄漏
- Vm，每个 Page 和自定义组件对应一个 Vm，List 的每个 Item 不触发 JIT 的情况也会有
- 自己 Page 中特有的对象和函数


![sample_eg26](/185e981127f6e4db7302928df73b0d86/sample_eg26.png)


#### 其他说明


- 标号 4 `_valid` 可以 Page 是否泄漏
- 标号 5 内容不为空（有右箭头），说明有 timer 泄漏


这个格式其实是 chrome 的 devtools 的标准格式


---


<!-- 文档 27: tutorial/perf-guide/perf-runtime/.md -->


## 运行时性能优化

## 运行时性能优化

更新时间：2025-04-27 11:06:02


本节提供的关键优化手段可显著提升页面渲染与更新效率。


### 避免在 CSS 中使用 ID 选择器


**推荐级别：强烈**


如果只需要在 css 中给组件添加样式，建议使用 class 选择器，只有需要使用 js 操作组件时，才会给组件注册 ID。


**反例 1**


```

<!-- 错误：在CSS中通过ID定义样式 -->
<template>
  <div id="red"></div>
</template>
<style>
 #red {
 color: red;
 } /\* 存在选择器性能损耗 \*/
</style>
```

复制代码
**正例 1**


```

<!-- 正确：使用class类选择器 -->
<template>
  <div class="red"></div>
</template>
<style>
 .red {
 color: red;
 } /\* 高效样式定义方式 \*/
</style>
```

复制代码
**特殊场景说明**


```

<!-- 当元素需被JS操作时保留id -->
<template>
  <!-- ID用于JS交互 -->
  <div id="root"></div>
</template>
<script>
 export default {
 onInit() {
 this.$element('root').animate() // 通过ID获取元素
 },
 }
</script>
```

复制代码
### 避免循环指令与条件指令叠加使用


**推荐级别：建议**


若需在循环渲染时进行条件过滤，建议在 JavaScript 中预处理数据，而非在模板层混合`for`与`if`指令。此优化可减少模板解析复杂度，避免重复渲染计算。


**反例**


```

<!-- 低效：模板中混合循环与条件判断 -->
<div for="{{foodList}}" if="{{$item.vegetarian}}">
  <text>{{$item.name}}</text>
  <text>{{$item.category}}</text>
</div>
```

复制代码
**正例**


```

<!-- 高效：数据层预过滤 -->
<!-- 直接渲染已过滤数据 -->
<div for="{{vegetarianFoods}}">
  <text>{{$item.name}}</text>
  <text>{{$item.category}}</text>
</div>
```

复制代码

```

export default {
  data: { vegetarianFoods: [] },
  onInit() {
    this.vegetarianFoods = foodList.filter((food) => food.vegetarian)
  },
}
```

复制代码
### 合理选择条件指令


**推荐级别：建议**


`if`与`show`指令的本质差异在于 DOM 树操作机制：


- `if`指令：触发组件级 DOM 树动态构建/销毁，适合低频次状态变更场景
- `show`指令：通过 CSS display 属性控制可视性，DOM 结构保持稳定，适用于高频次显隐切换场景


最佳实践原则：


- 首屏不可见但需快速激活 → `if`指令（降低初始化开销）
- 高频交互元素（如 Tab 切换） → `show`指令（减少 DOM 操作损耗）


**反例 1**


```

<!-- show指令导致隐藏元素参与首屏渲染，破坏分段加载设计 -->
<template>
  <div>
    <div>首屏核心模块</div>
    <div show="{{display}}">延迟加载模块</div>
  </div>
</template>
<script>
 export default {
 data: { display: false },
 onShow() {
 this.display = true // 触发CSS样式变更而非DOM操作
 },
 }
</script>
```

复制代码
**正例 1**


```

<template>
  <div>
    <div>首屏核心模块</div>
    <div if="{{display}}">动态加载模块</div>
  </div>
</template>
<script>
 export default {
 data: { display: false },
 onShow() {
 this.display = true // 触发DOM树动态构建
 },
 }
</script>
```

复制代码
**反例 2**


```

<!-- if指令导致高频DOM重建，引发布局抖动 -->
<template>
  <div>
    <text @click="changeView('A')">视图A</text>
    <text @click="changeView('B')">视图B</text>
    <div if="{{viewState == 'A'}">视图内容A</div>
    <div elif="{{viewState == 'B'}">视图内容B</div>
  </div>
</template>
```

复制代码
**正例 2**


```

<template>
  <div>
    <text @click="changeView('A')">视图A</text>
    <text @click="changeView('B')">视图B</text>
    <div show="{{viewState == 'A'}">视图内容A</div>
    <div show="{{viewState == 'B'}">视图内容B</div>
  </div>
</template>
```

复制代码
### 组件层级精简


**推荐级别：建议**


在页面布局中，尽量减少组件的嵌套，如 `list-item` 本身可以作为容器，不需在其内部要额外的 div 嵌套。


**反例**


冗余嵌套结构


```

<template>
  <list>
    <list-item>
      <!-- 冗余包装容器 -->
      <div>
        <text>数据项标题</text>
        <image src="item.png"></image>
      </div>
    </list-item>
  </list>
</template>
```

复制代码
**正例**


扁平化结构


```

<template>
  <list>
    <list-item>
      <text>数据项标题</text>
      <image src="item.png"></image>
    </list-item>
  </list>
</template>
```

复制代码
### 组件抽象平衡法则


**推荐级别：鼓励**


组件化需遵循以下原则：


1. 单一页面自定义组件数 ≤ 3
2. 简单元素组合（≤3 个基础组件）不建议抽象


**反例** 1


过度抽象


```

<!-- 简单统计模块被过度拆分为独立组件 -->
<import src="./components/heartRateBlock.ux" name="heartRate"></import>
<import src="./components/calorieBlock.ux" name="calorie"></import>
```

复制代码
**反例** 2


抽象组件滥用


```

<!-- 独立心率数字展示无需组件化 -->
<import src="./components/heartRate.ux"></import>
<template>
  <heartRate></heartRate>
</template>
```

复制代码
### 页面职责单一化原则


**推荐级别：鼓励**


工程化实践要求：


1. 功能模块隔离：独立业务状态使用独立页面承载
2. 路由参数规范：仅传递必要标识参数，避免状态注入
3. 页面体积控制：单文件源码 ≤ 1000 行（编译前）


**反例**


```

<template>
  <!-- 多态视图混合实例 -->
  <div if="{{status === 1}}">
    <div>视图模块A</div>
    <!-- 50+ 相关节点 -->
  </div>
  <div if="{{status === 2}}">
    <div>视图模块B</div>
    <!-- 30+ 相关节点 -->
  </div>
</template>

<script>
 export default {
 data: {
 status: 1, // 状态维护成本随功能增加而上升
 },
 }
</script>
```

复制代码
**正例**


采用路由级组件拆分：


```

<!-- modules/module-a.ux -->
<template>
  <div class="optimized-view">
    <div>独立视图模块A</div>
    <!-- 功能隔离的节点树 -->
  </div>
</template>

<!-- modules/module-b.ux -->
<template>
  <div class="optimized-view">
    <div>独立视图模块B</div>
    <!-- 精简的独立节点树 -->
  </div>
</template>
```

复制代码
### 指定列表渲染标识


**推荐级别：鼓励**


在动态列表场景中，通过`tid`属性指定唯一性标识，确保 Diff 算法准确执行节点复用。


**实施要点**


1. 使用业务主键而非数组索引
2. 确保`tid`值的全局唯一性


**正例**


```

<template>
  <!-- 使用唯一业务标识 -->
  <text for="{{athleteList}}" tid="athleteId" class="sport-item">
    {{$item.rank}} {{$item.name}}
  </text>
</template>

<script>
 export default {
 data: {
 athleteList: [
 { athleteId: 1001, rank: '金牌', name: '张三' },
 { athleteId: 1002, rank: '银牌', name: '李四' },
 ],
 },
 }
</script>
```

复制代码


---


<!-- 文档 28: tutorial/perf-guide/perf-src/.md -->


## 图片资源优化

## 图片资源优化

更新时间：2025-04-27 11:06:02


本章为 UI 设计师提供界面资源设计规范，通过科学管理图片资源降低内存占用、提升渲染性能、优化安装包体积，适用于设计阶段至开发交付全流程。


### 图片尺寸适配原则


**推荐级别：强烈**


图片物理尺寸必须与目标显示区域像素尺寸严格匹配，禁止使用超分辨率图片。大尺寸图片会导致内存占用激增，同时增加 GPU 渲染管线压力。


### 8 位色深资源优先


**推荐级别：建议**


智能手表等穿戴设备屏幕色域有限，建议采用 8 位色深（256 色）PNG 格式：


- 通常可以提供足够的颜色范围
- 有助于减少的存储空间
- 支持透明度通道且无画质损失


### png 图片替代 svg 图片


**推荐级别：建议**


svg 只在有动画或动态修改属性等特殊场景时使用，一般情况下都使用 png 格式图片资源


**反例**


```

<image src="/assets/images/logo.svg"></image>
```

复制代码
**正例**


```

<image src="/assets/images/logo.png"></image>
```

复制代码
### 删除冗余图片


**推荐级别：建议**


如果图片已经用不到了，需要及时的在项目中删除，否则冗余的图片会使得包体积增加。


### 资源复用体系


**推荐级别：鼓励**


设计的图片尽量实现共用，来减少存储占用。比如：确定、取消、返回、选中、未选中等使用频繁的按钮。


---


<!-- 文档 29: tutorial/perf-guide/perf-subscription/.md -->


## 退出页面释放监听

## 退出页面释放监听

更新时间：2025-04-27 09:58:15


在蓝河应用开发中，正确处理页面生命周期末端的资源释放是保障应用性能的关键。以下规范针对页面销毁阶段（onDestroy）必须执行的三类资源清理操作。


### 定时器资源释放


**推荐级别：强烈**


所有通过 `setTimeout`/`setInterval` 创建的计时器，必须在页面销毁时通过 `clearTimeout`/`clearInterval` 进行匹配清除。


**反例**


```

export default {
  onInit() {
    // 未记录定时器引用
    setTimeout(() => {
      // 业务逻辑
    }, 1000)
    setInterval(() => {
      // 周期任务
    }, 1000)
  },
  onDestroy() {}, // 未执行清理
}
```

复制代码
**正例**


```

// 声明模块级变量存储计时器ID
let timeoutId
let intervalId

export default {
  onInit() {
    timeoutId = setTimeout(() => {
      // 业务逻辑
    }, 1000)

    intervalId = setInterval(() => {
      // 周期任务
    }, 1000)
  },

  onDestroy() {
    // 精确清除计时器
    clearTimeout(timeoutId)
    clearInterval(intervalId)
  },
}
```

复制代码
### 事件监听器注销


**推荐级别：强烈**


页面中使用的监听类接口(如 feature、C2JS 等)，页面退出时必须清除监听。原因同上。


**反例**


```

import event from '@blueos.app.event.eventManager'

export default {
  onInit() {
    // 未记录订阅ID
    event.subscribe({
      eventName: 'usual.event.SCREEN\_AOD',
      callback: (res) => {
        // 事件处理
      },
    })
  },
  onDestroy() {}, // 监听器未注销
}
```

复制代码
**正例**


```

import event from '@blueos.app.event.eventManager'

// 使用容器存储多订阅ID
const eventSubscriptions = []

export default {
  onInit() {
    const subscriptionId = event.subscribe({
      eventName: 'usual.event.SCREEN\_AOD',
      callback: (res) => {
        // 事件处理
      },
    })
    eventSubscriptions.push(subscriptionId)
  },

  onDestroy() {
    // 批量注销所有事件监听
    eventSubscriptions.forEach((id) => event.unsubscribe({ id }))
    eventSubscriptions.length = 0 // 清空ID容器
  },
}
```

复制代码


---


<!-- 文档 30: tutorial/perf-guide/perf-treeshaking/.md -->


## 减少代码体积

## 减少代码体积

更新时间：2025-04-27 09:58:15


本节非常重要，优劣不同的写法会有明显的代码体积差异，而代码体积越小，会获得更快的加载速度。


### js 封装要支持 Treeshaking


**推荐级别：强烈**


统一支持 Treeshaking 是非常重要的，因为它可以在打包编译时移除未使用的代码，减小输出的文件大小。


在进行 JavaScript 封装时，请牢记以下两点：


- 在能使用函数实现的情况下，优先使用函数而非 class 或 Object。只有需要频繁创建实例的情况才需要考虑使用 class。
- 慎重使用 export default 导出。如果你的模块有多个导出，可以考虑逐个导出而非使用 default 导出，这样可以更好地遵循 Treeshaking 的原则，因为 default 导出整个模块会被引入，而逐个导出只会引入需要的部分。


**反例 1**


对象捆绑导出


```

const a = 1
const b = () => {}
// 未使用的变量仍会被打包
export default { a, b }
```

复制代码
**反例 2**


class 方法捆绑


```

// 即使只使用单个方法也会引入整个类
export default class Utils {
  a() {}
  b() {}
}
```

复制代码
**反例 3**


构造函数导出


```

// 方法被绑定在实例上无法分离
export default function Utils() {
  this.a = () => {}
  this.b = () => {}
}
```

复制代码
**反例 4**


返回对象函数


```

// 方法仍会整体打包
export default function Utils() {
  return {
    a() {},
    b() {},
  }
}
```

复制代码
**正例 1**


具名导出


```

const a = 1
const b = () => {}
export { a, b }
```

复制代码
**正例 2**


独立导出


```

export const a = 1
export const b = () => {}
```

复制代码
### 按需引入


**推荐级别：强烈**


精准导入所需内容，避免引入冗余代码。


**反例 1**


多引入未使用


```

import { sayHi, sayBye } from './say.js'
sayHi('Vance') // sayBye 未被使用但仍会打包
```

复制代码
**反例 2**


全量引入


```

import \* as say from './say.js'
say.sayHi('Vance') // 引入整个模块
```

复制代码
**正例**


精准引入


```

import { sayHi } from './say.js'
sayHi('Vance') // 仅引入必要方法
```

复制代码
### 避免 CommonJS 规范


**推荐级别：强烈**


虽然平台支持 require，但应始终使用 ESM 规范以支持 TreeShaking。


**反例**


使用 require


```

const userInfo = require('./userInfo.js') // 无法 TreeShaking
```

复制代码
**正例**


ESM 导入


```

import userInfo from './userInfo.js'
// 注意实际情况应避免全量导入，按需解构更佳
```

复制代码
### 使用常量优化


**推荐级别：强烈**


常量更易维护且利于 TreeShaking 识别未使用变量。


**反例**


对象打包


```

const a = { a1: 'a1', a2: 'a2', a3: 'a3' } // 全部属性会被打包
const b = ['a1', 'a2', 'a3'] // 数组元素无法分离
```

复制代码
**正例**


独立常量


```

const a1 = 'a1' // 未使用时可被 TreeShaking
const a2 = 'a2'
const a3 = 'a3'
const a = { a1, a2, a3 }
const b = [a1, a2, a3]
```

复制代码
### 谨慎引入第三方包


**推荐级别：建议**


优先评估包体积，必要时进行源码裁剪。


**反例**


全量引入


```

import _ from 'lodash' // 引入完整包（代码量大）
export default {
  onInit() {
    _.join(['a', 'b', 'c'], '~') // 仅使用单个方法
  },
}
```

复制代码
**正例**


原生实现


```

export default {
  onInit() {
    ;['a', 'b', 'c'].join('~') // 使用原生方法
  },
}
```

复制代码
### 慎用 @import 样式


**推荐级别：强烈**


避免全局样式引入导致冗余 CSS 打包。


**反例**


全量引入


```

<template>
  <div class="yellow">黄色</div>
  <div class="black">黑色</div>
  <div class="green">绿色</div>
</template>
<style>
 @import './color.css'; /\* 可能包含未使用的样式 \*/
</style>
```

复制代码
**正例**


```

<template>
  <div class="yellow">黄色</div>
  <div class="black">黑色</div>
  <div class="green">绿色</div>
</template>
<style>
 .yellow {
 background: yellow;
 }
 .black {
 background: black;
 }
 .green {
 background: green;
 }
</style>
```

复制代码
### 页面模板拆分策略


**推荐级别：鼓励**


采用模块化设计原则，建议将不同功能模块拆分为独立页面文件。避免在单个页面中使用条件渲染实现多状态视图，这会导致模板复杂度增长。


**反例**


模板臃肿


```

<!-- 单一页面承载多状态视图 -->
<div>
  <div if="{{status === 1}}">
    <div>A功能视图组件</div>
    <!-- 50+ 嵌套节点 -->
  </div>
  <div if="{{status === 2}}">
    <div>B功能视图组件</div>
    <!-- 50+ 嵌套节点 -->
  </div>
</div>
```

复制代码
**正例**


模块化拆分


```

<!-- pageA.ux -->
<template>
  <div class="module-container">
    <text>A功能核心组件</text>
    <!-- 精简DOM结构 -->
  </div>
</template>

<!-- pageB.ux -->
<template>
  <div class="module-container">
    <text>B功能核心组件</text>
    <!-- 独立维护的视图 -->
  </div>
</template>
```

复制代码
### Manifest 配置精简原则


**推荐级别：建议**


严格遵循最小权限原则，manifest.json 中应仅声明实际使用的 API 及权限。冗余配置会增加应用审核风险并影响启动性能。


### 国际化资源优化


**推荐级别：建议**


当应用仅支持单一语言时，建议直接使用硬编码文本而非国际化方案。多语言场景下应及时清理未使用的 i18n 键值。


### 箭头函数优先原则


**推荐级别：建议**


箭头函数相比传统函数表达式具有更简洁的语法结构，在代码压缩阶段能获得更好的优化效果。


**反例**


```

function fetchData() {
  // 业务逻辑
}
```

复制代码
**正例**


```

const fetchData = () => {
  // 箭头函数实现
}
```

复制代码
### 对象属性命名优化


**推荐级别：建议**


对象属性名称应保持语义明确且简洁。由于 JavaScript 引擎无法对属性名进行 tree-shaking，建议采用短命名策略，特别是在高频使用的属性上。


**反例**


```

const userProfile = {
  userIdentification: 'UXP-001',
  profileModificationDate: '2024-03',
}
```

复制代码
**正例**


```

const user = {
  id: 'UXP-001',
  update: '2024-03', // 上下文明确的短命名
}
```

复制代码
### 环境区分策略


**推荐级别：建议**


避免将调试阶段的数据、代码带到生产环境上，应该用编译时参数而非运行时参数来区分 [编译环境变量](/reference/question-answer/build-env/)


### CSS 代码复用规范


**推荐级别：鼓励**


采用原子化 CSS 设计模式，将高频样式声明抽象为可复用类。可以使用 Sass/Less 预处理工具管理样式资源。


**反例**


```

<style>
 .component-a {
 width: 80px;
 margin: 16px;
 border-radius: 8px;
 }
 .component-b {
 width: 80px;
 padding: 16px;
 border-radius: 8px;
 }
</style>
```

复制代码
**正例**


```

<style>
 /\* 基础原子类 \*/
 .full-width {
 width: 80px;
 }
 .padding-md {
 padding: 16px;
 }
 .margin-md {
 margin: 16px;
 }
 .rounded {
 border-radius: 8px;
 }

 /\* 组件专属样式 \*/
 .component-b {
 background: #f0f2f5;
 }
</style>
```

复制代码


---


<!-- 文档 31: tutorial/question-answer/build-env/.md -->


## 编译环境变量

## 编译环境变量

更新时间：2024-03-13 09:57:59


编译环境变量 `process.env.NODE_ENV` 用于在构建时判断生产环境或开发环境。它可以帮助在编译时去掉不必要构建的代码块。环境变量的一种使用场景是用于模拟器无法覆盖的能力，可以使用 JavaScript 来模拟这些情况。


### 编译环境变量取值


| 环境 | 取值 |
| --- | --- |
| 开发环境 | development |
| 正式环境 | production |


### 使用示例


```

let musicList = []

if (process.env.NODE\_ENV == 'development') {
  // 开发环境假数据模拟
  musicList = require('./musicList.js')
} else if (process.env.NODE\_ENV == 'production') {
  // 正式环境获取真实数据
  musicList = getMuisc()
}

export default {
  onInit() {
    console.log(musicList)
  },
}
```

复制代码


---


<!-- 文档 32: tutorial/question-answer/i18n/.md -->


## 国际化

## 国际化

更新时间：2025-10-09 11:25:10


蓝河应用平台的能力会覆盖多个国家地区，平台支持国际化(i18n)的能力后，可以做到让一个蓝河应用产品（一个 RPK 文件）同时支持多个语言版本的切换，开发者无需开发多个不同语言的源码项目，避免给项目维护带来困难。


使用系统默认的语言，开发者配置国际化的方式非常简单，只需要`定义资源`与`引用资源`两个步骤即可；如果允许用户在蓝河应用中修改地区语言，请参考第三步`获取更新语言`；


### 定义资源文件


资源文件用于存放多个语言的业务信息定义，与其它技术平台类似（它们使用`properties文件`或者`xml文件`的格式），蓝河应用平台使用`JSON文件`保存资源定义；


在项目源码`src目录`下定义`i18n文件夹`，内部放置每个语言地区下的资源定义文件即可；其中文件名定义为：`zh-CN.json`、`zh.json`；


每个 JSON 文件的内容格式如下：


```

{
  "message": {
    "pageA": {
      "text": "pure-text-content",
      "format": {
        "object": "type-{name}",
        "array": "type-{0}"
      },
      "plurals": {
        "double": "car | cars",
        "three": "no apples | one apple | {count} apples",
        "format": {
          "object": "type-{name}",
          "array": "type-{0}"
        }
      }
    }
  }
}
```

复制代码
页面中通过`message.pageA.text`类似的`path`引用对应内容`"pure-text-content"`；


### 页面中引用资源


页面中 i18n 的使用语法，主要体现在 ViewModel 的几个函数上，如：`$t`，这些方法可以在`<template`或`<script>`中使用；


如下代码所示：


```

<template>
  <div>
    <text>{{ $t('message.pageA.text') }}</text>
    <text>{{ $t('message.pageA.format.object', { name: 'arg-object' }) }}</text>
  </div>
</template>

<script>
 export default {
 onInit() {
 // 简单格式化：
 this.$t('message.pageA.text')
 this.$t('message.pageA.format.object', { name: 'arg-object' })
 },
 }
</script>
```

复制代码
#### 简单格式化方法


| 属性 | 类型 | 参数 | 描述 |
| --- | --- | --- | --- |
| $t | Function | path: String 资源路径  arg0: object | array 格式化参数，非必要参数，根据系统语言完成简单的替换：`this.$t('message.pageA.text')` |


比如：


```

// 示例：无额外参数的格式化
// 输出："pure-text-content"
this.$t('message.pageA.text')
// 示例：额外参数为对象，替换引用内容中的绑定
// 输出："type-arg-object"
this.$t('message.pageA.format.object', { name: 'arg-object' })
```

复制代码
#### 单复数格式化方法


| 属性 | 类型 | 参数 | 描述 |
| --- | --- | --- | --- |
| $tc | Function | path: String 资源路径  count: number 要表达的值 | 根据系统语言完成单复数替换：`this.$tc('message.plurals.double')`，注意：定义资源的内容通过 | 分隔为多个选项 |


比如：


```

// 示例：message的值为两个选项时，传递数值不为单数
// 输出："cars"
this.$tc('message.pageA.plurals.double', 0)
// 示例：message的值为两个选项时，传递数值为单数
// 输出："car"
this.$tc('message.pageA.plurals.double', 1)
// 示例：message的值为两个选项时，传递数值不为单数
// 输出："cars"
this.$tc('message.pageA.plurals.double', 2)

// 示例：message的值为三个及以上的选项时，传递数值不为单数
// 输出："no apples"
this.$tc('message.pageA.plurals.three', 0)
// 示例：message的值为三个及以上的选项时，传递数值为单数
// 输出："one apple"
this.$tc('message.pageA.plurals.three', 1)
// 示例：message的值为三个及以上的选项时，传递数值不为单数
// 输出："10 apples"
this.$tc('message.pageA.plurals.three', 10)
```

复制代码
#### manifest 中的 name 的国际化


此时可使用字符串模板声明，形如：${appName}


例如下面：


```

{
  "package": "com.example.i18n",
  "name": "${appName}",
  "versionName": "1.0.0",
  "versionCode": 1
}
```

复制代码
此时 i18n 也必须有相应的配置信息


```

// en.json
{
  "appName": "myApp"
}
```

复制代码

```

// zh-CN.json
{
  "appName": "我的应用"
}
```

复制代码
#### 获取更新语言


上面的能力用于资源内容的格式化，在某些场景下开发者可能需要获取当前系统的地区语言`locale`并进行更改，来完成不同的逻辑处理：


- 比如：不同的 locale 对应的页面布局不同；
- 比如：开发者为用户提供设置某种语言的能力；


此时开发者，可以通过`blueos.app.configuration`接口来完成


比如：


```

import configuration from '@blueos.app.configuration'

// 获取locale，后续开发者可以将locale设置为VM中的data属性，并在模板中判断以区分不同的布局
const localeObject = configuration.getLocale()
// 转换为字符串格式，如：'zh'或者'zh-CN'
const locale = [localeObject.language, localeObject.countryOrRegion].filter((n) => !!n).join('-')

console.info(`获取当前locale：${locale}`)
```

复制代码
设置多当前语言(setLocale)为系统接口，普通应用无法调用。


```

import configuration from '@blueos.app.configuration'

// 设置locale成功后，通过VM的生命周期函数 onConfigurationChanged 触发
configuration.setLocale({
  language: 'zh',
  countryOrRegion: 'CN',
})
```

复制代码
#### 修改地区语言后的回调


当用户在系统设置或者通过 configuration.setLocale 切换地区语言，都会触发 onConfigurationChanged 回调，且返回来的 event.type 值为`locale`


示例代码


```

// 监听语言、地区变化
onConfigurationChanged(event) {
  if (event && event.type && event.type === 'locale') {
    console.log('locale or language changed!')
  }
}
```

复制代码


---


<!-- 文档 33: tutorial/quickstart/introduction/.md -->


## 概述

## 概述

更新时间：2025-04-29 11:37:34


蓝河应用开发采用类 web 开发范式，使用 UI 组件来搭建页面布局，使用样式来描述组件和页面的效果，使用 Javascript 来进行业务逻辑的开发。蓝河应用支持 MVVM（Model-View-ViewModel）的架构，通过数据绑定视图的方式，数据发生变化时，会自动触发 UI 的更新。


  

如果开发者是首次接触蓝河应用，并希望立即开始编写代码，请从 [构建首个蓝河应用](/reference/quickstart/quick-start) 开始。


### 蓝河应用系统能力开放概览


蓝河应用具备完备的开放能力，支持在健康、运动、出行、娱乐等全场景的应用的高效开发。


#### 十二大系统能力


| 系统能力 | 描述 |
| --- | --- |
| 应用框架 | 1. 功能组件：Page、Service、Widget；  2. 通知能力：Event、Notification、Toast；3. 页面路由；4. 后台管理、窗口管理，包管理； |
| UI 组件 | 1. 基础组件、容器组件、表单组件、画布组件、导航组件； 2. 系统风格 UI 组件； 3. MVVM 编程模型； 4. 弹性布局，自适应布局； 5. 属性动画、SVG 矢量动画，帧动画； |
| AI 能力 | 1. AI 算法能力：视觉算法、语音算法、自然语言处理； 2. AI 服务引擎：支持调用连接端的强算力设备上的端侧大模型和云端大模型； 功能组件包括 Chain、Agent、Memory、Tools，LLM API、PromptTemplete; |
| 连接能力 | 1. 开放组件 Kit: HealthKit、ShareKit、KeyKit、RelayKit； 2. BlueXlink: 发现、连接、传输、策略、协议适配； |
| 运动健康能力 | 1. 睡眠数据、运动数据 ； 2. 健康数据：心率、卡路里； 3. 运动识别：行走、跑步、骑行、游泳、跳绳... ； 4. 姿态识别：久坐、站立； |
| 通信能力 | 1. 蓝牙、NFC ； 2. 上传下载 ； 3. 数据请求 ； 4.WebSocket； |
| 多媒体能力 | 1. 原子音乐播放组件； 2. 图像/音频编解码； 3. 音频录制、播放； 4. 音频管理； |
| 数据存储能力 | 1. 存储空间管理； 2. K-V 存储；  3. 文件存储；  4. 数据共享； |
| 电话能力 | 1. 通话、短信； 2. 蜂窝数据； 3. 网络搜索； 4. SIM 卡管理； |
| 基础硬件能力 | 1. 位置服务； 2. 振动； 3. 屏幕管理； 4. 电源管理； 5. 传感器：佩戴状态、抬腕、计步、罗盘、加速度、陀螺仪、气压； |
| 基础软件能力 | 1. 系统设置； 2. 全球化； 2. 解压缩、序列化； |
| 安全能力 | 1. 权限机制； 2. 加解密算法库； 3. 应用沙箱； |


#### 两套 API


为了兼顾高效开发和高性能，蓝河应用提供了两套 API，Javascript API 和 Native API


1. Javascript API 提供了完整的开放能力， 支持开发者高效率地完成应用的开发。
2. Native API 主要聚焦高性能场景，以及方便开发者对原有代码的复用。


### 三种应用形态


蓝河应用支持应用、表盘、快捷卡片三种应用形态。


1. 应用：它具有完整的功能，可以支持多页面，支持复杂的 UI 交互，支持应用间的跳转和数据交换。它可以在后台运行，在特定场景可以长期运行。
2. 表盘：它具备装饰属性， 也代表了用户的个性化选择。支持普通和 AOD 两种显示模式，支持动态交互和 20 多种数据展示。支持三种开发方案：AI 生成、表盘设计工具制作、代码编程实现。
3. 快捷卡片：是一种高效的信息展示方式，用户无需进入应用，在表盘界面只需左滑，即可查看信息和控制操作。


  

蓝河表盘是一种非常重要的应用形态，蓝河应用致力于为用户提供丰富的表盘。为此蓝河开发套件共提供三种开发表盘方案，开发者既可以通过自然语言交互快速生成表盘（即将开放）、也可以使用设计图配置生成表盘（即将开放）、还可以使用代码编程实现功能更丰富的表盘。如果您需要了解更多关于代码编程实现表盘的方式请移步 [表盘教程](/reference/extend/watchface/) 与 [UI 组件支持的表冠旋转](/component/common/ui-rotation/) 进行更详细的了解。


### 通用开发流程


#### 一、准备开发环境


BlueOS Studio 是面向蓝河应用开发推出的一款全新的一站式集成开发环境。开发者可以使用 BlueOS Studio 开发、调试和打包蓝河应用。BlueOS Studio 提供了丰富的功能和工具，可以极大地提高开发效率和代码质量。如果您想了解更多关于 BlueOS Studio 的功能和使用方法，请移步 [BlueOS Studio](https://studio.blueos.com.cn/) 的详细教程。同时，您也可以 [点击链接进入工具下载页面](https://studio.blueos.com.cn/install) ，安装 BlueOS Studio。


#### 二、开发 UI


蓝河应用主要使用 UI 组件和样式进行界面的开发。UI 组件是蓝河应用 UI 开发的最小单元，蓝河应用提供了基础、表单，布局/容器、画布、导航、动画、系统风格等类型的一系列组件。 组件、样式、js 代码大部分都是写在 `.ux` 的文件中，您想进一步了解组件、样式、js 代码是如何组织的，可以移步 [ux 文件](/reference/configuration/ux-file/) 进行更详细的了解。


  

在组件开发基础之上，蓝河应用还提供了丰富的样式支持，因此开发者可以开发出包含自己独特风格的蓝河应用。样式可以声明在<style>标签内也可以通过 style 属性以内联样式的形式声明在组件标签上，如果您想了解更多关于样式的详细信息，请移步 [style 样式](/reference/configuration/style-sheet/) 。蓝河应用支持的通用样式情况的详细信息，可以移步了解 [通用样式支持](/component/common/common-styles/)


#### 三、开发业务功能


蓝河应用提供了 JS API 和 Native API 两种接口，以支撑高效和高性能的开发场景。开发者可以根据需要选择不同的接口进行开发，以获得更好的开发体验和应用性能。


  

1.JS API 提供了完整的开放能力， 支持开发者高效率地完成应用的开发。开发者可以实现应用生命周期监听、系统弹窗、多设备互联等操作，如果您需要了解更多关于这些开放能力的信息，请移步 [JS 功能接口](/api/system/app/) 进行了解。


  

2.Native API 主要聚焦高性能场景，支持 Posix API 以及部分系统能力如连接能力、数据存储能力、通信能力等。如果您需要了解 Native API 更详细的信息，请移步 [Native API](/native/quickstart/introduction/) 。


#### 四、开发调试


在开发的过程中，可以首先使用 BlueOS Studio 的 [实时预览](https://studio.blueos.com.cn/debug/preview/) 查看开发的界面效果。


此外，开发者经常会遇到到 UI 问题、网络问题、内存问题等。


BlueOS Studio 也提供了对应的分析面板，例如： [UI 调试](https://studio.blueos.com.cn/debug/devtools/#element-%E9%9D%A2%E6%9D%BF) 、 [网络调试](https://studio.blueos.com.cn/debug/devtools/#network-%E9%9D%A2%E6%9D%BF) 、 [内存调试](https://studio.blueos.com.cn/debug/devtools/#memory-%E9%9D%A2%E6%9D%BF) 、 [查阅日志](https://studio.blueos.com.cn/debug/console/) ，助力开发者更高效地定位问题。


  

开发完成后，开发人员需要对应用进行测试。BlueOS Studio 提供了 [自动化测试的功能](https://studio.blueos.com.cn/test/autotest/) ，助力开发者提高测试效率。


#### 五、发布


开发测试完成后，就来到了最后的发布环节，开发者可以使用 BlueOS Studio 的打包功能，将开发的应用打成 rpk 包。


  

打包完成后，前往发布平台[发布](https://dev.vivo.com.cn/watchRpk/list)后，蓝河操作系统的用户即可使用到对应的蓝河应用。


#### 六、快应用开发支持


蓝河系统支持快应用标准，可以使用 BlueOS Studio 进行快应用的开发，快应用开发技术文档请参考[快应用官网](https://www.quickapp.cn)。


---


<!-- 文档 34: tutorial/quickstart/quick-start/.md -->


## 构建首个蓝河应用

## 构建首个蓝河应用

更新时间：2025-10-09 11:25:10


> 
> 本文将从开发工具、新建项目、安装依赖、调试项目、打包等方面入手，让您学习后，可以构建首个蓝河应用。
> 
> 
> 


### 开发


开发者可以使用 BlueOS Studio 开发、调试和打包蓝河应用。以下所有的操作均在 BlueOS Studio 中完成，开发者可以[点击链接进入工具下载页面](https://studio.blueos.com.cn/install)，先安装 BlueOS Studio 。


#### 一、新建项目


新建方法如下：


1. 点击`欢迎页`「**新建工程**」、或`菜单栏`「**新建工程」**、或`快捷入口`处「**新建工程**」，打开新建工程界面；
2. 点击「**下一步**」 ，填写项目名称、项目路径、应用名称和应用包名，点击「**完成**」，BlueOS Studio 会在项目路径下，新建项目并自动打开。


![createProject](/80d94f075f09e93fb0cec6fe3f76c089/createProject.png)
#### 二、安装依赖


- 准备工作：安装并配置 [Node](https://nodejs.org/en) 环境。
- 在 BlueOS Studio，我们提供了方便的方式来安装依赖，如下图示，只要点击「**安装依赖**」按钮，即可。
- 安装完毕之后，点击「**重新启动编译**」按钮，即能重新编译；之后编写代码，就能在预览区实时查看效果，而无需其他任何操作。


![install](/8c2d3657ae88ced5aed9bd50519a699e/install.png)
#### 三、文件组织说明


```

├── scripts                   工具脚本文件
├── src
│   ├── assets                公用资源
│   │   ├── images            图片资源
│   │   └── styles            应用样式
│   ├── pages                 页面目录
│   │   ├── Demo              应用首页
│   │   └── DemoDetail        应用详情页
│   ├── app.ux                入口文件。
│   └── manifest.json         项目配置文件，配置应用图标、页面路由等
└── jsconfig.json             js 配置文件，用于语法校验
└── package.json              定义项目需要的各种模块及配置信息
```

复制代码
#### 四、开发调试


- BlueOS Studio 支持实时预览功能，开发者只需保存修改后的代码，即可在右侧模拟器实时预览修改效果。你可以通过 BlueOS Studio 下方提供的 DevTools 面板，进行调试样式、查看请求等操作。


![simulatorPreview](/5ea041843d198cbfdd34f41b22751f85/simulatorPreview.png)
  
  


开发者可以跟着下面的步骤，一步步完成第一个蓝河应用的构建。


##### 1.构建 UI


安装依赖后，即可打开 "src/pages/Demo/index.ux"文件，设置 `<template>` 标签内容，来构建页面 UI。`<template>` 标签示例如下：


```

<template>
  <div class="wrapper">
    <text>Hello World</text>
  </div>
</template>
```

复制代码
##### 2.设置页面样式


在"src/pages/Demo/index.ux"文件中，新增`<style>`标签，对页面中文本、按钮等 UI 设置宽高、字体大小、间距等样式。`<style>`标签示例如下：


```

<style>
 .wrapper {
 flex-direction: column;
 align-items: center;
 justify-content: center;
 }

 text {
 font-size: 50px;
 lines: 2;
 }
</style>
```

复制代码
##### 3.处理业务逻辑


在"src/pages/Demo/index.ux"文件中，新增`<script>`标签处理业务逻辑。在初始`<template>`的基础上，我们添加一个 button 类型的 input 组件，作为按钮响应用户点击，从而实现业务逻辑。


```

<script>
 export default {
 data: {},

 buttonClick(event) {
 console.log('click event fired')
 },
 }
</script>

<template>
  <div class="flex-col items-center p-20">
    <text>Hello World</text>
    <input type="button" class="w-[400px] h-[80px] text-white bg-[#1890ff] rounded-[15px] mt-10" value="click" onclick="buttonClick" />
  </div>
</template>

<style>
@tailwind utilities;
</style>
```

复制代码
##### 4.在右侧模拟器实时预览。第一个页面效果如下图所示：


  

![examplePreview](/e24babd21ad1f732f39504452429b6e8/examplePreview.png)
#### 五、打包


开发完成后，可以使用 BlueOS Studio 打包出应用 rpk 包，步骤如下：


1. 点击顶部工具栏的「**打包** 」按钮，可以选择包类型和环境变量，包类型可选 release 和 debug，release 包需要填写信息生成签名后，再行打包；环境变量可选 production、development 和 test，根据环境不同可调用不同的后台接口而不用手动修改代码；
2. 打包成功之后，会在 dist 目录下生成相应的 rpk 包，可以「打开 rpk 所在位置」；
3. 打包成功之后，可以点击前往开放平台上传 rpk 包。


![package](/bca4efe3a2325b918bc3b75214f35e27/packageSettings.png)
  
   


![packageSuccess](/ab20807fa6e0c3863703cb8444912371/packageSuccess.png)


---


<!-- 文档 35: tutorial/widget/js-widget/.md -->


## 标准卡开发

## 标准卡开发

更新时间：2025-10-09 11:25:10


标准卡和普通蓝河页面开发范式相同，包含下列常见能力：


- 生命周期
- 页面样式与布局
- 列表渲染
- 条件指令
- 应用跳转及参数传递
- 事件绑定
- 自定义组件
- 国际化多语言


**示例：**


```

<script>
export default {
 data: {
 showSunny: false,
 },
 onInit() {
 // 这里可以添加初始化逻辑
 },
 onShow() {},
}
</script>

<template>
  <div class="weather-container">
    <text class="text-red-500 text-2xl">天气卡片</text>
    <text class="weather" if="{{ showSunny }}">晴</text>
    <text class="weather" else>雨</text>
  </div>
</template>

<style>
@tailwind utilities;
</style>
```

复制代码


---


<!-- 文档 36: tutorial/widget/lite-widget/.md -->


## 轻卡开发

## 轻卡开发

更新时间：2025-10-09 11:25:10


轻卡不运行 JavaScript，因此其开发范式与标准卡片存在差异，具体细节将在本节中进一步介绍。


### 基本范式


轻卡的开发 ux 文件开发分为`data`、`template`和`style`三个部分。


**例如：**


```

<data>
  {
   "uiData": {
    "content": "轻卡示例"
   }
  }
</data>

<template>
  <text class="text-xs">{{content}}</text>
</template>

<style>
@tailwind utilities;
</style>
```

复制代码
### 数据绑定


在 data 标签中使用 uiData 声明数据，然后在 template 中使用`{{}}`来绑定数据。


```

{
  "uiData": {
    "content": "Hello World!",
    "key1": "Hello",
    "key2": "World",
    "flag1": true,
    "flag2": false
  }
}
```

复制代码

```

<template>
  <div class="container">
    <text>{{content}}</text>
    <!-- 输出：Hello World！-->
    <text>{{key1}} {{key2}}</text>
    <!-- 输出：Hello World-->
    <text>key1 {{key1}}</text>
    <!-- 输出：key1 Hello-->
    <text>{{flag1 && flag2}}</text>
    <!-- 输出：false-->
    <text>{{flag1 || flag2}}</text>
    <!-- 输出：true-->
    <text>{{!flag1}}</text>
    <!-- 输出：false-->
  </div>
</template>
```

复制代码
**表达式支持**


卡片模版中支持表达式有以下几种：


| 操作符 | 描述 | 示例 |
| --- | --- | --- |
| `+`,`-`, `*`, `/`, `%`, `++`, `--`, `**` | 算术运算（+包含字符串拼接） | `a + b` |
| neg | 转负数 | `-a` |
| `>=`, `<=`, `>`, `<`, `==`, `!=`, `===`, `!==` | 比较运算 | `a > b` |
| &&, || | 逻辑运算 | a || b |
| ! | 取反运算 | `!a` |
| `.`, `[]` | 取属性运算 | `item.name`, `arr[3]` |
| ?: | 三目运算 | `a > 0 ? 'good' : 'bad'` |
| `` | 字符串拼接：1. 变量拼接变量；2. 常量拼接变量 | 1. { { key1 } } - { { key2 } } 2. my name is { { name } } |


其中，表达式支持的数据类型：


- 基本数据类型：字符串（String）、数字（Number）、布尔（Boolean）、空（Null）
- 引用数据类型：对象（Object）、数组（Array）


### 条件渲染


条件渲染分为 2 种实现：`if/elif/else` 和 `show`。


**if/elif/else**


`if/elif/else` 节点**必须是相邻的兄弟节点**，否则会导致编译失败。仅当条件成立时，对应的节点才会保留在虚拟 DOM（VDOM）中，其余节点会被移除。


```

{
  "uiData": {
    "display": false
  }
}
```

复制代码

```

<template>
  <div>
    <text if="{{display}}">Hello-1</text>
    <text elif="{{display}}">Hello-2</text>
    <text else>Hello-3</text>
  </div>
</template>
```

复制代码
**show**


`show` 控制组件的可见性。被设置为 `false` 时，组件不会被渲染到界面上，但仍然保留在 VDOM 中，不会被移除。


```

{
  "uiData": {
    "visible": false
  }
}
```

复制代码

```

<template>
  <text show="{{visible}}">Hello</text>
</template>
```

复制代码
### 列表渲染


使用 `for` 指令可循环渲染数组数据。其语法支持多种形式（`{{}}` 可省略）：


**基础写法：**


```

for="{{list}}"
```

复制代码
- `list` 是数组类型数据。
- 默认数组元素变量为 `$item`，索引为 `$idx`。


**自定义变量名：**


```

for="{{value in list}}"
```

复制代码
- `value` 是自定义的数组元素变量名。
- 索引仍默认为 `$idx`。


**自定义索引和元素变量名：**


```

for="{{(index, value) in list}}"
```

复制代码
- `index` 是索引变量名，`value` 是元素变量名。


**使用常数作为循环次数：**


你还可以使用一个常数作为数据源，表示循环执行的次数。等价于遍历从 `0` 到 `n - 1` 的索引。


```

for="{{value in 10}}"
for="{{(index, value) in 5}}"
```

复制代码
- 等价于遍历 `[0, 1, 2, ..., n - 1]`。
- 可以搭配 `index` 和 `value` 使用。


**tid 属性:**


用于指定每个循环项的唯一 ID，用于 DOM 节点复用和性能优化。若未指定，默认使用 `$idx`。


```

{
  "uiData": {
    "list": [
      { "name": "aa", "uniqueId": 1 },
      { "name": "bb", "uniqueId": 2 },
      { "name": "cc", "uniqueId": 3 }
    ]
  }
}
```

复制代码

```

<div for="value in list" tid="uniqueId">
  <text>{{$idx}}.{{value.name}}</text>
</div>
```

复制代码
### 事件绑定


轻卡仅支持组件的通用事件 click，对于事件的响应动作需要在 data 模块下 actions 下提前声明。


```

{
  "actions": {
    "onTextClick": {
      "type": "router",
      "url": "hap://app/com.example.quickapp/page",
      "params": {
        "param": "111"
      }
    }
  }
}
```

复制代码

```

<div>
  <!-- 标准格式 -->
  <text onclick="onTextClick"></text>
  <!-- 简写 -->
  <text @click="onTextClick"></text>
</div>
```

复制代码
**事件绑定传参：** 支持默认参数 $event 和 for 指令循环中 $item


**示例 1：** 组件事件参数通过 $event 获取


```

{
  "actions": {
    "onSwitchChange": {
      "type": "message",
      "params": {
        "checked": "{{$event.checked}}"
      }
    }
  }
}
```

复制代码

```

<switch @change="onSwitchChange"></switch>
```

复制代码
**示例 2：** for 循环列表中可以通 $item 获取列表 item


```

{
  "uiData": {
    "list": [
      { "name": "aa", "uniqueId": 1 },
      { "name": "bb", "uniqueId": 2 }
    ]
  },
  "actions": {
    "handleClick": {
      "type": "message",
      "params": {
        "name": "{{$item.name}}"
      }
    }
  }
}
```

复制代码

```

<div for="{{list}}" tid="uniqueId" @click="handleClick">
  <text>{{$item.name}}</text>
</div>
```

复制代码
轻卡当前支持的事件响应动作有跳转和消息以及代理事件，事件响应动作格式定义如下:


| **参数** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| type | "router" | "message" | 是 | 事件类型，下面详细介绍 |
| url | string | string[] | 否 | 事件类型为 router 时必填，描述跳转页面链接，支持单条或多条 deeplink，支持变量形式。事件类型为 message 时不需要。 |
| params | Record<string, any> | 否 | 参数对象，支持在顶层字段中使用 `{{变量}}`，嵌套对象或数组中的字段不支持变量绑定。 |


#### router


跳转事件是可以直接在卡片宿主里完成跳转动作, 示例如下：


支持主应用的页面跳转和公开的 scheme


```

{
  "uiData": {
    "pageUrl": "hap://app/com.example.demo/page",
    "a": "pa"
  },
  "actions": {
    "routerEvent": {
      "type": "router",
      "url": "{{ pageUrl }}",
      "params": {
        "a": "{{a}}",
        "b": "b",
        "c": { "s": "sss" }
      }
    }
  }
}
```

复制代码
**支持跳转的 deeplink 协议：**


```

{scheme}://{host}/{path}?{query}
```

复制代码
#### message


消息事件是指事件发送给 widgetProvider 处理。


```

{
  "uiData": {
    "name": "hello"
  },
  "actions": {
    "messageEvent": {
      "type": "message",
      "params": {
        "name": "{{name}}",
        "b": "b"
      }
    }
  }
}
```

复制代码
此时在 widgetProvider 中收到的消息如下：


```

export default {
  onWidgetEvent(id, { event }) {
    /\*\*
 \* event 示例:
 \* { action: "messageEvent", params: { name: "hello", b: "b" } }
 \*/
    console.log(`event`, event)
  },
}
```

复制代码


---


<!-- 文档 37: tutorial/widget/overview/.md -->


## 概述

## 概述

更新时间：2025-10-09 11:25:10


本节介绍卡片的定义、分类、模块架构和运行原理。


### 什么是卡片


卡片是一种轻量的应用形态。它可以嵌入到各类场景应用的页面中（如负一屏，桌面，全搜，锁屏，浏览器，语音助手等），为用户提供快速、直观且高度关联的服务体验。通过精准和便捷地展示信息或功能，卡片不仅提高了用户获取服务的效率，也为应用带来了更多曝光机会和用户参与度。


![img](/a849fd2199dc608fbaca6abce2a81186/widget-demo.png)


### 卡片分类


蓝河系统卡片分为**标准卡**和**轻卡**，不同的卡片的特点和使用场景不一样，下面是两种卡片的对比说明。


| 分类 | 标准卡 | 轻卡 |
| --- | --- | --- |
| 介绍 | 功能完备，具备完整数据处理及逻辑闭环 | 轻量，依赖外部数据和逻辑支持 |
| 特点 | 1.有 JS 代码2.支持 UI 组件3.支持 JS 组件动画4.不支持外部提供数据 | 1. 无 JS 代码2. 支持 UI 组件3.不支持 JS 组件动画4.支持外部提供数据 |
| 适用场景 | UI 和交互上需求更复杂的卡片 | 由外部提供数据，动效和交互不复杂的场景 |


### 模块架构


![卡片整体模块架构图](/3b68224337551e20ec7f032be2d1f618/CAPTURE_2025514_94644.png)


**卡片提供方：** 包含卡片的应用，提供卡片的显示内容、布局以及控件点击处理逻辑


- **卡片页面：** 卡片 UI 模块，包含页面组件、布局、事件等显示和交互信息
- **widgetProvider:** 处理卡片的生命周期与回调方法，给卡片页面提供和更新数据。不同类型的卡片此模块有所区别：轻卡有此模块，标准卡中无此模块。
- **配置文件：** 配置卡片刷新时间、尺寸、名称等信息
- **卡片可跳转的页面：** 用户点击卡片内容可以拉起这些页面，此模块非必须。


**卡片使用方(Host)：** 如 launcher 应用的桌面页面，他是卡片的宿主应用，可以显示卡片内容，控制卡片展示的位置。


- **widget-container：** 用于渲染卡片的 UI 组件，可以在 Host 应用显示的卡片界面，卡片显示的内容可以交互，也可以刷新。
	- **内容显示：** 显示不同尺寸规格的内容界面，将卡片页面挂在 Host 应用界面的节点上
	- **跳转应用：** 点击卡片可以拉起卡片提供方应用的界面
	- **刷新数据：** 卡片显示的数据内容，可以进行刷新，其中标准卡可以自主刷新，轻卡需要借助 widgetProvider 来完成


### 运行原理


![卡片运行功能模块图](/78bea754092e89ee53fc0dc80f26f16b/CAPTURE_2025514_94844.png)
- **widgetProvider**
	- **回调方法：** 由 Action 调起，用于响应 Action。
	- **生命周期：** 卡片的创建、销毁等生命周期
	- **widgetManager：** 用于更新卡片数据，可在生命周期和回调方法中使用
- **卡片页面**
	- **组件/样式：** 用于卡片页面布局
	- **uiData：** UI 数据，可由 widgetProvider 或卡片页面 JS 更新
	- **javascript:**
		- 标准卡：用于执行卡片所有业务逻辑。
	- **Action：** 一个功能概念，可以触发以下操作：
		- 页面跳转：跳转到卡片提供方页面。
		- 事件传递：调起 widgetProvider 的回调方法。


从上也可以得出来**两种卡片类型特点：**


- **标准卡：** 功能完备，具备完整数据处理及逻辑闭环，但是不够轻量
- **轻卡：** 轻量，依赖外部数据和逻辑支持，但是无法执行复杂的 UI 交互


### 存储沙箱


卡片的存储沙箱机制遵守蓝河系统沙箱机制，即：同一包名的应用共享同一个应用存储沙箱。


通常情况下，一个工程下的应用和卡片的应用沙箱存储共享，这意味着：


- 共用存储目录（files/preferences/）
- 共享数据库文件
- 共享 storage 存储的数据
- 共享缓存目录（cache/temp）


由于卡片与主应用共用包名时，可无缝访问主应用存储数据，因此需要注意以下事项：


- 敏感数据保护：应对重要数据进行加密处理，或采用独立包名机制
- 版本管理：需建立主应用与卡片间的数据版本协同更新机制


### 权限


- 权限申请：
	- 标准卡片由卡片应用向用户申请权限
	- 轻卡无 js 逻辑，不存在权限申请
- 权限共享：
	- 同一包名下已授权的权限可共享，可不用重复申请。


---


<!-- 文档 38: tutorial/widget/project-config/.md -->


## 卡片配置

## 卡片配置

更新时间：2025-10-09 11:25:10


本节介绍卡片配置及工程目录，通过示例展示了轻卡和标准卡的具体配置方法。


### 工程目录


在代码工程中支持两种卡片工程目录组织方式：


1. 一张卡片单独一个工程
2. 多张卡片和普通应用在同一个工程下，卡片和普通应用分属不同的文件目录。


**仅卡片**


> 
> 注意：卡片工程中不存在 app.ux 文件。
> 
> 
> 


```

└── src
│   ├── widgets                 # 统一存放项目快应用卡片代码
│   │    ├── widget1            # 表示卡片1的目录
│   │    │     ├──i18n          # 卡片1的国际化资料目录
│   │    │     ├──assets        # 卡片1的资源文件（卡片使用的非代码资源必须放在卡片目录下）
│   │    │     └──index.ux      # 卡片的ux和逻辑实现文件
│   │    └── widget2            # 表示卡片2的目录
│   └── manifest.json           # 配置应用基本信息
└── package.json                # 定义项目需要的各种模块及配置信息
```

复制代码

```

## 打包结果
- com.example.demo.rpks
  - com.example.demo_widgets.widget1.rpk
  - com.example.demo_widgets.widget2.rpk
```

复制代码
**普通应用 + 卡片**


> 
> 注意：为了保证卡片的打包体积最小化，卡片不得使用根目录下的 assets 资源文件。
> 
> 
> 


```

└── src
│   ├── widgets                 # 统一存放项目快应用卡片代码
│   │    ├── widget1            # 表示卡片1的目录
│   │    │     ├──i18n          # 卡片1的国际化资料目录
│   │    │     ├──assets        # 卡片1的资源文件（卡片使用的非代码资源必须放在卡片目录下）
│   │    │     └──index.ux      # 卡片的ux和逻辑实现文件
│   │    └── widget2            # 表示卡片2的目录
│   ├── assets                  # 应用的资源(Images/Styles/字体...)
│   ├── helper                  # 项目自定义辅助各类工具
│   ├── pages                   # 统一存放项目快应用页面级代码
│   │    ├── page1              # 表示页面1的目录
│   │    │     └──index.ux      # 页面的ux和逻辑实现文件
│   │    └── page2              # 表示页面2的目录
│   ├── app.ux                  # 快应用应用程序代码的入口文件
│   └── manifest.json           # 配置应用基本信息
└── package.json                # 定义项目需要的各种模块及配置信息
```

复制代码

```

## 打包结果
- com.example.demo.rpks
  - com.example.demo.rpk
  - com.example.demo_widgets.widget1.rpk
  - com.example.demo_widgets.widget2.rpk
```

复制代码
### manifest


标准卡和轻卡统一都在 manifest.json 下的 router.widgets 字段下配置，通过 type 区分


#### router.widgets


卡片的定义通过 manifest.json 中的 router.widgets 字段进行定义。


| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| **widgets** | Record<string, [Widget](#widget)> | 否 | 卡片信息，key 值为卡片名称，value 为卡片详细配置 widget |


> 
> 例如： `widgets/Widget1` 对应 `widgets/Widget1`目录，它也是卡片访问路径和卡片的唯一标识
> 
> 
> 


```

{
  "router": {
    "widgets": {
      "widgets/widget1": {}
    }
  }
}
```

复制代码
#### Widget


用于定义卡片的路由信息。


| 属性 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| type | js | lite | 是 | 卡片类型，`js` 表示标准卡，`lite` 表示轻卡 |
| name | string | 是 | 卡片名称 |
| description | string | 否 | 卡片描述 |
| component | string | 是 | 卡片对应的组件名，与 ux 文件名保持一致，例如'widget' 对应 'widget.ux' |
| minCardPlatformVersion | number | 是 | 支持的最小卡片平台版本号 |
| versionCode | number | 是 | 卡片版本号，如：2 |
| versionName | string | 是 | 卡片版本名称，如：`"1.0"` |
| targetManufacturers | string[] | 否 | 目标厂商，若配置此字段，则需要指定对应厂商，如不指定，可能不能在对应的厂商上架。可选值`vivo`、 `OPPO`、`xiaomi`、`honor` |
| features | [FeatureInfo](#featureinfo)[] | 否 | 卡片使用的 feature 列表，卡片的 feature 列表单独定义 |
| permissions | [PermissionInfo](/reference/configuration/manifest/#permissioninfo)[] | 否 | 权限申请，示例: `[{ "name": "watch.permission.LOCATION" }]` |
| sizes | [Size](#size)[] | 是 | 卡片支持的外观尺寸选项，如：`["2x2","2x1"]` |
| deviceTypeList | [DeviceType](#devicetype)[] | 否 | 卡片支持的设备类型，如：`["phone","watch"]` |
| previewImages | [PreviewImage](#previewimage)[] | 是 | 卡片各个尺寸下预览图。如在普通应用中新建卡片，预览图应放在卡片工程目录中。 |


轻卡独有字段：


| 属性 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| providerUri | [ProviderUri](#provideruri) | 是 | widgetProvider 的 uri 标识 |
| providerPackage | string | 是 | widgetProvider 所在应用的包名 |
| minProviderVersion | number | 是 | widgetProvider 所在应用的最小版本号 |
| refreshDuration | number | 否 | 1、表示定时数据刷新间隔，以秒为单位2、此字段会影响卡片的刷新执行，两次曝光的间隔小于数据刷新间隔值时，数据不会被拉取3、支持运营配置4、默认值 30x60=1800 （30 分钟）（小于默认值，上架会审核） |
| scheduledRefreshTime | string[] | 否 | 1、表示卡片的定点刷新的时刻，采用 24 小时制，精确到分钟，如["10:30", "21:30"]。 2、和 refreshDuration 同时指定时，scheduledRefreshTime 优先，指定多个定点刷新时刻，时刻间隔需大于 refreshDuration。 |


#### DeviceType


卡片支持的设备类型枚举，当前只支持 watch 和 phone


| 类型值 | 说明 |
| --- | --- |
| watch | 手表 |
| phone | 手机，暂不支持 |
| tv | 电视，暂不支持 |
| car | 汽车，暂不支持 |
| band | 手环，暂不支持 |


#### ProviderUri


专用于轻卡平台的字段，代表 widgetProvider 的 URI 标识。


| 分类 | 规范 | 说明 |
| --- | --- | --- |
| 蓝河应用 | `widget-provider://$packageName/$name` | 蓝河应用提供数据 |
| 手机安卓应用 | `content://$authority/$path/$id` | 手机安卓应用提供数据 |
| 服务端 | `https://$authority/$path` | 服务端提供数据 |


#### FeatureInfo


需要使用的 feature 声明，例如：


```

{
  "name": "blueos.network.fetch"
}
```

复制代码
#### Size


卡片在布局网格中的占位大小（宽度和高度，以栅格个数为单位），支持 "FULL"（全宽/全高）、"AUTO" (宽度/高度自适应)与具体数值的组合，并通过格式如 "2x2"、"FULLx4"、"1xFULL"、"4xAUTO"来定义。


**注意**：`2x2`中间没有空格。


#### PreviewImage


卡片预览图


```

{
  "size": "1x1",
  "images": ["/assest/a.png", "/assest/b.png"]
}
```

复制代码
### 实践示例


#### 标准卡


工程目录：


```

└── src
│   ├── widgets                 # 统一存放项目快应用卡片代码
│   │    └── widget1            # 表示卡片1的目录
│   │          ├──i18n          # 卡片1的国际化资料目录
│   │          ├──assets        # 卡片1的资源文件（卡片使用的非代码资源必须放在卡片目录下）
│   │          └──index.ux      # 卡片的ux和逻辑实现文件
│   └── manifest.json           # 配置应用基本信息
└── package.json                # 定义项目需要的各种模块及配置信息
```

复制代码
对应的 manifest.json：


```

{
  "router": {
    "widgets": {
      "widgets/widget1": {
        "type": "js",
        "name": "xx卡片",
        "description": "这是一个xx卡片",
        "component": "index",
        "features": [{ "name": "blueos.network.fetch" }],
        "minCardPlatformVersion": 2000,
        "sizes": ["2x2", "2x1"],
        "deviceTypeList": ["phone", "watch"],
        "previewImages": [
          {
            "size": "2x2",
            "images": ["/assest/a.png", "/assest/b.png"]
          },
          {
            "size": "2x1",
            "images": ["/assest/c.png", "/assest/d.png"]
          }
        ]
      }
    }
  }
}
```

复制代码
#### 轻卡


工程目录：


```

└── src
│   ├── widgets                 # 统一存放项目快应用卡片代码
│   │    └── widget1            # 表示卡片1的目录
│   │          ├──i18n          # 卡片1的国际化资料目录
│   │          ├──assets        # 卡片1的资源文件（卡片使用的非代码资源必须放在卡片目录下）
│   │          └──index.ux      # 卡片的ux和逻辑实现文件
│   └── manifest.json           # 配置应用基本信息
└── package.json                # 定义项目需要的各种模块及配置信息
```

复制代码
对应的 manifest.json：


```

{
  "router": {
    "widgets": {
      "widget/widget1": {
        "type": "lite",
        "name": "轻卡",
        "description": "这是一张轻卡",
        "component": "index",
        "providerUri": "widget-provider://com.example.demo/mymusic",
        "providerPackage": "com.example.demo",
        "minProviderVersion": 80801,
        "refreshDuration": 1800000,
        "scheduledRefreshTime": ["10:30", "21:30"],
        "minCardPlatformVersion": 2000,
        "sizes": ["2x2", "2x1"],
        "deviceTypeList": ["watch"]
      }
    }
  }
}
```

复制代码


---


<!-- 文档 39: tutorial/widget/widget-provider/.md -->


## widgetProvider 开发

## widgetProvider 开发

更新时间：2025-10-09 11:25:10


本节将介绍 widgetProvider 的核心概念和三种实现方式。鉴于不同平台的开发方式各有差异，开发者可以做在具体文档中查阅。本节重点讲解 widgetProvider 的顶层概念，通过理解这些概念，您将更容易掌握不同实现方式之间的互通性。


### 概述


#### widgetProvider 介绍


widgetProvider 是轻卡的核心组成部分，它负责执行轻卡页面的逻辑，并与轻卡页面进行数据传递。


根据数据来源的不同，widgetProvider 有三种不同的实现方式：


| 应用场景 | 实现方式 |
| --- | --- |
| 蓝河应用给轻卡提供数据 | 蓝河应用 |
| Android 手机应用给轻卡提供数据 | Android 应用 |
| 服务端接口通过网络请求给轻卡提供数据 | 服务端 |


![widgetProvider的实现](/4cce57f10d0ab3ca89c117f5ccc713d6/WX20241128-204446.png)
#### 核心组成与作用


![widgetProvider组成](/ab6c2a8e9658a62dad7c3e3e9592683c/WX20241128-211907.png)
##### 核心组成


widgetProvider 的组成部分为**生命周期、回调方法和 widgetManager**。


- **回调方法：** 响应轻卡页面传递过来的数据。
- **生命周期：** 响应轻卡的创建、销毁等生命周期
- **widgetManager：** 用于更新卡片数据


##### 响应卡片生命周期


widgetProvider 通过下面的生命周期，来执行轻卡的页面的业务逻辑。


- 创建：当卡片在入口被创建时触发
- 刷新：定时或定点条件满足时触发
- 销毁：销毁卡片时触发
- 系统语言变化：监听系统语言改变


**例如：**


```

export default {
  onWidgetCreate() {
    console.log('卡片创建')
  },
  onWidgetUpdate() {
    console.log('满足时刷新条件')
  },
  onWidgetDestroy() {
    console.log('销毁卡片')
  },
  onConfigurationChanged() {
    console.log('系统语言改变')
  },
}
```

复制代码
##### 响应卡片页面自定义事件


widgetProvider 上的 onWidgetEvent 回调可以响应卡片页面发过来的自定义事件和事件数据。


**例如：**


> 
> widgetProvider 接受数据
> 
> 
> 


```

export default {
  onWidgetEvent(id, event) {
    console.log('收到卡片页面的事件')
  },
}
```

复制代码

> 
> 卡片页面发送事件
> 
> 
> 


```

<text onclick="onTextClick">hello</text>
```

复制代码

```

{
  "actions": {
    "onTextClick": {
      "type": "message.md",
      "params": {
        "content": "hello"
      }
    }
  }
}
```

复制代码
##### 刷新轻卡数据


widgetProvider 还通过接口来刷新 轻卡 UI 页面中的 uiData 数据。


> 
> widgetProvider 发送数据给页面
> 
> 
> 


```

import widgetManager from '@blueos.app.widgetManager'
export default {
  // 卡片创建时触发
  onWidgetCreate(id) {
    widgetManager.updateUiData({
      instanceId: id,
      uiData: { cityName: `Shenzhen` },
    })
  },
}
```

复制代码

> 
> 卡片页面编写
> 
> 
> 


```

<text>{{cityName}}</text>
```

复制代码

```

{
  "uiData": {
    "cityName": ""
  }
}
```

复制代码
#### 权限与限制


**权限申请：** 当运行 widgetProvider 时需要用户授权，权限申请的主体应为 widgetProvider 所在的应用。


**跳转限制：** 为了防止 widgetProvider 随意启动应用并浪费系统资源，widgetProvider 中禁止跳转到其他应用页面。


### 开发实践


#### 注册 widgetProvider


在蓝河应用的 manifest.json 中配置如下信息


```

{
  "widgetProvider": [
    {
      "name": "mymusic",
      "path": "/widgetProvider/index.js"
    }
  ]
}
```

复制代码
此时对应轻卡需存在配置如下： **注意：需要卡片应用签名和蓝河应用签名一致才可以提供数据**


```

{
  "router": {
    "widgets": {
      "widget/lite\_widget": {
        "providerUri": "widget-provider://com.example.demo/mymusic",
        "providerPackage": "com.example.demo"
      }
    }
  }
}
```

复制代码
#### 实现 widgetProvider


需要在 `/widgetProvider/index.js` 完成 widgetProvider 功能。


可参考 [widgetProvider](/api/system/widget-provider/) 和 [widgetManager](/api/system/widget-manager/)


| 生命周期/回调 | 描述 |
| --- | --- |
| onWidgetCreate | 当卡片在入口被创建时触发 |
| onWidgetUpdate | 定时或定点条件满足时，卡片请求提供方刷新卡片 |
| onWidgetEvent | 当卡片页面触发 Action 的 message 事件时被调用 |
| onWidgetDestroy | 销毁卡片时触发，提供方可以做对应的释放 |
| onConfigurationChanged | 监听系统语言改变 |


**示例：**


下面示例实现了，点击播放/停止音乐，定位等功能。


> 
> widgetProvider/index.js
> 
> 
> 


```

import widgetManager from '@blueos.app.widgetManager'
import geolocation from '@blueos.hardware.location'
import media from '@blueos.media.audio.mediaManager'

let audioPlayer

const getLocation = () => {
  return new Promise((resolve, reject) => {
    geolocation.getLocation({
      success: resolve,
      fail: reject,
    })
  })
}

export default {
  async onWidgetCreate(id) {
    // 初始化数据
    audioPlayer = media.createAudioPlayer()
  },
  async onWidgetUpdate(id) {
    // 实现定时更新位置功能
    const { longitude, latitude } = await getLocation()
    widgetManager.updateUiData({
      instanceId: id,
      uiData: { longitude, latitude },
    })
  },
  onWidgetEvent(id, { event }) {
    // 实现点击音乐播放的功能
    const { type } = event
    switch (type) {
      case 'play':
        audioPlayer.src = 'xxxx'
        audioPlayer.play()
        break
      case 'stop':
        audioPlayer.stop()
        break
    }
  },

  onWidgetDestroy(id) {
    audioPlayer.release()
  },

  onConfigurationChanged(id, event) {
    // 实现改变语言
    if (event && event.type && event.type === 'locale') {
      widgetManager.updateUiData({
        instanceId: id,
        uiData: { songTitle: 'flute solo' },
      })
    }
  },
}
```

复制代码

> 
> 对应卡片界面
> 
> 
> 


```

<div>
  <text>{{songTitle}}</text>
  <text>{{longitude}}, {{latitude}}</text>
  <text @click="play">play</text>
  <text @click="stop">stop</text>
</div>
```

复制代码

```

{
  "uiData": {
    "songTitle": "笛子独奏",
    "longitude": "",
    "latitude": ""
  },
  "actions": {
    "play": {
      "type": "message.md",
      "params": {
        "type": "play"
      }
    },
    "stop": {
      "type": "message.md",
      "params": {
        "type": "stop"
      }
    }
  }
}
```

复制代码
### 其他平台 widgetProvider 实现


当手机 Android 应用或服务端需要为轻卡提供数据时，可以使用 Android 应用和服务端开发 widgetProvider。


这两种实现方式的原理与蓝河实现相同，可以参考[文档](https://www.quickapp.cn/document?menu=2%252C143&pathUrl=%252Fdoc%252Flitewidget%252Fguide%252Finterface%252Fintro.html)进行具体实现。


---
