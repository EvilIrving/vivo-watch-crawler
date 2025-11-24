# vivo BlueOS 手表开发文档 - UI 组件

> 本文档由爬虫自动生成，包含 55 个页面的内容

## 目录

- [动画样式](#动画样式)
- [a](#a)
- [animated-vector](#animated-vector)
- [概述](#概述)
- [arc-text](#arc-text)
- [barcode](#barcode)
- [image-animator](#image-animator)
- [image](#image)
- [marquee](#marquee)
- [概述](#概述)
- [physics-engine](#physics-engine)
- [progress](#progress)
- [qrcode](#qrcode)
- [span](#span)
- [svg-container](#svg-container)
- [text](#text)
- [颜色样式](#颜色样式)
- [通用属性](#通用属性)
- [通用事件](#通用事件)
- [通用方法](#通用方法)
- [通用样式](#通用样式)
- [组件动画](#组件动画)
- [div](#div)
- [list-item](#list-item)
- [list](#list)
- [概述](#概述)
- [scroll](#scroll)
- [stack](#stack)
- [swiper](#swiper)
- [cellular-list](#cellular-list)
- [drawer-navigation](#drawer-navigation)
- [drawer](#drawer)
- [概述](#概述)
- [自定义字体样式](#自定义字体样式)
- [概述](#概述)
- [vw-alert](#vw-alert)
- [vw-button](#vw-button)
- [vw-empty](#vw-empty)
- [vw-icon](#vw-icon)
- [vw-list-item](#vw-list-item)
- [vw-list](#vw-list)
- [vw-loading](#vw-loading)
- [vw-slide](#vw-slide)
- [vw-title](#vw-title)
- [渐变样式](#渐变样式)
- [canvas](#canvas)
- [概述](#概述)
- [artboard](#artboard)
- [input](#input)
- [label](#label)
- [概述](#概述)
- [picker](#picker)
- [slider](#slider)
- [switch](#switch)
- [UI 组件支持的表冠旋转](#ui-组件支持的表冠旋转)

---


<!-- 文档 1: ui-component/component/animation-styles.md -->


## 动画样式

## 动画样式

更新时间：2025-04-15 11:26:34


蓝河应用支持开发者制作动画，提供了`transform`类、`animation`类的动画样式属性，且参数格式与 CSS 对齐，更方便开发者上手适配动画


`transform`可参考此 [文档](https://developer.mozilla.org/zh-CN/docs/Web/CSS/transform) 入门


`animation`可参考此 [文档](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation) 入门


**动画样式列表**


| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| transform-origin | `<position>` | 0px 0px | 变换原点位置，单位目前仅支持 px，格式为：50px 100px |
| transform | `<string>` | - | 见下面 transform 操作 |
| animation-name | `<string>` | - | 与@keyframes 的 name 相呼应，见下面@keyframes 属性 |
| animation-delay | `<time>` | 0 | 目前支持的单位为[ s(秒) | ms(毫秒) ] |
| animation-duration | `<time>` | 0 | 目前支持的单位为[ s(秒) | ms(毫秒) ] |
| animation-iteration-count | `<integer>` | `infinite` | 1 | 定义动画播放的次数，可设置为`infinite`无限次播放 |
| animation-timing-function | linear | ease | ease-in | ease-out | ease-in-out | cubic-bezier(`<number>`, `<number>`, `<number>`, `<number>`) | step-start | step-end | steps(number\_of\_steps[, step-direction]?) | ease | 规定动画的速度曲线 |
| animation-fill-mode | none | forwards | none | 规定当动画不播放时（当动画完成时，或当动画有一个延迟未开始播放时），要应用到元素的样式 |
| animation-direction | normal | reverse | alternate | alternate-reverse | normal | 定义动画播放的方向，详情请看[文档](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-direction) |


**注**：


- animation-timing-function 类型


cubic-bezier(`<number>`, `<number>`, `<number>`, `<number>`) | step-start | step-end | steps(number\_of\_steps[, step-direction]?) 后支持 。其中：


steps(number\_of\_steps，step-direction)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| number\_of\_steps | `<integer>` | - | 是 | 表示等间隔步数的正整数 |
| step-direction | jump-start | jump-end | jump-none | jump-both | start | end | end | 否 | 指示函数左连续或右连续的关键字 |


- cubic-bezier(x1, y1, x2, y2)


参数 x1, y1, x2, y2 是 `<number>` 类型的值，代表当前定义的立方贝塞尔曲线中的 P1 和 P2 点的横坐标和纵坐标，x1 和 x2 必须在 [0，1] 范围内，否则当前值无效。


### transform


| 名称 | 类型 |
| --- | --- |
| translate | `<length>` | `<percent>` |
| translateX | `<length>` | `<percent>` |
| translateY | `<length>` | `<percent>` |
| scale | `<number>` |
| scaleX | `<number>` |
| scaleY | `<number>` |
| rotate | `<deg>` |


### animation-fill-mode


animation-fill-mode 属性规定当动画不播放时（当动画完成时，或当动画有一个延迟未开始播放时），要应用到元素的样式。


默认情况下，CSS 动画在第一个关键帧播放完之前不会影响元素，在最后一个关键帧完成后停止影响元素。animation-fill-mode 属性可重写该行为。


| 值 | 描述 |
| --- | --- |
| none | 默认值。动画在动画执行之前和之后不会应用任何样式到目标元素。 |
| forwards | 在动画结束后（由 animation-iteration-count 决定），动画将应用该属性值。 |
| backwards`暂不支持` | 动画将应用在 animation-delay 定义期间启动动画的第一次迭代的关键帧中定义的属性值。 |
| both`暂不支持` | 动画遵循 forwards 和 backwards 的规则。 |


### animation-name


指定所采用的一系列动画，属性值的每个名称代表一个由 @keyframes 属性定义的关键帧序列。该属性支持在组件中应用单个动画或多个动画 ，应用多个动画时动画同时开始执行。


示例代码：


```

/\* 单个动画 \*/
animation-name: Color;
animation-name: translate;
animation-name: rotate;

/\* 多个动画 \*/
animation-name: Color, Opacity;
animation-name: Width, translate, rotate;
```

复制代码
### @keyframes


| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| background-color | `<color>` | - | - |
| opacity | `<number>` | - | - |
| width/height | `<length>` | - | 暂不支持百分比 |
| transform | `<string>` | - | - |


**注**：


暂时不支持起始值(0%)或终止值(100%)缺省的情况，都需显式指定。


---


<!-- 文档 2: ui-component/component/basic/a.md -->


## a

## a

更新时间：2025-07-10 10:44:44


超链接（默认不带下划线）。文本内容写在标签内容区，支持转义字符`"\"`


#### 子组件


支持[<span>](/component/basic/span)


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| href | `<string>` | - | 否 | 支持的格式参见[页面路由](/api/system/router)中的 uri 参数。额外的:- href 还可以通过“?param1=value1”的方式添加参数，参数可以在页面中通过`this.param1`的方式使用。
- href 暂不支持加载网页

示例:`<a href="About?param1=value1">关于</a>``<a href="/about?param1=value1">关于</a>`<br/ |


#### 样式


支持[<text>样式](/component/basic/text)


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| font-family | `<string>` | - | 否 | 文本字体。可设置一个有先后顺序的，由字体名或者字体族名组成的列表，以逗号分隔。列表中第一个已安装的字体，会被选中作为文本的字体。 |


#### 事件


支持[通用事件](/component/common/common-events/)


---


<!-- 文档 3: ui-component/component/basic/animated-vector.md -->


## animated-vector

## animated-vector

更新时间：2023-10-31 20:58:14


#### 概述


animated-vector 组件，用于解析渲染安卓 xml 动画资源。


xml 动画通过将矢量可绘制对象资源与属性动画资源通过 AAPT 内嵌资源格式在 xml 文件中定义来实现，可在[安卓开发者文档](https://developer.android.com/guide/topics/graphics/vector-drawable-resources?hl=zh_cn)中了解更多。


animated-vector 组件提供配置 xml 动画，进行播放，暂停等操作的能力，只支持单个 xml 文件结构的矢量可绘制对象资源。


#### 子组件


不支持


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| src | `<uri>` | - | 是 | xml 源文件的位置，仅支持本地单 xml 文件 |
| loop | `<boolean>` | false | 否 | 配置动画是否循环播放 |
| autoplay | `<boolean>` | true | 否 | 配置动画是否自动播放 (不能动态设置，只能首次设置) |


#### 样式


支持[通用样式](/component/common/common-events/)


#### 方法


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| start | - | 播放动画，如果动画正在播放则无效 |
| pause | - | 暂停播放动画 |
| resume | - | 继续播放动画 |
| stop | - | 停止播放动画 |


#### 事件


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| animationEnd | - | 在一轮动画播放完毕或停止播放后，触发此回调 |


#### 示例代码


```

<template>
  <div>
    <animated-vector
 id="xml\_id"
 src="common/xml/ex.xml"
 @animationEnd="animationEnd"
 ></animated-vector>
  </div>
</template>
<script>
 export default {
 animationEnd() {
 prompt.showToast({
 message: 'animation end!',
 })
 },
 start() {
 this.$element('xml\_id').start()
 },
 pause() {
 this.$element('xml\_id').pause()
 },
 resume() {
 this.$element('xml\_id').resume()
 },
 stop() {
 this.$element('xml\_id').stop()
 },
 }
</script>
```

复制代码


---


<!-- 文档 4: ui-component/component/basic/animation-overview.md -->


## 概述

## 概述

更新时间：2023-10-30 17:10:04


提供用于实现页面元素动画效果的 UI 组件，通常用于增强用户交互体验，吸引用户的注意力，提高页面的美观度和可视化效果。


### 动画组件介绍


| 组件 | 简述 |
| --- | --- |
| svg-container | 渲染 svg 图片，可以动态修改 svg 属性 |
| image-animator | 图片帧动画播放器 |
| animated-vector | animated-vector 组件，用于解析渲染安卓 xml 动画资源 |


---


<!-- 文档 5: ui-component/component/basic/arc-text.md -->


## arc-text

## arc-text

更新时间：2023-10-20 10:02:06


弧形文本，文本内容展示在 arc-text 组件盒模型内最大且居中的圆周上，超出的内容将会被截断。


如下图示例


弧
形
文
本


.arc-text-eg {
 width: 150px;
 height: 100px;
 border: 1px solid #000;
 display: flex;
 justify-content: center;
}
.arc-text-eg-in {
 width: 98px;
 height: 98px;
 border: 1px solid #4761f6;
 border-radius: 98px;
 color: red;
}
.arc-text-eg-in-text {
 color: red;
}

#### 子组件


不支持


#### 属性


支持[通用属性](/component/common/common-attributes/)


#### 样式


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | `<color>` | #000000 | 否 | 文本颜色 |
| font-size | `<length>` | 30px | 否 | 文本尺寸 |
| font-weight | normal | bold | lighter | border | `<number>` | normal | 否 | 当前平台仅支持 normal 与 bold 两种效果 |
| direction | clockwise | counterclockwise | clockwise | 否 | 文本绘制方向，clockwise 顺时针方向，counterclockwise 逆时针方向。 |
| start-angle | `<deg>` | 0deg | 否 | 文本绘制起始角度，以时钟 0 点为基线，取值范围为 0 到 360。 |


#### 事件


支持[通用事件](/component/common/common-events/)


---


<!-- 文档 6: ui-component/component/basic/barcode.md -->


## barcode

## barcode

更新时间：2023-10-20 10:02:06


条形码，将文本内容转换为条形码展示。


#### 子组件


不支持


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| value | `<string>` | - | 是 | 条形码内容，码制为 Code128 码，长度小于等于 20 字节 |


#### 样式


支持[通用样式](/component/common/common-styles/)


#### 事件


支持[通用事件](/component/common/common-events/)


---


<!-- 文档 7: ui-component/component/basic/image-animator.md -->


## image-animator

## image-animator

更新时间：2023-12-21 13:49:50


图片帧动画播放器。


#### 属性


支持[通用属性](/component/common/common-attributes/)还支持如下属性：


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| images | `Array<ImageFrame>` | - | 是 | 设置图片帧信息集合。每一帧的帧信息包含图片路径、图片大小和图片位置信息。目前支持的图片格式为 png。 |
| predecode | `Number` | 0 | 否 | 是否启用预解码，默认值为 0，即不启用预解码，如该值设为 2，则播放当前页时会提前加载后面两张图片至缓存以提升性能 |
| iteration | number | string | infinite | 否 | 设置帧动画播放次数。number 表示固定次数，infinite 枚举表示无限次数播放。 |
| reverse | `boolean` | false | 否 | 设置播放顺序。false 表示从第 1 张图片播放到最后 1 张图片； true 表示从最后 1 张图片播放到第 1 张图片。 |
| fixedsize | `boolean` | true | 否 | 设置图片大小是否固定为组件大小。true 表示图片大小与组件大小一致，此时设置图片的 width 、height 、top 和 left 属性是无效的。false 表示每一张图片的独设置。 |
| duration | `String` | - | 是 | 每一帧图片的播放时长，单位支持[s(秒)或者 ms(毫秒)]，默认单位为 ms。示例:'1000ms' |
| fillmode | `String` | forwards | 否 | 指定帧动画执行结束后的状态。可选项有：none：恢复初始状态。forwards：保持帧动画结束时的状态 |
| transition-timing-function | `String` | linear | 否 | 运动曲线的[属性值](#motion)。 |
| poster | `String` | first | 否 | 设置帧动画不执行时的展示。可选项有：first：展示第一帧图片；last：展示最后一帧图片 |


ImageFrame 说明


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| src | `<uri>` | - | 是 | 图片路径，图片格式为 png。 |
| width | `<length>` | 0 | 否 | 图片宽度。示例:'100px' |
| height | `<length>` | 0 | 否 | 图片高度。 示例:'100px' |
| top | `<length>` | 0 | 否 | 图片相对于组件左上角的纵向坐标。示例:'100px' |
| left | `<length>` | 0 | 否 | 图片相对于组件左上角的横向坐标。 示例:'100px' |
| duration | `Number` | - | 否 | 每一帧图片的播放时长，单位毫秒。示例:100 |


##### transition-timing-function 属性值:


| 值 | 描述 |
| --- | --- |
| linear | 规定以相同速度开始至结束的过渡效果（等于 cubic-bezier(0,0,1,1)）。 |
| ease | 规定慢速开始，然后变快，然后慢速结束的过渡效果（cubic-bezier(0.25,0.1,0.25,1)）。 |
| ease-in | 规定以慢速开始的过渡效果（等于 cubic-bezier(0.42,0,1,1)）。 |
| ease-out | 规定以慢速结束的过渡效果（等于 cubic-bezier(0,0,0.58,1)）。 |
| ease-in-out | 规定以慢速开始和结束的过渡效果（等于 cubic-bezier(0.42,0,0.58,1)）。 |
| cubic-bezier(n,n,n,n) | 在 cubic-bezier 函数中定义自己的值。可能的值是 0 至 1 之间的数值。 |


#### 样式


支持[通用样式](/component/common/common-styles/)


#### 事件


支持[通用事件](/component/common/common-events/)外，还支持如下事件：


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| start | - | 帧动画启动时触发。 |
| pause | - | 帧动画暂停时触发。 |
| stop | - | 帧动画结束时触发。 |
| resume | - | 帧动画恢复时触发。 |
| updatetime | {currentTime} | 帧动画播放过程中触发。 |


#### 支持如下方法


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| start | - | 开始播放图片帧动画。再次调用，重新从第 1 帧开始播放。 |
| pause | - | 暂停播放图片帧动画。 |
| stop | - | 停止播放图片帧动画。 |
| resume | - | 继续播放图片帧。 |
| getState | - | 获取播放状态。playing：播放中。paused：已暂停 stopped：已停止。 |


#### 示例


```

<template>
  <div class="container">
    <image-animator class="animator" id="animator" images="{{frames}}" />
    <div class="btn-box">
      <input class="btn" type="button" value="start" onclick="handleStart" />
      <input class="btn" type="button" value="stop" onclick="handleStop" />
      <input class="btn" type="button" value="pause" onclick="handlePause" />
      <input class="btn" type="button" value="resume" onclick="handleResume" />
    </div>
  </div>
</template>

<script>
 export default {
 data: {
 frames: [
 {
 src: '/common/asserts/heart78.png',
 },
 {
 src: '/common/asserts/heart79.png',
 },
 ],
 },
 onReady() {
 let state = this.$element('animator').getState()

 switch (state) {
 case 'playing':
 //实现具体的业务逻辑
 break
 case 'paused':
 //实现具体的业务逻辑
 break
 case 'stopped':
 //实现具体的业务逻辑
 break
 }
 },
 handleStart() {
 this.$element('animator').start()
 },
 handlePause() {
 this.$element('animator').pause()
 },
 handleResume() {
 this.$element('animator').resume()
 },
 handleStop() {
 this.$element('animator').stop()
 },
 }
</script>
```

复制代码


---


<!-- 文档 8: ui-component/component/basic/image.md -->


## image

## image

更新时间：2024-03-15 09:29:57


渲染图片，不支持子组件、事件、方法


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| src | `<uri>` | - | 否 | 图片的 uri，支持本地图片和网络图片，支持的图片格式包括静态类型(png, svg, .9, gif) |
| alt | `<uri>` | 'blank' | - | 否 | 加载时显示的占位图；只支持本地图片资源(png)。 |


注意：alt 属性详情如下：


a.如果 Image 组件没有设置 alt 值，终端会加上默认的灰色占位图。


b.src 为本地图片地址时，不会有占位图


c.src 为远程图片地址时，如果之前已经成功加载过图片，有本地缓存，则不会有占位图


d.src 为远程图片地址时，且 Image 组件 的 alt 值传入字符串 "blank" 值，不会有占位图。（可避免一些远程地址的小图标第一次加载时瞬间闪烁的现象）


e.设置 alt 为本地图片地址时，占位图缩放模式由原来的居中不缩放改为居中保持宽高比缩放，减少了占位图资源文件的分辨率与体积大小


##### SVG 图片格式说明


| 完全支持的标签 | 描述 |
| --- | --- |
| `<path>` | 绘制路径。 |
| `<rect>` | 用于绘制矩形、圆角矩形。 |
| `<circle>` | 圆形形状。 |
| `<ellipse>` | 椭圆形状。 |
| `<line>` | 绘制线条。 |
| `<polyline>` | 绘制折线。 |
| `<polygon>` | 绘制多边形。 |
| `<linearGradient>` | 线性渐变。 |
| `<stop>` | 可縮放矢量圖形。 |
| `<g>` | 用于对其他 SVG 元素进行分组的容器。 |


| 受限制支持的标签 | 只支持的属性 |
| --- | --- |
| `<svg>` | width,height,viewBox 。 |
| `<defs>` | 只支持渐变的定义。 |
| `<style>` | 只支持部分属性。 |


| 暂时完全不支持的标签 | 描述 |
| --- | --- |
| `<radialGradient>` | 不支持文本，字体，动画，滤镜 |
| `<use>` | 不支持文本，字体，动画，滤镜 |
| `<image>` | 不支持文本，字体，动画，滤镜 |
| `<clipPath>` | 不支持文本，字体，动画，滤镜 |
| `<desc>` | 不支持文本，字体，动画，滤镜 |
| `<marker>` | 不支持文本，字体，动画，滤镜 |
| `<mask>` | 不支持文本，字体，动画，滤镜 |
| `<switch>` | 不支持文本，字体，动画，滤镜 |
| `<symbol>` | 不支持文本，字体，动画，滤镜 |
| `<title>` | 不支持文本，字体，动画，滤镜 |
| `<view>` | 不支持文本，字体，动画，滤镜 |
| `<pattern>` | 不支持文本，字体，动画，滤镜 |


#### 样式


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| object-fit | contain | cover | fill | none | scale-down | cover | 否 | 图片的缩放类型 |


object-fit ，参数列表如下：


| 类型 | 描述 |
| --- | --- |
| contain | 保持宽高比，缩小或者放大，使得图片完全显示在显示边界内，居中显示 |
| cover | 保持宽高比，缩小或者放大，使得两边都大于或等于显示边界，居中显示 |
| fill | 不保存宽高比，填充满显示边界 |
| none | 居中，无缩放 |
| scale-down | 保持宽高比，缩小或保持不变，取 `contain` 和 `none`中显示较小的一个，居中显示 |


##### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | `<string>` | - | 否 | 唯一标识 |
| style | `<string>` | - | 否 | 样式声明 |
| class | `<string>` | - | 否 | 引用样式表 |
| for | `<array>` | - | 否 | 根据数据列表，循环展开当前标签 |
| if | `<boolean>` | - | 否 | 根据数据 boolean 值，添加或移除当前标签 |
| src | `<uri>` | - | 否 | 图片的 uri，同时支持本地，支持的图片格式包括静态类型（png, svg, .9, gif） |


##### 样式


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| width | `<length>` | - | 否 | 图片的宽度，不设置时使用图片原始的宽度 |
| height | `<length>` | - | 否 | 图片的高度，不设置时使用图片原始的高度 |


---


<!-- 文档 9: ui-component/component/basic/marquee.md -->


## marquee

## marquee

更新时间：2025-08-13 20:11:57


跑马灯组件，用于展示一段滚动文字，默认为单行显示。


#### 子组件


不支持子组件。


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| scrollamount | `<number>` | 1 | 否 | 每秒滚动的距离，单位：px。 |
| loop | `<number>` | 3 | 否 | 滚动的次数，默认值为 3。 |
| direction | `<string>` | left | 否 | 滚动方向，可选值：`left`，`right` |
| text-offset | `<number>` | 0 | 否 | 设置内容首尾相接时的间距，需为大于 0 的整数，单位：px。 |
| double-ended-shadow | `<bool>` | true | 否 | 是否显示两端阴影效果。 |
| double-ended-shadow-color | `<color>` | rgb(0,0,0) | 否 | 两端阴影的颜色 |


#### 样式


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | `<color>` | rgba(0, 0, 0, 0.54) | 否 | 文字颜色。 |
| font-size | `<length>` | 30px | 否 | 文字大小。 |
| font-family | `<string>` | - | 否 | 字体名称，当前仅支持 `HYQiHei-65S`。 |
| text-align | left | center | right | left | 否 | 文字水平对齐方式。 |


#### 事件


支持[通用事件](/component/common/common-events/)


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| bounce | - | 当 marquee 滚动至末尾时触发 |
| finish | - | 当 marquee 按照 `loop` 属性设置的次数滚动完成时触发。仅当 `loop` 设置为大于 0 的数值时有效。 |
| start | - | 当 marquee 开始滚动时触发 |


#### 方法


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| start | - | 开始滚动 marquee |
| stop | - | 停止滚动 marquee |


#### 示例代码


```

<template>
  <div class="container">
    <marquee>这段文字展示跑马灯效果默认连续滚动ABCDEFGHIJKLMN</marquee>
    <marquee id="marquee" loop="1" onbounce="bounce" onfinish="finish" onstart="start">
      这段文字展示跑马灯效果滚动一次ABCDEFGHIJKLMN
    </marquee>
    <input type="button" class="btn" @click="startHandler" value="start" />
    <input type="button" class="btn" @click="stopHandler" value="stop" />
  </div>
</template>

<script>
 import prompt from '@system.prompt'
 export default {
 startHandler() {
 this.$element('marquee').start()
 },
 stopHandler() {
 this.$element('marquee').stop()
 },
 bounce() {
 prompt.showToast({
 message: 'bounce',
 })
 },
 finish() {
 prompt.showToast({
 message: 'finish',
 })
 },
 start() {
 prompt.showToast({
 message: 'start',
 })
 },
 }
</script>

<style>
 .container {
 width: 100%;
 height: 100%;
 flex-direction: column;
 align-items: center;
 justify-content: center;
 }
 marquee {
 width: 500px;
 height: 80px;
 color: #9acd32;
 font-size: 50px;
 margin: 20px 0;
 }
 .btn {
 width: 300px;
 height: 80px;
 text-align: center;
 border-radius: 5px;
 color: #ffffff;
 font-size: 30px;
 background-color: #0faeff;
 margin: 20px;
 }
</style>
```

复制代码


---


<!-- 文档 10: ui-component/component/basic/overview.md -->


## 概述

## 概述

更新时间：2023-10-31 19:37:39


作为组成复杂组件和应用的基础模块，基本的 UI 展示功能通常包括文本框、链接和图片等元素。这些 UI 组件是构建用户界面的重要基础，通过这些基本元素的组合与拼接，可以实现丰富多彩、充满个性化的 UI 设计。蓝河系统提供了这些基本 UI 展示功能的实现和支持，以帮助您快速构建和部署丰富多样的用户界面和互动性应用。


## 基础组件介绍

更新时间：2023-10-31 19:37:39


| 组件 | 简述 |
| --- | --- |
| a | 超链接 |
| image | 渲染图片，不支持子组件、事件、方法 |
| text | 文本，文本内容写在标签内容区 |
| span | 格式化的文本，只能作为子组件，不支持事件，目前不支持换行 |
| marquee | 跑马灯，用于插入一段滚动的文字，默认为单行 |
| progress | 进度条，不支持子组件 |
| arc-text | 弧形文本，文本内容展示在 arc-text 组件盒模型内最大且居中的圆周上，超出的内容将会被截断 |
| barcode | 条形码，将文本内容转换为条形码展示 |
| qrcode | 二维码，将文本内容转换为二维码展示 |
| canvas | 画布组件，通过使用 JavaScript 中的脚本，可以在 canvas 上绘制图形，文字等 |


---


<!-- 文档 11: ui-component/component/basic/physics-space.md -->


## physics-engine

## physics-engine

更新时间：2025-10-10 09:34:52


### 概述


物理引擎是一种用于模拟现实世界物理规律的能力，包括重力、碰撞、摩擦、弹性、刚体运动等，使应用中的物体行为更加自然、真实。


**基本概念：**


**空间 (Space)**


**空间**是物理引擎中用于模拟物理效果的容器。


在一个空间中，可以添加多个刚体（Body）和形状（Shape）。


每个 `physics-engine` 组件对应一个独立的空间实例。


**刚体 (Body)**


**刚体**用于描述物体的物理属性，例如质量、位置、旋转和速度等。


刚体本身没有形状，需要通过附加形状（Shape）来定义其外观和碰撞范围。


在一个 `physics-engine` 组件中，每个子组件都表示一个刚体。


**形状 (Shape)**


**形状**定义物体的表面属性，如摩擦力和弹性。


当形状附加到刚体上时，二者共同构成具有物理特性和几何形状的对象。


当前，每个刚体仅能绑定一个形状。


### 子组件


支持，子组件作为刚体载体，每个子组件映射为一个 Body。


### 属性


支持[通用属性](/component/common/common-attributes/)


### 样式


支持[通用样式](/component/common/common-events/)


### 方法


#### initSpace()


初始化空间，初始化属性及对应的值，可以同时设置多种属性


**参数**：


参数以下格式的 JSON 字符串，具体信息参考 [SpaceAttr](#spaceattr)


```

{
  space: {
    attribute_0: value_0,
    attribute_1: value_1,
    ...
  }
}
```

复制代码
**示例**：


```

this.$element('engine').initSpace(
  JSON.stringify({
    space: {
      gravityX: 0, //重力方向
      gravityY: 200, //重力方向为Y轴正方向，大小为200像素每秒
      touch: true, //可以通过touch修改刚体位置
      crown: 'scale', //对space中的刚体进行缩放
    },
  })
)
```

复制代码
#### setSpaceAttr()


设置空间属性及对应的值，可以同时设置多种属性。


**参数**：


参数以下格式的 JSON 字符串，具体信息参考 [SpaceAttr](#spaceattr)


```

{
  attribute_0: value_0,
  attribute_1: value_1,
  ...
}
```

复制代码
**示例**：


```

this.$element('engine\_test').setSpaceAttr(
  JSON.stringify({
    friction: 1,
  })
)
```

复制代码
#### initBody()


刚体初始化，可以同时完成多个参数的初始化


刚体初始化的顺序必须和 xml 中组件对象的顺序一致，否则会顺序错误


**参数**：


参数为以下格式的JSON字符串，具体body信息参考[BodyAttr](#bodyattr)


```

{
  init:[
    {
      //body\_0 相关属性
    },
    { 
      //body\_1 相关属性
    },
    ...
  ]
}
```

复制代码
**示例**：


```

this.$element('engine\_test').initBody(JSON.stringify({
  init: [
    {
      shape: 'circle',
      originX: 188,
      originY: 200,
      radius: 66,
      mass: 1,
      elasticity: 0.8,
      name: 'weather',
    },
    {
      shape: 'circle',
      originX: 200,
      originY: 200,
      radius: 85,
      mass: 1,
      elasticity: 0.8,
      name: 'pressure',
    },
  ],
}))
```

复制代码
#### setBodyAttr()


设置空间属性及对应的值，可以同时设置多种属性


**参数**：


参数为以下格式的JSON字符串，具体body信息参考[BodyAttr](#bodyattr)


```

{
    bodyName: {
        attribute_0: value_0,
        attribute_1: value_1,
        ......
    }
}
```

复制代码
**示例**：


```

// 设置名称为sleep的刚体 的enableRotation 属性为false
this.$element('engine\_test').setBodyAttr(
  JSON.stringify({
    sleep: {
      enableRotation: false,
    },
  })
)
```

复制代码
#### getBodyPosition()


获取刚体的实时位置


**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bodyName | string | 是 | 指定获取位置的刚体名称 |
| callback | CommonCallback<[BodyPosition](#bodyposition)> | 是 | 结果回调，返回刚体位置 |


**示例**：


```

// 获取名称为bird的刚体实时位置
this.$element('engine\_test').getBodyPosition('bird', {
  success: (position) => {
    // 成功获取位置数据
  },
  fail: (data, code) => {
    // 获取失败
  },
})
```

复制代码
#### getBodyVelocity()


获取刚体的实时速度


**参数**：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bodyName | string | 是 | 指定获取速度的刚体名称 |
| callback | CommonCallback<[BodyVelocity](#bodyvelocity)> | 是 | 结果回调，返回刚体速度 |


**示例**：


```

// 获取名称为bird的刚体实时速度
this.$element('engine\_test').getBodyVelocity('bird', {
  success: (velocity) => {
    // 成功获取速度数据
  },
  fail: (data, code) => {
    // 获取失败
  },
})
```

复制代码
### 数据对象


#### SpaceAttr


空间属性对象，下面属性都为非必填。


| 属性 | 类型 | 范围 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| iteration | uint32\_t | >0 | 10 | 用来设置物理空间(space)计算的精度，数值大则会占用更多的 CPU，数值小则计算精度变差，默认 10 可以满足大部分需求，**一般不建议修改** |
| gravityX | number(浮点数) | - | 0 | X 轴方向上重力的大小，当 gravityX 大于 0 时，表示空间(space)中所有普通刚体(body)都会受到 X 轴正方向的重力，反之则为 X 轴负方向的重力 |
| gravityY | number(浮点数) | - | 0 | Y 轴方向上重力的大小，当 gravityY 大于 0 时，表示空间(space)中所有普通刚体(body)都会受到 Y 轴正方向的重力，反之则为 Y 轴负方向的重力 |
| damping | number(浮点数) | >0 | 1 | 应用于空间(space)的简单阻尼量。值为 0.9 表示每个刚体(body)每秒将损失 10% 的速度。默认为 1。与重力一样，它可以在每个刚体(body)的基础上进行覆盖。 |
| collisionSlop | number(浮点数) | >0 | 0.1 | 允许的形状(shape)间重叠量。为了提高稳定性，请将其设置为尽可能高，但不要出现明显的重叠。默认值为 0.1。 |
| originX | number(浮点数) | - | 0 | 空间(space)原点 X 轴坐标。 |
| originY | number(浮点数) | - | 0 | 空间(space)原点 Y 轴坐标。 |
| height | number(浮点数) | >0 | 200 | 空间(space)的高度，仅设置为空间(space)为**方形时有效** |
| width | number(浮点数) | >0 | 200 | 空间(space)的宽度，仅设置为空间(space)为**方形时有效** |
| radius | number(浮点数) | >0 | 233 | 空间(space)的半径，仅设置为空间(space)为**圆形时有效** |
| polygonSides | number(无符号 32 位整数) | >2 | 12 | 空间(space)的边数，仅设置为空间(space)为**圆形时有效**，因为空间(space)不能真正的设置为圆形，所以使用正多边形模拟圆形效果，从实际效果上看，边数为 12 时效果就很好了，边数太多会增大 CPU 计算开销 |
| elasticity | number(浮点数) | [0,1] | 1 | 空间(space)边界的弹性，值为 0.0 时不会产生弹跳，而值为 1.0 时会产生“完美”的弹跳。 |
| friction | number(浮点数) | >= 0 | 1 | 空间(space)边界的摩擦系数。Chipmunk 使用库仑摩擦模型，值为 0.0 表示无摩擦。 |
| touch | boolean | - | false | 表示是否可以使用手指触摸的方式移动刚体(body)，默认为 false |
| crown | string | - | scale | 旋转表冠缩放空间(space)中的刚体(body) |
| |  | - | gravity\_up | 旋转表冠改变空间(space)中的重力大小 |
| |  | - | gravity\_angle | 旋转表冠改变空间(space)中的重力方向 |
| scaleMax | number(浮点数) | >=100 | 110 | 空间(space)中的刚体(body)最大放大的百分比，默认最大放大 110% |
| scaleMin | number(浮点数) | <=100 | 90 | 空间(space)中的刚体(body)最小缩小的百分比，默认最小缩小 90% |
| scale | number(浮点数) | >0 | 100 | 将空间(space)中的刚体(body)缩放到指定百分比，默认为 100% |
| running | boolean | - | true | 表示空间(space)是否是运行状态，当值为 false 时，不会进行任何计算 |
| shape | string | - | circle | 表示空间(space)是圆形 |
| |  | - | rect | 表示空间(space)是方形 |
| feature | string | - | planet | 表示特殊功能 planet，所有刚体(body)的重力方向指向空间(space)原点 |


#### BodyAttr


刚体属性对象，下面属性都为非必填。


| 属性 | 类型 | 范围 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| shape | string | | circle | 表示该刚体(body)绑定一个圆形形状(shape) |
| |  | | segment | 表示该刚体(body)绑定一个线段/条形状(shape)，可以用来做矩形 |
| |  | | poly | 表示该刚体(body)绑定一个多边形形状(shape)，**不建议使用，性能很差**，因为多边形的逻辑是由多个线段形状(shape)组合而成，所以一个四边型相当于 4 个线段形状(shape) |
| originX | number(浮点数) | - | 0 | 刚体(body)原点 X 轴坐标。 |
| originY | number(浮点数) | - | 0 | 刚体(body)原点 Y 轴坐标。 |
| mass | number(浮点数) | >= 0 | 0 | 刚体(body)质量，碰撞计算时需要。 |
| height | number(浮点数) | >= 0 | 0 | 刚体(body)的高度，仅设置刚体(body)为**线段形状** 时有效 |
| width | number(浮点数) | >= 0 | 0 | 刚体(body)的宽度，仅设置刚体(body)为**线段形状**时有效 |
| pivotX | number(浮点数) | - | - | 刚体(body)重心的 X 轴坐标，默认值为刚体(body)的中心，坐标轴的位置为以刚体中心为坐标轴原点的**笛卡尔坐标系** |
| pivotY | number(浮点数) | - | - | 刚体(body)重心的 Y 轴坐标，默认值为刚体(body)的中心，坐标轴的位置为以刚体中心为坐标轴原点的**笛卡尔坐标系** |
| velocityX | number(浮点数) | - | 0 | 刚体(body)在 X 轴的速度 |
| velocityY | number(浮点数) | - | 0 | 刚体(body)在 Y 轴的速度 |
| angularVelocity | number(浮点数) | - | 0 | 刚体(body)的旋转角速度，值大于 0 时是以刚体(body)重心顺时针旋转，值小于 0 时是以刚体(body)重心逆时针旋转。 |
| angle | number(浮点数) | - | 0 | 刚体(body)的旋转角度 |
| elasticity | number(浮点数) | 0-1 | 1 | 刚体(body)的弹性，值为 0.0 时不会产生弹跳，而值为 1.0 时会产生“完美”的弹跳。 |
| friction | number(浮点数) | >0 | 1 | 刚体(body)的摩擦系数。内部使用库仑摩擦模型，值为 0.0 表示无摩擦。 |
| name | string | - | item\_N | 刚体(body)的名称，可以用来查找刚体，如果不设置，则会被设置为"item\_" + 当前空间(space)中刚体(body)的编号。 |
| type | string | - | static | static 刚体(body) 不会受空间(space)和约束计算的影响，可以把它看为一堵墙或一个柱子，因为不会移动和旋转等，所以对性能的影响很小。 |
| |  | | kinematic | kinematic 刚体(body) 只受代码逻辑的影响不受空间(space)计算的影响，不受重力影响，质量无限大，因此不会对与其他刚体(body)的碰撞或力做出反应。kinematic 刚体(body)通过设置速度来控制，这将导致它们移动。kinematic 刚体(body)的典型例子可能包括移动平台等。接触或连接到 kinematic 刚体(body)的刚体(body)永远不会进入休眠状态，所以对性能影响较大 |
| |  | | 其他 | 普通刚体(body)，受空间(space)计算的影响。 |
| radius | number(浮点数) | >0 | 20 | 刚体(body)的半径，仅设置刚体(body)为**圆形**时有效 |
| collisionType | number(无符号 32 位整数) | string | uint32\_t：1-1000， string取值:oneWayUp, oneWayDown, oneWayLeft, oneWayRight | - | 刚体(body)碰撞类型，应用层可以设置一个值方便监听。 当使用 1-1000 的数值时，表示用户自定义的碰撞监听，js 端可以接收到返回的数据。 当使用 string 类型是，表示用户使用引擎内置的特殊碰撞方式的监听。 oneWayUp：其他刚体(body)从上往下可以和本刚体发生碰撞，其他方向的刚体(body)会穿透过去。 oneWayDown：其他刚体(body)从下往上可以和本刚体发生碰撞，其他方向的刚体(body)会穿透过去。 oneWayLeft：其他刚体(body)从左往右可以和本刚体发生碰撞，其他方向的刚体(body)会穿透过去。 oneWayRight：其他刚体(body)从右往左可以和本刚体发生碰撞，其他方向的刚体(body)会穿透过去。 |
| enableRotation | boolean | - | true | 刚体(body)碰撞/移动后，内部的子组件是否需要旋转，仅设置刚体(body)为**圆形**时有效 |
| vertsCount | number(无符号 32 位整数) | >2 | - | 刚体(body)形状(shape)的顶点数量，仅设置刚体(body)为**多边形**时有效 |
| verts | {x,y} 均为 number(浮点数) | - | - | 刚体(body)形状(shape)的顶点坐标值，仅设置刚体(body)为**多边形**时有效 |
| variable | boolean | - | true | 刚体(body)是否会被一些通用逻辑影响，目前只对通用放大 scale 产生影响，后续可能会增加。variable 为 false 时，空间(space)属性 crown 为 scale 时，刚体(body)不受旋转表冠的影响 |
| pivotJoint | {x,y} 均为 number(浮点数) | - | {0,0} | 刚体(body)可以设置一个旋转静态约束关节，坐标轴的位置为以刚体中心为坐标轴原点的**笛卡尔坐标系(其他坐标系都是屏幕坐标系)**。x, y 的值为 float 类型。 |
| dampedSpring | { p0\_x, p0\_y, p1\_x, p1\_y, restLength, stiffness, damping } 均为 number(浮点数) | - | { 0, 0, 0, 0, 0, 0, 10, } | 刚体(body)可以设置一个阻尼弹簧; p0\_x , p0\_y : 以刚体(body)中心为坐标轴原点的**笛卡尔坐标系(其他坐标系都是屏幕坐标系)，弹簧的一个端点。** p1\_x , p1\_y : 以空间(space)中心为坐标轴原点的**笛卡尔坐标系(其他坐标系都是屏幕坐标系)，弹簧的另一个端点。** restLength: 弹簧的复位长度。 stiffness: 弹簧的刚性。 damping: 弹簧的阻尼量。 |


#### BodyPosition


刚体在空间中的位置


| 名称 | 属性 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 刚体在 x 轴的位置 |
| y | number | 是 | 刚体在 y 轴的位置 |


#### BodyVelocity


刚体在空间中的速度


| 名称 | 属性 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 刚体在 x 轴的速度 |
| y | number | 是 | 刚体在 y 轴的位置 |


### 事件


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | - | 碰撞事件，当有刚体碰撞时，触发此回调 |


### 示例


#### 初始化


```

<template>
  <physics-engine id="space">
    <stack id="weather">
      <image></image>
    </stack>

    <stack id="kcal">
      <image></image>
      <text>calorie</text>
    </stack>
  </physics-engine>
</template>

<script>
 // space 属性参数
 let spaceConfig = {
 space: {
 //重力方向
 gravityX: 0,
 gravityY: 199,
 crown: 'scale',
 scaleMax: 105,
 scaleMin: 80,
 friction: 0.1,
 },
 }

 // 刚体属性参数
 let bodyConfig = {
 init: [
 {
 shape: 'circle', //圆形
 originX: 348, // 初始X轴坐标
 originY: 200, // 初始Y轴坐标
 radius: 60, // 圆形半径
 mass: 1, // 刚体质量
 elasticity: 0.3, // 弹性系数
 friction: 0.1,
 name: 'weather', // 刚体名称
 },
 {
 shape: 'segment', //条形
 originX: 180, // 初始X轴坐标
 originY: 385, // 初始Y轴坐标
 width: 143, // 宽度143
 height: 0, // 高度为0 ，表示为水平方向，高度通过下面的radius来设置
 radius: 39, // 半径为45意味着height为90
 mass: 1, // 刚体质量
 elasticity: 0.3, // 弹性系数
 friction: 0.1,
 name: 'kcal', // 刚体名称
 },
 ],
 }

 export default {
 onShow() {
 this.$element('space').initSpace(JSON.stringify(spaceConfig)) //初始化物理引擎space参数
 this.$element('space').initBody(JSON.stringify(bodyConfig)) //初始化物理引擎刚体参数
 this.spaceRunning()
 },
 spaceRunning() {
 // 将刚体running 属性设置为true，使物理引擎运行起来
 this.$element('space').setSpaceAttr(
 JSON.stringify({
 space: {
 running: true,
 },
 })
 )
 },
 }
</script>
```

复制代码
#### 监听碰撞事件


碰撞回调


```

<template>
  <physics-engine @change="onCollision" />
</template>
<script>
 export default {
 onCollision(evt) {
 let event = JSON.parse(evt["info"])
 }
 }
</script>
```

复制代码
返回数据分为两种，根据 collisionType 的类型来区分：


- 用户自定义碰撞，返回碰撞监听编号
- 系统内置碰撞类型，返回特殊的碰撞状态


当刚体(body)的 collision\_type 为用户自定义的碰撞监听时，以上示例中 event 的值为：


```

{
  x: XXX //碰撞点的X轴坐标
  y: XXX //碰撞点的Y轴坐标
  collision_type: XXX // 用户自定义的碰撞监听编号，1-1000
  bodyA: XXX // 碰撞刚体A的名称
  bodyB: XXX // 碰撞刚体B的名称
}
```

复制代码
当刚体(body)的 collision\_type 为系统内置(onway\_up/onway\_down/onway\_left/onway\_right)的碰撞监听时，onCollision 将会在两个刚体(body)开始碰撞和分离时分别收到 event。


当刚体(body)发生碰撞时：


```

{
    bodyA: XXX // 碰撞刚体A的名称
    bodyB: XXX // 碰撞刚体B的名称
    collisionType: XXX // 系统内置的碰撞监听string名称
    action： "colliding" // 两个刚体碰撞开始
    flag： XXX // 表示两个刚体是否要发生碰撞，false表示需要发生碰撞，true表示不需要发生碰撞，两个刚体会发生穿透
}
```

复制代码
当刚体(body)分离时：


```

{
    bodyA: XXX // 碰撞刚体A的名称
    bodyB: XXX // 碰撞刚体B的名称
    collisionType: XXX // 系统内置的碰撞监听string名称
    action： "separate"// 两个刚体开始分离
}
```

复制代码
**注意：当刚体碰撞到空间(space)的边缘时，bodyB 为"edge"。**


---


<!-- 文档 12: ui-component/component/basic/progress.md -->


## progress

## progress

更新时间：2025-07-08 14:41:29


进度条，不支持子组件，支持[通用事件](/component/common/common-events/)


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| percent | `<number>` | 0 | 否 | 当前进度 |
| type | horizontal | arc | horizontal | 否 | 进度条类型，不支持动态修改 |


#### 样式


支持[通用样式](/component/common/common-styles/)


horizontal progress 底色为(136, 136, 136)


arc progress 默认宽高为 32px，宽高设置不一致时，arc 图标为宽高的较小值


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | `<color>` | `#33b4ff` | 否 | 进度条的颜色 |
| stroke-width | `<length>` | 32px | 否 | 进度条的宽度 |
| background-color `deprecated` | `<color>` | `#f0f0f0` | 否 | 进度条的背景颜色，该属性已经废弃，仅手表设备有支持 |
| layer-color | `<color>` | `#f0f0f0` | 否 | 进度条的背景颜色 |
| start-angle | `<deg>` | - | 否 | 弧形进度条起始角度，以时钟 0 点为基线，取值范围为 0 到 360（顺时针）。 |
| total-angle | `<deg>` | - | 否 | 弧形进度条总长度，范围为-360 到 360，负数标识起点到终点为逆时针。 |


#### 方法


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| progressTo | Object | 设置进度条到指定进度 |


**progressTo 的参数说明:**


| 名称 | 类型 | 是否必选 | 默认值 | 备注 |
| --- | --- | --- | --- | --- |
| progress | Number | 是 | 无 | 进度条的目标进度 |
| foreground | `<color>` | 否 | 无 | 进度条的目标颜色 |
| background | `<color>` | 否 | 无 | 进度条背景的目标颜色 |
| duration | Number | 否 | 500 | 动画持续时间，单位为 ms |
| timingFunction | String | 否 | ease | 绘制进度条的动画速度曲线，支持 linear |ease |ease-in |ease-out | ease-in-out |cubic-bezier(<number>, <number>, <number>, <number>) |


**timingFunction 说明**


| 值 | 说明 |
| --- | --- |
| linear | 表示动画以匀速运动 |
| ease | 表示动画在中间加速，在结束时减速 |
| ease-in | 表示动画一开始较慢，随着动画属性的变化逐渐加速，直至完成 |
| ease-out | 表示动画一开始较快，随着动画的进行逐渐减速 |
| ease-in-out | 表示动画属性一开始缓慢变化，随后加速变化，最后再次减速变化 |
| cubic-bezier(<number>, <number>, <number>, <number>) | 开发者自定义的三次贝塞尔曲线，其中第一位参数和第三位参数的值必须在 0 到 1 的范围内 |


---


<!-- 文档 13: ui-component/component/basic/qrcode.md -->


## qrcode

## qrcode

更新时间：2023-12-21 13:49:50


二维码，将文本内容转换为二维码展示。


#### 子组件


不支持


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| value | `<string>` | - | 是 | 二维码内容，长度小于等于 400 字节 |
| eclevel | `<number>` | 1 | 否 | 二维码纠错等级 取值范围为 0 到 3 |
| type | normal | circle | normal | 否 | 二维码样式设置 normal 常规样式，circle 圆点样式 |


#### 样式


支持[通用样式](/component/common/common-styles/)


#### 事件


支持[通用事件](/component/common/common-events/)


---


<!-- 文档 14: ui-component/component/basic/span.md -->


## span

## span

更新时间：2023-10-20 10:02:06


格式化的文本，只能作为[<text>](/component/basic/text)子组件，不支持事件，目前不支持换行。


#### 属性


支持[通用属性](/component/common/common-attributes/)


#### 样式


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | `<color>` | #000000 | 否 | 文本颜色 |
| font-size | `<length>` | 30px | 否 | 文本尺寸 |
| font-weight | normal | bold | lighter | border | `<number>` | normal | 否 | 当前平台仅支持 normal 与 bold 两种效果 |


---


<!-- 文档 15: ui-component/component/basic/svg-container.md -->


## svg-container

## svg-container

更新时间：2024-10-11 11:55:18


渲染 svg 图片，可以动态修改 svg 属性


#### 子组件


无


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| src | `<uri>` | - | 是 | 只支持本地 uri |


##### 支持动态修改的属性说明：


###### 基本图形属性


| 标签 | 属性 | 描述 | 备注 |
| --- | --- | --- | --- |
| rect | x | 横坐标 | |
| | y | 纵坐标 | |
| | rx | 水平角半径 | |
| | ry | 垂直角半径 | |
| | width | 宽度 | |
| | height | 高度 | |
| circle | cy | 圆心纵坐标 | |
| | cx | 圆心横坐标 | |
| | r | 圆的半径 | |
| ellipse | cy | 圆心纵坐标 | |
| | cx | 圆心横坐标 | |
| | rx | 水平半径 | |
| | ry | 垂直半径 | |
| line | x1 | 起点横坐标 | |
| | y1 | 起点纵坐标 | |
| | x2 | 终点横坐标 | |
| | y2 | 终点纵坐标 | |


###### 渐变属性


| 标签 | 属性 | 描述 |
| --- | --- | --- |
| <linearGradient> | x1 | 线性渐变起点横坐标 |
| | y1 | 线性渐变起点纵坐标 |
| | x2 | 线性渐变终点横坐标 |
| | y2 | 线性渐变终点纵坐标 |
| | gradientUnits | 渐变作用域 |
| | spreadMethod | 渐变扩散模式 |
| <stop> | offset | 渐变颜色位置 |
| | stop-color | 渐变色 |
| | stop-opacity | 渐变透明度 |


###### 通用属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| fill | `<color>` | black | 否 | 使用简写属性设置元素的填充色。 |
| fill-opacity | `number` | 1 | 否 | 填充色的透明度，取值范围为 0 到 1，1 表示为不透明，0 表示为完全透明。 |
| fill-rule | `<string>` | nonzero | 否 | nonzero:非零规则; evenodd:奇偶规则 |
| opacity | `number` | 1 | 否 | 元素的透明度，取值范围为 0 到 1，1 表示为不透明，0 表示为完全透明。 |
| stroke | `<color>` | - | 否 | 设置形状轮廓的颜色。 |
| stroke-linejoin | `<string>` | miter | 否 | 进行描边时在路径的拐角处使用的形状。bevel：使用斜角连接路径段；miter：使用尖角连接路径段；round：使用圆角连接路径段。 |
| stroke-linecap | `<string>` | butt | 否 | 路径描边时在它们的结尾处使用的形状。butt：不在路径两端扩展；round：在路径的末端延伸半个圆，直径等于线度。square：在路径的末端延伸半个圆，宽度等于线宽的一半，高度等于线宽。 |
| stroke-miterlimit | `number` | 4 | 否 | 设置将锐角绘制成斜角的极限值。 |
| stroke-opacity | `number` | 1 | 否 | 轮廓线条的透明度，取值范围为 0 到 1，1 表示为不透明，0 表示为完全透明。 |
| stroke-width | `<length>` | 1 | 否 | 设置轮廓线条的宽度。 |


#### 样式


支持[通用样式](/component/common/common-styles/)


#### 方法


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| setSvgAttr | Object | 设置属性 |


##### setSvgAttr 的参数说明


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | `<string>` | 无 | 是 | svg 元素的 ID |
| name | `<string>` | 无 | 是 | 属性名 |
| value | `<string>` | 无 | 是 | 属性值 |


#### 示例代码：


```

<template>
  <div>
    <svg-container
 id="svgId"
 src="../common/svg/a.svg"
 @animationEnd="animationEnd"
 ></svg-container>
  </div>
</template>
<script>
 export default {
 onInit() {
 this.$element('svgId').setSvgAttr({
 id: 'text',
 name: 'fill',
 value: 'red',
 })
 },
 animationEnd() {
 console.log('animationEnd')
 },
 }
</script>
```

复制代码


---


<!-- 文档 16: ui-component/component/basic/text.md -->


## text

## text

更新时间：2023-10-20 10:02:06


文本，文本内容写在标签内容区


#### 子组件


支持[<span>](/component/basic/span)


#### 属性


支持[通用属性](/component/common/common-attributes/)


#### 样式


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| min-width | `<length>` | `<percentage>` | - | 否 | 指定元素的最小宽度 |
| min-height | `<length>` | `<percentage>` | - | 否 | 指定元素的最小高度 |
| max-width | `<length>` | `<percentage>` | - | 否 | 指定元素的最大宽度 |
| max-height | `<length>` | `<percentage>` | - | 否 | 指定元素的最大高度 |
| lines | `<number>` | -1 | 否 | 文本行数，-1 代表不限定行数 |
| color | `<color>` | `#757575` | 否 | 文本颜色 |
| font-size | `<length>` | 30px | 否 | 文本尺寸 |
| font-weight | normal | bold | lighter | border | | normal | 否 | 当前平台仅支持 normal 与 bold 两种效果 |
| text-decoration | underline | line-through | none | none | 否 | 用于设置文本的修饰线外观 |
| text-align | left | center | right | left | 否 | 文本的水平对齐方式。 |
| line-height | `<length>` | - | 否 | 行高设置 |
| text-overflow | clip | ellipsis | clip | 否 | 在设置了行数的情况下生效 |


#### 事件


支持[通用事件](/component/common/common-events/)


---


<!-- 文档 17: ui-component/component/color.md -->


## 颜色样式

## 颜色样式

更新时间：2023-10-30 22:39:21


蓝河应用支持[颜色值类型](/component/common/common-styles)


开发者可参考 [MDN 文档](https://developer.mozilla.org/zh-CN/docs/Web/CSS/color_value) 了解更多颜色值的入门知识


### 颜色值格式示例


- `'#f0f'` (#rgb)
- `'#ff00ff'` (#rrggbb)
- `'#ff00ff13'` (#rrggbbaa)
- `rgb(255, 0, 255)`
- `rgba(255, 255, 255, 1.0)`
- `black,white`


---


<!-- 文档 18: ui-component/component/common-attributes.md -->


## 通用属性

## 通用属性

更新时间：2023-10-31 17:06:23


通用属性，即所有组件都支持的属性。


开发者可以在所有的组件标签上都使用`通用属性`


### 示例代码


```

<template>
  <div>
    <text id="text1" class="text-normal">line 1</text>
    <text id="text2" class="text-normal red">line 2</text>
  </div>
</template>
```

复制代码
### 常规属性


| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| id | `<string>` | - | 唯一标识 |
| style | `<string>` | - | 样式声明 |
| class | `<string>` | - | 引用样式表 |
| disabled | `<boolean>` | false | 表明当前组件是否可用 |


### 渲染属性


| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| for | `<array>` | - | 根据数据列表，循环展开当前标签 |
| if | `<boolean>` | - | 根据数据 boolean 值，添加或移除当前标签 |
| show | `<boolean>` | - | 根据数据 boolean 值，显示或隐藏当前标签，相当于控制{ display: flex | none } |


渲染属性工作方式详见[ux 文件](/reference/configuration/ux-file)


注意：属性和样式不能混用，不能在属性字段中进行样式设置


---


<!-- 文档 19: ui-component/component/common-events.md -->


## 通用事件

## 通用事件

更新时间：2025-10-09 11:25:10


通用事件指所有组件均支持的事件回调。


开发者可以在组件标签上通过 `on{eventName}`（如 `onclick`）或 `@{eventName}`（如 `@click`）的形式注册事件处理函数。 两种写法的效果一致，其中 `@event` 是语法糖，更适用于框架风格的开发方式。


有关事件绑定的更多说明，请参考 [事件绑定](/reference/app-service/event-on) 文档。


### 示例代码


```

<template>
  <div>
    <text onclick="clickFunction1">line 1</text>
    <text @click="clickFunction2">line 2</text>
  </div>
</template>
```

复制代码

> 
> 注：请确保 `clickFunction1` 和 `clickFunction2` 在组件的逻辑代码中有相应定义。
> 
> 
> 


### 通用事件


| 名称 | 参数 | 描述 | 冒泡 |
| --- | --- | --- | --- |
| touchstart | [TouchEvent](#touchevent) | 手指刚触摸组件时触发 | 支持 |
| touchmove | [TouchEvent](#touchevent) | 手指触摸后移动时触发 | 支持 |
| touchend | [TouchEvent](#touchevent) | 手指触摸动作结束时触发 | 支持 |
| touchcancel | [TouchEvent](#touchevent) | 触摸操作被系统中断时触发，如来电、弹窗等 | 支持 |
| click | [MouseEvent](#mouseevent) | 用户点击组件时触发 | 支持 |
| longpress | [MouseEvent](#mouseevent) | 用户长按组件时触发 | 支持 |


### 事件对象


#### TouchEvent


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| type | string | 事件名称，如 touchstart、touchmove、click 等 |
| touches | [Touch](#touch)[] | 当前停留在屏幕中的触摸点信息的数组 |


#### Touch


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| clientX | number | 距离可见区域左边沿的 X 轴坐标，不包含任何滚动偏移。 |
| clientY | number | 距离可见区域上边沿的 Y 轴坐标，不包含任何滚动偏移以及状态栏和 titlebar 的高度。 |
| pageX | number | 距离可见区域左边沿的 X 轴坐标，包含任何滚动偏移。 |
| pageY | number | 距离可见区域上边沿的 Y 轴坐标，包含任何滚动偏移。（不包含状态栏和 titlebar 的高度） |
| offsetX | number | 距离事件触发对象左边沿 X 轴的距离 |
| offsetY | number | 距离事件触发对象上边沿 Y 轴的距离 |


#### MouseEvent


与 TouchEvent 中属性相同，表示鼠标事件相关的坐标信息。


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| clientX | number | 距离可见区域左边沿的 X 轴坐标，不包含任何滚动偏移。 |
| clientY | number | 距离可见区域上边沿的 Y 轴坐标，不包含任何滚动偏移以及状态栏和 titlebar 的高度。 |
| pageX | number | 距离可见区域左边沿的 X 轴坐标，包含任何滚动偏移。 |
| pageY | number | 距离可见区域上边沿的 Y 轴坐标，包含任何滚动偏移。（不包含状态栏和 titlebar 的高度） |
| offsetX | number | 距离事件触发对象左边沿 X 轴的距离 |
| offsetY | number | 距离事件触发对象上边沿 Y 轴的距离 |


### 实战示例


如下示例在一个 `div` 元素上绑定了 `click` 和 `touchmove` 事件，触发时打印事件信息：


```

<script>
 export default {
 data: {},
 click(event) {
 console.log('click event fired')
 },
 move(event) {
 console.log('move event touches:' + JSON.stringify(event.touches))
 },
 }
</script>

<template>
  <div class="w-full h-full flex justify-center items-center bg-white">
    <div
 class="w-4/5 h-1/5 bg-gray-700"
 onclick="click"
 ontouchmove="move"></div>
  </div>
</template>

<style>
@tailwind utilities;
</style>
```

复制代码
**打印结果如下，click 事件：**


```

move event touches:[
  {
    "offsetX": 296,
    "identifier": 0,
    "offsetY": 113.48148345947266,
    "clientY": 113.48148345947266,
    "clientX": 360,
    "pageY": 113.48148345947266,
    "pageX": 360
  }
]
```

复制代码

```

click event fired
```

复制代码


---


<!-- 文档 20: ui-component/component/common-methods.md -->


## 通用方法

## 通用方法

更新时间：2024-10-11 11:55:18


通用方法，提供给所有组件调用的方法


在组件使用`id`标记 id 属性后，开发者可通过`this.$element('idName')`获取 dom 节点，再调用以下列举的`通用方法`


`id`属性赋值可以查看此[文档](/component/common/common-attributes/#%E5%B8%B8%E8%A7%84%E5%B1%9E%E6%80%A7)入门


`this.$element`可以查看此[文档](/reference/configuration/script/#%E5%85%AC%E5%85%B1%E6%96%B9%E6%B3%95)入门


### getBoundingClientRect(Object object)


返回元素的大小及其相对于视窗的位置


#### 参数


Object object


| 属性 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| success | function | | 否 | 接口调用成功的回调函数 |
| fail | function | | 否 | 接口调用失败的回调函数 |


##### object.success 回调函数


###### 参数


Object rect


| 属性 | 类型 | 描述 |
| --- | --- | --- |
| left | number | 元素的左边界坐标 |
| right | number | 元素的右边界坐标 |
| top | number | 元素的上边界坐标 |
| bottom | number | 元素的下边界坐标 |
| width | number | 元素的宽度 |
| height | number | 元素的高度 |


#### 示例代码


```

<template>
  <div>
    <div id="box1" class="box-normal"></div>
    <div id="box2" class="box-normal"></div>
  </div>
</template>
<script>
 export default {
 onShow() {
 this.$element('box1').getBoundingClientRect({
 success: function (data) {
 const { top, bottom, left, right, width, height } = data
 prompt.showToast({
 message: `getBoundingClientRect结果： width:${width}, height:${height},
 top:${top}, bottom:${bottom}, left:${left}, right:${right}`,
 })
 },
 fail: (errorData, errorCode) => {
 prompt.showToast({
 message: `错误原因：${JSON.stringify(errorData)}, 错误代码：${errorCode}`,
 })
 },
 complete: function () {
 console.info('complete')
 },
 })
 },
 }
</script>
```

复制代码


---


<!-- 文档 21: ui-component/component/common-styles.md -->


## 通用样式

## 通用样式

更新时间：2025-02-20 20:02:23


通用样式，即所有组件都可以支持的样式


它们均与 css 的属性样式用法保持一致，开发者可写在`内联样式`或`<style>`标签里，实现组件样式的定制化


关于组件样式的设置，可以参考此[文档](/reference/configuration/style-sheet)入门


### 类型说明


#### 长度类型


| 名称 | 类型定义 | 描述 |
| --- | --- | --- |
| length | String |Number | 用于描述尺寸单位，输入为 number 类型时，使用 px 单位；输入为 string 类型时，需要显式指定像素单位，当前支持的像素单位有： px：逻辑尺寸单位。 |
| percentage | String | 百分比尺寸单位，如“50%”。 |


#### 颜色类型


| 名称 | 类型定义 | 描述 |
| --- | --- | --- |
| color | String |[颜色枚举字符串](#TypeColor) | 用于描述颜色信息。字符串格式如下： 'rgb(255, 255, 255)'  'rgba(255, 255, 255, 1.0)'  HEX 格式：'#rrggbb'，'#aarrggbb'  枚举格式：'black'，'white'。 |


#### 当前支持的颜色枚举


| 枚举名称 | 对应颜色 | 颜色 |
| --- | --- | --- |
| aliceblue | #f0f8ff | |
| antiquewhite | #faebd7 | |
| aqua | #00ffff | |
| aquamarine | #7fffd4 | |
| azure | #f0ffff | |
| beige | #f5f5dc | |
| bisque | #ffe4c4 | |
| black | #000000 | |
| blanchedalmond | #ffebcd | |
| blue | #0000ff | |
| blueviolet | #8a2be2 | |
| brown | #a52a2a | |
| burlywood | #deB887 | |
| cadetblue | #5f9ea0 | |
| chartreuse | #7fff00 | |
| chocolate | #d2691e | |
| coral | #ff7f50 | |
| cornflowerblue | #6495ed | |
| cornsilk | #fff8dc | |
| crimson | #dc143c | |
| cyan | #00ffff | |
| darkblue | #00008b | |
| darkcyan | #008b8b | |
| darkgoldenrod | #b8860b | |
| darkgray | #a9a9a9 | |
| darkgreen | #006400 | |
| darkgrey | #a9a9a9 | |
| darkkhaki | #bdb76b | |
| darkmagenta | #8b008b | |
| darkolivegreen | #556b2f | |
| darkorange | #ff8c00 | |
| darkorchid | #9932cc | |
| darkred | #8b0000 | |
| darksalmon | #e9967a | |
| darkseagreen | #8fbc8f | |
| darkslateblue | #483d8b | |
| darkslategray | #2f4f4f | |
| darkslategrey | #2f4f4f | |
| darkturquoise | #00ced1 | |
| darkviolet | #9400d3 | |
| deeppink | #ff1493 | |
| deepskyblue | #00bfff | |
| dimgray | #696969 | |
| dimgrey | #696969 | |
| dodgerblue | #1e90ff | |
| firebrick | #b22222 | |
| floralwhite | #fffaf0 | |
| forestgreen | #228b22 | |
| fuchsia | #ff00ff | |
| gainsboro | #dcdcdc | |
| ghostwhite | #f8f8ff | |
| gold | #ffd700 | |
| goldenrod | #daa520 | |
| gray | #808080 | |
| green | #008000 | |
| greenyellow | #adff2f | |
| grey | #808080 | |
| honeydew | #f0fff0 | |
| hotpink | #ff69b4 | |
| indianred | #cd5c5c | |
| indigo | #4b0082 | |
| ivory | #fffff0 | |
| khaki | #f0e68c | |
| lavender | #e6e6fa | |
| lavenderblush | #fff0f5 | |
| lawngreen | #7cfc00 | |
| lemonchiffon | #fffacd | |
| lightblue | #add8e6 | |
| lightcoral | #f08080 | |
| lightcyan | #e0ffff | |
| lightgoldenrodyellow | #fafad2 | |
| lightgray | #d3d3d3 | |
| lightgreen | #90ee90 | |
| lightpink | #ffb6c1 | |
| lightsalmon | #ffa07a | |
| lightseagreen | #20b2aa | |
| lightskyblue | #87cefa | |
| lightslategray | #778899 | |
| lightslategrey | #778899 | |
| lightsteelblue | #b0c4de | |
| lightyellow | #ffffe0 | |
| lime | #00ff00 | |
| limegreen | #32cd32 | |
| linen | #faf0e6 | |
| magenta | #ff00ff | |
| maroon | #800000 | |
| mediumaquamarine | #66cdaa | |
| mediumblue | #0000cd | |
| mediumorchid | #ba55d3 | |
| mediumpurple | #9370db | |
| mediumseagreen | #3cb371 | |
| mediumslateblue | #7b68ee | |
| mediumspringgreen | #00fa9a | |
| mediumturquoise | #48d1cc | |
| mediumvioletred | #c71585 | |
| midnightblue | #191970 | |
| mintcream | #f5fffa | |
| mistyrose | #ffe4e1 | |
| moccasin | #ffe4b5 | |
| navajowhite | #ffdead | |
| navy | #000080 | |
| oldlace | #fdf5e6 | |
| olive | #808000 | |
| olivedrab | #6b8e23 | |
| orange | #6b8e23 | |
| orchid | #da70d6 | |
| palegoldenrod | #eee8aa | |
| palegreen | #98fb98 | |
| paleturquoise | #afeeee | |
| palevioletred | #db7093 | |
| papayawhip | #ffefd5 | |
| peachpuff | #ffdab9 | |
| peru | #cd853f | |
| pink | #ffc0cb | |
| plum | #dda0dd | |
| powderblue | #b0e0e6 | |
| purple | #800080 | |
| rebeccapurple | #663399 | |
| red | #ff0000 | |
| rosybrown | #bc8f8f | |
| royalblue | #4169e1 | |
| saddlebrown | #8b4513 | |
| salmon | #fa8072 | |
| sandybrown | #f4a460 | |
| seagreen | #2e8b57 | |
| seashell | #fff5ee | |
| sienna | #a0522d | |
| silver | #c0c0c0 | |
| skyblue | #87ceeb | |
| slateblue | #6a5acd | |
| slategray | #708090 | |
| slategrey | #708090 | |
| snow | #fffafa | |
| springgreen | #00ff7f | |
| steelblue | #4682b4 | |
| tan | #d2b48c | |
| teal | #008080 | |
| thistle | #d8Bfd8 | |
| tomato | #ff6347 | |
| turquoise | #40e0d0 | |
| violet | #ee82ee | |
| wheat | #f5deb3 | |
| white | #ffffff | |
| whitesmoke | #f5f5f5 | |
| yellow | #ffff00 | |
| yellowgreen | #9acd32 | |


### 示例代码


```

<template>
  <div>
    <div class="box-normal" style="background-color: #f00"></div>
    <div class="box-normal"></div>
  </div>
</template>
<style>
 .box-normal {
 background-color: #ff0;
 width: 100px;
 height: 100px;
 }
</style>
```

复制代码
### 属性列表


**注**：


通用样式均为非必填项。


| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| width | `<length>` | `<percentage>` | - | 未设置时使用组件自身内容需要的宽度 |
| height | `<length>` | `<percentage>` | - | 未设置时使用组件自身内容需要的高度 |
| padding | `<length>` | 0 | 简写属性，在一个声明中设置所有的内边距属性，该属性可以有 1 到 4 个值，具体请参考[MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding)文档 |
| padding-[left|top|right|bottom] | `<length>` | 0 | 设置一个元素的某个方向的内边距，padding 区域指一个元素的内容和其边界之间的空间，该属性不能为负值。 |
| margin | `<length>` | 0 | 简写属性，在一个声明中设置所有的外边距属性，该属性可以有 1 到 4 个值，具体请参考 [MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin)文档 |
| margin-[left|top|right|bottom] | `<length>` | 0 | 设置一个元素的某个方向的外边距，该属性不能为负值 |
| border | - | 0 | 简写属性，在一个声明中设置所有的边框属性，可以按顺序设置属性 width style color，不设置的值为默认值 |
| border-[left|top|right|bottom] | - | 0 | 简写属性，在一个声明中设置对应位置的所有边框属性，可以按顺序设置属性 width style color，不设置的值为默认值 |
| border-style | solid | solid | 暂时仅支持 1 个值，为元素的所有边框设置样式 |
| border-width | `<length>` | 0 | 简写属性，在一个声明中设置元素的所有边框宽度，或者单独为各边边框设置宽度，具体请参考 [MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-width) 文档 |
| border-[left|top|right|bottom]-width | `<length>` | 0 | 为元素的某个方向的边框设置边框宽度 |
| border-color | `<color>` | black | 简写属性，在一个声明中设置元素的所有边框颜色，或者单独为各边边框设置颜色，颜色值的填入请参考 [颜色配置](/component/common/color) |
| border-[left|top|right|bottom]-color | `<color>` | black | 颜色值的填入请参考 [颜色配置](/component/common/color) |
| border-radius | `<length>` | `<percentage>` | 0 | border-radius 属性允许你设置元素的外边框圆角。设置时需要同时设置 border-width、border-color，单独设置 border-[left|top|right|bottom]-width，border-[left|top|right|bottom]-color 时 border-radius 无效 |
| border-[top|bottom]-[left|right]-radius | `<length>` | `<percentage>` | 0 | 设置四个角的圆角弧度 |
| background | `<linear-gradient>` | - | 暂时不能与 background-color、background-image 同时使用 |
| background-color | `<color>` | - | 颜色值的填入请参考 [颜色配置](/component/common/color) |
| color | `<color>` | - | 颜色值的填入请参考 [颜色配置](/component/common/color) |
| background-image | `<uri>` | - | 暂时不支持与 background-color，border-color 同时使用；支持本地图片资源；暂不支持网络图片资源 |
| background-size | contain | cover | auto | `<length>` | `<percentage>` | auto auto | 设置背景图片大小 |
| background-repeat | repeat-x | repeat-y | no-repeat | repeat | repeat | 设置是否及如何重复绘制背景图像 |
| background-position | `<length>` |`<percentage>`| left | right | top | bottom | center | 0px 0px | 描述了背景图片在容器中绘制的位置，支持 1-4 个参数 |
| opacity | `<number>` | 1 | opacity 属性指定了一个元素的透明度。 |
| display | flex | none | flex | 蓝河应用只支持 flex 布局；将当前元素的 display 设置为 none 蓝河应用页面将不渲染此元素 |
| visibility | visible | hidden | visible | visibility 属性控制显示或隐藏元素而不更改文档的布局 |
| flex-direction | column | row | column-reverse | row-reverse | row | 默认为横向`row`，父容器为`<div>、<list-item>`时生效 |
| align-items | stretch | flex-start | flex-end | center | flex-start | align-items 定义了伸缩项目可以在伸缩容器的当前行的侧轴上对齐方式。flex-start(默认值)：伸缩项目在侧轴起点边的外边距紧靠住该行在侧轴起始的边。flex-end：伸缩项目在侧轴终点边的外边距靠住该行在侧轴终点的边 。center：伸缩项目的外边距盒在该行的侧轴上居中放置。stretch：伸缩项目拉伸填充整个伸缩容器。 |
| justify-content | flex-start | flex-end | center | space-between | space-around | flex-start | justify-content 定义了伸缩项目沿着主轴线的对齐方式。flex-start(默认值)：伸缩项目向一行的起始位置靠齐。flex-end：伸缩项目向一行的结束位置靠齐。center：伸缩项目向一行的中间位置靠齐。space-between：伸缩项目会平均地分布在行里。第一个伸缩项目一行中的最开始位置，最后一个伸缩项目在一行中最终点位置。space-around：伸缩项目会平均地分布在行里，两端保留一半的空间。 |
| position | fixed | absolute | relative | relative | 父容器为`<list>、<swiper>`时不生效，scroll 不支持 。 |
| [left|top|right|bottom] | `<length>` | - | 一般配合`fixed`或`absolute`布局使用 |


**注意**：


flex 布局仅支持上面列出的样式，w3c 中的其他标准切勿使，如 `flex: 1;`，否则将会产生无法预知的布局问题。


---


<!-- 文档 22: ui-component/component/component-animation.md -->


## 组件动画

## 组件动画

更新时间：2025-10-09 11:25:10


除了提供常规的 CSS 样式动画，蓝河应用还具备 JS 组件动画的方法。相比于 CSS 样式动画，这种动画方式拥有更为灵活、个性化的逻辑控制能力。


### Element.animate()


创建一个 `Animation` 对象实例；调用其 `play` 方法，即可执行动画，表现为一系列变换 （位置、大小、旋转角度、背景颜色和不透明度）。


#### 语法


```

const element = this.$element('elementIdName')
const animation = element.animate(keyframes, options)
animation.play()
```

复制代码
#### 参数


##### keyframes 关键帧


关键帧：动画序列中定义关键帧的样式来控制 CSS 动画序列中的中间步骤。


代表关键帧的一个数组集合，支持的属性有：


| 名称 | 类型 | 必填 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| time | number | 是 | - | 表示在哪个阶段触发这个帧所包含的样式，0 表示开始时刻，100 表示结束时刻。 |
| width | number | 否 | - | 组件宽度 |
| height | number | 否 | - | 组件高度 |
| left/right/top/bottom | number | 否 | - | 组件定位值，当组件设置了 position 样式时生效，left 优先于 right，top 优先于 bottom |
| opacity | number | 否 | 1 | 组件不透明度 |
| transform | object | 否 | - | 变换类型，支持下表列出的属性。 |
| transformOrigin | string | 否 | '50% 50%' | 变化中心点和 transform 搭配使用，第一个参数代表 x 轴位置，第二个参数代表 y 轴位置，单位 px 或百分比值；如："0 0"或者"10px 10px"或者"30% 50%" |


如上 `transform` 参数说明如下：


| 参数名 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| translate/translateX/translateY | string | - | 指定元素要移动到的位置，例如: `translate: 10px 10px`, `translateX: 10px`,`translateY: 10px` |
| scale/scaleX/scaleY | number | - | 按比例放大或缩小元素，例如：`scale: 1.5`, `scale: 1.5 2`, `scaleX: 2`, `scaleY: 2` |
| rotate | string | - | 指定元素将被旋转的角度，例如： `rotate: 45deg` |


**示例 1：中心旋转**


```

[
  {
    time: 0,
    transform: {
      rotate: '0deg',
    },
  },
  {
    time: 100,
    transform: {
      rotate: '360deg',
    },
  },
]
```

复制代码
**示例 2：左上角为中心旋转**


```

[
  {
    time: 0,
    transform: {
      rotate: '0deg',
    },
    transformOrigin: '0px 0px',
  },
  {
    time: 100,
    transform: {
      rotate: '360deg',
    },
    transformOrigin: '0px 0px',
  },
]
```

复制代码
##### options 可选项


| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| id | `<string>` | 从'0'开始自减的 string | 动画 id。为减小内存消耗，请开发者尽可能使用该字段复用动画。注：1. 复用动画后，被复用的前一个动画的 onfinish 等实例事件将被清除，不被触发； 2. 请勿使用从'0'开始自减的 string 作为 id，以免与引擎内部 id 重复。 |
| delay | `<number>` | 0 | 延迟动画开始的毫秒数。 |
| fill | "forwards" | "none" | "none" | 在动画完成播放（"forwards"）之后保留，"none" 动画执行前后不会应用任何样式到目标元素 |
| duration | `<number>` | 0 | 每次迭代动画完成所需的毫秒数。如果此值为 0，则不会运行动画。 |
| easing | linear | ease | ease-in | ease-out | ease-in-out | 自定义 cubic-bezier，例如`cubic-bezier(0.42, 0, 0.58, 1)` | linear | 动画的变化率，随着时间的推移而变化。 |


#### 实例方法


| 方法 | 参数 | 描述 |
| --- | --- | --- |
| play | - | 开始执行动画 |
| finish | - | 结束动画 |
| pause | - | 暂停动画 |
| cancel | - | 取消动画 |
| reverse | - | 反转动画执行方向 |


#### 实例事件


| 事件 | 描述 | 示例 |
| --- | --- | --- |
| cancel | 动画被取消 | animation.oncancel = () => { //do something } |
| finish | 动画执行结束 | animation.onfinish = () => { //do something } |


#### 示例 Demo


```

<script>
 const keyframes1 = [
 {
 time: 0,
 width: 100,
 opacity: 1,
 transform: {
 translateY: '0',
 },
 },
 {
 time: 50,
 width: 300,
 opacity: 0.5,
 transform: {
 translateY: '-150',
 },
 },
 {
 time: 100,
 width: 100,
 opacity: 1,
 transform: {
 translateY: '0',
 },
 },
 ]

 const keyframes2 = [
 {
 time: 0,
 transform: {
 rotate: '0deg',
 },
 },
 {
 time: 100,
 transform: {
 rotate: '360deg',
 },
 },
 ]

 const keyframes3 = [
 {
 time: 0,
 transform: {
 rotate: '0deg',
 },
 transformOrigin: '0px 0px',
 },
 {
 time: 100,
 transform: {
 rotate: '360deg',
 },
 transformOrigin: '0px 0px',
 },
 ]

 const options = {
 duration: 1500,
 easing: 'cubic-bezier(0.140, 0.640, 0.710, 0.240)',
 delay: 0,
 }
 export default {
 animate1() {
 const element = this.$element('animate')
 const animation = element.animate(keyframes1, options)
 animation.play()
 },
 animate2() {
 const element = this.$element('animate')
 const animation = element.animate(keyframes2, options)
 animation.play()
 },
 animate3() {
 const element = this.$element('animate')
 const animation = element.animate(keyframes3, options)
 animation.onfinish = () => {
 console.log('onfinish')
 }
 animation.play()
 },
 }
</script>

<template>
  <div class="flex flex-col justify-center items-center">
    <div class="w-[100px] h-[100px] bg-[#ff0000]" id="animate"></div>
    <input class="w-[450px] h-[80px] rounded-[40px] bg-[#09ba07] text-white text-[30px] mt-[80px]" type="button" value="跳跃" onclick="animate1" />
    <input class="w-[450px] h-[80px] rounded-[40px] bg-[#09ba07] text-white text-[30px] mt-[80px]" type="button" value="旋转(默认中心点)" onclick="animate2" />
    <input class="w-[450px] h-[80px] rounded-[40px] bg-[#09ba07] text-white text-[30px] mt-[80px]" type="button" value="旋转(变换中心点)" onclick="animate3" />
  </div>
</template>

<style>
 @tailwind utilities;
</style>
```

复制代码


---


<!-- 文档 23: ui-component/component/container/div.md -->


## div

## div

更新时间：2023-11-06 14:52:55


基本容器，支持子组件，支持[通用属性](/component/common/common-attributes)，支持[通用样式](/component/common/common-styles)，支持[通用事件](/component/common/common-events)


#### 样式


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| flex-direction | column | row | column-reverse | row-reverse | row | 否 | 默认为横向 `row`，父容器为`<div>、<list-item>`时生效 |
| flex-wrap | nowrap | wrap | wrap-reverse | nowrap | 否 | 规定 flex 容器是单行或者多行，同时横轴的方向决定了新行堆叠的方向 |
| justify-content | flex-start | flex-end | center | space-between | space-around | flex-start | 否 | 设置或检索弹性盒子元素在主轴（横轴）方向上的对齐方式 |
| align-items | stretch | flex-start | flex-end | center | stretch | 否 | 定义 flex 子项在 flex 容器的当前行的侧轴（纵轴）方向上的对齐方式 |
| align-content | stretch | flex-start | flex-end | center | space-between | space-around | stretch | 否 | 属性在弹性容器内的各项没有占用交叉轴上所有可用的空间时对齐容器内的各项（垂直），容器内必须有多行的项目，该属性才能渲染出效果 |


---


<!-- 文档 24: ui-component/component/container/list-item.md -->


## list-item

## list-item

更新时间：2025-06-19 19:54:46


[`<list>`](/component/container/list)的子组件，用来展示列表具体 item，宽度默认充满 list 组件，支持子组件，支持[通用属性](/component/common/common-attributes)，支持[<div>样式](/component/container/div/)，不支持 position 样式，支持[通用样式](/component/common/common-styles)，支持[通用事件](/component/common/common-events)


#### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | `<string>` | - | 是 | list-item 类型，值为自定义的字符串，如'loadMore'。**相同的 type 的 list-item 必须具备完全一致的 DOM 结构**。因此，在 list-item 内部需谨慎使用 if 和 for，因为 if 和 for 可能造成相同的 type 的 list-item 的 DOM 结构不一致，从而引发错误 |


#### 样式


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| column-span | `<number>` | 1 | 否 | list-item 在 list 中所占列数，一般用于 list 多列显示时。 |


#### Slots


| name | 描述 |
| --- | --- |
| right | 左滑后，在右端显示 |


---


<!-- 文档 25: ui-component/component/container/list.md -->


## list

## list

更新时间：2025-06-19 19:54:46


列表视图容器，仅支持[`<list-item>`](/component/container/list-item)子组件，支持[通用属性](/component/common/common-attributes)，支持[通用样式](/component/common/common-styles)


#### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | normal|fisheye|grid | normal | 否 | 设置列表的的布局方式，默认为普通的 list 布局；fisheye 是类似鱼眼镜头效果布局；grid 是网格布局。该属性不可动态变更 |
| scrollbar | `<boolean>` | false | 否 | 是否启用滚动条 |
| title | `<boolean>` | false | 否 | 值为 true <list-item> 的第一个元素将会作为 list 的标题，标题位置固定在 list 开头，向上滑动时标题会渐渐消失（透明度逐渐变为完全透明) |
| circular | `<boolean>` | false | 否 | 是否循环展示 <list-item>, 值为 true 时部分滚动事件不可用。 |
| alignmentnum | `<number>` | 3 | 否 | 鱼眼 list 一屏幕 <list-item> 对齐数量，type 为 fisheye 时生效，设置范围：3-7，超出范围则自动设置为默认值 |
| bounces | `<boolean>` | true | 否 | 是否启用回弹 |


#### 样式


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| flex-direction | column | row | column | 否 | - |
| columns | `<number>` | 1 | 否 | list 显示列数 |


#### 事件


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| scrollbottom | - | 列表滑动到底部 |
| scrolltop | - | 列表滑到到顶部 |
| scrollindex | {first, last} | 返回 list 可视范围的索引范围。first:可视范围第一个 item 的索引；last:可视范围最后一个 item 的索引。 |


#### 方法


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| scrollTo | Object | list 滚动到指定 item 位置 |


**scrollTo 的参数说明:**


| 名称 | 类型 | 是否必选 | 默认值 | 备注 |
| --- | --- | --- | --- | --- |
| index | number | 是 | 无 | list 滚动的目标 item 位置 |
| behavior | smooth|instant|auto | 否 | auto | 是否平滑滑动，支持参数 smooth (平滑滚动)，instant (瞬间滚动)，默认值 auto，效果等同于 instant |


---


<!-- 文档 26: ui-component/component/container/overview.md -->


## 概述

## 概述

更新时间：2023-10-31 20:58:14


布局/容器组件是实现 UI 布局的核心模块之一，不仅可以提供独立的布局功能，还可以多个容器组合，实现更为复杂的布局模式和视觉效果。布局容器还能够为其它 UI 组件提供适当的间距及排列方式，使得整个页面更加美观，构建更丰富的 UI 界面。


### 布局/容器组件介绍


| 组件 | 简述 |
| --- | --- |
| div | 基本容器 |
| list | 列表视图容器，仅支持[`<list-item>`](/component/container/list-item)子组件 |
| list-item | [`<list>`](/component/container/list)的子组件，用来展示列表具体 item，宽度默认充满 list 组件 |
| stack | 基本容器，子组件排列方式为层叠排列，每个直接子组件按照先后顺序依次堆叠，覆盖前一个子组件 |
| swiper | 滑块视图容器 |
| scroll | 滚动视图容器。竖向或水平方向滚动容器，竖向滚动需要设置定高，水平滚动需要设置定宽 |


---


<!-- 文档 27: ui-component/component/container/scroll.md -->


## scroll

## scroll

更新时间：2025-10-09 11:25:10


滚动视图容器。竖向或水平方向滚动容器，竖向滚动需要设置定高，水平滚动需要设置定宽。


### 子组件


支持，也支持嵌套 `scroll`。


### 属性


支持[通用属性](/component/common/common-attributes)


| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| scroll-x | Boolean | false | 否 | 是否允许横向滚动 |
| scroll-y | Boolean | false | 否 | 是否允许纵向滚动 |
| scroll-top | Number/String | | 否 | 设置竖向滚动条位置，内容顶部到 scroll 顶部的距离，如果有滚动吸附效果则先执行`scroll-top`再吸附。 |
| scroll-bottom | Number/String | | 否 | 设置竖向滚动条位置，内容底部到 scroll 底部的距离，如果有滚动吸附效果则先执行`scroll-bottom`再吸附。同时设置`scroll-top`和`scroll-bottom` 以`scroll-top`为准 |
| scroll-left | Number/String | | 否 | 设置横向滚动条位置，内容左侧到 scroll 左侧的距离，如果有滚动吸附效果则先执行`scroll-left`再吸附。 |
| scroll-right | Number/String | | 否 | 设置横向滚动条位置，内容右侧到 scroll 右侧的距离，如果有滚动吸附效果则先执行`scroll-right`再吸附。同时设置`scroll-left`和`scroll-right` 以`scroll-left`为准 |
| bounces | Boolean | false | 否 | 是否边界回弹 |


### 样式


支持[通用样式](/component/common/common-styles)


> 
> scroll 组件暂不支持 margin, padding 相关样式
> 
> 
> 


| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| scroll-snap-type | - | | 作用在 `scroll` 组件上，表示 `scroll` 的滚动吸附类型。第一个参数为 `x` 或 `y` ，表示水平方向上滚动或竖直方向上滚动；第二个参数为 `mandatory` 或`proximity`。`mandatory` 表示选择距离最近的锚点吸附，`proximity` 距离吸附锚点不到容器高度的 30% 时才会吸附。默认为 `proximity`； |
| scroll-snap-align | none | start | center | end | none | 作用在 `scroll` 子组件上，表示子组件和 `scroll` 的对齐形式；start：表示组件和 `scroll` 顶部对齐。center: 表示组件和 `scroll` 底部对齐。end：表示组件和 `scroll` 中心对齐。none：无需对齐，默认值。 |
| scroll-snap-stop | - | normal | 作用在 `scroll` 组件上，是否允许滚动容器“越过”可能的捕捉位置；`normal`可以越过捕捉位置，`always` 不能越过捕捉位置 |


### 事件


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| scrolltop | | 滚动到顶部触发 |
| scrollbottom | | 滚动到底部触发 |
| scroll | { scrollX，scrollY } | 滚动触发`scrollX` 表示滚动的水平距离；`scrollY` 表示滚动的垂直距离； |


### 方法


| 名称 | 描述 |
| --- | --- |
| getScrollRect | 获取滚动内容的尺寸 |
| revealScrollbar | 短暂显示滚动条。仅当内容超出滚动容器（scroll 容器）时生效。 |


#### getScrollRect


获取滚动内容的尺寸


```

function getScrollRect(options: {
  success?: (res: { width: number; height: number }) => void
  fail?: (data: string, code: number) => void
}): void
```

复制代码
**返回值说明：**


| 属性 | 类型 | 描述 |
| --- | --- | --- |
| width | Number | 滚动内容的宽度，包含`border`和`padding` |
| height | Number | 滚动内容的高度，包含`border`和`padding` |


**示例：**


```

this.$element('scroll').getScrollRect({
  success({ width, height }) {
    console.log('宽度', width)
    console.log('高度', height)
  },
  fail(data, code) {},
})
```

复制代码
#### revealScrollbar


短暂显示滚动条。仅当内容超出滚动容器（scroll 容器）时生效。


```

function revealScrollbar(options: {
  success?: () => void
  fail?: (data: string, code: number) => void
}): void
```

复制代码
**示例：**


```

this.$element('scroll').revealScrollbar({
  success() {},
  fail(data, code) {},
})
```

复制代码


---


<!-- 文档 28: ui-component/component/container/stack.md -->


## stack

## stack

更新时间：2023-12-21 13:49:50


基本容器，子组件排列方式为层叠排列，每个直接子组件按照先后顺序依次堆叠，覆盖前一个子组件，支持子组件，支持[通用属性](/component/common/common-attributes/)


#### 样式


支持[<div> 样式](/component/container/div)，支持[通用样式](/component/common/common-styles/)


#### 事件


支持[通用事件](/component/common/common-events/)


---


<!-- 文档 29: ui-component/component/container/swiper.md -->


## swiper

## swiper

更新时间：2025-04-09 17:46:39


滑块视图容器，支持子组件


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| index | `<number>` | 0 | 否 | 当前显示的子组件索引 |
| indicator | `<boolean>` | true | 否 | 是否启用 indicator，默认 true |
| scrollbar | `<boolean>` | false | 否 | 是否启用滚动条，如果 indicator 启用，则滚动条不会启用 |
| vertical | `<boolean>` | false | 否 | 滑动方向是否为纵向，纵向时 indicator 也为纵向 |
| previousmargin | `<string>` | 0px | 否 | 前边距，可用于露出前一项的一小部分，支持单位：px 和% |
| nextmargin | `<string>` | 0px | 否 | 后边距，可用于露出后一项的一小部分，支持单位：px 和% |
| enableswipe | `<boolean>` | true | 否 | 是否支持手势滑动 swiper |


**备注**：`previousmargin`和`nextmargin`的总和不应该超过整个 swiper 大小的 1/2，超过部分将会被截取。


#### 样式


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| indicator-type | normal | arc | normal | 否 | indicator 排列形状（普通或者弧形） |
| indicator-color | `<color>` | rgba(255, 255, 255, 0.4) | 否 | indicator 填充颜色 |
| indicator-selected-color | `<color>` | #ffffff 或者 rgb(255, 255, 255) | 否 | indicator 选中时的颜色 |
| indicator-size | `<length>` | 12px | 否 | indicator 组件的直径大小 |
| indicator-[top|left|right|bottom] | `<length>` | `<percentage>` | - | 否 | indicator 相对于 swiper 的位置，indicator-type 为 arc 时，该样式无效 |
| indicator-spacing | `<number>` | - | 否 | indicator 间距，indicator-type 为 normal 时指间隔距离，indicator-type 为 arc 时指间隔角度 |


#### 事件


支持[通用事件](/component/common/common-events/)


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | {index:currentIndex} | 当前显示的组件索引变化时触发 |
| scrollbottom | - | 滑动到底部或者最右边 |
| scrolltop | - | 滑动到顶部或者最左边 |


#### 方法


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| swipeTo | Object | swiper 滚动到 index 位置 |


##### swipeTo 的参数说明:


| 名称 | 类型 | 是否必选 | 默认值 | 备注 |
| --- | --- | --- | --- | --- |
| index | number | 是 | 无 | swiper 滚动到 index 位置 |
| behavior | smooth|instant|auto | 否 | auto | 是否平滑滑动，支持参数 smooth (平滑滚动)，instant (瞬间滚动)，默认值 auto，效果等同于 instant |


---


<!-- 文档 30: ui-component/component/extend/cellular-list.md -->


## cellular-list

## cellular-list

更新时间：2024-02-28 14:36:29


蜂窝列表组件，将指定结构的数组渲染成蜂窝状列表。


```

 * 排列方式
 *     19___20
 *      |
 *      |  7___8___9
 *      | |        \
 *     18  | 1___2   10
 *    /    |  \   \   \
 *   17    6   0   3   11
 *    \     \     /   /
 *     16    5___4   12
 *      \           /
 *       15___14___13
```

复制代码
#### 子组件


不支持


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必 | |
| --- | --- | --- | --- | --- |
| content | `<array>` | - | 是 | 蜂窝列表数据内容，详见`content-item`数据结构 |
| center-index | `<number>` | - | 否 | 居中图标位置索引，不填写则居中索引为 0 的图标 |


content-item 数据结构


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| name | `<string>` | - | 否 | 图标名称 |
| image | `<string>` | - | 是 | 图标图片地址，仅支持本地图片 |


#### 样式


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| outer-radius | `<length>` | 80px | 否 | 图标外半径，用来控制图标与图标之间的距离 |
| inner-radius | `<length>` | 64px | 否 | 图标内半径，用来控制图标的大小 |


#### 事件


支持[通用事件](/component/common/common-events/)


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| iconclick | [ICON\_EVENT](#ICON_EVENT) | 当前图标被点击时触发，返回索引位置和名称 |
| wheelfocus | [ICON\_EVENT](#ICON_EVENT) | 中心图标放大到最大时触发，返回索引位置和名称 |


###### ICON\_EVENT


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| index | `<Integer>` | 当前被点击图标索引位置 |
| name | `<String>` | 当前被点击图标名称 |


---


<!-- 文档 31: ui-component/component/extend/drawer-navigation.md -->


## drawer-navigation

## drawer-navigation

更新时间：2025-10-09 11:25:10


[<drawer>](/component/extend/drawer/)的子组件，用来展示具体的抽屉内容


#### 子组件


支持


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| direction | start | end | up | down | start | 否 | drawer-navigation 的滑出方向，支持 start/end/up/down。如果多个 drawer-navigation 重复设置同样的值，则添加第一个 drawer-navigation。 |
| enable-blur | boolean | true | 否 | 是否启用高斯模糊 |


#### 样式


支持[通用样式](/component/common/common-styles/)


---


<!-- 文档 32: ui-component/component/extend/drawer.md -->


## drawer

## drawer

更新时间：2023-10-20 10:02:06


抽屉容器，抽屉默认隐藏。可通过边缘滑动，支持 flex 布局。


#### 子组件


支持,包括 [<drawer-navigation>](/component/extend/drawer-navigation/) 子组件


#### 属性


支持[通用属性](/component/common/common-attributes/)


#### 样式


支持[通用样式](/component/common/common-styles/)


#### 事件


支持[通用事件](/component/common/common-events/)


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | {direction:directionValue, state: stateValue} | 抽屉打开关闭时回调。direction：抽屉的位置，值为 start 或 end 或 up 或 down。 start：左边，end：右边，up：上边，down：下边。state:打开或者关闭状态。0：关闭，1：打开 |


#### 方法


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


---


<!-- 文档 33: ui-component/component/extend/overview.md -->


## 概述

## 概述

更新时间：2024-10-11 11:55:18


用于简化页面导航的 UI 组件，通过提供直观的导航形式、清晰的页面路径和视觉创意等，提供了便捷的导航体验


### 导航组件介绍


| 组件 | 简述 |
| --- | --- |
| drawer | 抽屉容器，抽屉默认隐藏。可通过边缘滑动，支持 flex 布局 |
| drawer-navigation | <drawer>的子组件，用来展示具体的抽屉内容 |
| cellular-list | 蜂窝列表组件，将指定结构的数组渲染成蜂窝状列表 |


---


<!-- 文档 34: ui-component/component/font-face-style.md -->


## 自定义字体样式

## 自定义字体样式

更新时间：2023-12-21 17:59:06


font-face 用于定义字体样式。当需要为文本组件设置自定义字体时，可以在 style 中定义 font-face 作为自定义字体，然后在 font-family 中可以引用该字体。


自定义字体可以是从项目中的字体文件或网络字体文件中加载的字体。


注： 只支持 ttf 和 otf 格式的字体。


### 定义 font-face


```

@font-face {
  font-family: myfont;
  src: url('http://www.example.com/myfont.ttf');
}
```

复制代码
#### font-family


自定义字体的名称。


#### src


自定义字体的来源。


目前支持的字体来源有 3 种：


- 项目中的字体文件: 通过 url 指定项目中的字体文件路径(只支持绝对路径)
- 网络字体文件：通过 url 指定网络字体的地址
- 系统字体：通过 local 指定系统字体名称


### 使用 font-face


在 style 中定义了 font-face 后，我们可以在文本组件的 font-family 样式中指定 font-face 的名称，该组件即可应用 font-face 定义的字体。 font-face 中暂不支持设置多个 src 。


##### 示例


```

<template>
  <!-- template里只能有一个根节点 -->
  <div class="demo-page">
    <text class="font">测试自定义字体 test custom font</text>
  </div>
</template>

<style>
 @font-face {
 font-family: myfont;
 src: url('http://www.example.com/myfont.ttf');
 }
 .demo-page {
 flex-direction: column;
 justify-content: center;
 align-items: center;
 }
 .font {
 font-family: myfont, serif;
 }
</style>
```

复制代码
### 图标字体 icon-font


将图标制作成字体文件，保存到项目文件中（如:src/Common/iconfont.ttf），在 style 中定义一个 font-face ，然后在需要使用图标字体的地方使用该 font-face 作为组件的字体，组件的内容为字体文件中我们需要使用的图标的字符。


```

<template>
  <!-- template里只能有一个根节点 -->
  <div class="demo-page">
    <text>测试text中嵌套iconfont<span class="icon-font-span">&#xe822;</span>test icon font</text>
  </div>
</template>

<style>
 @font-face {
 font-family: iconfont;
 src: url('/Common/iconfont.ttf');
 }
 .demo-page {
 flex-direction: column;
 justify-content: center;
 align-items: center;
 }
 .icon-font-span {
 font-family: iconfont;
 font-size: 40px;
 color: #ff0000;
 }
</style>
```

复制代码


---


<!-- 文档 35: ui-component/component/global/overview.md -->


## 概述

## 概述

更新时间：2023-10-30 19:29:42


提供基于蓝河应用的特定的设计规范和标准所设计的 UI 组件，这些组件具有统一的设计风格、布局、图标元素和字体字号等，旨在为用户提供全面的业务场景下的界面设计需求。


### 系统风格组件介绍


| 组件 | 简述 |
| --- | --- |
| vw-alert | 弹窗组件，此组件为应用内主动触发的信息、操作确认弹窗 |
| vw-button | 一种基础的组件，点击后可执行对应（按钮表意）的操作。包含“文字按钮”“图标按钮”两类 |
| vw-empty | 页面无用户生成的内容时，显示空白页控件元素 |
| vw-icon | 提供一套常用图标 |
| vw-slide | 用来快速调节设置值，如音量、亮度、色彩饱和度等. 用户通过点击左侧/右侧按钮的方式增加/降低数值. |
| vw-title | 标题显示在页面顶部，作为关键导航信息，用来告知用户当前在哪里 |
| vw-list | 列表包含一系列连续的列表项，可以呈现文本、图标等内容。 |
| vw-list-item | 列表选项可以作为列表的子项，当列表的每一项不同时可以用列表选项拼接实现 |
| vw-loading | loading 用于定性地指示一种过程状态，多用于数据加载过程，如加载应用列表，或从网络端获取内容的过程 |


---


<!-- 文档 36: ui-component/component/global/vw-alert.md -->


## vw-alert

## vw-alert

更新时间：2025-04-30 20:56:55


控件定义：弹窗组件，此组件为应用内主动触发的信息、操作确认弹窗（注意：此组件不包含应用外的系统通知提醒弹窗）


#### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| icon | `<string>` | - | 否 | 图标 |
| title | `<string>` | - | 否 | 标题 |
| content | `<string>` | - | 是 | 正文 |
| des | `<string>` | - | 否 | 副文本/辅助信息 |
| buttons | `<Array>` | - | 是 | 按钮 |
| type | `<string>` | ALERT | 否 | 弹窗类型，根据视图布局上差异，可选值为ALERT，NOTICE |


##### buttons Array 类型


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| eventType | `<string>` | - | 是 | 按钮点击事件类型。支持自定义事件名，例如 confirm:确定，cancel:忽略 |
| type | `<string>` | - | 是 | 按钮类型。plain,primary,success,warning,danger |
| value | `<string>` | - | 否 | 按钮文本，同vw-button定义 |
| color | `<string>` | - | 否 | 按钮颜色，同vw-button定义 |
| bgColor | `<string>` | | 否 | 按钮背景颜色，同vw-button定义 |


---


<!-- 文档 37: ui-component/component/global/vw-button.md -->


## vw-button

## vw-button

更新时间：2025-04-30 20:56:55


一种基础的组件，点击后可执行对应（按钮表意）的操作。包含“文字按钮”“图标按钮”两类；


#### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | `<string>` | plain | 否 | 类型包括以下五种类型： plain,primary,success,warning,danger |
| value | `<string>` | - | 是 | 按钮文本 |
| disabled | `<boolean>` | false | 否 | 按钮禁用状态 |
| color | `<string>` | - | 否 | 文字颜色 |
| bg-color | `<string>` | - | 否 | 按钮颜色 |
| text-size | `<string>` | - | 否 | 文本字号 |


#### 事件


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| click | MouseEvent | 组件被点击时触发 |


---


<!-- 文档 38: ui-component/component/global/vw-empty.md -->


## vw-empty

## vw-empty

更新时间：2025-04-30 20:56:55


控件定义：页面无用户生成的内容时，显示空白页控件元素：


- （1） 图标
- （2） 正文
- （3） 辅助信息


#### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| icon | `<string>` | - | 否 | icon 名称/自定义路径定义 |
| content | `<string>` | - | 是 | 正文描述 |
| des | `<string>` | - | 否 | 辅助信息描述 |
| content-color | `<string>` | - | 否 | 正文的文字颜色，默认:#ffffff; |
| des-color | `<string>` | - | 否 | 辅助信息的文字颜色，默认:#888888; |
| is-loading | `<bool>` | false | 否 | 与icon 互斥，显示加载中状态 |


#### vw-empty 用法


```

<vw-empty
 icon="delete"
 content="正文这"
 des="辅助信息"
 content-color="#ff0000"
 des-color="#888888"
></vw-empty>
<vw-empty icon="delete" content="正文这"></vw-empty>
<vw-empty icon="/assets/images/icon.png" content="正文这" des="辅助信息"></vw-empty>
<vw-empty is-loading="true" content="正文这" des="辅助信息"></vw-empty>

```

复制代码


---


<!-- 文档 39: ui-component/component/global/vw-icon.md -->


## vw-icon

## vw-icon

更新时间：2025-04-30 20:56:55


控件定义：提供一套常用图标


#### 常用 icon 列表


| icon | 描述 |
| --- | --- |
| delete | 删除 |
| arrow-left | 左箭头 |
| arrow-right | 右箭头 |
| plus | 加号 |
| minus | 减号 |
| warn | 警告 |
| finish | 完成 |
| arrow-right-black | 指向右边的黑色箭头 |
| info-light | 浅色信息图标 |
| info-dark | 深色信息图标 |
| setup | 设置 |


#### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| icon | `<string>` | - | 否 | icon 名称 |
| [path] | `<string>` | - | 否 | 应用内部路径，可选 |
| [size] | `<number>` | 72 | 否 | 推荐尺寸参考下方 icon 尺寸表 |
| [width] | `<number>` | - | 否 | 自定义宽度，单位 px |
| [height] | `<number>` | - | 否 | 自定义高度，单位 px |
| [disabled] | `<boolean>` | false | 否 | 禁用状态(opacity:0.4) |


#### icon 尺寸表


| 尺寸 | 描述 |
| --- | --- |
| xs | 36px \* 36px |
| sm | 48px \* 48px |
| normal | 72px \* 72px |
| md | 96px \* 96px |
| lg | 114px \* 114px |
| xl | 198px \* 198px |


---


<!-- 文档 40: ui-component/component/global/vw-list-item.md -->


## vw-list-item

## vw-list-item

更新时间：2025-04-30 20:56:55


列表选项可以作为列表的子项，当列表的每一项不同时可以用列表选项拼接实现。 list-item 代表一类组件，命名上我们用 li 缩写代替 list-item


参考当前需求，将列表选项分为以下几种：


vw-li: 通用列表子项，（itemData 必填属性为 title ，可填属性 des ，icon ，inputType，checked），通过以下随机组合可以实现以下几种布局


1.只有标题 （（itemData 仅设置 title）


2.带辅助文本的列表子项（itemData 设置属性为 title、des）


3.带图标的列表子项（itemData 设置属性为 title、icon）


4.带图标、描述文本的列表子项（itemData 设置属性为 icon、title、des）


5.带辅助文本和开关（或单选、多选）的列表子项（itemData 设置属性为 title、des、inputType、checked）


6.带图标、描述文本和开关（或单选、多选）的列表子项（itemData 设置属性为 icon、title、des、inputType、checked）


注意：带 radio 的列表子项，在选项变化时需要同时更新其他选项绑定的的 checked 标志位，否则会出现诸多显示问题


#### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| item-data | `<Object>` | - | 是 | 列表子项对象 |
| disabled | `<boolean>` | false | 否 | 列表选项是否为禁用状态 |
| remind | `<boolean>` | false | 否 | 是否显示红点 |
| widget-disabled | `<boolean>` | false | 否 | inputType配置switch/radio/checkbox 时，用来禁用右侧的部件但文字不会置灰 |


##### itemData 需要填哪些必填属性根据类型确定，可以包含的属性有：


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| icon | `<string>` | - | 否 | 列表项的图标路径 |
| title | `<string>` | - | 是 | 列表项的标题 |
| des | `<string>` | - | 否 | 列表项的辅助文本 |
| subIcon | `<string>` | - | 否 | 列表项的右侧图标路径 |
| checked | `<boolean>` | true | 否 | 当inputType配置 switch/radio/checkbox生效，表示开关状态 |
| inputType | `<string>` | - | 否 | 可枚举值为 switch/radio/checkbox，控制列表项右侧显示控件类型 |


#### 事件


| 名称 | 回调参数 | 说明 |
| --- | --- | --- |
| itemclick | - | 列表选项点击事件 |
| widgetclick | { event} | 右边小组件点击事件（只在有 checkbox、radio、switch 组件的时候有此参数，event 和对应的原生组件点击事件一致） |
| animationend | | 单选点击事件（目前只有带 radio 的 list-item 有） |


#### vw-list-item 用法


**vw-list**


```

<template>
  <list>
    <list-item type="liIconArrow">
      <vw-li item-data="{{listArray[0]}}" onitemclick="handleClick"></vw-li>
    </list-item>
    <list-item type="liIconSw">
      <vw-li item-data="{{listArray[1]}}" onwidgetclick="handleWidgetClick"></vw-li>
    </list-item>
    <list-item type="liIcon">
      <vw-li item-data="{{listArray[2]}}"></vw-li>
    </list-item>
    <list-item type="liIconDesSw">
      <vw-li
 item-data="{{listArray[3]}}"
 onwidgetclick="handleWidgetClick"
 ></vw-li>
    </list-item>
    <list-item type="li">
      <vw-li item-data="{{listArray[4]}}"></vw-li>
    </list-item>
    <list-item type="liDes">
      <vw-li item-data="{{listArray[5]}}"></vw-li>
    </list-item>

    <list-item type="liSw">
      <vw-li item-data="{{listArray[6]}}" onwidgetclick="handleWidgetClick"></vw-li>
    </list-item>
    <list-item type="liDesSw">
      <vw-li item-data="{{listArray[7]}}" onwidgetclick="handleWidgetClick"></vw-li>
    </list-item>
    <list-item type="liRadio">
      <vw-li item-data="{{listArray[8]}}"></vw-li>
    </list-item>
  </list>
</template>

<script>
 export default {
 data: {
 listArray: [
 {
 icon: '/assets/images/logo.png',
 title: '图标+标题+箭头',
 },
 {
 icon: '/assets/images/logo.png',
 title: '图标+标题+开关',
 inputType: 'switch',
 checked: true,
 },
 {
 icon: '/assets/images/logo.png',
 title: '图标+标题',
 },
 {
 icon: '/assets/images/logo.png',
 title: '图标+标题+辅助文本+开关',
 des: '辅助文本超长示例辅助文本超长示例辅助文本超长示例',
 inputType: 'switch',
 checked: true,
 },
 {
 title: '只有标题',
 },
 {
 title: '标题+辅助文本',
 des: '辅助文本',
 },
 {
 title: '标题+开关',
 inputType: 'switch',
 checked: true,
 },
 {
 title: '标题+开关+辅助文本',
 des: '辅助文本',
 checked: true,
 },
 {
 title: '标题+单选+辅助文本',
 des: '辅助文本',
 inputType: 'radio',
 checked: true,
 }
 ],
 },
 handleWidgetClick() {},
 handleClick() {},
 }
</script>
```

复制代码


---


<!-- 文档 41: ui-component/component/global/vw-list.md -->


## vw-list

## vw-list

更新时间：2025-04-30 20:56:55


列表包含一系列连续的列表项，可以呈现文本、图标等内容。 list 只提供每个选项相同的列表，如果每个选项不同可使用 list-item 类组件进行实现。


参考当前需求，将列表分为以下几种：


1.vw-list:最常用的列表，包含图标、标题、箭头（listArray 子项必填选项为 icon、title，list 属性可选 type 为 normal 或 fisheye）


2.vw-list-radio:右侧带单选按钮的列表（listArray 子项必填选项为 title、checked）


3.vw-list-icon-radio:左侧为图标，右侧带单选按钮的列表（listArray 子项必填选项为 icon、title、checked）


4.vw-list-radio-left:左侧带单选按钮的列表（listArray 子项必填选项为 title、checked）


5.vw-list-des-radio-left:左侧带单选按钮且带辅助文本的列表（listArray 子项必填选项为 title、des、checked）


6.vw-list-checkbox:右侧带多选按钮的列表（listArray 子项必填选项为 title、checked）


7.vw-list-icon-checkbox:左侧为图标，右侧带多选按钮的列表（listArray 子项必填选项为 icon、title、checked）


#### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| title | `<string>` | 列表 | 是 | 列表的标题 |
| listArray | `<Array>` | - | 是 | 列表数据数组 |
| scrollbar | `<boolean>` | true | 否 | 是否启用滚动条 |
| type | `<string>` | normal | 否 | 设置列表的的布局方式，值为 normal（正常列表）或 fisheye（鱼眼列表）（只有 vw-list 生效） |
| remind | `<boolean>` | false | 否 | 是否显示红点（只有 vw-list 支持） |
| buttons | `<Array>` | - | 是 | 按钮（只有 vw-list-checkbox 和 vw-list-icon-checkbox 支持） |


##### listArray 的成员为 Object，需要填哪些必填属性根据 list 类型确定，可以包含的属性有：


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| icon | `<string>` | - | 根据 list 类型确定 | 列表选项的图标路径 |
| title | `<string>` | - | 是 | 列表选项的标题 |
| des | `<string>` | - | 根据 list 类型确定 | 列表选项的辅助文本 |
| checked | `<boolean>` | true | 根据 list 类型确定 | 列表选项的 switch/radio/checkbox 开关状态 |
| index | `<number>` | - | 根据 list 类型确定 | 列表选项的序号 |
| disabled | `<boolean>` | false | 否 | 列表选项是否为禁用状态 |
| widgetDisabled | `<boolean>` | false | 否 | 列表右侧有 switch/radio/checkbox 时，用来仅禁用右侧的部件但文字不会置灰 |


#### 事件


| 名称 | 回调参数 | 说明 |
| --- | --- | --- |
| itemclick | {index} | 列表选项点击事件 |
| widgetclick | {index, event} | 右边小组件点击事件（只在有 checkbox、radio、switch 组件的时候有此事件，event 和对应的原生组件点击事件一致） |
| back | 无 | 列表标题点击事件 |
| animationend | {index} | 单选点击事件（目前只有带 radio 的 list 有） |


#### vw-list 用法


**vw-list**


```

<template>
  <vw-list
 list-array="{{listArray}}"
 onitemclick="handleClick"
 title="列表"
 onback="handleBack"
 onscrollbottom="handleBottom"
 ></vw-list>
</template>

<script>
 export default {
 data: {
 listArray: [
 {
 icon: '/assets/images/setupSound.png',
 title: '图标+标题+箭头',
 },
 {
 icon: '/assets/images/setupSound.png',
 title: '图标+标题+箭头',
 },
 {
 icon: '/assets/images/setupSound.png',
 title: '图标+标题+箭头',
 },
 ],
 },
 }
</script>
```

复制代码
**vw-list-radio**


```

<template>
  <vw-list-radio
 list-array="{{listArray}}"
 onitemclick="handleClick"
 onwidgetclick="handleWidgetClick"
 title="单选列表"
 onback="handleBack"
 onscrollbottom="handleBottom"
 ></vw-list-radio>
</template>
<script>
 export default {
 data: {
 listArray: [
 {
 title: '无图标单选',
 checked: false,
 },
 {
 title: '无图标单选',
 checked: true,
 },
 {
 title: '无图标单选',
 checked: false,
 },
 ],
 },
 }
</script>
```

复制代码
**vw-list-icon-radio**


```

<template>
  <vw-list-icon-radio
 list-array="{{listArray}}"
 onitemclick="handleClick"
 onwidgetclick="handleWidgetClick"
 title="有图标单选列表"
 onback="handleBack"
 onscrollbottom="handleBottom"
 ></vw-list-icon-radio>
</template>
<script>
 export default {
 data: {
 listArray: [
 {
 icon: '/assets/images/setupSound.png',
 title: '有图标单选列表',
 checked: false,
 },
 {
 icon: '/assets/images/setupSound.png',
 title: '有图标单选列表',
 checked: true,
 },
 {
 icon: '/assets/images/setupSound.png',
 title: '有图标单选列表',
 checked: false,
 },
 ],
 },
 }
</script>
```

复制代码
**vw-list-radio-left**


```

<template>
  <vw-list-radio-left
 list-array="{{listArray}}"
 onitemclick="handleClick"
 onwidgetclick="handleWidgetClick"
 title="左侧单选列表"
 onback="handleBack"
 onscrollbottom="handleBottom"
 ></vw-list-radio-left>
</template>
<script>
 export default {
 data: {
 listArray: [
 {
 title: '左侧单选',
 checked: false,
 },
 {
 title: '左侧单选',
 checked: true,
 },
 {
 title: '左侧单选',
 checked: false,
 },
 ],
 },
 }
</script>
```

复制代码
**vw-list-des-radio-left**


```

<template>
  <vw-list-des-radio-left
 list-array="{{listArray}}"
 onitemclick="handleClick"
 onwidgetclick="handleWidgetClick"
 title="左侧单选辅助文本列表"
 onback="handleBack"
 onscrollbottom="handleBottom"
 ></vw-list-des-radio-left>
</template>
<script>
 export default {
 data: {
 listArray: [
 {
 title: '左侧单选带辅助文本',
 checked: false,
 des: '辅助文本',
 },
 {
 title: '左侧单选带辅助文本',
 checked: true,
 des: '辅助文本',
 },
 {
 title: '左侧单选带辅助文本',
 checked: false,
 des: '辅助文本',
 },
 ],
 },
 }
</script>
```

复制代码
**vw-list-checkbox**


```

<template>
  <vw-list-checkbox
 list-array="{{listArray}}"
 onitemclick="handleClick"
 onwidgetclick="handleWidgetClick"
 title="多选列表"
 onback="handleBack"
 onscrollbottom="handleBottom"
 ></vw-list-checkbox>
</template>
<script>
 export default {
 data: {
 listArray: [
 {
 title: '无图标多选',
 checked: true,
 },
 {
 title: '无图标多选',
 checked: true,
 },
 {
 title: '无图标多选',
 checked: false,
 },
 ],
 },
 }
</script>
```

复制代码
**vw-list-icon-checkbox**


```

<template>
  <vw-list-icon-checkbox
 list-array="{{listArray}}"
 onitemclick="handleClick"
 onwidgetclick="handleWidgetClick"
 title="有图标多选列表"
 onback="handleBack"
 onscrollbottom="handleBottom"
 ></vw-list-icon-checkbox>
</template>
<script>
 export default {
 data: {
 listArray: [
 {
 icon: '/assets/images/setupSound.png',
 title: '有图标多选',
 checked: true,
 },
 {
 icon: '/assets/images/setupSound.png',
 title: '有图标多选',
 checked: true,
 },
 {
 icon: '/assets/images/setupSound.png',
 title: '有图标多选',
 checked: false,
 },
 ],
 },
 }
</script>
```

复制代码


---


<!-- 文档 42: ui-component/component/global/vw-loading.md -->


## vw-loading

## vw-loading

更新时间：2025-04-30 20:56:55


用于定性地指示一种过程状态，多用于数据加载过程，如加载应用列表，或从网络端获取内容的过程


#### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| size | `<number>` | - | 是 | loading 控件的大小 |


---


<!-- 文档 43: ui-component/component/global/vw-slide.md -->


## vw-slide

## vw-slide

更新时间：2025-04-30 20:56:55


滑动条组件用来快速调节设置值，如音量、亮度、色彩饱和度等. 用户通过点击左侧/右侧按钮的方式增加/降低数值.


#### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | `<string>` | 'normal' | 是 | 类型，普通(normal)和栅格(grid) |
| value | `<number>` | - | 是 | 当前进度数值 |
| maxValue | `<number>` | - | 是 | 数值范围的最大值 |
| minValue | `<number>` | - | 是 | 数值范围的最小值 |
| step | `<number>` | - | 是 | 步数间距 |
| focusing | `<boolean>` | - | 是 | 是否处于聚焦状态 |


#### 事件


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| touchstart | 请参考通用事件中的 TouchEvent | 手指刚触摸组件时触发 |
| touchmove | 请参考通用事件中的 TouchEvent | 手指触摸后移动时触发 |
| touchend | 请参考通用事件中的 TouchEvent | 手指触摸动作结束时触发 |
| touchcancel | 请参考通用事件中的 TouchEvent | 手指触摸动作被打断时触发 |


#### vw-slide 用法


```

<vw-slide
 style="margin-top:20px"
 type="normal"
 value="{{valueA}}"
 min-value="45"
 max-value="255"
 step="42"
 focusing="{{true}}"
 ontouchstart="onStartA"
 ontouchend="onEnd"
 ontouchmove="onEnd"
 ontouchcancel="onEnd"
></vw-slide>
```

复制代码


---


<!-- 文档 44: ui-component/component/global/vw-title.md -->


## vw-title

## vw-title

更新时间：2025-04-30 20:56:55


标题显示在页面顶部，作为关键导航信息，用来告知用户当前在哪里。


#### 属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| value | `<string>` | - | 是 | 标题文本内容 |
| is-fixed | `<boolean>` | true | 否 | 标题是否固定顶部 |
| icon-left | `<string>` | - | 否 | 标题左侧图标（仅方表生效） |
| icon-right | `<string>` | - | 否 | 标题右侧图标（仅方表生效） |
| level | Number | 2 | 否 | 值为1:一级标题，值为2:二级标题 |


#### 事件


| 名称 | 回调参数 | 说明 |
| --- | --- | --- |
| back | 无 | 点击事件，只在有返回按钮时生效 |
| iconleftclick | 无 | 点击标题左侧icon事件，仅icon-left 配置后生效 |
| iconrightclick | 无 | 点击标题右侧icon事件，仅icon-right配置后生效 |


#### vw-title 用法


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


---


<!-- 文档 45: ui-component/component/gradient-styles.md -->


## 渐变样式

## 渐变样式

更新时间：2023-10-20 10:02:06


渐变 (gradients) 可以在两个或多个指定的颜色之间显示平稳的过渡，用法与 CSS 渐变一致。


当前框架支持以下渐变效果：


- 线性渐变 (linear-gradient)
- 重复线性渐变 (repeating-linear-gradient)


### 线性渐变 / 重复线性渐变


创建一个线性渐变，需要定义两类数据：1) 过渡方向；2) 过渡颜色，因此需要指定至少两种颜色。


1. 过渡方向：通过`direction`或者`angle`两种形式指定
2. 过渡颜色：支持方式：`#FF0000`、`#F00`


- direction: 方向渐变


```

background: linear-gradient(direction, color-stop1, color-stop2, ...);
background: repeating-linear-gradient(direction, color-stop1, color-stop2, ...);
```

复制代码
#### 参数


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| direction | `to` `<side-or-corner>`  `<side-or-corner>` = [`left` | `right`] || [`top` | `bottom`] | `to bottom` (从上到下渐变) | 否 | 例如：`to right` (从左向右渐变) |
| |  | |  | |
| color-stop | `<color>` [`<length>`|`<percentage>`] | | 是 | 从起点到`stop`的区域显示的背景色为`color` |


#### 示例


```

#gradient {
  height: 100px;
  width: 200px;
}
```

复制代码

```

/\* 从顶部开始渐变。起点是红色，慢慢过渡到蓝色 \*/
background: linear-gradient(#f00, #00f);
```

复制代码
![gradientTop](/7a6a6ec851205bddd62ad5ffc091a61b/gradientTop.png)


```

/\* 从左向右渐变，在距离左边90px和距离左边120px (200\*0.6) 之间30px宽度形成渐变\*/
background: linear-gradient(to right, #f00 90px, #00f 60%);
```

复制代码
![gradientTop](/c3840778f9e5ffc721b716b3cd892885/gradientThree.png)


---


<!-- 文档 46: ui-component/component/others/canvas.md -->


## canvas

## canvas

更新时间：2024-10-11 11:55:18


画布组件，通过使用 JavaScript 中的脚本，可以在 canvas 上绘制图形，文字等。


#### 子组件


不支持


#### 属性


支持[通用属性](/component/common/common-attributes/)


#### 样式


支持[通用样式](/component/common/common-styles/)


#### 方法


##### canvas.getContext()


创建 canvas 绘图上下文


###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| contextType | `<string>` | 目前支持传入'2d' |


###### 返回值


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| '2d' | `CanvasRenderingContext2D` | 返回一个 CanvasRenderingContext2D 对象，用于 2D 绘制，请参考 [CanvasRenderingContext2D](#context2d)对象 |


###### 示例


```

const canvas = this.$element('canvasid')
const ctx = canvas.getContext('2d')
```

复制代码


---


## CanvasRenderingContext2D

更新时间：2024-10-11 11:55:18


通过 CanvasRenderingContext2D 可以在 canvas 上绘制矩形、文本和其他对象。可以在 canvas 上调用 getContext('2d') 来获取 CanvasRenderingContext2D 的对象。


#### 方法和属性


##### **填充和描边样式**


##### CanvasRenderingContext2D.fillStyle


设置填充色


###### 语法


```

ctx.fillStyle = color
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| color | `<string>` | CSS color |
| gradient | `CanvasGradient` | 参考 [CanvasGradient](#canvasgradient) 对象，可通过 CanvasRenderingContext2D.createLinearGradient() 方法创建 |


##### CanvasRenderingContext2D.strokeStyle


设置边框颜色


###### 语法


```

ctx.strokeStyle = color
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| color | `<string>` | CSS color |
| gradient | `CanvasGradient` | 参考 [CanvasGradient](#canvasgradient) 对象，可通过 CanvasRenderingContext2D.createLinearGradient() 方法创建 |


##### **渐变和图案**


##### CanvasRenderingContext2D.createLinearGradient()


创建一个线性的渐变颜色


###### 语法


```

ctx.createLinearGradient(x0, y0, x1, y1)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x0 | `<number>` | 起点的 x 坐标 |
| y0 | `<number>` | 起点的 y 坐标 |
| x1 | `<number>` | 终点的 x 坐标 |
| y1 | `<number>` | 终点的 y 坐标 |


##### **路径**


##### CanvasRenderingContext2D.beginPath()


开始创建一个新路径


###### 语法


```

ctx.beginPath()
```

复制代码
##### CanvasRenderingContext2D.closePath()


封闭一个路径


###### 语法


```

ctx.closePath()
```

复制代码
##### CanvasRenderingContext2D.moveTo()


把路径移动到画布中的指定点


###### 语法


```

ctx.moveTo(x, y)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | `<number>` | 目标位置的 x 坐标 |
| y | `<number>` | 目标位置的 y 坐标 |


##### CanvasRenderingContext2D.lineTo()


使用直线连接子路径的终点到 x，y 坐标


###### 语法


```

ctx.lineTo(x, y)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | `<number>` | 目标位置的 x 坐标 |
| y | `<number>` | 目标位置的 y 坐标 |


##### CanvasRenderingContext2D.arc()


画一条弧线


###### 语法


```

ctx.arc(x, y, radius, startAngle, endAngle, anticlockwise)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | `<number>` | 圆心的 x 坐标 |
| y | `<number>` | 圆心的 y 坐标 |
| radius | `<number>` | 圆的半径 |
| startAngle | `<number>` | 起始弧度， x 轴方向开始计算，单位以弧度表示。 |
| endAngle | `<number>` | 终止弧度 |
| anticlockwise | Boolean | 可选。如果为 true，逆时针绘制圆，反之，顺时针绘制 |


##### CanvasRenderingContext2D.arcTo()


根据控制点和半径绘制圆弧路径


###### 语法


```

ctx.arcTo(x1, y1, x2, y2, radius)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x1 | `<number>` | 第一个控制点的 x 轴坐标 |
| y1 | `<number>` | 第一个控制点的 y 轴坐标 |
| x2 | `<number>` | 第二个控制点的 x 轴坐标 |
| y2 | `<number>` | 第二个控制点的 y 轴坐标 |
| radius | `<number>` | 圆弧的半径 |


##### CanvasRenderingContext2D.bezierCurveTo()


绘制三次贝塞尔曲线路径


###### 语法


```

ctx.bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| cp1x | `<number>` | 第一个贝塞尔控制点的 x 坐标 |
| cp1y | `<number>` | 第一个贝塞尔控制点的 y 坐标 |
| cp2x | `<number>` | 第二个贝塞尔控制点的 x 坐标 |
| cp2y | `<number>` | 第二个贝塞尔控制点的 y 坐标 |
| x | `<number>` | 结束点的 x 坐标 |
| y | `<number>` | 结束点的 y 坐标 |


##### CanvasRenderingContext2D.quadraticCurveTo()


创建二次贝塞尔曲线路径


###### 语法


```

ctx.quadraticCurveTo(cpx, cpy, x, y)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| cpx | `<number>` | 贝塞尔控制点的 x 坐标 |
| cpy | `<number>` | 贝塞尔控制点的 y 坐标 |
| x | `<number>` | 结束点的 x 坐标 |
| y | `<number>` | 结束点的 y 坐标 |


##### CanvasRenderingContext2D.rect()


创建一个矩形


###### 语法


```

ctx.rect(x, y, width, height)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | `<number>` | 矩形路径左上角的 x 坐标 |
| y | `<number>` | 矩形路径左上角的 y 坐标 |
| width | `<number>` | 矩形路径的宽度 |
| height | `<number>` | 矩形路径的高度 |


##### **线型**


##### CanvasRenderingContext2D.lineWidth


设置线条的宽度


###### 语法


```

ctx.lineWidth = lineWidth
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| lineWidth | `<number>` | 线条的宽度 |


##### CanvasRenderingContext2D.lineCap


设置线条的端点样式


###### 语法


```

ctx.lineCap = lineCap
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| lineCap | `<string>` | 'butt'(默认)、'round'、'square' |


##### **绘制路径**


##### CanvasRenderingContext2D.fill()


对当前路径中的内容进行填充


###### 语法


```

ctx.fill()
```

复制代码
##### CanvasRenderingContext2D.stroke()


画出当前路径的边框


###### 语法


```

ctx.stroke()
```

复制代码
##### **绘制矩形**


##### CanvasRenderingContext2D.clearRect()


清除画布上在该矩形区域内的内容(矩形区域大于等于 canvas 组件时，清除之前绘制内容；小于 canvas 组件时，清除区域默认为黑色，可通过设置 canvas 背景色更改)


###### 语法


```

ctx.clearRect(x, y, width, height)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | `<number>` | 矩形区域左上角的 x 坐标 |
| y | `<number>` | 矩形区域左上角的 y 坐标 |
| width | `<number>` | 矩形区域的宽度 |
| height | `<number>` | 矩形区域的高度 |


##### CanvasRenderingContext2D.fillRect()


填充一个矩形


###### 语法


```

ctx.fillRect(x, y, width, height)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | `<number>` | 矩形路径左上角的 x 坐标 |
| y | `<number>` | 矩形路径左上角的 y 坐标 |
| width | `<number>` | 矩形路径的宽度 |
| height | `<number>` | 矩形路径的高度 |


##### CanvasRenderingContext2D.strokeRect()


画一个非填充矩形


###### 语法


```

ctx.strokeRect(x, y, width, height)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | `<number>` | 矩形路径左上角的 x 坐标 |
| y | `<number>` | 矩形路径左上角的 y 坐标 |
| width | `<number>` | 矩形路径的宽度 |
| height | `<number>` | 矩形路径的高度 |


##### **文本样式**


##### CanvasRenderingContext2D.font


设置当前字体样式的属性


###### 语法


```

ctx.font = value
```

复制代码
###### 参数


| 参数 | 描述 | 类型 |
| --- | --- | --- |
| value | 支持字重与字体大小，可以独立设置字重和字体，如果同时设置字重和字体需要空格分割，字重在前面。默认值为 "normal 30px" | `<string>` |


###### Value 值


| 可选值 | 是否必填 | 说明 |
| --- | --- | --- |
| font-weight | 否 | 规定字体的粗细。可能的值：normalboldbolderlighter100200300400500600700800900默认为 normal |
| font-size | 否 | 规定字号，以像素计。默认 30 px |


##### CanvasRenderingContext2D.textAlign


设置文字的对齐方式


###### 语法


```

ctx.textAlign = align
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| align | `<string>` | 'start'(默认),'end','left','center','right' |


##### CanvasRenderingContext2D.textBaseline


设置文字的水平对齐


###### 语法


```

ctx.textBaseline = textBaseline
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| textBaseline | `<string>` | 'alphabetic'(默认),'middle','top','hanging','bottom','ideographic' |


##### **绘制文本**


##### CanvasRenderingContext2D.fillText()


填充文本


###### 语法


```

ctx.fillText(text, x, y)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| text | `<string>` | 在画布上输出的文本 |
| x | `<number>` | 绘制文本的左上角 x 坐标位置 |
| y | `<number>` | 绘制文本的左上角 y 坐标位置 |


##### CanvasRenderingContext2D.fillArcText()


填充弧形文本


###### 语法


```

ctx.fillArcText(text, x, y, radius, startAngle)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| text | `<string>` | 要绘制的文本 |
| x | `<number>` | 文本起始点的 x 轴坐标 |
| y | `<number>` | 文本起始点的 y 轴坐标 |
| radius | `<number>` | 圆的半径 |
| startAngle | `<number>` | 起始弧度， y 轴方向开始计算，单位以弧度表示。 |


##### **变换**


##### CanvasRenderingContext2D.rotate()


顺时针旋转当前坐标轴


###### 语法


```

ctx.rotate(angle)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| rotate | `<number>` | 顺时针旋转的弧度。如果你想通过角度值计算，可以使用公式： degree \* Math.PI / 180 。旋转中心点一直是 canvas 的起始点。 如果想改变中心点，可以通过 translate() 方法移动 canvas. |


##### CanvasRenderingContext2D.scale()


据 x 水平方向和 y 垂直方向，为 canvas 单位添加缩放变换。


###### 语法


```

ctx.scale(x, y)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | `<number>` | 水平方向的缩放因子 |
| y | `<number>` | 垂直方向的缩放因子 |


##### CanvasRenderingContext2D.translate()


对当前坐标系的原点(0, 0)进行变换


###### 语法


```

ctx.translate(x, y)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | `<number>` | 水平坐标平移量 |
| y | `<number>` | 竖直坐标平移量 |


##### CanvasRenderingContext2D.shear()


据 x 水平方向和 y 垂直方向，为 canvas 单位添加错切变换。


###### 语法


```

ctx.shear(x, y)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | `<number>` | 水平坐标错切量 |
| y | `<number>` | 竖直坐标错切量 |


---


## CanvasGradient

更新时间：2024-10-11 11:55:18


渐变对象，通过 CanvasRenderingContext2D.createLinearGradient() 创建


#### 语法


```

const gradient = ctx.createLinearGradient(0, 0, 200, 0)
gradient.addColorStop(0, '#ff0000')
gradient.addColorStop(1, '#0000ff')
```

复制代码
#### 方法


##### CanvasGradient.addColorStop()


该方法在 CanvasGradient 对象上添加一个由偏移值和颜色值指定的断点


###### 语法


```

gradient.addColorStop(offset, color)
```

复制代码
###### 参数


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| offset | `<number>` | `0`到`1`之间的值，表示渐变点在起点和终点中的位置 |
| color | `<string>` | CSS Color |


---


<!-- 文档 47: ui-component/component/rule.md -->


## 概述

## 概述

更新时间：2024-11-27 10:08:05


UI 组件是编写整个界面的基础。蓝河系统的组件拥有多项核心能力，包括属性、样式、事件和方法，同时还支持表冠旋转相关的事件处理和复杂动画，让您的界面更加生动有趣。


### 通用能力介绍


| 能力 | 简述 |
| --- | --- |
| 通用事件 | 即所有组件都支持的事件回调 |
| 通用属性 | 即所有组件都支持的属性。开发者可以在所有的组件标签上都使用通用属性 |
| 通用样式 | 即所有组件都可以支持的样式，它们均与 css 的属性样式用法保持一致 |
| 通用方法 | 提供给所有组件调用的方法 |
| UI 组件支持的表冠旋转 | 提供支持表冠旋转的 UI 组件与对应属性 |
| 颜色样式 | 支持颜色值类型 |
| 动画样式 | 支持开发者制作动画，提供了 transform 类、animation 类的动画样式属性，且参数格式与 CSS 对齐 |
| 渐变样式 | 渐变 (gradients) 可以在两个或多个指定的颜色之间显示平稳的过渡，用法与 CSS 渐变一致 |
| 组件动画 | 提供一个新的执行动画的便捷方法，创建一个 Animation 对象实例 |


---


<!-- 文档 48: ui-component/component/table/artboard.md -->


## artboard

## artboard

更新时间：2025-02-24 15:08:18


提供可交互的界面，接收用户的笔画输入


#### 子组件


不支持


#### 属性


支持[通用属性](/component/common/common-attributes/)


#### 样式


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| default-pen-color | `<color>` | #000 | 否 | 画笔颜色 |
| default-pen-size | `<length>` | 24px | 否 | 画笔尺寸 |
| width | `<length>` | `<percentage>` | - | 否 | 组件宽度 |
| height | `<length>` | `<percentage>` | - | 否 | 组件高度 |


#### 事件


支持[通用事件](/component/common/common-events/)


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| changewritepanel | number[] | 轨迹点数据，格式为：[x1,y1,x2,y2,...,xn,yn,-1,0,-1,-1]，其中最后四位 -1,0,-1,-1 为笔画结束符 |


#### 方法


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| clearData | 无 | 清除轨迹 |


---


<!-- 文档 49: ui-component/component/table/input.md -->


## input

## input

更新时间：2024-03-08 15:41:38


提供可交互的界面，接收用户的输入，默认为单行


#### 子组件


不支持


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | button | checkbox | radio | text | date | speak | text | 否 | 支持动态修改，`text` 为输入法录入， `speak` 为语音录入 |
| checked | `<boolean>` | false | 否 | 当前组件的 checked 状态，可触发 checked 伪类，type 为 checkbox 时生效 |
| name | `<string>` | - | 否 | input 组件名称 |
| value | `<string>` | - | 否 | input 组件的值 |
| placeholder | `<string>` | - | 否 | 提示文本的内容，type 为 text | date | speak 时生效 |


#### 样式


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | `<color>` | #000 | 否 | 文本颜色 |
| caret-color | `<color>` | #000 | 否 | 光标颜色 |
| font-size | `<length>` | 43.2px | 否 | 文本尺寸 |
| text-decoration | `<string>` | underline | 否 | 文本下划线，目前只支持 underline |
| placeholder-color | `<color>` | #000 | 否 | 提示文本的颜色，type 为 text | date | speak 时生效 |
| width | `<length>` | `<percentage>` | - | 否 | 组件宽度 |
| height | `<length>` | `<percentage>` | - | 否 | 组件高度 |


#### 事件


支持[通用事件](/component/common/common-events/)


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | 不同 type 参数不同，具体见下方 change 事件参数 | input 组件的值、状态发生改变时触发，type 为 button 时无 change 事件 |
| focus | index | 获取光标返回的下标值 |


##### change 事件参数


| 参数 | text | speak | checkbox | radio | 备注 |
| --- | --- | --- | --- | --- |
| name | | √ | √ | |
| value | √ | √ | √ | |
| checked | | √ | |  |


#### 方法


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| setSpan | Object | 动态设置文字样式，方法的入参不是必填项 目前只支持设置 color 和 text-decoration |
| focus | 无 | type 为 text | speak 时 生效。speak 可拉起语音输入，text 可拉起文字输入法 |


setSpan 参数说明如下:


| 属性 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| start | Number | - | 指定开始的位置 |
| end | Number | - | 指定结束的位置 |
| style | Object | - | 设置文字样式 ，不设置样式默认组件本身的样式 |


#### 示例


```

<template>
    <div style="flex-direction:column;">
       <input id="input" value="{{value}}" onfocus="focus"></input>
    </div>
    <div onclick="setSpan">设置文字样式</div>
</template>

<script>
 export default {
 data:{
 value:'input'
 },

 //组件获取光标后的回调值，在对应的位置插入值
 focus(index){

 //把输入框的值转为数组
 let data = String(this.value).split('')

 //在对应的位置插入对应的值
 data.splice(index,0,'插入input的值')

 //把转换后的值赋值回去给input组件的value
 this.value = data.join('');
 },

 setSpan(){
 //设置文字样式
 this.$element('input').setSpan({
 start:0,
 end:10,
 style:{
 'text-decoration':'underline',
 'color':'#000'
 }
 });
 }
 }
</script>
```

复制代码
#### 示例


修改 checkbox 组件的颜色


```

<template>
    <div style="flex-direction:column;">
       <input checked="{{checked}}" color='#a52a2a' type='checkbox'></input>
    </div>
</template>

<script>
 export default {
 data:{
 checked:true
 }
 }
</script>
```

复制代码
#### 示例


修改 radio 组件的颜色


```

<template>
    <div style="flex-direction:column;">
       <input checked="{{checked}}" color="#399FFF" type="radio"> </input>
    </div>
</template>

<script>
 export default {
 data:{
 checked:true
 }
 }
</script>
```

复制代码


---


<!-- 文档 50: ui-component/component/table/label.md -->


## label

## label

更新时间：2023-10-20 10:02:06


为 [input](/component/table/input/) 组件定义标注


#### 子组件


不支持


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| target | `<string>` | - | 否 | 目标 input 组件 id |


#### 样式


支持[通用样式](/component/common/common-styles/)


支持[text 样式](/component/basic/text/)


#### 事件


点击 label 组件，触发 target 绑定 id 的 checkbox 或者 radio 组件点击事件，扩大点击范围


---


<!-- 文档 51: ui-component/component/table/overview.md -->


## 概述

## 概述

更新时间：2024-10-11 11:55:18


用于收集和展示用户的信息，以便后续的处理。可通过搭配使用不同的表单组件，实现不同的业务需求，比如登录、注册和信息填写等


### 表单组件介绍


| 组件 | 简述 |
| --- | --- |
| input | 提供可交互的界面，接收用户的输入，默认为单行 |
| label | 为 [input](https://developers-watch.vmic.xyz/component/table/input/) 组件定义标注 |
| picker | 滚动选择器，支持四种选择器，普通选择器，日期选择器，时间选择器，弧形选择器 |
| slider | 滑动型输入器 |
| switch | 开关选择 |
| artboard | 提供可交互的界面，接收用户的笔画输入 |


---


<!-- 文档 52: ui-component/component/table/picker.md -->


## picker

## picker

更新时间：2025-03-31 12:03:25


滚动选择器，支持四种选择器，普通选择器，日期选择器，时间选择器，索引栏选择器。


#### 子组件


不支持


#### 属性


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


#### 样式


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| font-size | `<length>` | 40px | 否 | 未选中项文本尺寸 |
| selected-font-size | `<length>` | 56px | 否 | 选中项文本尺寸 |
| color | `<color>` | #ffffffff | 否 | 未选中项文本颜色 |
| selected-color | `<color>` | #ffffffff | 否 | 选中项文本颜色 |
| selected-background-color | `<color>` | #ff415fff | 否 | 选中项背景颜色 |
| linecolor | `<color>` | - | 否 | 下划线的颜色 |


#### 事件


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


#### 方法


**索引栏选择器**


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| scrollTo | { index: number } | 索引栏选择器平滑的滚动到 index 位置，index 为选项值的序号(从 0 开始)，调用后会触发 change 事件。scrollTo 和赋值属性 selected 的区别：selected 赋值是瞬间到达索引位置，scrollTo 方法是平滑的到索引位置 |


---


<!-- 文档 53: ui-component/component/table/slider.md -->


## slider

## slider

更新时间：2024-02-28 14:20:00


滑动型输入器


#### 子组件


不支持


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| min | `<number>` | 0 | 否 | - |
| max | `<number>` | 100 | 否 | - |
| value | `<number>` | 0 | 否 | - |
| type | `<string>` | 无 | 否 | type = `vertical` 为垂直方向，不设置为水平 |
| show-block | `<boolean>` | true | 否 | 配置滑块是否展示，默认为 true 展示滑块，值为 false 隐藏滑块 |


#### 样式


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | `<color>` | #f0f0f0 | 否 | 背景条颜色 |
| selected-color | `<color>` | #009688 | 否 | 已选择颜色 |
| block-color | `<color>` | - | 否 | 滑块的颜色 |
| padding-[left|right] | `<length>` | 32px | 否 | 左右边距 |


#### 事件


支持[通用事件](/component/common/common-events/)


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | {progress:progressValue, isFromUser:isFromUserValue } | 拖动过程中触发的事件  isFromUser 说明:  该事件是否由于用户拖动触发 |


---


<!-- 文档 54: ui-component/component/table/switch.md -->


## switch

## switch

更新时间：2023-10-20 10:02:06


开关选择


#### 子组件


不支持


#### 属性


支持[通用属性](/component/common/common-attributes/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| checked | `<boolean>` | false | 否 | 可触发 checked 伪类 |


#### 样式


支持[通用样式](/component/common/common-styles/)


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| thumb-color | `<color>` | `#009385` | 否 | 滑块颜色 |
| track-color | `<color>` | `#009385` | 否 | 滑轨颜色 |


#### 事件


支持[通用事件](/component/common/common-events/)


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | {checked:checkedValue} | checked 状态改变时触发 |


---


<!-- 文档 55: ui-component/component/ui-rotation.md -->


## UI 组件支持的表冠旋转

## UI 组件支持的表冠旋转

更新时间：2025-10-09 11:25:10


作为手表上非常重要的交互按钮，表冠在蓝河系统中得到了充分的支持。我们严格遵守了只有在获得表冠焦点后才能响应表冠事件的规则，在此前提下，蓝河系统提供了丰富的表冠响应方式，并支持开发者进行自定义和个性化的表冠响应。这些支持和机制的存在，可以让开发人员更加便捷地使用 UI 组件和表冠交互控制，提高表冠的交互性和可用性。


### UI 组件表冠焦点


为实现 UI 组件随表冠的旋转而滑动，务必确保 UI 组件处于获焦状态。同时，页面中只允许有一个组件获得焦点。


默认焦点分配在最外层的最后一个可响应表冠的组件上。


### 自定义 UI 组件对旋转表冠的响应


开发者可以根据实际情况对组件响应旋转表冠事件进行自定义处理。


### 默认支持的表冠组件如下：


默认支持表冠的组件，其响应表冠选择和手指操作一致，组件上该触发的生命周期都会触发。


| 组件名称 | 类型 |
| --- | --- |
| list | 用来呈现连续、多行数据的组件，包含一系列相同类型的列表项。 |
| swiper | 一种带滚动功能的组件，它采用滑动的方式在有限的区域内显示更多的内容。 |
| picker | 滚动选择器，允许用户从预定义范围中进行选择。当前支持时间选择器、日期选择器。 |
| slider | 滑动型输入器。 |
| scroll | 滚动视图容器。竖向或水平方向滚动容器，竖向滚动需要设置定高，水平滚动需要设置定宽。 |


### 接口定义


### 属性


#### 以下属性都是组件的通用属性


| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| vibration-effectEnabled | Boolean | true | 否 | 表冠旋转的时候是否具有振动的效果，true 表示有振动效 果，false 表示没有振动效果 |
| rotation-sensitivity | Number | 1 | 否 | 表冠灵敏度数值可设置为 高，正常，低以及默认的灵敏 度 1:低级，2:正常，3:高级 |
| touch-focusable | Boolean | false | 否 | 设置组件在触摸模式下是否可以接收对焦 。 |


### 事件


| 事件名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| rotation | Function | - | 否 | 组件监听表冠旋转的回调事件，组件的通用事件。 |


#### 事件参数返回值 Object 对象的具体参数说明如下:


| 接收参数 | 类型 | 说明 |
| --- | --- | --- |
| direction | Boolean | 旋转方向，表冠逆时针是正转返回 true，顺时针是反转返回 false。 |
| delta | delta | 单次旋转变化量，重新旋转时会清零，正常低速情况下变化量的绝对值恒为 1，正 负代表旋转方向，正转为正，反转为负，单位为旋转事件的最小刻度。 |
| velocity | Number | 旋转速度，方向之分与 delta 相同，单位为刻度/秒。 |
| duration | Number | 事件时间间隔，本次和上一次事件触发时的时间间隔，首次触发事件时时间为 0， 单位为毫秒。 |
| state | Number | 表冠旋转的状态，可取的值为 1:开始旋转，2:旋转中 ，3:旋转结束。 |


### 方法


| 方法名称 | 类型 | 说明 |
| --- | --- | --- |
| requestFocus | Boolean | 设置当前要获取焦点的组件，入参为 true 让当前组件抢占焦点，优先级最 高。此方法也是组件的通用方法。 |


#### 示例


##### 以 Picker 组件是默认支持表冠旋转的，旋转表冠组件聚焦设置示例代码如 下:


```

<script>
 export default {
 onReady() {
 const picker = this.$element('picker')
 picker.requestFocus(true)
 },
 }
</script>

<template>
  <picker class="w-[750px] h-[750px] bg-black" id="picker" type="time"></picker>
</template>

<style>
@tailwind utilities;
</style>
```

复制代码
##### 自定义 UI 组件支持表冠旋转


```

<script>
 export default {
 rotationHandler(ev){
 console.log('表冠事件输出'+ev )
 // 改变亮度
 },
 onReady () {
 const div = this.$element("div")
 div.requestFocus(true)
 }
 }
</script>

<template>
  <div class="w-full h-full flex flex-col justify-center items-center">
    <div class="w-60 h-60 bg-black" id="div" @rotation="rotationHandler">
  </div>
</template>

<style>
@tailwind utilities;
</style>
```

复制代码


---
