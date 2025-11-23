# vivo BlueOS 手表开发文档 - JavaScript API

> 本文档由爬虫自动生成，包含 67 个页面的内容

## 目录

- [自然语言处理](#自然语言处理)
- [概述](#概述)
- [语音技术](#语音技术)
- [视觉技术](#视觉技术)
- [K-V 数据存储](#k-v-数据存储)
- [存储空间统计](#存储空间统计)
- [通用错误码](#通用错误码)
- [概述](#概述)
- [调用规则](#调用规则)
- [说明](#说明)
- [vivo 智能终端设备侧](#vivo-智能终端设备侧)
- [概述](#概述)
- [手机侧](#手机侧)
- [vivo 智能终端设备 SDK 隐私政策](#vivo-智能终端设备-sdk-隐私政策)
- [vivo 智能终端设备 SDK](#vivo-智能终端设备-sdk)
- [穿戴业务 Kit](#穿戴业务-kit)
- [应用沙箱目录](#应用沙箱目录)
- [生命周期](#生命周期)
- [运动健康](#运动健康)
- [数据共享](#数据共享)
- [文件存储](#文件存储)
- [概述](#概述)
- [应用管理](#应用管理)
- [概述](#概述)
- [音频](#音频)
- [音频管理](#音频管理)
- [电量信息](#电量信息)
- [蓝牙](#蓝牙)
- [屏幕亮度](#屏幕亮度)
- [密码算法](#密码算法)
- [概述](#概述)
- [日志打印](#日志打印)
- [设备信息](#设备信息)
- [公共事件](#公共事件)
- [解压缩](#解压缩)
- [数据请求](#数据请求)
- [生成签名证书指纹](#生成签名证书指纹)
- [地理位置](#地理位置)
- [概述](#概述)
- [输入法](#输入法)
- [多媒体](#多媒体)
- [概述](#概述)
- [网络状态](#网络状态)
- [消息通知](#消息通知)
- [包管理](#包管理)
- [页面栈管理](#页面栈管理)
- [概述](#概述)
- [权限管理](#权限管理)
- [概述](#概述)
- [弹窗](#弹窗)
- [录音](#录音)
- [上传下载](#上传下载)
- [页面路由](#页面路由)
- [定时任务](#定时任务)
- [屏幕管理](#屏幕管理)
- [传感器](#传感器)
- [系统设置](#系统设置)
- [短信](#短信)
- [sim 卡管理](#sim-卡管理)
- [概述](#概述)
- [应用上下文](#应用上下文)
- [解包](#解包)
- [电话](#电话)
- [振动](#振动)
- [websocket](#websocket)
- [widgetManager](#widgetmanager)
- [widgetProvider](#widgetprovider)

---


<!-- 文档 1: js-api/ai/nlp/.md -->


## 自然语言处理

## 自然语言处理

更新时间：2025-04-30 20:56:55


### 使用前提条件


该接口底层依赖以下接口实现，开发者使用前需要在 manifest.json 中声明以下接口:


```

{ "name": "blueos.network.fetch" }
```

复制代码
### 使用


```

import nlp from "@blueos.ai.nlp"

```

复制代码
### 接口总览


| 接口名称 | 接口说明明 |
| --- | --- |
| translateText | 翻译一段源语言文本为目标语言文本，支持多国语言之间的互译。 |


#### nlp.translateText(params:TranslateParams):Promise<TranslateData>


翻译一段源语言文本为目标语言文本，支持多国语言之间的互译。


##### TranslateParams 参数


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| text | 是 | string | 翻译文本，utf-8 编码，长度限制 1200 |
| auth | 是 | Auth | 请求的身份验证信息，确保请求来源合法 |
| options | 否 | object | 源语言与目标语言参数，默认 from: 'en'，to: 'zh-CHS' |


##### Auth


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| appId | 是 | string | 应用 appId |
| appKey | 是 | string | 应用 appKey |


注： appId & appKey，需要在 [vivo 开发者平台](https://developers-ai.vivo.com.cn/documents?id=720) 申请


##### options 参数


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| from | 否 | string | 源语言，语言 code 见下方语言代码对照表 |
| to | 否 | string | 目标语言，语言 code 见下方语言代码对照表 |


##### 语言代码对照表


下表为各语言对应代码：


| 语言 | 代码 |
| --- | --- |
| 中文（简体） | zh-CHS |
| 英文 | en |
| 日文 | ja |
| 韩文 | ko |


##### 返回值 TranslateData


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| text | string | 原文 |
| from | string | 源语言 |
| to | string | 目标语言 |
| translation | string | 翻译后的文本 |


##### 异常错误码 TranslateCode 描述


| code 值 | 说明 |
| --- | --- |
| 20000 | 参数问题 |
| 10000 | 服务异常 |


##### 示例


```

nlp.translateText({
    text: 'Hello, World',
    auth: {
        appId:"12345678", // 需要替换自己的appId
        appKey: "dkjdkjfi" // 需要替换自己的appKey
        }
    })
    .then((result:TranslateData) => {
        console.log('翻译结果：', result);
        })
    .catch((data:string,code:TranslateCode) => {
        console.error('翻译失败：', code);
    });
```

复制代码


---


<!-- 文档 2: js-api/ai/overview/.md -->


## 概述

## 概述

更新时间：2024-11-13 15:38:47


基于 [vivo 算法平台](https://developers.vivo.com/product/ai/algorithm)，蓝河 AI 服务为开发者提供了图像、语音、自然语言处理等优质能力。通过这些能力，开发者可以为用户提供更智能的服务及体验。


### 子模块介绍


| 模块 | 简述 |
| --- | --- |
| 视觉技术 | 通过计算机视觉技术来处理和分析图像和视频数据，对其进行识别、分类、分割等操作 |
| 自然语言处理 | 通过计算机算法和人工智能技术来分析、理解、生成和处理人类语言 |
| 语音技术 | 通过计算机语音技术能够识别与合成人类语音。 |


---


<!-- 文档 3: js-api/ai/speech/.md -->


## 语音技术

## 语音技术

更新时间：2025-04-30 20:56:55


语音技术目前支持 ASR 与 TTS 两种技术。
  
  


> 
> ASR，自动语音识别技术（Automatic Speech Recognition）是一种将人的语音转换为文本的技术, 支持实时短语音识别与长语音听写。  
> 
> TTS，文字转语音技术（Text to Speech）是一种将文字转成语音的技术，可将上传的单句文本转成播报音频，包含了短音频生成和长音频生成能力。
> 
> 
> 


### 使用前提条件


该接口底层依赖以下接口实现，开发者使用前需要在 manifest.json 中声明以下接口:


```

{ "name": "blueos.network.webSocket" }
{ "name": "blueos.media.audio.mediaManager" }
```

复制代码
### 使用


```

import speech from "@blueos.ai.speech"
```

复制代码
### speech 接口总览


| 接口名称 | 接口说明 |
| --- | --- |
| createAsr | 创建 ASR 语音识别服务实例 AsrInstance |
| createTts | 创建 TTS 文字转语音服务实例 TtsInstance |


### AsrInstance 实例接口总览


| 接口名称 | 接口说明 |
| --- | --- |
| start() | 开启语音识别服务 |
| send(data:ArrayBuffer|TypedArray) | 发送语音数据，语音数据建议分帧发送，每帧包含的语音时长是 40 毫秒，单句不超过 60s |
| finish() | 结束语音识别服务 |
| onMessage = (result:ShortModeResult|LongModeResult) =>{} | 语音识别信息回调。通过 send()接口发送语音数据后，语音识别结果将通过该回调事件返回 |
| onStarted = () =>{} | 语音识别服务开启成功的回调。在服务开启成功后，语音识别服务将开始处理通过 send() 接口发送的数据 |
| onFinished = () =>{} | 语音识别服务结束回调。该回调可通过调用 finish()接口触发或者 endVadTime 超时自动触发 |
| onError = (data:string, code: number) =>{} | 语音识别服务异常回调 |


### TtsInstance 实例接口总览


| 接口名称 | 接口说明 |
| --- | --- |
| connect() | 连接文本转语音服务 |
| disconnect() | 断开文本转语音服务，并且释放网络资源与相关播放器资源，建议在应用销毁时调用。 |
| send(data:string) | 发送文本内容 |
| pauseAudio() | tts 实例服务暂停播放音频 |
| resumeAudio() | tts 实例服务恢复播放音频 |
| onMessage = (result:TtsResult) =>{} | 文本识别信息回调。通过 send()接口发送文本内容后，文本识别结果将通过该回调事件返回 |
| onConnected = () =>{} | 文字转语音服务连接成功的回调。在调用 connect() 连接服务成功后触发。服务连接成功后，文字转语音服务将开始处理通过 send() 接口发送的文本内容。 |
| onSpeakStarted() | 播放开始回调 |
| onSpeakPaused() | 播放暂停回调，调用了TtsInstance.pauseAudio()后会触发此回调 |
| onSpeakProgress(progress:string) | 播放进度信息回调。开始播放后，播放进度信息会通过该回调多次触发，直到播放完毕 |
| onSpeakFinished() | 播放完毕回调 |
| onSpeakResumed() | 恢复播放回调，调用了TtsInstance.resumeAudio()后会触发此回调 |
| onError = (data:string, code: number) =>{} | 文字转语音服务异常回调 |


#### createAsr(asrParams: AsrParams):AsrInstance


创建 ASR 实例


##### AsrParams 参数


| 属性 | 必填 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| auth | 是 | Auth | 无 | 请求的身份验证信息，确保请求来源合法 |
| model | 是 | AsrModel | AsrModel.ShortInput | 使用的 ASR 模型，支持短语音与长语句模型。 |
| config | 否 | AsrConfig | 无 | 初始化 ASR 客户端相关配置 |


##### Auth


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| appId | 是 | string | 应用 appId |
| appKey | 是 | string | 应用 appKey |


注： appId & appKey，需要在 [vivo 开发者平台](https://developers-ai.vivo.com.cn/documents?id=720) 申请


##### AsrModel


| 属性 | 说明 |
| --- | --- |
| ShortInputt | 短语音，输入法模型。 |
| ShortJovi | 短语音，语音助手模型 |
| LongListen | 长语句，听说模型。 |
| LongSubtitle | 长语句，字幕模型 |


###### 注：


1. 短语音指单轮识别时长在 60s 之内。
2. 长语句指单轮识别不限制时长。


##### AsrConfig


| 参数 | 类型 | 说明 | 必填 | 默认值 | 备注 |
| --- | --- | --- | --- | --- | --- |
| audioType | AudioType | 音频类型 | 否 | AudioType.Pcm | 使用的音频类型 |
| isWithPunctuation | boolean | 是否打开标点符号 | 否 | true | |
| endVadTime | number | 后端检测时间 | 否 | 1000 | 单位：毫秒， 仅实时短语音支持该参数 |
| isChinese2digital | boolean | 是否打开汉字转数字 | 否 | true | 仅实时短语音支持该参数 |
| lang | AsrLang | 语言 | 否 | AsrLang.Cn | 仅长语音听写支持该参数 |


##### AudioType


| 属性 | 说明 |
| --- | --- |
| Pcm | pcm 音频类型 |
| Opus | opus 音频类型 |


##### AsrLang


| 属性 | 说明 |
| --- | --- |
| Cn | 中文 |
| En | 英文 |


#### AsrInstance.start()


开启语音识别服务


#### AsrInstance.send(data:ArrayBuffer|TypedArray)


发送语音数据，语音数据建议分帧发送，每帧包含的语音时长是 40 毫秒，单句不超过 60s


#### AsrInstance.onMessage = (result:ShortModeResult|LongModeResult) =>{}


语音识别信息回调。通过 send()接口发送语音数据后，语音识别结果将通过该回调事件返回


##### ShortModeResult


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| text | string | asr 识别结果 |
| resultId | number | 结果序列号 |
| reformation | number | asr 识别返回， 1 代表修正 0 代表追加 |
| isLast | boolean | 是否为本次会话最后一条结果 |


##### LongModeResult


| **参数** | **类型** | **说明** |
| --- | --- | --- |
| code | ResultCodeEnum | 结果代码描述 |
| midPoint | string | 识别中间 midPoint 结果即一句话中间结果 |
| endPoint | string | 识别中间 rec 结果即完整一句话或者最后一句结果 |
| beginTime | number | 开始时间，单位毫秒 |
| endTime | number | 结束时间，单位毫秒 |
| speaker | number | 当有角色分离时返回 0 表示当前说话人， 非 0 表示角色 id，有角色变化 |


##### ResultCodeEnum


| 属性 | 说明 |
| --- | --- |
| 0 | 表示本次返回为识别中间结果，即一句话的完整结果，整个过程就是一句话中间结果，一句话完整结果…结束 |
| 8 | 表示本次返回为识别中间 midPoint 结果，即一句话的中间结果。 |
| 9 | 表示为客户端发完语音数据后的最后一句，客户端可以断开链接。 |


###### 举例说明 9、8 和 0 的区别：


比如有两句话，一句是“今天天气怎么样”，下一句是“明天天气怎么样”，
第一次返回“今天”，就是 8
第二次返回“今天天气怎么样”，就是 0，表示一句话的结束
第三次返回“明天”，就是 8
第四次返回“明天天气怎么样”，就是 9
然后就结束了


#### AsrInstance.onStarted = () =>{}


语音识别服务开启成功的回调。在服务开启成功后，语音识别服务将开始处理通过 send() 接口发送的数据


#### AsrInstance.onFinished = () =>{}


语音识别服务结束回调。该回调可通过调用 finish()接口触发或者 endVadTime 超时自动触发


#### AsrInstance.onError = (data:string, code: number) =>{}


语音识别服务异常回调


##### onError 回调参数定义


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | string | 失败信息描述 |
| code | FailCodeEnum | 失败业务码 |


##### FailCodeEnum


| 属性 | 说明 |
| --- | --- |
| 10000 | 参数校验失败 |
| 10002 | 引擎服务异常 |
| 10003 | 获取中间识别结果失败 |
| 10004 | 获取最终识别结果失败 |
| 10005 | 解析引擎数据异常 |
| 10006 | 引擎内部错误 |
| 10007 | 请求 nlu 出错 |
| 10008 | 音频超长 |
| 50001 | 使用超量 |


##### createAsr 示例代码


```

import media from "@blueos.media.audio.mediaManager";
import speech from "@blueos.ai.speech";

/\*\*
 \* 录音状态
 \* @enum {number}
 \*/
const AudioRecordState = {
  /\*\* 录音中 \*/
  record: 1,
  /\*\* 录音结束 \*/
  stop: 2,

  ready: 3,
};

export default {
  data: {
    result: "结果",
    auth: {
      appId: "xxx",
      appKey: "xxxx",
    },
    asr: null,
    model: "",
    pagraph: "",
    audioRecorder: null,
    audioRecordState: AudioRecordState.stop,
  },
  createAsr() {
    this.model = speech.AsrModel.ShortInput;
    const asr = speech.createAsr({
      auth: this.auth,
      model: this.model,
      config: {
        audioType: speech.AudioType.Pcm,
        isWithPunctuation: true,
        endVadTime: 1000,
        isChinese2digital: false,
      },
    });
    const arrs = [];
    asr.onMessage = (data) => {
      console.log(`onmessage data :${JSON.stringify(data)}`);
      if (this.model === speech.AsrModel.LongListen || this.model === speech.AsrModel.LongSubtitle ) {
        if (data.midPoint) {
          this.result = data.midPoint;
        } else if (data.endPoint) {
          arrs.push(data.endPoint);
          this.pagraph = arrs.join("\n");
          this.result = "";
        }
      } else {
        this.result = data.text;
      }
    };
    asr.onStarted = () => {
      console.log("onstarted");
      this.audioRecordState = AudioRecordState.ready;
    };
    this.asr = asr;
  },
  async recordAudio() {
    console.log("recordAudio start");

    if (this.audioRecordState == AudioRecordState.record) {
      console.log(`正在录音中，不允许重复录音`);
      return;
    }
    if (this.audioRecordState != AudioRecordState.ready) {
      console.log(`asr 接口还没ready ，请稍后`);
      return;
    }

    const audioRecorder = media.createAudioRecord({
      channelConfig: 1,
      sampleRateInHz: 16000,
    });

    this.audioRecordState = AudioRecordState.record;
    audioRecorder.read({
      callback: (buffer) => {
        this.asr.send(buffer);
      },
    });

    this.asr.onError = (data, code) => {
      console.log(`ux ws.onError data:${data};code:${code}`);
      this.audioRecordState = AudioRecordState.stop;
      audioRecorder.stop();
      audioRecorder.release();
    };
    this.asr.onFinished = (reason) => {
      console.log(`ux onFinished ${reason}`);
      this.audioRecordState = AudioRecordState.stop;
      audioRecorder.stop();
      audioRecorder.release();
    };

    this.audioRecorder = audioRecorder;
  },
  startWebsocket() {
    this.asr.start();
  },
  releaseRecord() {
    if (this.audioRecorder) {
      this.audioRecorder.stop();
      this.audioRecorder.release();
      this.asr && this.asr.finish();
    }
    this.audioRecordState = AudioRecordState.stop;
  },
};
```

复制代码
#### createTts(auth:Auth,engineId:string,clientInfo:ClientInfo):TtsInstance


创建 TTS 文字转语音服务实例


##### 参数


| 属性 | 必填 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| auth | 是 | Auth | 无 | 请求的身份验证信息，确保请求来源合法 |
| model | 是 | TtsModel | TtsModel.LongDefault | TTS 音频生成模型，支持短音频模型与长音频生成模型 |
| config | 否 | TtsConfig | 无 | 初始化 TTS 客户端相关配置 |
| isNeedPlay | 否 | boolean | false | 设置是否让TTS实例来播放声音，如果不需要TTS实例播放声音，则可以通过回调方法onMessage中 TtsResult.audio 获得合成语音的PCM类型数据 |


##### Auth


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| appId | 是 | string | 应用 appId |
| appKey | 是 | string | 应用 appKey |


注： appId & appKey，需要在 [vivo 开发者平台](https://developers-ai.vivo.com.cn/documents?id=720) 申请


##### TtsModel


| 属性 | 说明 |
| --- | --- |
| ShortJovi | 短音频生成，适用于对话合成场景，比如语音助手的应用场景 |
| LongDefault | 长音频生成，适用于长文本合成场景，比如小说阅读，屏幕朗读 |


##### TtsConfig


| 参数 | 类型 | 说明 | 必填 | 默认值 |
| --- | --- | --- | --- | --- |
| engineType | EngineType | 引擎类型, 支持中英文与优化效果 | 否 | EngineType.normal |
| audioType | AudioType | 音频类型 | 否 | AudioType.Pcm |
| sampleRate | number | 采样率。采样率越高，语音合成播放的效果越好，但是占用流量更多。可选值：[8000,16000,24000] | 否 | 24000 |
| speaker | ShortSpeaker|LongSpeaker | 语音合成的发音人 | 否 | ShortSpeaker.yige|LongSpeaker.yige |
| speed | number | 语速，可选值：[0-100] | 否 | 50 |
| volume | number | 音量，可选值：[1-100] | 否 | 50 |
| isStream | boolean | 是否按照流式方式返回音频，假如设置为 false 则按标点分段返回 | 否 | true |


##### EngineType


| 属性 | 说明 |
| --- | --- |
| normal | 普通效果 |
| enZh | 中英文 |
| en | 英文 |
| optimized | 优化效果 |


##### AudioType


| 属性 | 说明 |
| --- | --- |
| Pcm | pcm 音频类型 |
| Opus | opus 音频类型 |


##### ShortSpeaker


| 属性 | 说明 |
| --- | --- |
| yiwen | 奕雯 |
| yunye | 云野-温柔 |
| wanqing | 婉清 |
| xiaofu | 晓芙-少女 |
| yigeChild | 小萌-女童 |
| yige | 依格 |
| yiyi | 依依 |
| xiaoming | 小茗 |


##### LongSpeaker


| 属性 | 说明 |
| --- | --- |
| yiwen | 奕雯 |
| yunye | 云野-温柔 |
| yunyeNews | 云野-稳重 |
| yige | 依格-甜美 |
| yigeNews | 依格-稳重 |
| huaibin | 怀斌-浑厚 |
| zhaokun | 兆坤-成熟 |
| yaheng | 亚恒-磁性 |
| haiwei | 海蔚-大气 |
| qianqian | 倩倩-清甜 |
| enFemale | 英文女声 |
| xiaoyun | 晓云-稳重 |


#### TtsInstance.connect(data:string)


连接文本转语音服务


#### TtsInstance.disconnect()


断开文本转语音服务，并且释放网络资源与相关播放器资源。建议在应用销毁时调用。


#### TtsInstance.send(data:string)


发送文本内容


#### TtsInstance.pauseAudio()


tts 实例服务暂停播放音频


#### TtsInstance.resumeAudio()


tts 实例服务恢复播放音频


#### TtsInstance.onConnected = () =>{}


文字转语音服务连接成功的回调。在调用 connect() 连接服务成功后触发。服务连接成功后，文字转语音服务将开始处理通过 send() 接口发送的文本内容。


#### TtsInstance.onMessage = (result:TtsResult) =>{}


文本识别信息回调。通过 send()接口发送文本内容后，文本识别结果将通过该回调事件返回


##### TtsResult


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| audio | Unit8Array | 合成后的音频片段 |
| status | number | 当前音频流状态，0 表示开始合成（返回的第一帧数据），1 表示合成中，2 表示合成结束(返回的最后一帧数据） |
| progress | string | 合成进度，指当前合成文本的字符数-总的字符数。注：请注意合成是以句为单位切割的，若文本只有一句话，则每次返回结果是相同的。 |
| slice | int | 返回的第几帧数据 |


#### TtsInstance.onSpeakStarted = () =>{}


播放开始回调


#### TtsInstance.onSpeakPaused = () =>{}


播放暂停回调，调用了TtsInstance.pauseAudio()后会触发此回调


#### TtsInstance.onSpeakProgress = (progress:string) =>{}


播放进度信息回调。开始播放后，播放进度信息会通过该回调多次触发，直到播放完毕。


##### 返回值


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| progress | string | 播放进度，指当前播放文本的字符数-总的字符数。注：请注意合成是以句为单位切割的，若文本只有一句话，则每次返回结果是相同的。 |


#### TtsInstance.onSpeakFinished = () =>{}


播放完毕回调


#### TtsInstance.onSpeakResumed = () =>{}


恢复播放回调，调用了TtsInstance.resumeAudio()后会触发此回调


#### TtsInstance.onError = (data:string, code: number) =>{}


文字转语音服务异常回调


##### onError 回调参数定义


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | string | 失败信息描述 |
| code | FailCodeEnum | 失败业务码 |


##### FailCodeEnum


| 属性 | 说明 |
| --- | --- |
| 10000 | 缺少请求参数或者签名错误 （http 协议返回，status=400） |
| 10001 | 升级到 websocket 协议失败（http 协议返回，status=400） |
| 10010 | 发送数据不是 json 格式 |
| 10011 | 发送文本时，缺少必要的参数 |
| 10012 | 发送文本时，签名错误 |
| 以下是逻辑层服务器错误 | |
| 10030 | 发送文本到引擎时错误 |
| 10031 | 获取 audio 数据发生错误 |
| 10032 | 无可用的引擎服务器 |
| 以下是引擎层服务器错误 | |
| 11001 | 负载过大，拒绝新的请求 |
| 11002 | 请求头协议错误 |
| 11003 | 设置合成文本的请求参数错误 |
| 11004 | 获取 andio 数据的请求参数错误 |
| 11005 | session 重复了 |
| 11006 | 获取数据时，找到不到 session |
| 11007 | 创建引擎错误 |
| 11008 | 向算法引擎获取数据时出错 |
| 11009 | opus 压缩出现问题 |
| 11010 | 输入的合成文本不合法 |
| 以下是语音服务层错误 | |
| 20000 | 语音正在合成中，不允许发送新的文字 |
| 20010 | 语音缓存已满 |
| 20030 | 语音服务已经断连 |


##### createTts 示例代码


```

import media from "@blueos.media.audio.mediaManager";
import speech from "@blueos.ai.speech";

/\*\*
 \* 录音状态
 \* @enum {number}
 \*/
const AudioRecordState = {
  /\*\* 录音结束 \*/
  init: 0,
  inited: 1,
  play: 1,
  stop: 2,
  release: 3,
};

export default {
  data: {
    title: "欢迎体验 AI 服务",
    inputtext: "你好",
    auth: {
      appId: "您的appId",
      appKey: "您的appKey",
    },
    tts: null,
    model: "",
    audioRecorder: null,
    audioRecordState: AudioRecordState.stop,
  },

  createShort() {
    this.model = speech.TtsModel.ShortJovi;
    this.createTts();
  },
  createLong() {
    this.model = speech.TtsModel.LongDefault;
    this.createTts();
  },
  createTts() {
    const tts = speech.createTts({
      auth: this.auth,
      model: this.model,
      config: {
        speaker: speech.ShortSpeaker.yige,
        sampleRate: 24000,
        isStream: false,
      },
    });
    tts.onMessage = (data) => {
      if (this.audioRecorder) {
        this.audioRecorder.write({
          buffer: data.audio.buffer,
        });
      }
    };
    tts.onConnected = () => {
      logtool("onConnected");
      this.modetext = "短语音实例已连接"
    };

    this.tts = tts;
  },
  async createAudio() {
    const audioRecorder = media.createAudioTrack({
      sampleRateInHz: 24000,
      contentType: "speech",
      channelConfig: 1,
      audioFormat: 16,
    });
    audioRecorder.onError = function () {
      logtool(`createAudioRecord error`);
      this.audioRecordState = AudioRecordState.stop;
    };
    this.audioRecordState = AudioRecordState.inited;
    logtool(`createAudioRecord success`);
    this.audioRecorder = audioRecorder;
  },
  connect() {
    this.tts && this.tts.connect()
  },
  send() {
    this.tts && this.tts.send(this.inputtext);
  },
  stop() {
    this.audioRecordState = AudioRecordState.stop
    this.audioRecorder && this.audioRecorder.stop();
  },
  release() {
    this.audioRecordState = AudioRecordState.release
    this.audioRecorder && this.audioRecorder.release();
  },
  play() {
    this.audioRecordState = AudioRecordState.play
    this.audioRecorder && this.audioRecorder.play();
  },
  releaseRecord() {
    if (this.audioRecorder) {
      this.audioRecorder.stop();
      this.audioRecorder.release();
    }
  },
};
```

复制代码


---


<!-- 文档 4: js-api/ai/vision/.md -->


## 视觉技术

## 视觉技术

更新时间：2025-04-30 20:56:55


### 使用前提条件


该接口底层依赖以下接口实现，开发者使用前需要在 manifest.json 中声明以下接口:


```

{ "name": "blueos.network.fetch" }
```

复制代码
### 使用


```

import vision from "@blueos.ai.vision"

```

复制代码
### 接口总览


| 接口名称 | 接口说明 |
| --- | --- |
| commonOcr | 识别图片中的所有文字，并返回文字在图片中的位置信息，方便用户进行文字排版的二次处理参考 |
| segmentFace | 基于 AI 抠图技术，对图像中的人体头部进行分割，可用于图片背景切换或换脸玩法。 |
| segmentForeground | 对人像、猫、狗、车的图像进行分割 |
| inpaintForeground | 一种图像编辑方式。去除图片中不希望存在的人、猫、狗、车等，并填充以自然的图案，力求看不出修复痕迹。 |
| cropImage | 基于图像的主体内容及画幅要求，提供优质的图像智能裁剪能⼒ |
| generateIdPhoto | 通过人像分割算法识别照片面部区域，将其抠出后修改背景色，使之成为证件照。 |
| idCardOcr | 识别提取身份证中的姓名、性别、民族、出生日期、住址、公民身份证号码信息 |
| demoire | 对屏幕拍摄的带摩尔纹的图像进行摩尔纹去除 |
| deshadow | 提供文档图像阴影去除能力，同时保证原图文字清晰度 |


#### vision.commonOcr(params:OcrParams):Promise<OcrResult>


识别图片中的所有文字，并返回文字在图片中的位置信息，方便用户进行文字排版的二次处理


##### OcrParams 参数


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| auth | 是 | Auth | 请求的身份验证信息，确保请求来源合法 |
| image | 是 | string | 图片的 base64 编码（目前只支持识别 jpg、png、bmp 格式的图片） |
| options | 否 | OcrOptions | 请求的参数配置 |


##### Auth


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| appId | 是 | string | 应用 appId |
| appKey | 是 | string | 应用 appKey |


注： appId & appKey，需要在 [vivo 开发者平台](https://developers-ai.vivo.com.cn/documents?id=720) 申请


##### OcrOptions 说明


| 参数 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| pos | 否 | string | 默认为 2，可取值为 0,1,2。0 代表只需要文字信息，1 代表提供文字信息和坐标信息(坐标绝对值)，2 代表将 0 和 1 的信息同时提供. |
| checkDirection | 否 | boolean | 选择是否支持旋转图像、非正向文字识别，默认为 false 不支持 |


##### OcrResult 返回值


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| words | Array<WordInfo> | 文字信息 |
| OCR | Array<OcrInfo> | 文字与坐标信息 |
| angle | number | 旋转角度 |


###### WordInfo


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| words | string | 识别的文字信息 |


###### OcrInfo


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| words | string | 识别的文字信息 |
| location | locationInfo | 文字相关的坐标信息 |


###### locationInfo


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| top\_left | {x:number,y:number} | 左上角坐标信息 |
| top\_right | {x:number,y:number} | 右上角坐标信息 |
| down\_left | {x:number,y:number} | 左下角坐标信息 |
| down\_right | {x:number,y:number} | 右下角坐标信息 |


```

// 当pos 参数为0 时的返回结果
"OcrResult": {
    "words": [
        {"words": "取消"},
        {"words": "编辑"}
    ],
    "angle": 0
}


// 当pos 参数为1 时的返回结果
"OcrResult": {
    "OCR": [
        {
            "words": "取消",
            "location": {
                "top\_left": {"x": 658.0, "y": 1130.0},
                "top\_right": {"x": 893.0, "y": 1130.0},
                "down\_left": {"x": 658.0, "y": 1174.0},
                "down\_right": {"x": 893.0, "y": 1174.0}
            }
        },
        {
            "words": "编辑",
            "location": {
                "top\_left": {"x": 398.0, "y": 825.0},
                "top\_right": {"x": 1912.0, "y": 825.0},
                "down\_left": {"x": 398.0, "y": 1004.0},
                "down\_right": {"x": 1912.0, "y": 1004.0}
            }
        }
    ],
    "angle": 0
}
```

复制代码
##### 示例


```

vision.commonOcr({
    image: '',
    auth: {
        appId:"12345678", // 需要替换自己的appId
        appKey: "dkjdkjfi" // 需要替换自己的appKey
        }
})
.then((result:OcrResult) => {
    console.log('commonOcr result', result);
    })
.catch((data:string,code:OcrErrorCode) => {
        console.error(`commonOcr 失败, code:${code};data:${data}`);
    });
```

复制代码
##### 异常错误码 OcrErrorCode 描述


| code 值 | 说明 |
| --- | --- |
| 1 | ocr 识别失败 |
| 2 | 图像错误 |


#### vision.segmentFace(params:SegmentFaceParams):Promise<SegmentFaceResult>


人脸分割，基于 AI 抠图技术，对图像中的人体头部进行分割，可用于图片背景切换或换脸玩法。


##### SegmentFaceParams 参数


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| image | 是 | string | 图片 base64 编码,图片尺寸最大不超过 1024 个像素 |
| auth | 是 | Auth | 请求的身份验证信息，确保请求来源合法 |


##### SegmentFaceResult 返回值


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| originMask | string | 总的 mask 的 base64 编码，图像为单通道灰度图 |
| partBox | Array<string> | partMask 的 box 类别和位置，包含 idx, xmax, xmin,ymax,ymin；代表类别 idx 和 box 框在原图的坐标位置比例(0-1 之间) |
| partMask | Array<string> | partBox 对应框的的 mask 的 base64 编码，图像也为单通道灰度图 |
| size | {width:number,height:number} | 包含 height, width 字段，orginMask 的长宽型 |


##### 异常错误码 SegmentFaceErrorCode 描述


| code 值 | 说明 |
| --- | --- |
| 1 | 未检测到人脸 |
| 2 | 分割失败 |
| 3 | 无图 |


##### 示例


```

vision.segmentFace({
    image: ''
    auth: {
        appId:"12345678", // 需要替换自己的appId
        appKey: "dkjdkjfi" // 需要替换自己的appKey
    }
    })
    .then((result:SegmentFaceResult) => {
        console.log('face segment result', result);
    })
    .catch((data:string,code:SegmentFaceErrorCode) => {
        console.error(`segmentFace 失败, code:${code};data:${data}`);
    });
```

复制代码
#### vision.segmentForeground(params:SegmentForegroundParams):Promise<SegmentForegroundResult>


前景分割，对人像、猫、狗、车的图像进行分割


##### SegmentForegroundParams 参数


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| image | 是 | string | 图片 base64 编码,图片尺寸最大不超过 1024 个像素 |
| auth | 是 | Auth | 请求的身份验证信息，确保请求来源合法 |


##### SegmentForegroundResult 返回值


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| orginMask | string | 总的 mask 的 base64 编码，图像为单通道灰度图 |
| inpaintMask | string | 用于修复部分的 mask,为单通道灰度图，背景 0，前景 255 |
| partBox | Array<string> | partMask 的 box 类别和位置，包含 idx,xmax,xmin,ymax,ymin；代表类别 idx 和 box 框在原图的坐标位置比例(0-1 之间) |
| partMask | Array<string> | partBox 对应框的的 mask 的 base64 编码，图像也为单通道灰度图 |
| size | {width:number,height:number} | 包含 height, width 字段，orginMask 的长宽 |


##### 异常错误码 segmentForegroundErrorCode 描述


| code 值 | 说明 |
| --- | --- |
| 1 | 分割失败 |
| 2 | 未检测到图片 |


##### 示例


```

vision.segmentForeground({
    image: '',
    auth: {
        appId:"12345678", // 需要替换自己的appId
        appKey: "dkjdkjfi" // 需要替换自己的appKey
        }
    })
    .then((result:SegmentForegroundResult) => {
        console.log('segmentForeground result', result);
    })
    .catch((data:string,code:SegmentFaceErrorCode) => {
        console.error(`segmentForeground 失败, code:${code};data:${data}`);
    });
```

复制代码
#### vision.inpaintForeground(params:InpaintForegroundParams):Promise<InpaintForegroundResult>


前景修复，一种图像编辑方式。使用分割算法去除图片中不希望存在的人、猫、狗、车等，并填充以自然的图案，力求看不出修复痕迹。


##### InpaintForegroundParams 参数


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| image | 是 | string | 图片 base64 编码 |
| mask | 是 | string | Mask 的 base64 编码 |
| auth | 是 | Auth | 请求的身份验证信息，确保请求来源合法 |


##### InpaintForegroundResult 返回值


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| inpaintImg | string | 修复结果图的 base64 编码 |


##### 示例


```

vision.inpaintForeground({
    image: '',
    mask: '',
    auth: {
        appId:"12345678", // 需要替换自己的appId
        appKey: "dkjdkjfi" // 需要替换自己的appKey
        }
    })
    .then((result:InpaintForegroundResult) => {
        console.log('inpaintForeground result', result);
    })
    .catch((data:string,code:number) => {
        console.error(`inpaintForeground 失败, code:${code};data:${data}`);
    });
```

复制代码
#### vision.cropImage(params:CropImageParams):Promise<CropImageResult>


构图裁剪，基于图像的主体内容及画幅要求，提供优质的图像智能裁剪能⼒


##### CropImageParams 参数


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| auth | 是 | object | 请求的身份验证信息，确保请求来源合法 |
| imageList | 是 | object | 裁剪的图片信息列表，详见下方 imageList 说明 |
| aspectRatio | 是 | Array<string> | 裁剪比例列表 ,例如["100*60","103*83"] |


##### imageList


| 参数 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| imageUrl | 是 | string | 图片链接 |
| imgSymbol | 是 | string | 图片唯一标识 |


##### CropImageResult 返回值


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| imageList | Array<ImageResult> | 返回的图片信息列表，详见下方 ImageResult 说明 |


##### ImageResult


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| imageSymbol | string | 图片名称标识 |
| cropResult | Array<CropResult> | 裁剪结果，详见下方 CropResult 说明 |


##### CropResult 说明


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| aspectRatio | string | 输入的裁剪比例 |
| box | Array<number> | 该裁剪比例对应的裁剪坐标 |


##### 示例


```

const auth = {
        appId:"12345678", // 需要替换自己的appId
        appKey: "dkjdkjfi" // 需要替换自己的appKey
    }
    const request = {
        auth: auth,
        imageList:   {
            image\_url: "imageUrl" // 替换具体的图片路径
            },
            aspectRatio:["100\*60","103\*83"]
        }

    vision.cropImage(request)
        .then((result:CropImageResult) => {
            console.log('cropImage result', result);
        })
        .catch((data:string,code:number) => {
            console.error(`cropImage 失败, code:${code};data:${data}`);
        });
```

复制代码


---


<!-- 文档 5: js-api/api/storage/localstorage.md -->


## K-V 数据存储

## K-V 数据存储

更新时间：2025-10-09 11:25:10


### 接口声明


```

{ "name": "blueos.storage.storage" }
```

复制代码
### 导入模块


```

import storage from '@blueos.storage.storage' 或 const storage = require('@blueos.storage.storage')
```

复制代码
### 接口定义


#### storage.get(OBJECT)


读取存储内容


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | String | 是 | 索引 |
| default | String | 否 | 如果 key 不存在，返回 default。如果 default 未指定，返回长度为 0 的空字符串 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


##### success 返回值：


key 对应的存储内容


##### 示例：


```

storage.get({
  key: 'A1',
  success: function (data) {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### storage.getSync(OBJECT)


同步读取存储内容


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | String | 是 | 索引 |


##### 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| value | String | Boolean | Number | Object | Array | key 对应的存储内容 |


##### 示例：


```

const value = storage.getSync({ key: 'A1' })
```

复制代码
#### storage.set(OBJECT)


修改存储内容


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | String | 是 | 索引 |
| value | String | Boolean | Number | Object | Array | 否 | 新值。如果新值是长度为 0 的空字符串，会删除以 key 为索引的数据项 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


##### 示例：


```

storage.set({
  key: 'A1',
  value: 'V1',
  success: function (data) {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
##### 示例：


```

storage.set({
  key: 'A1',
  value: true,
  success: function (data) {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
##### 示例：


```

storage.set({
  key: 'A1',
  value: 18,
  success: function (data) {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
##### 示例：


```

storage.set({
  key: 'A1',
  value: { name: '李四', age: 18 },
  success: function (data) {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
##### 示例：


```

storage.set({
  key: 'A1',
  value: [18, 20],
  success: function (data) {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### storage.clear(OBJECT)


清空存储内容


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


##### 示例：


```

storage.clear({
  success: function (data) {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### storage.delete(OBJECT)


删除存储内容


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | String | 是 | 索引 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


##### 示例：


```

storage.delete({
  key: 'A1',
  success: function (data) {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### storage.key(OBJECT)


返回存储中某个 index 的键名


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | Number | 是 | 要查询的键名对应的索引 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


##### success 返回值：


index 对应的键名


##### 示例：


```

storage.key({
  index: 1,
  success: function (data) {
    console.log(`handling success, key = ${data}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### 属性


| 名称 | 参数类型 | 是否可读 | 是否可写 | 描述 |
| --- | --- | --- | --- | --- |
| length 　 | Number | 是 | 否 | 存储里的数据项的数量 |


##### 示例：


```

let length = storage.length
```

复制代码
##### 通用 fail 回调参数定义


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | string | 接口失败信息描述 |
| code | FailCodeEnum | 接口失败业务码 |


##### FailCodeEnum


| 属性 | 说明 |
| --- | --- |
| 302 | 存储空间不足 |


---


<!-- 文档 6: js-api/api/storage/statvfs.md -->


## 存储空间统计

## 存储空间统计

更新时间：2025-08-13 20:11:57


statvfs 一个用来获取应用空间的模块，包含了获取可用空间与总空间接口，支持同步与异步。


### 接口声明


```

{ "name": "blueos.storage.statvfs" }
```

复制代码
### 导入模块


```

import statvfs from '@blueos.storage.statvfs'
```

复制代码
### 接口定义


#### statvfs.getFreeSize()


查询指定文件系统可用空间大小，异步接口


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要查询的文件系统的文件路径 URI |
| success | (size:number)=>{} | 否 | 成功回调,返回 空闲的字节数，（单位为 Byte） |
| fail | Function | 否 | 失败回调 |


**使用示例：**


```

statvfs.getFreeSize({
  path: 'internal://files',
  success(size) {
    console.info('getFreeSize successfully, Size: ' + size)
  },
})
```

复制代码
#### statvfs.getFreeSizeSync()


查询指定文件系统可用空间大小，同步接口


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要查询的文件系统的文件路径 URI |


**返回值：**


空闲的字节数，（单位为 Byte）


**使用示例：**


```

const freeSize = statvfs.getFreeSizeSync('internal://files')
console.log(freeSize)
```

复制代码
#### statvfs.getTotalSize()


查询指定文件系统总空间大小，异步接口


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要查询的文件系统的文件路径 URI |
| success | (size:number)=>{} | 否 | 成功回调,返回总空间大小的字节数，（单位为 Byte） |
| fail | Function | 否 | 失败回调 |


**使用示例：**


```

statvfs.getTotalSize({
  path: 'internal://files',
  success(size) {
    console.info('getTotalSize successfully, Size: ' + size)
  },
})
```

复制代码
#### statvfs.getTotalSizeSync()


查询指定文件系统总空间大小，同步接口


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 需要查询的文件系统的文件路径 URI |


**返回值：**


总空间大小字节数，（单位为 Byte）


**使用示例：**


```

const totalSize = statvfs.getTotalSizeSync('internal://files')
console.log(totalSize)
```

复制代码


---


<!-- 文档 7: js-api/common/error-code/.md -->


## 通用错误码

## 通用错误码

更新时间：2024-01-10 16:04:30


### 提供公共的错误码


#### 其中，错误码 200 为系统通用错误码，所有系统未知异常发生时抛出。比如系统申请内存空间失败等。


| code | 含义 |
| --- | --- |
| 200 | 通用错误。 |
| 202 | 参数错误。 |
| 300 | I/O 错误。 |


---


<!-- 文档 8: js-api/common/overview/.md -->


## 概述

## 概述

更新时间：2023-10-31 19:37:39


在本章节中，我们将为您介绍蓝河系统 JS API 的调用规则和通用的错误码。通过阅读本章节，您将了解 JS API 的三种调用形式——同步、异步和订阅，并且掌握一些常见的错误码。


---


<!-- 文档 9: js-api/common/rule/.md -->


## 调用规则

## 调用规则

更新时间：2024-08-13 15:19:43


### 同步


同步方法调用后必须等到方法结果返回后才能继续后续的行为，返回值可以是任意类型。


### 示例


```

import context from '@blueos.app.context'

export default {
  getInfo() {
    const info = context.getInfo()
    console.log(JSON.stringify(info))
  },
}
```

复制代码
### 异步


异步方法调用整个过程不会阻碍调用者的工作。业务执行完成后会调用开发者提供的回调函数。


##### 异步接口支持的回调函数


| 回调函数 | 参数名 | 类型 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| success | data | any | 可选，返回值可以是任意类型，详见接口使用文档。 | 在执行成功时触发。 |
| fail | data,code | any,number | 错误信息内容，一般是字符串，也可能是其他类型，详见接口使用文档。 | 在执行失败时触发。 [code 是错误码](/api/common/error-code/) |
| complete | - | - | - | 在执行完成时触发。 |


##### 说明


```

success、fail和complete四个回调函数是否支持参考具体接口描述。
success、fail两个回调函数的触发是互斥的，即会且只会在一个回调函数中触发，触发任意一个都会再次调用complete回调。
```

复制代码
### 示例


```

import deviceInfo from '@blueos.hardware.deviceInfo'

export default {
  getInfo() {
    deviceInfo.getInfo({
      success: function (data) {
        console.log('Device information obtained successfully. Device brand:' + data.brand)
      },
      fail: function (data, code) {
        console.log(
          'Failed to obtain device information. Error code:' + code + '; Error information: ' + data
        )
      },
    })
  },
}
```

复制代码
### 订阅


订阅接口不会立即返回结果，开发者要在参数中设置相应的回调函数；该回调函数会在完成时或者事件变化时进行回调；可以执行多次。


##### 订阅接口支持以下回调函数


| 回调函数 | 参数名 | 类型 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| callback | data | any | 返回值可以是任意类型，详见接口使用文档。 | 接口调用成功或事件变更时触发，可能会触发多次。 |
| fail | data,code | any,number | 错误信息内容，一般是字符串，也可能是其他类型，详见接口使用文档。 | 在执行失败时触发。一旦触发该回调函数，callback 不会再次被调用，接口调用结束。[code 是错误码](/api/common/error-code/) |


##### 以监听罗盘数据为例


```

import sensor from '@blueos.hardware.sensor'

export default {
  subscribeCompass() {
    sensor.subscribeCompass({
      callback: function (ret) {
        console.log(`handling callback, direction = ${ret.direction}`)
      },
      fail: function (data, code) {
        console.log(`handling fail, code = ${code}`)
      },
    })
  },
}
```

复制代码


---


<!-- 文档 10: js-api/connect/brief-introduction/.md -->


## 说明

## 说明

更新时间：2025-04-29 11:37:34


针对手机及vivo智能终端设备互联，向第三方应用开发者提供高层次的、简单易用的 API。  

第三方应用开发者无需关心手机及vivo智能终端设备的互联细节，通过 API 提供的能力可以简单地实现设备状态查询订阅、设备信息查询、数据传输等操作。  

vivo智能终端设备SDK及穿戴业务Kit分别为手机及vivo智能终端设备提供API。  

手机侧应用基于 Java 开发，vivo智能终端设备侧应用基于 JS/Native 开发。  


| 设备 | 语言开发 | SDK | 说明 |
| --- | --- | --- | --- |
| 手机 | Java | vivo智能终端设备SDK | 基于Java语言的手机侧应用开发接口，可以实现与vivo智能终端设备侧应用的数据交互、获取vivo智能终端设备状态及信息等。 |
| vivo智能终端设备 | JS | 穿戴业务Kit | 基于JS语言的vivo智能终端设备侧应用开发接口，可以实现与手机侧应用的数据交互、获取手机设备状态及信息等。 |
| Native | 穿戴业务Kit | 基于C++语言的vivo智能终端设备侧应用开发接口，将在后续版本提供。 |


---


<!-- 文档 11: js-api/connect/interconnect/.md -->


## vivo 智能终端设备侧

## vivo 智能终端设备侧

更新时间：2025-01-17 11:58:56


用于和搭配使用的手机 app 进行通信，收发手机 app 数据。


### 接口声明


```

{ "name": "blueos.bluexlink.connectionManager" }
```

复制代码
### 导入模块


```

import interconnect from '@blueos.bluexlink.connectionManager' 或 const interconnect = require('@blueos.bluexlink.connectionManager')
```

复制代码
### interconnect.getPeerDeviceStatus(OBJECT)


获取 vivo 智能终端设备和手机的连接状态


**参数：**


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| success | 否 | Function | 成功回调 |
| fail | 否 | Function | 失败回调 |


**success 返回值:**


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| status | number | 0:未连接。1:已连接 |


**示例：**


```

interconnect.getPeerDeviceStatus({
  success: function (data) {
    if (data.status == 1) {
      console.log('已连接')
    } else if (data.status == 0) {
      console.log('未连接')
    }
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
### interconnect.instance(OBJECT)


创建连接实例


**参数：**


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| package | 是 | string | 手机 APP 包名 |
| fingerprint | 否 | string | 手机 APP 的证书指纹信息。 [证书指纹的获取方法](/api/system/generatecertificatethumbprint/) |


**返回值：**


[Connect](#connect)


**示例：**


```

const connnect = interconnect.instance({ package: 'com.xx.xx', fingerprint: 'xxxxx' })
```

复制代码
### connect


#### getReadyState(OBJECT)


获取 App 连接状态


**参数：**


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| success | 否 | Function | 成功回调 |
| fail | 否 | Function | 失败回调 |


**success 返回值:**


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| status | number | 1:连接成功。2:连接断开 |


**fail 返回值:**


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| data | string | 错误信息 |
| code | number | 错误码，1006 表示 连接断开 |


**示例：**


```

connect.getReadyState({
  success: function (data) {
    if (data.status == 1) {
      console.log('连接成功')
    } else if (data.status == 2) {
      console.log('连接失败')
    }
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### getPeerDeviceClientVersion(OBJECT)


查询 App 版本状态


**参数：**


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| success | 否 | Function | 成功回调 |
| fail | 否 | Function | 失败回调 |


**success 返回值:**


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| version | number | 手机应用版本号，有则正常返回，-1:未安装 |


**fail 返回值:**


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| data | string | 错误信息 |
| code | number | 错误码，1006 表示 连接断开 |


**示例：**


```

connect.getPeerDeviceClientVersion({
  success: function (data) {
    console.log(`handling success, version = ${data.version}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### send(OBJECT)


发送数据到手机 App 端


**参数：**


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| data | 否 | Object | 发送的数据 |
| success | 否 | Function | 成功回调 |
| fail | 否 | Function | 失败回调 |


**fail 返回值:**


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| data | string | 错误信息 |
| code | number | 错误码，1006 表示 连接断开 |


**示例：**


```

connect.send({
  data: { name: 'zangsan' },
  success: function () {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log('handling fail')
  },
})
```

复制代码
#### sendFile(OBJECT)


发送文件到手机 App 端


**参数：**


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| uri | 否 | String | 目录的 uri |
| success | 否 | Function | 成功回调 |
| fail | 否 | Function | 失败回调 |


**fail 返回值:**


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| data | string | 错误信息 |
| code | number | 错误码，1006 表示 连接断开 |


**示例：**


```

connect.sendFile({
  uri: 'internal://files/work/demo',
  success: function () {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log('handling fail')
  },
})
```

复制代码
#### close(OBJECT)


关闭当前连接


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 接口调用成功的回调函数 |
| fail | Function | 否 | 接口调用失败的回调函数 |


**示例：**


```

connect.close({
  success() {
    console.log(`close success`)
  },
  fail(data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### onOpen


用于指定连接打开时的回调


**示例：**


```

connect.onOpen = function () {
  console.log('connection opened')
}
```

复制代码
#### onClose


用于指定连接关闭时回调


**示例：**


```

connect.onClose = function () {
  console.log('connection closed')
}
```

复制代码
#### onMessage


用于指定接收手机 App 端数据的回调


**回调返回:**


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| isFileType | boolean | 是否是文件 |
| fileUri | string | 文件存储路径 |
| fileName | string | 文件名称 |


**示例：**


```

// 监听手机app的数据
connect.onMessage = function (data) {
  if (data && data.isFileType) {
    console.log('filename is', data.fileName)
  } else {
    console.log('msg is', data.data)
  }
}
```

复制代码
#### onError


用于指定连接失败后的回调


**回调返回:**


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | string | 错误信息 |
| code | number | 错误码, 1000：未知错误， 1001：手机 APP 未安装， 1002：手机三方 APP 和健康未连接，1006：蓝牙未连接，1007：指纹校验失败 |


**示例：**


```

connect.onError = function (error) {
  console.log(`connection error code =${error.code} data = ${error.data}`)
}
```

复制代码


---


<!-- 文档 12: js-api/connect/introduce/.md -->


## 概述

## 概述

更新时间：2023-11-02 15:33:26


基于开放兼容的 BlueXlink 互联底座，可以实现不同设备间的能力互补，为用户提供一致的交互体验。


  

BlueXlink 互联底座实现了设备发现，连接，组网，安全认证，协议兼容等复杂工作，开发者只需要调用简单的 API，就可实现设备互联功能的开发。


  

另外，我们提供了支持多种开发语言的，多套 SDK 支持不同设备间的互联。当前向手机及 vivo 智能终端设备第三方应用开发者开放 BlueXlink 互联能力。


  

基于 BlueXlink 互联底座提供的设备发现、连接、组网能力及运动健康应用，开发者可以无感地实现手机与 vivo 智能终端设备间的发现与连接，基于 BlueXlink 互联底座提供的数据交互能力，开发者可简单地实现手机侧应用及 vivo 智能终端设备侧应用间的消息通知发送、数据文件传输、设备状态获取等能力。


  

手机及 vivo 智能终端设备间的互联及数据共享为消费者提供更丰富的场景与体验，同时为第三方应用提供了更多的机会。


### 支持的设备


| 设备 | 要求 |
| --- | --- |
| 手机 | 安装 vivo 运动健康应用 |
| vivo 智能终端设备 | vivo WATCH3 |


### 开放能力


| 能力 | 手机侧应用 | vivo 智能终端设备侧应用 |
| --- | --- | --- |
| 设备发现 | √ | √ |
| 设备连接 | √ | √ |
| 设备信息查询 | √ | √ |
| 设备状态查询及订阅 | √ | √ |
| 数据传输（文件/字节流） | √ | √ |


### 技术架构


![structure](/a96058b8072db85ac79ffa2bfde1f9ff/structure.png)


### 手机侧


手机侧运动健康应用集成互联底座能力，我们针对手机侧第三方应用提供 vivo 智能终端设备 SDK。  
 基于 vivo 智能终端设备 SDK，第三方应用可以实现与 vivo 运动健康应用之间的数据通信和交互，以及与 vivo 智能终端设备侧第三方应用、vivo 智能终端设备之间的业务数据通信能力。  


### vivo 智能终端设备侧


vivo 智能终端设备集成互联底座能力，我们针对 vivo 智能终端设备侧第三方应用提供穿戴业务 Kit。  
 穿戴业务 Kit 为第三方应用提供设备状态查询与订阅、设备信息查询及数据传输能力的接口，设备发现及连接细节由互联底座完成，第三方应用开发者无需关心。  


### 开发指导


[开发指导](/api/connect/development-guidance/rpc-sdk-guidance/)


### API 参考


[API 参考](/api/connect/brief-introduction/)


---


<!-- 文档 13: js-api/connect/mobile-side/.md -->


## 手机侧

## 手机侧

更新时间：2023-10-30 19:45:39


### 接口使用


#### 同步发送数据


##### 命令发送 API


```

Request request = new Request.Builder()
                    .action(Constant.Action.ACTION\_DEVICE\_BUSINESS\_DATA)
                    .pkgName("com.vivo.health")
                    .data(data)
                    .build();
    Response response = RpcClient.getInstance().callSync(request);
    RpcLogger.i("test test\_send response:" + response.getData());
```

复制代码
#### 异步发送数据


```

    String data = "业务自定义数据";
    Request request = new Request.Builder()
            .action(Constant.Action.ACTION\_DEVICE\_BUSINESS\_DATA)
            .pkgName("com.vivo.health")
            .data(data)
            .build();
    RpcClient.getInstance().callAsync(request, new Callback() {
        @Override
        public void onResponse(Response response) {
            MockLogger.i("test test\_send\_async response:" + response.getData());
        }
    });
```

复制代码
#### 接收数据监听


```

DeviceRpcManager.getInstance().startDataReceiver(new IDataReceiver() {
            @Override
            public void onReceiveData(Request request) {
                switch (request.getAction()){
                     case Constant.Action.ACTION\_DEVICE\_BUSINESS\_DATA:
                        String data = request.getData();                        //接收端数据处理
                        String result = "填写的response";
                        response = Util.responseData(request, result);
                        DeviceRpcManager.getInstance().onResponse(response);
                        break;
                     default:
                        break;
                }
            @Override
            public void onReceiveNotification(Notification notification) {
                //处理接收的notification事件
            }
        });
```

复制代码
#### 发送通知数据


###### 通知数据没有返回值。


- 请求的数据：


```

String data = "业务自定义数据";
Notification notification = new Notification.Builder()
        .action(Constant.Action.ACTION\_DEVICE\_BUSINESS\_DATA)
        .pkgName("com.vivo.health")
        .data(data)
        .build();
RpcClient.getInstance().notify(notification);
```

复制代码
- 返回的数据：通知类数据没有返回结果。


### code 描述


| code | 描述 |
| --- | --- |
| 0 | 成功 |
| 1 | 目标 app 没有处理对应 ACTION |
| 2 | 数据解析错误 |
| 3 | 设备命令失败 |
| 4 | 设备未连接 |
| 5 | 请求设备数据超时 |
| 6 | 设备不存在 |
| 7 | 请求目标 app 超时 |
| 8 | 目标 app 不支持 sdk 功能或目标 app 未安装 |
| 9 | 权限拒绝 |
| -1 | 未知错误 |


### ACTION 列表


- ACTION\_DEVICE\_INFO 当前连接的设备信息
- ACTION\_DEVICE\_BUSINESS\_DATA 发送设备业务数据
- ACTION\_DEVICE\_DYNAMIC 设备动态信息更新


### 接口列表


#### 1.读取运动健康功能版本号


###### 获取运动健康功能版本号，版本号大于等于 2 说明具备当前能力


###### 请求的数据：


```

int version = DeviceRpcManager.getInstance().getHealthDeviceVersion();
```

复制代码
#### 2.获取当前连接的设备信息


###### 同步请求的数据


```

Request request = new Request.Builder()
        .action(Constant.Action.ACTION\_DEVICE\_INFO)
        .pkgName("com.vivo.health")
        .data(data)
        .build();
Response response = RpcClient.getInstance().callSync(request);
```

复制代码
###### 返回的数据：


```

{
    "device":
        {
        "deviceName":"Watch Name XXX2",
        "battery":90, //范围0-100
        "connected":true,
        "freeStorage":200000, //单位byte
        "mac":"11:11:11:11:11:11",
        "productId":2,
        "totalStorage":800000000 //单位byte
        "batteryState":1 //充电状态
        }
}

```

复制代码
#### 3.给设备发送 Request 消息


###### 同步请求的数据


```

JSONObject jsonObject = new JSONObject();
jsonObject.put("msg", "业务自定义数据");

Request request = new Request.Builder()
        .action(Constant.Action.ACTION\_DEVICE\_BUSINESS\_DATA)
        .pkgName("com.vivo.health")
        .data(jsonObject.toJSONString())
        .build();
Response response = RpcClient.getInstance().callSync(request);
```

复制代码
###### 返回的数据：


```

data：{"code":0}
```

复制代码
#### 4.设备动态信息更新


###### 数据监听


```

DeviceRpcManager.getInstance().registerDataReceiver(new IDataReceiver() {
            @Override
            public void onReceiveRequest(Request request) {

            }

            @Override
            public void onReceiveNotification(Notification notification) {
                try {
                    RpcLogger.i("server onReceiveNotification:" + notification);
                    switch (notification.getAction()) {
                        case Constant.Action.ACTION\_DEVICE\_DYNAMIC:
                            String data = notification.getData();
                            break;
                        default:
                            break;
                    }
                }catch (Exception e){
                    e.printStackTrace();
                }
            }
        });
```

复制代码
###### 获取到的 data 数据：在 onReceiveNotification 回调中，得到的 data 是如下格式：


```

{
    "device":
        {
        "deviceName":"Watch Name XXX2",
        "battery":90, //范围0-100
        "connected":true,
        "freeStorage":200000, //单位byte
        "mac":"11:11:11:11:11:11",
        "productId":2,
        "totalStorage":800000000 //单位byte
        "batteryState":1 //充电状态
        }
}
```

复制代码


---


<!-- 文档 14: js-api/development-guidance/privacy-policy/.md -->


## vivo 智能终端设备 SDK 隐私政策

## vivo 智能终端设备 SDK 隐私政策

更新时间：2024-10-11 12:02:48


#### 生效日期：2023 年 11 月 1 日


### 引言


本隐私政策适用于维沃移动通信有限公司及其关联方（以下简称“我们”或“vivo”，注册地址：广东省东莞市长安镇维沃路 1 号）提供的 vivo 智能终端设备 SDK 产品及服务（以下统称“SDK 产品”）。本文档要向开发者及其终端用户(“终端用户”)说明，为了实现产品的相关功能，本服务将如何处理终端用户的个人信息。


请开发者及终端用户务必认真阅读本规则。如您是开发者，请您确认充分了解并同意本规则后再集成 SDK 产品，如果您不同意本规则的任何内容，应立即停止接入及使用 SDK 产品；同时，您应仅在获得终端用户的同意后集成 SDK 产品并处理终端用户的个人信息。为了保障您的 App 合法合规，请 App 开发者务必将 SDK 产品升级到最新版本。   


#### 特别说明：


如您是开发者，您应当：   


1. 遵守法律、法规收集、使用和处理终端用户的个人信息，包括但不限于制定和公布有关个人信息保护的隐私政策等;
2. 在集成 SDK 产品前，告知终端用户 SDK 产品处理终端用户个人信息的情况，并依法获得终端用户同意;
3. 在获得终端用户的同意前，除非法律法规另有规定，不应收集终端用户的个人信息；
4. 向终端用户提供易于操作且满足法律法规要求的用户权利实现机制，并告知终端用户如何查阅、复制、修改、删除个人信息，撤回同意，以及限制个人信息处理、转移个人信息、获取个人信息副本和注销账号；
5. 遵守本规则的要求。   
 如开发者和终端用户对本规则内容有任何疑问、意见或建议的，可随时通过本规则第六条提供的方式与我们联系。


### 一、我们将如何收集和使用信息


#### （一）为实现 SDK 产品功能所需收集的个人信息：


开发者通过集成 vivo 智能终端设备 SDK，使用 vivo 智能终端设备 SDK 提供的能力，实现第三方 APP 同 vivo 运动健康之间进行数据通信和交互，也可实现 vivo 智能终端设备上的第三方 APP 同 vivo 智能终端设备的业务数据通信功能。为实现 SDK 产品的相应功能所必须，我们将向终端用户或开发者收集终端用户在使用与 SDK 产品相关的功能时产生的如下个人信息：


基于不同的设备和系统及系统版本，以及开发者在集成、使用我们 SDK 产品时决定的权限，收集的设备信息会有所不同，因此开发者应对实际收集的个人信息向用户进行说明。


vivo 智能终端设备 SDK 主要用于提供给第三方 APP 集成，他提供了一种简便的和运动健康之间建立数据连接通道的方式，用于三方 APP 和 vivo 运动健康之间进行数据通信和交互，间接实现了三方 APP 与 vivo 手表设备的业务数据通信功能。  


| 个人信息类型 | 个人信息清单 | 使用目的 | 存留期 |
| --- | --- | --- | --- |
| 设备信息 | 设备名称、电量、连接状态、可用空间、mac地址、存储空间、充电状态 | 用于接入SDK的第三方app查询或订阅穿戴设备状态、提供开放能力。 | 不涉及，该数据不存储至本地，不上云 |


如果您是开发者，在您接入、使用本服务前，我们要求您在隐私政策中向终端用户告知我们 SDK 的名称、SDK 提供方名称、收集个人信息类型、使用目的、隐私政策链接，并获取用户的同意或取得其他合法性基础。您可以参考如下方式提供条款内容：  


##### 第三方 SDK 名称：vivo 智能终端设备 SDK


##### 第三方名称：维沃移动通信有限公司


##### 收集个人信息类型：设备信息（设备名称、电量、连接状态、可用空间、mac 地址、存储空间、充电状态）


##### 使用目的：用于接入 SDK 的第三方 app 查询或订阅穿戴设备状态，提供开放能力。


##### 隐私政策链接：[SDK 隐私政策](/api/connect/development-guidance/privacy-policy/)


#### （二）根据法律法规的规定，以下是征得用户同意的例外情形：


##### （1）与国家安全、国防安全有关的；


##### （2）与公共安全、公共卫生、重大公共利益有关的；


##### （3）与犯罪侦查、起诉、审判和判决执行等有关的；


##### （4）出于维护个人信息主体或其他个人的生命、财产等重大合法权益但又很难得到本人同意的；


##### （5）所收集的个人信息是个人信息主体自行向社会公众公开的；


##### （6）从合法公开披露的信息中收集的您的个人信息的，如合法的新闻报道、政府信息公开等渠道；


##### （7）根据您的要求签订合同所必需的；


##### （8）用于维护所提供的产品与/或服务的安全稳定运行所必需的，例如发现、处置产品与/或服务的故障；


##### （9）为合法的新闻报道所必需的；


##### （10）学术研究机构基于公共利益开展统计或学术研究所必要，且对外提供学术研究或描述的结果时，对结果中所包含的个人信息进行去标识化处理的。


### 二、信息的存储


#### （一）存放地域


我们遵守法律法规的规定，将在中华人民共和国境内收集和产生的个人信息存储在境内。  


#### （二）存储期限


除非法律法规另有要求，我们仅在实现本声明所述目的所必需的时间内保留您的个人信息，超期会进行删除或进行匿名化处理。  


### 三、数据安全保护


为保护网络的完整性，vivo 采取了符合业界标准的安全防护措施以保护个人信息，防止数据遭到未经授权的访问、使用、修改、公开披露。我们将采取一切合理可行的措施保护个人信息，包括但不限于：  


#### a) 进行安全检查、使用加密工具和软件、以及其他合理的安全措施和程序；


#### b) 采取加密技术确保信息传输与存储过程的安全性和保密性，并建立安全事件响应团队，及时进行问题的定位、分析、处理；


#### c) 限定授权访问人员，并采取分级权限管理措施，仅网络管理员和基于业务必要需了解资料的人员才能从内部访问用户的非公开个人信息。


如果 vivo 知悉 vivo IT 数据网络安全受到危害或由于外部行为（包括但不限于外部安全攻击）使用户的非公开信息披露给不相关第三方，尽管本隐私政策中有其他规定，vivo 仍将采取其认为适当的合理措施，包括但不限于内部调查、上报并通知执法机构、以及配合执法机构工作等；如果 vivo 发现用户提供给 vivo IT 数据网络的个人信息以非本隐私声明允许的方式进行了非法披露，vivo 将尽快采取合法合理措施通知相关用户，告知被披露的信息以及 vivo IT 数据网络对该信息的知悉程度，最大程度采取补救措施。  


### 四、未成年人保护


本 SDK 产品主要面向成年人。  
 若您是开发者，如果终端用户是未满 14 周岁的未成年人（“儿童”），您应当向儿童的父母或其他监护人告知本规则，并在征得儿童的父母或其他监护人同意的前提下处理儿童个人信息。如果我们发现开发者未征得儿童监护人同意向我们提供儿童个人信息的，我们将会采取措施尽快删除。  
 若您是儿童监护人，当您对您所监护儿童个人信息保护有相关疑问或权利请求时，您可以联系开发者，或通过本规则第六条提供的方式与我们联系。  


### 五、变更


我们可能适时修订本规则内容。如果某一功能或服务未在前述说明中且需要收集终端用户的信息，我们将在变更生效前，通过网站公告等方式进行提示。如您是开发者，当更新后的本规则对处理终端用户的个人信息情况有重大变化的，您应当适时更新隐私政策，并以弹框形式通知终端用户并且获得其同意，如果终端用户不同意接受本规则，请停止集成 SDK 产品。  


### 六、如何联系我们


如果您有任何疑问、意见或建议，请拨打我们的客服电话 95033 或发送电子邮件至[iotpartners@vivo.com](mailto:iotpartners@vivo.com)的方式与我们联系。


---


<!-- 文档 15: js-api/development-guidance/rpc-sdk-guidance/.md -->


## vivo 智能终端设备 SDK

## vivo 智能终端设备 SDK

更新时间：2025-07-23 09:40:34


### 开发准备，申请 appid


##### 1. 申请 app 开发者接入，接入地址：[vivo 开放平台](https://dev.vivo.com.cn/)，已有账号则无需申请，直接登录


##### 2. 申请账号后，注册对应的 app，取到 appid


### SDK 集成


```

implementation files('libs/device-rpc.aar')
```

复制代码
### 初始化


```

 // 在 app 恰当的时候初始化，如果需要拉起并发送到通知，建议放 application 里面。
 DeviceRpcManager.getInstance().init(getApplicationContext(), String encryStr,InitCallBack initCallBack);
```

复制代码
##### encryStr:需联系 vivo 对接人员获取（[xiaoming.ling@vivo.com](mailto:xiaoming.ling@vivo.com)），请提供包名、appid


##### InitCallBack:鉴权结果回调


##### manifest 中添加 meta 数据，固定格式和名称，用于设备查询 app 功能信息


```

<meta-data android:name="health.device.manager.version" android:value="1" />
<meta-data android:name="appid" android:value="开发平台申请的appid" />
```

复制代码
### 三方 APP 协议参考设计


三方 App 除了获取“运动健康功能版本号”，“读取设备对应功能版本号”外，通常需要使用接口<给设备发送 Request 数据>跟手机交换数据，为了区分不同 Request 数据类型，建议使用如下 Json 格式


```

{
     "type":"type\_xxxx"
     "data":{}
}
```

复制代码
##### 对应的 Response 数据类型，建议使用如下 Json 格式：


```

{
     "code"：0
     "result":{}
}
```

复制代码
##### 其中


- type 指定数据类型，不同的业务对应不同的类型，用于对端区分数据，作相应处理
- data 数据，不同业务有不同的数据
- code 对端的业务执行结果
- result 结果依赖不同的 type 而不同


### SDK 下载


[vivo 智能终端设备 SDK](https://h5.vivo.com.cn/health/rpcsdk/new/device-rpc.aar)


### API 参考


[手机侧](/api/connect/mobile-side/)


### 隐私政策


[隐私政策](/api/connect/development-guidance/privacy-policy/)


---


<!-- 文档 16: js-api/development-guidance/watch-guidance/.md -->


## 穿戴业务 Kit

## 穿戴业务 Kit

更新时间：2023-10-31 19:37:39


### 代码示例


##### 创建连接实例


```

 create() {
    console.log(`click here!`)
    connect = interconnect.instance({ package: 'com.vivo.health.deviceRpcSdk.demo', fingerprint: '5de8782b74c1e2e064786428c229ab68884e7563704d0642466bf5f51dfa1330' })
    this.create_text = "成功创建"
    this.onopen()
    this.onclose()
    this.onerror()
    this.onmessage()
    timer = setTimeout(() => {
      console.log(`等待 3s 执行send`)
      this.send()
    }, 3 \* 1000)

  },
```

复制代码
##### 数据发送


```

  send() {
    console.log('send--------')
    const self = this;
    if (connect == null) {
      console.log('interconnect feature not instanced!!')
      return
    }
    connect.send({
      data: {
        type: 'getIsLogin'
      },
      success: function () {
        self.send_status = '是'
        console.log(`handling success`)
      },
      fail: function (data, code) {
        self.send_status = '否'
        console.log(`handling fail, code = ${code}`)
      }
    })
  },
```

复制代码
##### 数据接收


```

  onmessage() {
    console.log('onmessage--------')
    // 监听手机侧应用的数据
    const self = this
    if (connect == null) {
      console.log('interconnect feature not instanced!!')
      return
    }
    connect.onmessage = function (data) {
      if (data && data.isFileType) {
        console.log('filename is', data.fileName)
      } else {
        console.log('msg is', data)
      }
      self.onmessage_data = data
    }

  },
```

复制代码
##### 断开及销毁


```

  close() {
    const self = this
    if (connect == null) {
      console.log('interconnect feature not instanced!!')
      return
    }
    connect.close({

      success() {
        console.log(`close success`)
        self.close_data = 'success!'
      },
      fail(data, code) {
        console.log(`handling fail, code = ${code}`)
        self.close_data = 'fail!'
      },
    })
  },

  onDestroy() {
    if(timer != null){
      clearTimeout(timer) // 清除定时函数
    }
    this.close()
  },
```

复制代码
### API 参考


[vivo 智能终端设备侧](/api/connect/interconnect/)


---


<!-- 文档 17: js-api/extend/file-sandbox/.md -->


## 应用沙箱目录

## 应用沙箱目录

更新时间：2025-10-09 11:25:10


蓝河应用框架给每个应用分配了一个专属的应用目录，蓝河应用的数据访问和操作都被限制在该目录内，此目录下存放的数据可以保护数据的安全性，这个目录称为 “应用的沙箱目录”。


### 应用沙箱目录定义


应用沙箱目录定义详细说明


| **沙箱目录名** | **定义说明** |
| --- | --- |
| files | 应用在本设备上用于存放小而重要的数据目录（如用户登录数据），安全且持久有效，随应用卸载而删除。 |
| cache | 应用在本设备上用于存放缓存文件的目录（如图片、音频缓存），此目录可能会因系统空间不足而被清理，用户也可通过系统管理类应用清理该目录，此目录随应用卸载而删除，适合保存不重要的缓存数据。 |
| mass | 应用在本设备上用于存放大文件的目录（如下载的音频文件），此目录随应用卸载而删除。 |
| tmp | 应用在本设备上用于存放临时文件的目录（如临时日志），应用退出后就会清理该目录，此目录随应用卸载而删除，适合存放使用后即可删除的文件数据。 |
| preferences | 应用在本设备上用于存放 key-val 数据的目录，有大小限制，此目录下的数据通过 storage 的 API 写入，适合保存首选项和配置文件，随应用卸载而删除。 |


### 访问沙箱目录


沙箱目录是通过 URI 形式访问，每个沙箱目录都有对应的 URI 标准标识。可以使用 URI 的地方都可以访问到沙箱目录，下面表格展示了不同沙箱目录的对应的 URI 格式。


| **沙箱目录名** | **URI 定义** |
| --- | --- |
| files | internal://files/ |
| cache | internal://cache/ |
| mass | internal://mass/ |
| tmp | internal://tmp/ |


如需要往 files 沙箱存放一个 json 文件，则可如下操作：


```

file.writeText({
  uri: 'internal://files/demo.json',
  text: '{"name": "张三"}',
  success: function () {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
### 如何选择存放沙箱目录的位置


沙箱目录的不同划分是为了对数据进行分类管理，将数据放在合理的目录下会让应用获得更大的收益。


对于不同沙箱目录的使用场景如下：


- files：此目录用于存放小而重要的数据，目录长期有效，可以保存的文本文件，如 json。
- mass：此目录用于存放大而不太重要的数据，目录长期有效，可以保存需要需要持久化的图片、音频、视频等文件。
- cache：此目录用于存放缓存文件，适合保存不重要的缓存数据，如缓存的音频、视频等。
- tmp：此目录用于存放临时文件，应用退出后可能被清理，适合存放日志等临时文件。
- preferences：此目录只能通过 storage 能力访问，适合存放应用运行中的 key-val 数据。


### JS 如何正确的使用沙箱目录


要在 js 中使用沙箱目录，只要遵循蓝河应用框架开发即可。


- 存放/获取 文件时，使用 blueos.storage.file 能力，并且使用 URI 拼接，避免使用绝对路径写法。
- 存放/获取 key-val 时，使用 blueos.storage.storage 能力。
- 存放在沙箱目录内的图片，如果要用 image 标签访问，也需要使用 URI 访问。
- 同上，音频和视频文件如果要播放同样是需要 URI 访问。


---


<!-- 文档 18: js-api/extend/lifecycle/.md -->


## 生命周期

## 生命周期

更新时间：2025-07-03 13:00:36


> 
> 了解应用/页面/自定义组件的生命周期与状态
> 
> 
> 


![生命周期图](/dbc9b48af6d508812e00cdec9404e8e0/lifecycle.png)
### 应用生命周期


#### onCreate


监听应用创建，应用创建时调用。


**参数**


无


#### onDestroy


监听应用销毁，应用销毁时调用。


**参数**


无


#### onShow


应用显示在前台时调用。


**参数**


无


#### onHide


应用退到后台时调用。


**参数**


无


### 页面生命周期


#### onInit


监听页面初始化。当页面完成初始化时调用，只触发一次


**参数**


无


#### onReady


监听页面创建完成。当页面完成创建可以显示时触发，只触发一次


**参数**


无


#### onShow


onShow 是一个页面生命周期函数，用于监听页面显示的事件。当一个页面被打开或从后台切换到前台时(当应用处于后台时打开页面但页面没有在前台显示时 onShow 方法不会被触发)，onShow 方法会被触发。


**参数**


无


#### onHide


onHide 是一个页面生命周期函数，用于监听页面隐藏的事件。当一个页面被切换到后台或关闭时(当应用处于后台时页面被关闭 onHide 方法不会被触发)，onHide 方法会被触发。


**参数**


无


#### onDestroy


监听页面退出。当页面跳转离开（退出页面栈）时触发


**参数**


无


#### onBackPress


监听返回动作。当用户执行返回操作时触发。只有当前页面配置了 followHand : disable，该接口才生效。


**参数**


无


**返回值**


| 类型 | 描述 |
| --- | --- |
| boolean | 返回 true 表示页面自己处理返回逻辑，返回 false 表示使用默认的返回逻辑，不返回值会作为 false 处理； 注意：该函数不支持声明为异步函数（即：使用`async`标识），因为返回值代表界面要立即响应用户操作； |


#### onRefresh


监听页面重新打开。onRefresh 在 onShow 之前执行。


当页面在 manifest 中 launchMode 标识为'singleTask'时，仅会存在一个目标页面实例，用户多次打开目标页面时触发此函数。


该回调中参数为重新打开该页面时携带的参数。


详见[页面启动模式](/reference/extend/launch-mode)


**参数**


| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| query | Object | 通过 deeplink、router.push 等接口传入的 uri 中 query 解析成的对象，或者 router.push 等接口传入的 params 对象 |


#### onKey


监听按键响应。当按键被触发时回调


**参数**


| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| event | Object | 被触发的按键事件 |


**event 参数**


| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| keyCode | Number | 按下的键位，0：下键(电源键)，1：上键 |
| keyAction | Number | 按下或弹起的动作 0：按下 1：短按弹起 2：长按弹起 |
| repeatCount | Number | 连续按的次数，按键在长按的时候，会连续产生多个按下事件，这个时候第一个按下事件的 repeatCount 为 0，之后的按下事件 repeatCount 会递增。 |


**示例代码：**


```

onKey(event) {
  console.log(`key pressed! ${JSON.stringify(event)}`);
  console.info(`触发页面生命周期 onKey`)
}
```

复制代码
#### onConfigurationChanged


监听系统语言改变


**参数**


| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| event | Object | 应用配置发生变化的事件 |


**event 参数：**


| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| type | String | 应用配置发生变化的原因类型，支持的 type 值如下所示 |


**event 中`type` 现在支持的参数值如下：**


| 参数值 | 描述 |
| --- | --- |
| locale | 应用语言、地区变化而发生改变 |


**示例代码：**


```

onConfigurationChanged(evt) {
  if (event && event.type && event.type === 'locale') {
    console.log('locale or language changed!')
  }
}
```

复制代码
#### onPalmOver


监听手掌覆盖事件


**参数**


无


**返回值**


`true` 表示不将事件继续传递给 launcher，其他值或者不返回都会将事件继续传递给 launcher。


**示例代码：**


```

onPalmOver(evt) {
  console.info(`大手掌事件 onPalmOver`)
  return true;
}
```

复制代码
### 自定义组件生命周期


自定义组件，指的是通过 import 标签引入的 ViewModel 组件


#### onInit


监听初始化，当数据驱动化完成时触发


**参数**


无


#### onReady


监听模板创建完成，当模板创建完成时触发


**参数**


无


#### onDestroy


监听组件销毁，当销毁时触发


**参数**


无


---


<!-- 文档 19: js-api/health/health/.md -->


## 运动健康

## 运动健康

更新时间：2025-06-30 19:53:14


### 概述


蓝河应用等运动健康模块旨在支持用户的运动和健康数据管理。该模块提供了两个主要部分：采样数据和统计数据，为用户提供了全面的健康数据管理和实时监控功能，对于健康和运动类应用、健康监测工具和健康管理应用非常有用。


### 接口声明


```

{ "name": "blueos.health.health" }
```

复制代码
### 导入模块


```

import health from '@blueos.health.health' 或 const health = require('@blueos.health.health')
```

复制代码
**开发者需要在 manifest.json 里面配置权限：**


```

{
  "permissions": [{ "name": "watch.permission.READ\_HEALTH\_DATA" }]
}
```

复制代码
### 接口定义


#### getRecentSamples


获取最近一次采样数据


**参数**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataTypes | [DataType](#datatype)[] | 是 | 数据类型 |
| success | (recentSamples: [RecentSample](#recentsample)[]) => void | 是 | 回调函数，返回值是一个 [RecentSample](#recentsample) 数组 |
| complete | () => void | 否 | 完成的回调函数 |
| fail | (data: string, code: number) => void | 否 | 失败回调函数 |


**示例**


```

health.getRecentSamples({
  dataTypes: [health.DATA\_TYPES.HEART\_RATE, health.DATA\_TYPES.STEP\_COUNT],
  success: (res) => {
    console.log(`current heart rate(${res[0].dataType}) is`, res[0].data.value, 'bpm')
  },
})
```

复制代码
#### subscribeSample


监听采样数据变化


**参数**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | [DataType](#datatype) | 是 | 数据类型 |
| callback | (sample: [Sample](#sample)) => void | 是 | 回调函数，返回值是一个[Sample](#sample) |
| fail | (data: string, code: number) => void | 否 | 失败回调函数 |


**示例**


```

health.subscribeSample({
  dataType: health.DATA\_TYPES.HEART\_RATE,
  callback: (res) => {
    console.log(`current heart rate(${res.value}) is`)
  },
})
```

复制代码
#### unsubscribeSample


取消监听采样数据变化


**参数**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | [DataType](#datatype) | 是 | 数据类型 |


**示例**


```

health.unsubscribeSample({
  dataType: health.DATA\_TYPES.HEART\_RATE,
})
```

复制代码
#### getTodayStatistic


查询当日统计数据


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | [DataType](#datatype) | 是 | 数据类型 |
| statisticType | [StatisticType](#statistictype) | 否 | 统计的维度，不同的 dataType 支持的维度不一样 |
| success | (statistic: [Statistic](#statistic)) => void | 是 | 回调函数，返回值是一个[Statistic](#statistic), 统计类型由 dataType 决定 |
| complete | () => void | 否 | 完成的回调函数 |
| fail | (data: string, code: number) => void | 否 | 失败回调函数 |


**示例**


```

health.getTodayStatistic({
  dataType: health.DATA\_TYPES.HEART\_RATE,
  statisticType: health.STATISTIC\_TYPES.SUM,
  success(data) {
    console.log(data)
  },
  fail(data, code) {
    console.log(data, code)
  },
})
```

复制代码
#### getStatistic


根据时间段，查询统计数据。


**说明：**


1. 仅支持查询当天的数据，数据粒度为小时级；
2. `startTime` 和 `endTime` 向下取整；
3. `startTime` 为空时，默认取当天 0 点；
4. 若 `startTime` 早于当天 0 点，则自动取当天 0 点；
5. 若 `endTime` 晚于当前时间，则自动取当前时间；
6. 若 `startTime` 晚于 `endTime`，则将 `startTime` 设置为 `endTime`；


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | [DataType](#datatype) | 是 | 数据类型 |
| statisticType | [StatisticType](#statistictype) | 否 | 统计的维度，不同的 dataType 支持的维度不一样 |
| startTime | timeStamp | 否 | 开始时间，在这个时间之后发生的活动，包含在这个时间段之前已经发生，但是还没有结束的活动 |
| endTime | timeStamp | 否 | 结束时间，在这个时间之前发生的活动，包含正在发生但还没有完全结束的活动 |
| success | (statistic: [Statistic](#statistic)) => void | 否 | 回调函数，返回值是一个[Statistic](#statistic) , 统计类型由 dataType 决定 |
| complete | () => void | 否 | 完成的回调函数 |
| fail | (data: string, code: number) => void | 否 | 失败回调函数 |


**示例**


```

health.getStatistic({
  dataType: health.DATA\_TYPES.HEART\_RATE,
  statisticType: health.STATISTIC\_TYPES.SUM,
  startTime: new Date().setHours(9, 0, 0, 0), // 9点
  endTime: new Date().setHours(15, 0, 0, 0), // 15点
  success(data) {
    console.log(data)
  },
  fail(data, code) {
    console.log(data, code)
  },
})
```

复制代码
#### subscribeTodayStatistic


监听当日统计数据


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | [DataType](#datatype) | 是 | 每个值都是一个 DataType 的枚举类型 |
| statisticType | [StatisticType](#statistictype) | 否 | 统计的维度，不同厂商，不同的 dataType 支持的维度不一样 |
| callback | (statistic: [Statistic](#statistic)) => void | 是 | 回调函数，返回值是一个 [Statistic](#statistic) , 统计类型由 dataType 决定 |
| fail | (data: string, code: number) => void | 否 | 失败回调函数 |


**示例**


```

health.subscribeTodayStatistic({
  dataType: health.DATA\_TYPES.HEART\_RATE,
  statisticType: health.STATISTIC\_TYPES.SUM,
  callback(data) {
    console.log(data)
  },
  fail(data, code) {
    console.log(data, code)
  },
})
```

复制代码
#### unsubscribeTodayStatistic


取消监听当日统计数据


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | [DataType](#datatype) | 是 | 数据类型 |


**示例**


```

health.unsubscribeTodayStatistic({
  dataType: health.DATA\_TYPES.HEART\_RATE,
})
```

复制代码
#### RecentSample


最近一次采样数据结构


| 属性名 | 值类型 | 说明 |
| --- | --- | --- |
| dataType | [DataType](#datatype) | 数据类型 |
| data | [Sample](#sample) | 采样数据 |


**示例：**


```

{
  "dataType": 0,
  "data": {
    "timeStamp": 1732706966443,
    "value": 80
  }
}
```

复制代码
#### Sample


采样查询接口返回的数据结构


| 属性 | 值类型 | 说明 |
| --- | --- | --- |
| timeStamp | timeStamp | 采样时间 |
| value | Int |Float |[SleepUnit](#sleepunit) |[SleepStage](#sleepstage)[] | 数据类型由查询时的 [DataType](#datatype) 决定 |


**示例：**


```

{
  "timeStamp": 1732705884223,
  "value": 80
}
```

复制代码
#### DataType


健康数据类型


```

const heartRate = health.DATA\_TYPES.HEART\_RATE
```

复制代码


| 类型 | 类型值 | 返回值类型 | 返回单位 | 说明 |
| --- | --- | --- | --- | --- |
| HEART\_RATE | 0 | Int | bpm | 心率 |
| HEART\_RATE\_STEP | 1 | Int | bpm | 步行心率 |
| HEART\_RATE\_RESTING | 2 | Int | bpm | 静息心率 |
| STANDING | 3 | Int | hour | 站立，以时长衡量。1 小时内站立超过 1 分钟即算作站立 1 小时，**仅支持统计数据** |
| INTENSITY\_SPORT | 4 | Int | minutes | 中高强度运动的持续时长，**仅支持统计数据** |
| STEP\_COUNT | 5 | Int | 步 | 步数，**仅支持统计数据**，按时间段查询的最小粒度为小时 |
| SPO2 | 6 | Int | % | 血氧 |
| DISTANCE | 7 | Int | 米 | 距离，由骑行、跑步、步行产生，**仅支持统计数据** |
| CALORIES | 8 | Int | 千卡 | 总卡路里，**仅支持统计数据** |
| STRESS | 9 | Int | | 压力值 |
| WALKING\_SPEED | 10 | Int | 步/min | 步频 |
| SLEEP\_UNIT | 11 | [SleepUnit](#sleepunit) | | 睡眠时段，**暂不支持** |
| SLEEP\_STAGES | 12 | [SleepStage](#sleepstage)[] | | 一个完整睡眠包含的睡眠分期，**暂不支持** |
| SLEEP\_STATUS | 13 | Int | 0:清醒 1:睡眠 | 睡眠状态 |
| ENERGY | 14 | Int | % | 活力值，**暂不支持** |
| WALKING\_STATUS | 15 | Int | 0:非步行 1:步行 | 步行状态 |
| SPEED | 16 | Float | 米/s | 配速，**暂不支持** |


#### SleepUnit


睡眠时段返回值


| 属性 | 单位 | 说明 |
| --- | --- | --- |
| enterSleep | timeStamp | 入睡时间戳 |
| exitSleep | timeStamp | 出睡时间戳 |


**示例：**


```

{
  "enterSleep": 1732705884223,
  "exitSleep": 1732706966443
}
```

复制代码
#### SleepStage


| 属性 | 单位 | 说明 |
| --- | --- | --- |
| enterTimeStamp | timeStamp | 进入该睡眠分期的时间戳 |
| sleepType | Int | 进入的睡眠分期类型 1:深睡 2:浅睡 3:快速眼动 4:清醒 |


**示例：**


```

{
  "enterTimeStamp": 1732705884223,
  "sleepType": 1
}
```

复制代码
#### StatisticType


统计数据类型


```

const sum = health.STATISTIC\_TYPES.SUM
```

复制代码
不同[DataType](#datatype)支持的统计类型如下：


| 类型 | 类型值 | 说明 |
| --- | --- | --- |
| AVERAGE | 0 | 平均值 |
| SUM | 1 | 总和 |
| MAX | 2 | 最大值 |
| MIN | 3 | 最小值 |


各数据类型的统计类型支持情况与统计 API 支持情况：


| 数据类型 | 最大小值 | 总和 | 平均值 | getTodayStatistic | subscribeTodayStatistic | getStatistic |
| --- | --- | --- | --- | --- | --- | --- |
| HEART\_RATE | 支持 | |  | 支持 | 支持 | |
| SPO2 | 支持 | |  | 支持 | 支持 | |
| STRESS | 支持 | |  | 支持 | 支持 | |
| STANDING | | 支持 | | 支持 | | 支持 |
| INTENSITY\_SPORT | | 支持 | | 支持 | | 支持 |
| STEP\_COUNT | | 支持 | | 支持 | | 支持 |
| DISTANCE | | 支持 | | 支持 | | 支持 |
| CALORIES | | 支持 | | 支持 | | 支持 |


#### Statistic


统计数据，获取采样数据的统计值。统计数据的数据结构如下：


| 属性 | 值类型 | 说明 |
| --- | --- | --- |
| value | Int | Float |[SleepUnit](#sleepunit) | [SleepStage](#sleepstage)[] | 数据类型由查询时的 [DataType](#datatype) 决定 |
| statisticType | - | 统计类型。如果数据返回的不是统计类型，则此值是 null |
| startTime | timeStamp | 统计开始时间 |
| endTime | timeStamp | 统计结束时间 |


**示例：**


```

{
  "value": 80,
  "statisticType": 0,
  "startTime": 1732705884223,
  "endTime": 1732706966443
}
```

复制代码


---


<!-- 文档 20: js-api/storage/exchange/.md -->


## 数据共享

## 数据共享

更新时间：2024-10-11 11:55:18


提供了一个不同蓝河应用间数据交互的方式。蓝河应用可以利用它发布数据，或从其他蓝河应用获取数据


数据交互有三个数据空间，分别是应用空间（application）、应用开发商空间（vendor）和全局空间（global）


application：数据发布在应用空间，读取、修改、删除 时需同时指定发布方的包名和签名，并且需要发布方授权


vendor：数据发布在应用开发商空间，同签名的多个应用的写操作会相互覆盖，读取时不能指定发布方的包名和签名，不需要发布方授权


global：数据发布在全局空间，多个应用的写操作会相互覆盖，读取时不能指定发布方的包名和签名，不需要发布方授权


**注意**：


1、set、get 操作支持在 `application`、`vendor` 和`global` 空间上操作数据。 2、exchange 的数据不做持久化处理，系统重启后数据会丢失。


### 接口声明


```

{ "name": "blueos.storage.exchange" }
```

复制代码
### 导入模块


```

import exchange from '@blueos.storage.exchange'
```

复制代码
### 接口定义


#### exchange.get(OBJECT)


读取蓝河应用平台数据，可获取到`应用空间`（application）、`应用开发商空间`（vendor ）或`全局空间`（global）的数据


##### 参数


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| package | String | 否 | 数据发布方的包名，scope 为 `application` 时必须提供，为 `vendor`或 `global` 时必须为空 |
| sign | String | 否 | 数据发布方签名的 SHA-256，scope 为 `application` 时必须提供，为 `vendor` 或 `global` 时必须为空 |
| scope | String | 否 | 数据发布的空间类型，支持 application、vendor 和 global，默认为 application |
| key | String | 是 | 数据的 key |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调（调用成功、失败都会执行） |


##### 返回值:


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| value | String | Boolean | Number | Object | Array | 数据的值，与 set 设置的类型一致 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 1000 | 没有权限 |


##### 示例


```

exchange.get({
  package: 'com.example',
  sign: '7a12ec1d66233f20a20141035b1f7937',
  key: 'token',
  success: function (ret) {
    console.log(`handling success, value = ${ret.value}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### exchange.getSync(Object)


同步读取蓝河应用平台数据，可获取到`应用空间`（application）、`应用开发商空间`（vendor ）或`全局空间`（global）的数据


##### 参数


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| package | String | 否 | 数据发布方的包名，scope 为 `application` 时必须提供，为 `vendor`或 `global` 时必须为空 |
| sign | String | 否 | 数据发布方签名的 SHA-256，scope 为 `application` 时必须提供，为 `vendor` 或 `global` 时必须为空 |
| scope | String | 否 | 数据发布的空间类型，支持 application、vendor 和 global，默认为 application |
| key | String | 是 | 数据的 key |


##### 返回值


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| value | String | Boolean | Number | Object | Array | 数据的值，与 set 设置的类型一致 |


##### 示例


```

const value = exchange.getSync({
  package: 'com.example',
  sign: '7a12ec1d66233f20a20141035b1f7937',
  key: 'token',
})
```

复制代码
#### exchange.set(OBJECT)


发布数据到蓝河应用平台，可发布到`应用空间`（application）、`应用开发商空间` 或`全局空间`（global）


##### 参数


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | String | 是 | 数据的 key |
| value | String | Boolean | Number | Object | Array | 是 | 数据的值 |
| scope | String | 否 | 数据发布的空间类型，支持 application、vendor 和 global，默认为 application |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调（调用成功、失败都会执行） |
| package | String | 否 | 配置需要写入数据到某蓝河应用的`应用空间`时某蓝河应用的`包名`，仅在`scope`参数不设置或设置为`application`时生效，在`scope`为`vendor`或`global`时必须设为空值 |
| sign | String | 否 | 配置需要写入数据到某蓝河应用的`应用空间`时某蓝河应用的`签名`的 SHA-256，仅在`scope`参数不设置或设置为`application`时生效，在`scope`为`vendor`或`global` 时必须设为空值 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |


##### 示例


```

exchange.set({
  key: 'token',
  value: '12347979',
  success: function () {
    console.log(`handling success`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
##### 示例


```

exchange.set({
  key: 'token',
  value: false,
  success: function () {
    console.log(`handling success`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
##### 示例


```

exchange.set({
  key: 'token',
  value: 10,
  success: function () {
    console.log(`handling success`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
##### 示例


```

exchange.set({
  key: 'token',
  value: { name: '张三', age: 18 },
  success: function () {
    console.log(`handling success`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
##### 示例


```

exchange.set({
  key: 'token',
  value: [2, 3, 4],
  success: function () {
    console.log(`handling success`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码


---


<!-- 文档 21: js-api/storage/file/.md -->


## 文件存储

## 文件存储

更新时间：2025-01-15 16:19:38


### 接口声明


```

{ "name": "blueos.storage.file" }
```

复制代码
### 导入模块


```

import file from '@blueos.storage.file'
```

复制代码
**注意：下面文件操作仅支持 URI 的写法，不支持文件绝对路径。**


### 接口定义


#### file.move(OBJECT)


将源文件移动到指定位置


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcUri | String | 是 | 源文件的 uri，不能是应用资源路径和 tmp 类型的 uri |
| dstUri | String | 是 | 目标文件的 uri，不能是应用资源路径和 tmp 类型的 uri |
| success | Function | 否 | 成功回调，返回目标文件的 uri |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |


##### 示例：


```

file.move({
  srcUri: 'internal://cache/path/to/file',
  dstUri: 'internal://files/path/to/file',
  success: function (uri) {
    console.log(`move success: ${uri}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### file.copy(OBJECT)


将源文件复制一份并存储到指定位置，接口中使用的 URI 描述请参考[文件组织](/reference/configuration/file-organization)


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcUri | String | 是 | 源文件的 uri |
| dstUri | String | 是 | 目标文件的 uri，不能是应用资源路径和 tmp 类型的 uri |
| success | Function | 否 | 成功回调，返回目标文件的 uri |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |


##### 示例：


```

file.copy({
  srcUri: 'internal://cache/path/to/file',
  dstUri: 'internal://files/path/to/file',
  success: function (uri) {
    console.log(`copy success: ${uri}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### file.list(OBJECT)


获取指定目录下的文件列表，接口中使用的 URI 描述请参考[文件组织](/reference/configuration/file-organization)


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | String | 是 | 目录 uri，不能是应用资源路径和 tmp 类型的 uri。 支持应用资源路径 |
| success | Function | 否 | 成功回调，返回{fileList:[{uri:'file1', lastModifiedTime:1234456, length:123456} ...]} |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| fileList | Array | 文件列表，每个文件的格式为{uri:'file1', lastModifiedTime:1234456, length:123456} |


###### 每个文件的元信息：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| uri | String | 文件的 uri，该 uri 可以被其他组件或 Feature 访问 |
| length | Number | 文件大小，单位 B |
| lastModifiedTime | Number | 文件的保存是的时间戳，从 1970/01/01 00:00:00 GMT 到当前时间的毫秒数 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |


##### 示例：


```

file.list({
  uri: 'internal://files/movies/',
  success: function (data) {
    console.log(data.fileList)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### file.get(OBJECT)


获取本地文件的文件信息，接口中使用的 URI 描述请参考[文件组织](/reference/configuration/file-organization)


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | String | 是 | 文件的 uri，不能是应用资源路径。 支持应用资源路径 |
| recursive | Boolean | 否 | 是否递归获取子目录文件列表。默认 false |
| success | Function | 否 | 成功回调，返回{uri:'file1', length:123456, lastModifiedTime:1233456} |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| uri | String | 文件的 uri，该 uri 可以被其他组件或 Feature 访问 |
| length | Number | 文件大小，单位 B |
| lastModifiedTime | Number | 文件的保存是的时间戳，从 1970/01/01 08:00:00 到当前时间的毫秒数 |
| type | String | 文件类型，dir：目录；file：文件 |
| subFiles | Array | 文件列表，recursive 为 true 且 type 为 dir 时递归返回子目录文件细信息，否则不返回 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |


##### 示例：


```

file.get({
  uri: 'internal://files/path/to/file',
  success: function (data) {
    console.log(data.uri)
    console.log(data.length)
    console.log(data.lastModifiedTime)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### file.delete(OBJECT)


删除本地存储的文件，接口中使用的 URI 描述请参考[文件组织](/reference/configuration/file-organization)


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | String | 是 | 需要删除的文件 uri，不能是应用资源路径和 tmp 类型的 uri |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |


##### 示例：


```

file.delete({
  uri: 'internal://files/path/to/file',
  success: function (data) {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### file.writeText(OBJECT)


写文本到文件


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | String | 是 | 本地文件路径，不支持资源文件路径和 tmp 分区，如果文件不存在会创建文件 |
| text | String | 是 | 需要写入的字符串 |
| encoding | String | 否 | 编码格式，默认 UTF-8 |
| append | Boolean | 否 | 是否追加模式，默认 false |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |


##### 示例：


```

file.writeText({
  uri: 'internal://files/work/demo.txt',
  text: 'test',
  success: function () {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### file.writeArrayBuffer(OBJECT)


写 Buffer 到文件


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | String | 是 | 本地文件路径，不支持资源文件路径和 tmp 分区，如果文件不存在会创建文件 |
| buffer | Uint8Array | 是 | 需要写入的 Buffer |
| position | Number | 否 | 指向文件开始写入数据的位置的偏移量，默认 0 |
| append | Boolean | 否 | 是否追加模式，默认 false。当为 true 时，position 参数无效 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |


##### 示例：


```

file.writeArrayBuffer({
  uri: 'internal://files/work/demo',
  buffer: buffer,
  success: function () {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### file.readText(OBJECT)


从文件中读取文本


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | String | 是 | 本地文件路径 |
| encoding | String | 否 | 编码格式，默认 UTF-8 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| text | String | 读取的文本 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |
| 301 | 文件不存在 |


##### 示例：


```

file.readText({
  uri: 'internal://files/work/demo.txt',
  success: function (data) {
    console.log('text: ' + data.text)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### file.readArrayBuffer(OBJECT)


从文件中读取 Buffer


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | String | 是 | 本地文件路径 |
| position | Number | 否 | 读取的起始位置，默认值为文件的起始位置 |
| length | Number | 否 | 读取的长度，不填写则读取到文件结尾 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| buffer | Uint8Array | 读取的文件内容 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |
| 301 | 文件不存在 |


##### 示例：


```

file.readArrayBuffer({
  uri: 'internal://files/work/demo',
  position: 100,
  length: 100,
  success: function (data) {
    console.log('buffer.byteLength: ' + data.buffer.byteLength)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### file.access(OBJECT)


判断文件或目录是否存在


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | String | 是 | 目录或文件 uri，不能是应用资源路径和 tmp 类型的 uri。 支持应用资源路径 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |


##### 示例：


```

file.access({
  uri: 'internal://files/test',
  success: function (data) {
    console.log(`handling success`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### file.mkdir(OBJECT)


创建目录


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | String | 是 | 目录的 uri，不能是应用资源路径和 tmp 类型的 uri |
| recursive | Boolean | 否 | 是否递归创建该目录的上级目录后再创建该目录。默认 false |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |


##### 示例：


```

file.mkdir({
  uri: 'internal://files/dir/',
  success: function (data) {
    console.log(`handling success`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### file.rmdir(OBJECT)


删除目录


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | String | 是 | 目录的 uri，不能是应用资源路径和 tmp 类型的 uri |
| recursive | Boolean | 否 | 是否递归删除子文件和子目录。默认 false |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |


##### 示例：


```

file.rmdir({
  uri: 'internal://files/dir/',
  success: function (data) {
    console.log(`handling success`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
##### 通用 fail 回调参数定义


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | string | 接口失败信息描述 |
| code | FailCodeEnum | 接口失败业务码 |


##### FailCodeEnum


| 属性 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |
| 301 | 文件不存在 |
| 302 | 存储空间不足 |


---


<!-- 文档 22: js-api/storage/overview/.md -->


## 概述

## 概述

更新时间：2025-08-13 20:11:57


蓝河应用的数据存储能力模块使应用能够更好地管理和存储数据，提供了广泛的工具和功能，从简单的键值存储到文件操作，以及跨应用数据共享，提供了多样化数据管理和共享能力。


### 子模块介绍


| 模块 | 简述 |
| --- | --- |
| 存储空间统计 | 提供获取可用空间与总空间的能力，支持同步与异步。 |
| K-V 数据存储 | 提供读取、修改、设置、删除、清空存储内容等数据存储能力 |
| 文件存储 | 提供对应用沙箱目录下的文件的一些操作能力 |
| 数据共享 | 提供三个维度的不同蓝河应用间数据共享能力 |


---


<!-- 文档 23: js-api/system/am/.md -->


## 应用管理

## 应用管理

更新时间：2024-03-14 09:45:42


### 接口声明


#### JS 接口声明


```

{ "name": "blueos.app.appmanager.appState" }
```

复制代码
#### 导入模块


```

import am from '@blueos.app.appmanager.appState'
```

复制代码
### 在工程里面的 manifest 文件中配置如下内容


#### 申请权限


```

{
  "permissions": [{ "name": "watch.permission.AM" }]
}
```

复制代码
#### 应用状态


蓝河应用的状态有三种，应用处于前台，后台以及应用未运行。对应的三种状态值枚举如下：


| 状态值 | 说明 |
| --- | --- |
| foreground | 应用处于前台 |
| background | 应用处于后台 |
| noRunning | 应用未运行 |


### JS 接口定义


#### am.moveTaskToBack()


将当前栈顶应用移动到后台


##### 参数


无


##### 返回值


如果当前任务成功移动到后台，则返回值为 `true`，否则返回值为 `false`。


示例


```

am.moveTaskToBack()
```

复制代码


---


<!-- 文档 24: js-api/system/app/.md -->


## 概述

## 概述

更新时间：2023-10-31 18:07:58


蓝河应用的应用框架为开发者提供了广泛的能力，以构建、管理蓝河应用的各个方面。通过这些能力，开发者可以更好地控制和定制蓝河应用的行为、用户体验以及数据操作。


### 子模块介绍


| 模块 | 简介 |
| --- | --- |
| 应用上下文 | 提供了管理和控制应用的重要功能，可帮助开发者获得更多应用信息、整合外部资源，以及有效退出应用 |
| 页面路由 | 提供应用能够有效管理和导航不同页面的能力，以确保应用的流畅导航和用户体验 |
| 应用管理 | 该模块负责跟踪和管理应用的状态，包括前台运行、后台运行以及应用未运行的情况，以实现灵活的应用控制 |
| 生命周期 | 提供了页面、自定义组件、应用的生命周期接口，开发者可以选择在应用运行的特定阶段执行相应的业务代码 |
| 包管理 | 该模块允许检测应用是否存在，安装应用，获取应用版本信息、签名摘要信息以及应用分类，为应用操作和信息检索提供全面的支持 |
| 页面栈管理 | 管理页面栈信息 |
| 应用沙箱目录 | 蓝河应用框架给每个应用分配了一个专属的应用目录，蓝河应用的数据访问和操作都被限制在该目录内，此目录下存放的数据可以保护数据的安全性 |
| 通知能力 | 提供多应用间数据传递和事件交互的能力，应用发布通知能力以及弹窗能力 |
| 后台管理 | 提供定时触发事件或执行特定操作的功能，允许应用在预定的时间或间隔内执行后台任务 |


---


<!-- 文档 25: js-api/system/audio/.md -->


## 音频

## 音频

更新时间：2025-07-10 11:01:16


### 接口声明


```

{ "name": "blueos.media.audio.audioPlayer" }
```

复制代码
### 导入模块


```

import audio from '@blueos.media.audio.audioPlayer' 或 const audio = require('@blueos.media.audio.audioPlayer')
```

复制代码
### 接口定义


#### audio.play()


开始播放音频


##### 参数


无


##### 示例：


```

audio.play()
```

复制代码
#### audio.pause()


暂停播放音频


##### 参数


无


##### 示例


```

audio.pause()
```

复制代码
#### audio.stop()


停止音频播放，可以通过 play 重新播放音频


##### 参数


无


##### 示例：


```

audio.stop()
```

复制代码
#### audio.getPlayState(OBJECT)


获取当前播放状态数据


##### 参数


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


##### success 返回值：


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| state | String | 播放状态,分别为'play','pause','stop','idle' |
| src | String | 播放的音频媒体 uri |
| currentTime | Number | 当前音频的当前进度，单位秒,停止时返回-1 |


##### 示例：


```

audio.getPlayState({
  success: function (data) {
    console.log(`
 handling success: state: ${data.state},
 src:${data.src}
 `)
  },
  fail: function (data, code) {
    console.log('handling fail, code=' + code)
  },
})
```

复制代码
#### 属性


| 名称 | 参数类型 | 是否可读 | 是否可写 | 必填 | 描述 |
| --- | --- | --- | --- | --- | --- |
| src | String | 是 | 是 | 是 | 播放的音频媒体 uri |
| currentTime | Number | 是 | 是 | 否 | 音频的当前进度，单位秒，对值设置可以调整播放进度 |
| duration | Number | 是 | 否 | 否 | 音频文件的总时长，单位秒，未知返回 NaN |
| streamType | String | 是 | 是 | 否 | [streamType](#streamType) 指定使用音频类型，默认为 music。 |


##### streamType 参数


| 名称 | 说明 | 取值 |
| --- | --- | --- |
| MEDIA | 媒体 | music |
| VOICE\_CALL | 通话 | voicecall |


##### 示例：


```

let streamType = audio.streamType
audio.streamType = 'voicecall'
```

复制代码
#### 事件


| 名称 | 描述 | 返回值 |
| --- | --- | --- |
| Play | 在调用 play 方法后的回调事件 | |
| Pause | 在调用 pause 方法后的回调事件 | |
| Stop | 在调用 stop 方法后的回调事件 | |
| Ended | 播放结束时的回调事件 | |
| Error | 播放发生错误时的回调事件 | |
| TimeUpdate | 在 `currentTime` 属性更新时会触发的回调事件 | |
| DurationChange | 在 `duration` 属性更新时被触发的回调事件 | |
| LoadedData | 第一次获取到音频数据的回调事件 | |


##### 示例：


```

audio.onError = function (error) {
  console.info(`audio error called, error: ${error}`)
}
```

复制代码


---


<!-- 文档 26: js-api/system/audiomanager/.md -->


## 音频管理

## 音频管理

更新时间：2025-07-10 11:01:16


### 接口声明


```

{ "name": "blueos.media.audio.audioManager" }
```

复制代码
### 导入模块


```

import audioManager from '@blueos.media.audio.audioManager'
```

复制代码
### 接口定义


#### setVolume(OBJECT)


设置音量


**参数**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](#audiovolumetype) | 是 | 音量流类型 |
| volume | number | 是 | 音量等级, 设置的音量，0.00-1.00 之间。 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


**返回值：**


无


**示例：**


```

audioManager.setVolume({
  volumeType: 'music',
  volume: 0.5,
  success() {
    console.log("设置音量成功")
  }
})
```

复制代码
#### getVolume(OBJECT)


获取音量


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](#audiovolumetype) | 是 | 音量流类型 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


**返回值：**


| 类型 | 必填 | 说明 |
| --- | --- | --- |
| number | 是 | 音量等级, 设置的音量，0.00-1.00 之间。 |


**示例**


```

audioManager.getVolume({
  volumeType: 'music',
  success(volume) {
    console.log(`音量等级为：${volume}`)
  }
})
```

复制代码
#### getVolumeSync(OBJECT)


同步获取音量


**参数**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](#audiovolumetype) | 是 | 音量流类型 |


**返回值**


| 类型 | 说明 |
| --- | --- |
| number | 音量等级, 设置的音量，0.00-1.00 之间。 |


**示例**


```

const value = audioManager.getVolumeSync({
  volumeType: 'music',
})
console.log(`音量等级为：${value}`)
```

复制代码
#### getMinVolume(OBJECT)


获取指定流的最小音量


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](#audiovolumetype) | 是 | 音量流类型 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


**success 返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 最小音量 |


**示例：**


```

audioManager.getMinVolume({
  volumeType: 'music',
  success(volume) {
    console.log(`最小音量为：${volume}`)
  },
})
```

复制代码
#### getMaxVolume(OBJECT)


获取指定流的最大音量


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](#audiovolumetype) | 是 | 音量流类型 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


**success 返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 最大音量 |


**示例：**


```

audioManager.getMaxVolume({
  volumeType: 'music',
  success(volume) {
    console.log(`最大音量为：${volume}`)
  },
})
```

复制代码
#### mute(OBJECT)


设置指定音量流静音或取消静音


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](#audiovolumetype) | 是 | 音量流类型 |
| isMute | number | 是 | 是否将音量流静音（1:设置静音 ；0:设置取消静音） |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


**返回值：**


无


**示例：**


```

audioManager.mute({
  volumeType: 'music',
  isMute: 1,
  success() {
    console.log(`静音成功`)
  }
})
```

复制代码
#### isMute(OBJECT)


获取指定音量流是否被静音


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](#audiovolumetype) | 是 | 音量流类型 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 是否将音量流静音（1:设置静音 ；0:设置取消静音)。 |


**示例**


```

audioManager.isMute({
  volumeType: 'music',
  success(isMute) {
    console.log(isMute)
  }
})
```

复制代码
#### subscribe(OBJECT)


监听音量变化


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | `volume`：表示音量 |
| callback | Function | 是 | 监听音量变化数据回调函数的执行 |
| fail | Function | 否 | 失败回调 |


**callback 返回值：**


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| volumeType | [AudioVolumeType](#audiovolumetype) | 音量流类型 |
| value | number | 音量等级, 设置的音量，0.00-1.00 之间 |


**示例：**


```

audioManager.subscribe({
  type: 'volume',
  callback(data) {
    console.log(`value = ${data.value} volumeType = ${data.volumeType}`)
  }
})
```

复制代码
#### unsubscribe(OBJECT)


取消监听音量变化


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | `volume`：表示音量 |


**示例：**


```

audioManager.unsubscribe({
  type: 'volume',
})
```

复制代码
#### isMicrophoneMute(OBJECT)


获取麦克风是否为静音状态


**参数**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


**返回值**


| 类型 | 必填 | 说明 |
| --- | --- | --- |
| number | 是 | 是否将音量流静音（1:设置静音 ；0:设置取消静音)。 |


**示例**


```

audioManager.isMicrophoneMute({
  success(isMicrophoneMute) {
    console.log(isMicrophoneMute)
  }
})
```

复制代码
#### AudioVolumeType


枚举，音量流的类型


| 名称 | 说明 | 取值 |
| --- | --- | --- |
| RING | 铃声 | ring |
| MEDIA | 媒体声音 | music |


#### AudioFocusAcquireType


音频焦点变更类型枚举


| **名称** | **说明** | **取值** |
| --- | --- | --- |
| GAIN | 获得音频焦点 | gain |
| LOSS | 失去音频焦点 | loss |
| TRANSIENT | 短暂失去音频焦点，(预留，暂不支持) | transient |
| DUCK | 降音量，未失去音频焦点 ，(预留，暂不支持) | duck |


---


<!-- 文档 27: js-api/system/battery/.md -->


## 电量信息

## 电量信息

更新时间：2024-08-13 15:19:43


### 接口声明


```

{ "name": "blueos.hardware.battery" }
```

复制代码
### 导入模块


```

import battery from '@blueos.hardware.battery' 或 const battery = require('@blueos.hardware.battery')
```

复制代码
### 接口定义


#### battery.getStatus(OBJECT)


获取当前设备的电量信息。


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| charging | Boolean | 是否正在充电 |
| level | Number | 当前电量，0.0 - 1.0 之间 |


##### 示例：


```

battery.getStatus({
  success: function (data) {
    console.log(`handling success: ${data.level}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### battery.getStatusSync()


同步获取当前设备的电量信息。


##### 参数


无


##### 返回值


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| batteryStatus | Object | 当前电量信息 |


##### batteryStatus 参数描述


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| charging | Boolean | 是否正在充电 |
| level | Number | 当前电量，0.0 - 1.0 之间 |


##### 示例


```

const batteryStatus = battery.getStatusSync()
```

复制代码


---


<!-- 文档 28: js-api/system/bluetooth/.md -->


## 蓝牙

## 蓝牙

更新时间：2025-10-09 11:25:10


### 一、蓝牙整体介绍


#### 传统蓝牙


传统蓝牙本机管理：打开和关闭蓝牙、设置和获取本机蓝牙名称、扫描和取消扫描周边蓝牙设备、获取本机蓝牙 profile 对其他设备的连接状态、获取本机蓝牙已配对的蓝牙设备列表。


传统蓝牙远端设备操作：查询远端蓝牙设备名称和 MAC 地址、设备类型和配对状态，以及向远端蓝牙设备发起配对。


#### 低功率蓝牙 BLE


BLE 设备交互时会分为不同的角色：


中心设备和外围设备：中心设备负责扫描外围设备、发现广播。外围设备负责发送广播。


GATT（Generic Attribute Profile，通用属性配置文件）服务端与 GATT 客户端：两台设备建立连接后，其中一台作为 GATT 服务端，另一台作为 GATT 客户端。


### 二、低功耗蓝牙 BLE


#### 概述


BLE 扫描和广播：根据指定状态获取外围设备、启动或停止 BLE 扫描、广播。


BLE 中心设备与外围设备进行数据交互：BLE 外围设备和中心设备建立 GATT 连接后，中心设备可以查询外围设备支持的各种数据，向外围设备发起数据请求，并向其写入特征值数据。


BLE 外围设备数据管理：BLE 外围设备作为服务端，可以接收来自中心设备（客户端）的 GATT 连接请求，应答来自中心设备的特征值内容读取和写入请求，并向中心设备提供数据。同时外围设备还可以主动向中心设备发送数据。


#### ① 应用场景


通过 BLE 扫描和广播提供的开放能力，可以根据指定状态获取外围设备、启动或停止 BLE 扫描、广播。


#### ② 模块导入


接口声明


```

{ "name": "blueos.bluetooth.ble" }
```

复制代码
接口导入


```

import bluetooth from '@blueos.bluetooth.ble'
```

复制代码
权限要求


```

{
  "permissions": [{ "name": "blueos.permission.BLUETOOTH" }]
}
```

复制代码
#### ③ API 说明


**低功率蓝牙 BLE 管理类 bluetooth.BLE 的主要接口，本文档仅实现 createGattServer。**


| 接口名 | 功能描述 |
| --- | --- |
| createGattClientDevice | 创建一个可使用的 GattClientDevice 实例。 |
| createGattServer | 创建一个可使用的 GattServer 实例。 |
| getConnectedBLEDevices | 获取和当前设备连接的 BLE 设备。 |
| getLeMaximumAdvertisingDataLength | 广播的最大数据长度。 |
| startBLEScan | 发起 BLE 扫描流程。 |
| stopBLEScan | 停止 BLE 扫描流程。 |
| subscribeBLEDeviceFind | 订阅 BLE 设备发现上报事件。 |
| unsubscribeBLEDeviceFind | 取消订阅 BLE 设备发现上报事件。 |


#### bluetooth.BLE.createGattServer()


创建一个可使用的 GattServer 实例。


##### 参数


无


##### 返回值


| 类型 | 说明 |
| --- | --- |
| [GattServer](#gattserver) | server 端类，使用 server 端方法之前需要创建该类的实例进行操作。 |


##### GattServer


server 端类，使用 server 端方法之前需要创建该类的实例进行操作，通过 createGattServer()方法构造此实例。


##### 示例


```

const gattServer = bluetooth.BLE.createGattServer()
```

复制代码
**BLE 外围设备管理类 GattServer(外围设备)server 端类，使用 server 端方法之前需要创建该类的实例进行操作，通过 createGattServer()方法构造此实例。(let gattServer = bluetooth.BLE.createGattServer()) 的主要接口：**


| 接口名 | 功能描述 |
| --- | --- |
| startAdvertising | 开始发送 BLE 广播。 |
| stopAdvertising | 停止发送 BLE 广播。 |
| addService | server 端添加服务。 |
| removeService | 删除已添加的服务。 |
| close | 关闭服务端功能，去注册 server 在协议栈的注册，调用该接口后[GattServer](#gattserver)实例将不能再使用。 |
| notifyCharacteristicChanged | server 端特征值发生变化时，主动通知已连接的 client 设备。 |
| sendResponse | server 端回复 client 端的读写请求。 |
| subscribeCharacteristicRead | server 端订阅特征值读请求事件。 |
| unsubscribeCharacteristicRead | server 端取消订阅特征值读请求事件。 |
| subscribeCharacteristicWrite | server 端订阅特征值写请求事件。 |
| unsubscribeCharacteristicWrite | server 端取消订阅特征值读请求事件。 |
| subscribeDescriptorRead | server 端订阅描述符读请求事件。 |
| unsubscribeDescriptorRead | server 端取消订阅描述符读请求事件。 |
| subscribeDescriptorWrite | server 端订阅描述符写请求事件。 |
| unsubscribeDescriptorWrite | server 端取消订阅描述符写请求事件。 |
| subscribeConnectStateChange | server 端订阅 BLE 连接状态变化事件。 |
| unsubscribeConnectStateChange | server 端取消订阅 BLE 连接状态变化事件。 |


**BLE 外围设备管理类 GattServer(外围设备)server 端类接口详细描述：**


#### gattServer.startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData)


开始发送 BLE 广播。


##### 参数


| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| setting | [AdvertiseSetting](#advertisesetting) | 是 | BLE 广播的相关参数。 |
| advData | [AdvertiseData](#advertisedata) | 是 | BLE 广播包内容。 |
| advResponse | [AdvertiseData](#advertisedata) | 否 | BLE 回复扫描请求回复响应。 |


##### AdvertiseSetting


描述蓝牙低功耗设备发送广播的参数。


| 参数名 | 类型 | 是否必填 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| interval | number | 否 | 1600 | 表示广播间隔，最小值设置 32 个 slot 表示 20ms，最大值设置 16384 个 slot，默认值设置为 1600 个 slot 表示 1s。 |
| txPower | number | 否 | -7 | 表示发送功率，最小值设置-127，最大值设置 1，默认值设置-7，单位 dbm。 |
| connectable | boolean | 否 | true | 表示是否是可连接广播，默认值设置为 true。 |


##### AdvertiseData


描述 BLE 广播数据包的内容。


| 参数名 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| serviceUuids | Array<string> | 否 | 表示要广播的服务 UUID 列表。 |
| manufactureData | Array<[ManufactureData](#manufacturedata)> | 否 | 表示要广播的广播的制造商信息列表。 |
| serviceData | Array<[ServiceData](#servicedata)> | 否 | 表示要广播的服务数据列表。 |


> 
> serviceUuids 和 serviceData 至少填写一个。
> 
> 
> 


##### ManufactureData


描述 BLE 广播数据包的内容。


| 参数名 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| manufactureId | string | number | 是 | 表示制造商的 ID，由蓝牙 SIG 分配。 |
| manufactureValue | ArrayBuffer | 是 | 表示制造商发送的制造商数据。 |


##### ServiceData


描述广播包中服务数据内容。


| 参数名 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| serviceUuid | string | 是 | 表示服务的 UUID。 |
| serviceValue | ArrayBuffer | 是 | 表示服务数据。 |


##### 示例


```

let manufactureValueBuffer = new Uint8Array(4)
manufactureValueBuffer[0] = 1
manufactureValueBuffer[1] = 2
manufactureValueBuffer[2] = 3
manufactureValueBuffer[3] = 4

let serviceValueBuffer = new Uint8Array(4)
serviceValueBuffer[0] = 4
serviceValueBuffer[1] = 6
serviceValueBuffer[2] = 7
serviceValueBuffer[3] = 8
console.info('manufactureValueBuffer = ' + JSON.stringify(manufactureValueBuffer))
console.info('serviceValueBuffer = ' + JSON.stringify(serviceValueBuffer))
let gattServer = bluetooth.BLE.createGattServer()
gattServer.startAdvertising(
  {
    interval: 150,
    txPower: 60,
    connectable: true,
  },
  {
    serviceUuids: ['00001888-0000-1000-8000-00805f9b34fb'],
    manufactureData: [
      {
        manufactureId: 4567,
        manufactureValue: manufactureValueBuffer.buffer,
      },
    ],
    serviceData: [
      {
        serviceUuid: '00001888-0000-1000-8000-00805f9b34fb',
        serviceValue: serviceValueBuffer.buffer,
      },
    ],
  },
  {
    serviceUuids: ['00001889-0000-1000-8000-00805f9b34fb'],
    manufactureData: [
      {
        manufactureId: 1789,
        manufactureValue: manufactureValueBuffer.buffer,
      },
    ],
    serviceData: [
      {
        serviceUuid: '00001889-0000-1000-8000-00805f9b34fb',
        serviceValue: serviceValueBuffer.buffer,
      },
    ],
  }
)
```

复制代码
#### gattServer.stopAdvertising()


停止发送 BLE 广播。


##### 无参数


##### 无返回结果


##### 示例


```

const gattServer = bluetooth.BLE.createGattServer()
gattServer.stopAdvertising()
```

复制代码
#### gattServer.addService(service: GattService)


server 端添加服务。


##### 参数


| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| service | [GattService](#gattservice) | 是 | 服务端的 service 数据。BLE 广播的相关参数 |


##### 返回值：


| 类型 | 说明 |
| --- | --- |
| boolean | 添加服务操作，成功返回 true，否则返回 false。 |


##### GattService


描述 service 的接口参数定义。


| 参数名 | 类型 | 可读 | 可写 | 描述 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 是 | 是 | 特定服务（service）的 UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| isPrimary | boolean | 是 | 是 | 如果是主服务设置为 true，否则设置为 false。 |
| characteristics | Array<[BLECharacteristic](#blecharacteristic)> | 是 | 是 | 当前服务包含的特征列表。 |
| includeServices | Array<[GattService](#gattservice)> | 是 | 是 | 当前服务依赖的其它服务。 |


##### BLECharacteristic


描述 characteristic 的接口参数定义 。


| 参数名 | 类型 | 可读 | 可写 | 描述 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 是 | 是 | 特定服务（service）的 UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 是 | 是 | 特定特征（characteristic）的 UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| characteristicValue | ArrayBuffer | 是 | 是 | 特征对应的二进制值。 |
| descriptors | Array<[BLEDescriptor](#bledescriptor)> | 是 | 是 | 特定特征的描述符列表。 |
| properties | Array<[CharacteristicProperties](#characteristicproperties)> | 是 | 是 | 特定特征的属性。 |


##### BLEDescriptor


描述 descriptor 的接口参数定义 。


| 参数名 | 类型 | 可读 | 可写 | 描述 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 是 | 是 | 特定服务（service）的 UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 是 | 是 | 特定特征（characteristic）的 UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| descriptorUuid | string | 是 | 是 | 描述符（descriptor）的 UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| descriptorValue | ArrayBuffer | 是 | 是 | 描述符对应的二进制值。 |


##### CharacteristicProperties


| 名称 | 取值 | 描述 |
| --- | --- | --- |
| PROPERTY\_BROADCAST | 0 | 表示 characteristic 是可广播的。 |
| PROPERTY\_EXTENDED\_PROPS | 1 | 表示 characteristic 有扩展的属性 descriptor。 |
| PROPERTY\_INDICATE | 2 | 表示 characteristic 支持 indicate 操作。 |
| PROPERTY\_NOTIFY | 3 | 表示 characteristic 支持 notification 操作。 |
| PROPERTY\_READ | 4 | 表示 characteristic 是可读的。 |
| PROPERTY\_WRITE | 5 | 表示 characteristic 是可写的。 |
| PROPERTY\_SIGNED\_WRITE | 6 | 表示 characteristic 支持带签名写入 |
| PROPERTY\_WRITE\_NO\_RESPONSE | 7 | 表示 characteristic 支持没有回复的写入 |


##### 示例


```

// 创建descriptors
let descriptors = []
let arrayBuffer = new ArrayBuffer(8)
let descV = new Uint8Array(arrayBuffer)
descV[0] = 11
let descriptor = {
  serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB',
  descriptorValue: arrayBuffer,
}
descriptors[0] = descriptor

// 创建characteristics
let characteristics = []
let arrayBufferC = new ArrayBuffer(8)
let cccV = new Uint8Array(arrayBufferC)
cccV[0] = 1
let characteristic = {
  serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  characteristicValue: arrayBufferC,
  descriptors: descriptors,
  properties: [1, 4, 6],
}

characteristics[0] = characteristic

// 创建gattService
let gattService = {
  serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  isPrimary: true,
  characteristics: characteristics,
  includeServices: [],
}

let gattServer = bluetooth.BLE.createGattServer()
let ret = gattServer.addService(gattService)
if (ret) {
  console.log('add service successfully')
} else {
  console.log('add service failed')
}
```

复制代码
#### gattServer.removeService(serviceUuid: string)


删除已添加的服务。


##### 参数


| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| serviceUuid | string | 是 | service 的 UUID，例如“00001810-0000-1000-8000-00805F9B34FB”。 |


##### 返回值：


| 类型 | 说明 |
| --- | --- |
| boolean | 删除服务操作，成功返回 true，否则返回 false。 |


##### 示例


```

const gattServer = bluetooth.BLE.createGattServer()
gattServer.removeService('00001810-0000-1000-8000-00805F9B34FB')
```

复制代码
#### gattServer.close()


关闭服务端功能，去注册 server 在协议栈的注册，调用该接口后[GattServer](#gattserver)实例将不能再使用。


```

let gattServer = bluetooth.BLE.createGattServer()
gattServer.close()
```

复制代码
#### gattServer.notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic)


server 端特征值发生变化时，主动通知已连接的 client 设备。


##### 参数


| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| deviceId | string | 是 | service 的 UUID，例如“00001810-0000-1000-8000-00805F9B34FB”。 |
| notifyCharacteristic | [NotifyCharacteristic](#notifycharacteristic) | 是 | 通知的特征值数据。 |


##### 返回值：


| 类型 | 说明 |
| --- | --- |
| boolean | 通知操作，成功返回 true，否则返回 false。 |


##### 示例


```

// 创建descriptors
let descriptors = []
let arrayBuffer = new ArrayBuffer(8)
let descV = new Uint8Array(arrayBuffer)
descV[0] = 11
let descriptor = {
  serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB',
  descriptorValue: arrayBuffer,
}
descriptors[0] = descriptor

let arrayBufferC = new ArrayBuffer(8)
let characteristic = {
  serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  characteristicValue: arrayBufferC,
  descriptors: descriptors,
}
let notifyCharacteristic = {
  serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB',
  characteristicValue: characteristic.characteristicValue,
  confirm: false,
}
let gattServer = bluetooth.BLE.createGattServer()
gattServer.notifyCharacteristicChanged('XX:XX:XX:XX:XX:XX', notifyCharacteristic)
```

复制代码
##### NotifyCharacteristic


描述 server 端特征值发生变化时，server端发送特征值通知的参数结构。


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serviceUuid | string | 是 | 特征值所属的服务UUID。例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 是 | 内容发生变化的特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| characteristicValue | ArrayBuffer | 是 | 特征值对应的数据内容。 |
| confirm | boolean | 是 | true表示发送的是指示，需要client端回复确认。false表示发送的是通知，不需要client端回复确认。 |


#### gattServer.sendResponse(serverResponse: ServerResponse)


server 端回复 client 端的读写请求。


##### 参数


| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| serverResponse | [ServerResponse](#serverresponse) | 是 | service 的 UUID，例如“00001810-0000-1000-8000-00805F9B34FB”。 |


##### 返回值：


| 类型 | 说明 |
| --- | --- |
| boolean | 回复响应操作，成功返回 true，否则返回 false。 |


##### ServerResponse


描述 server 端回复 client 端读/写请求的响应参数结构。


| 参数名 | 类型 | 可读 | 可写 | 描述 |
| --- | --- | --- | --- | --- |
| deviceId | string | 是 | 否 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 是 | 否 | 表示请求的传输 ID，与订阅的读/写请求事件携带的 ID 保持一致。 |
| status | number | 是 | 否 | 表示响应的状态，设置为 0 即可，表示正常。 |
| offset | number | 是 | 否 | 表示请求的读/写起始位置，与订阅的读/写请求事件携带的 offset 保持一致。 |
| value | ArrayBuffer | 是 | 否 | 表示回复响应的二进制数据。 |


##### 示例


```

/\* send response \*/
let arrayBufferCCC = new ArrayBuffer(8)
let cccValue = new Uint8Array(arrayBufferCCC)
cccValue[0] = 1123
let serverResponse = {
  deviceId: 'XX:XX:XX:XX:XX:XX',
  transId: 0,
  status: 0,
  offset: 0,
  value: arrayBufferCCC,
}

let gattServer = bluetooth.BLE.createGattServer()
let ret = gattServer.sendResponse(serverResponse)
if (ret) {
  console.log('bluetooth sendResponse successfully')
} else {
  console.log('bluetooth sendResponse failed')
}
```

复制代码
#### gattServer.subscribeCharacteristicRead(OBJECT)


server 端订阅特征值读请求事件。


##### OBJECT 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 回调此函数 |
| fail | Function | 否 | 失败回调。 |


##### callback 返回值:


| 类型 | 说明 |
| --- | --- |
| [CharacteristicReadReq](#characteristicreadreq) | 描述 server 端订阅后收到的特征值读请求事件参数结构。 |


##### CharacteristicReadReq


描述 server 端订阅后收到的特征值读请求事件参数结构。


| 参数名 | 类型 | 可读 | 可写 | 描述 |
| --- | --- | --- | --- | --- |
| deviceId | string | 是 | 否 | 表示发送特征值读请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 是 | 否 | 表示读请求的传输 ID，server 端回复响应时需填写相同的传输 ID。 |
| offset | number | 是 | 否 | 表示读特征值数据的起始位置。例如：k 表示从第 k 个字节开始读，server 端回复响应时需填写相同的 offset。 |
| characteristicUuid | string | 是 | 否 | 特定特征（characteristic）的 UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 是 | 否 | 特定服务（service）的 UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |


##### 示例


```

let gattServer = bluetooth.BLE.createGattServer()

let arrayBufferCCC = new ArrayBuffer(8)
let cccValue = new Uint8Array(arrayBufferCCC)
cccValue[0] = 1123
function ReadCharacteristicReq(CharacteristicReadReq) {
  let deviceId = CharacteristicReadReq.deviceId
  let transId = CharacteristicReadReq.transId
  let offset = CharacteristicReadReq.offset
  let characteristicUuid = CharacteristicReadReq.characteristicUuid

  let serverResponse = {
    deviceId: deviceId,
    transId: transId,
    status: 0,
    offset: offset,
    value: arrayBufferCCC,
  }

  let ret = gattServer.sendResponse(serverResponse)
  if (ret) {
    console.log('bluetooth sendResponse successfully')
  } else {
    console.log('bluetooth sendResponse failed')
  }
}

gattServer.subscribeCharacteristicRead({
  callback: function (data) {
    ReadCharacteristicReq(data)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### gattServer.unsubscribeCharacteristicRead()


server 端取消订阅特征值读请求事件。


##### 无参数


##### 无返回值


##### 示例


```

const gattServer = bluetooth.BLE.createGattServer()
gattServer.unsubscribeCharacteristicRead()
```

复制代码
#### gattServer.subscribeCharacteristicWrite(OBJECT)


server 端订阅特征值写请求事件。


##### OBJECT 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 回调此函数 |
| fail | Function | 否 | 失败回调。 |


##### callback 返回值:


| 类型 | 说明 |
| --- | --- |
| [DescriptorWriteReq](#descriptorwritereq) | 描述 server 端订阅后收到的描述符写请求事件参数结构。 |


##### DescriptorWriteReq


描述 server 端订阅后收到的描述符写请求事件参数结构。


| 参数名 | 类型 | 可读 | 可写 | 描述 |
| --- | --- | --- | --- | --- |
| deviceId | string | 是 | 否 | 表示发送描述符写请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 是 | 否 | 表示写请求的传输 ID，server 端回复响应时需填写相同的传输 ID。 |
| offset | number | 是 | 否 | 表示写描述符数据的起始位置。例如：k 表示从第 k 个字节开始写，server 端回复响应时需填写相同的 offset。 |
| isPrep | boolean | 是 | 否 | 表示写请求是否立即执行。 |
| needRsp | boolean | 是 | 否 | 表示是否要给 client 端回复响应。 |
| value | ArrayBuffer | 是 | 否 | 表示写入的描述符二进制数据。 |
| descriptorUuid | string | 是 | 否 | 表示描述符（descriptor）的 UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 是 | 否 | 特定特征（characteristic）的 UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 是 | 否 | 特定服务（service）的 UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |


##### 示例


```

let gattServer = bluetooth.BLE.createGattServer()

let arrayBufferCCC = new ArrayBuffer(8)
let cccValue = new Uint8Array(arrayBufferCCC)
function WriteCharacteristicReq(CharacteristicWriteReq) {
  let deviceId = CharacteristicWriteReq.deviceId
  let transId = CharacteristicWriteReq.transId
  let offset = CharacteristicWriteReq.offset
  let isPrep = CharacteristicWriteReq.isPrep
  let needRsp = CharacteristicWriteReq.needRsp
  let value = new Uint8Array(CharacteristicWriteReq.value)
  let characteristicUuid = CharacteristicWriteReq.characteristicUuid

  cccValue[0] = value[0]
  let serverResponse = {
    deviceId: deviceId,
    transId: transId,
    status: 0,
    offset: offset,
    value: arrayBufferCCC,
  }

  let ret = gattServer.sendResponse(serverResponse)
  if (ret) {
    console.log('bluetooth sendResponse successfully')
  } else {
    console.log('bluetooth sendResponse failed')
  }
}

gattServer.subscribeCharacteristicWrite({
  callback: function (data) {
    WriteCharacteristicReq(data)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### gattServer.unsubscribeCharacteristicWrite()


server 端取消订阅特征值读请求事件。


##### 无参数


##### 无返回值


##### 示例


```

const gattServer = bluetooth.BLE.createGattServer()
gattServer.unsubscribeCharacteristicWrite()
```

复制代码
#### gattServer.subscribeDescriptorRead(OBJECT)


server 端订阅描述符读请求事件。


##### OBJECT 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 回调此函数 |
| fail | Function | 否 | 失败回调。 |


##### callback 返回值:


| 类型 | 说明 |
| --- | --- |
| [DescriptorReadReq](#descriptorreadreq) | 描述 server 端订阅后收到的描述符读请求事件参数结构。 |


##### DescriptorReadReq


描述 server 端订阅后收到的描述符读请求事件参数结构。


| 参数名 | 类型 | 可读 | 可写 | 描述 |
| --- | --- | --- | --- | --- |
| deviceId | string | 是 | 否 | 表示发送描述符读请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 是 | 否 | 表示读请求的传输 ID，server 端回复响应时需填写相同的传输 ID。 |
| offset | number | 是 | 否 | 表示读描述符数据的起始位置。例如：k 表示从第 k 个字节开始读，server 端回复响应时需填写相同的 offset。 |
| descriptorUuid | string | 是 | 否 | 表示描述符（descriptor）的 UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 是 | 否 | 表示是否要给 client 端回复响应。 |
| value | ArrayBuffer | 是 | 否 | 表示写入的描述符二进制数据。 |
| descriptorUuid | string | 是 | 否 | 表示描述符（descriptor）的 UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 是 | 否 | 特定特征（characteristic）的 UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 是 | 否 | 特定服务（service）的 UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |


##### 示例


```

let gattServer = bluetooth.BLE.createGattServer()

let arrayBufferDesc = new ArrayBuffer(8)
let descValue = new Uint8Array(arrayBufferDesc)
descValue[0] = 1101
function ReadDescriptorReq(DescriptorReadReq) {
  let deviceId = DescriptorReadReq.deviceId
  let transId = DescriptorReadReq.transId
  let offset = DescriptorReadReq.offset
  let descriptorUuid = DescriptorReadReq.descriptorUuid

  let serverResponse = {
    deviceId: deviceId,
    transId: transId,
    status: 0,
    offset: offset,
    value: arrayBufferDesc,
  }

  let ret = gattServer.sendResponse(serverResponse)
  if (ret) {
    console.log('bluetooth sendResponse successfully')
  } else {
    console.log('bluetooth sendResponse failed')
  }
}

gattServer.subscribeDescriptorRead({
  callback: function (data) {
    ReadDescriptorReq(data)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### gattServer.unsubscribeDescriptorRead()


server 端取消订阅描述符读请求事件。


##### 无参数


##### 无返回值


##### 示例


```

const gattServer = bluetooth.BLE.createGattServer()
gattServer.unsubscribeDescriptorRead()
```

复制代码
#### gattServer.subscribeDescriptorWrite(OBJECT)


server 端订阅描述符写请求事件。


##### OBJECT 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 回调此函数 |
| fail | Function | 否 | 失败回调。 |


##### callback 返回值:


| 类型 | 说明 |
| --- | --- |
| [DescriptorWriteReq](#descriptorwritereq) | 描述 server 端订阅后收到的描述符写请求事件参数结构。 |


##### DescriptorWriteReq


描述 server 端订阅后收到的描述符写请求事件参数结构。


| 参数名 | 类型 | 可读 | 可写 | 描述 |
| --- | --- | --- | --- | --- |
| deviceId | string | 是 | 否 | 表示发送描述符写请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 是 | 否 | 表示写请求的传输 ID，server 端回复响应时需填写相同的传输 ID。 |
| offset | number | 是 | 否 | 表示写描述符数据的起始位置。例如：k 表示从第 k 个字节开始写，server 端回复响应时需填写相同的 offset。 |
| isPrep | boolean | 是 | 否 | 表示写请求是否立即执行。 |
| needRsp | boolean | 是 | 否 | 表示是否要给 client 端回复响应。 |
| value | ArrayBuffer | 是 | 否 | 表示写入的描述符二进制数据。 |
| descriptorUuid | string | 是 | 否 | 表示描述符（descriptor）的 UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 是 | 否 | 特定特征（characteristic）的 UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 是 | 否 | 特定服务（service）的 UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |


##### 示例


```

let gattServer = bluetooth.BLE.createGattServer()

let arrayBufferCCC = new ArrayBuffer(8)
let cccValue = new Uint8Array(arrayBufferCCC)
function WriteCharacteristicReq(CharacteristicWriteReq) {
  let deviceId = CharacteristicWriteReq.deviceId
  let transId = CharacteristicWriteReq.transId
  let offset = CharacteristicWriteReq.offset
  let isPrep = CharacteristicWriteReq.isPrep
  let needRsp = CharacteristicWriteReq.needRsp
  let value = new Uint8Array(CharacteristicWriteReq.value)
  let characteristicUuid = CharacteristicWriteReq.characteristicUuid

  cccValue[0] = value[0]
  let serverResponse = {
    deviceId: deviceId,
    transId: transId,
    status: 0,
    offset: offset,
    value: arrayBufferCCC,
  }

  let ret = gattServer.sendResponse(serverResponse)
  if (ret) {
    console.log('bluetooth sendResponse successfully')
  } else {
    console.log('bluetooth sendResponse failed')
  }
}

gattServer.subscribeDescriptorWrite({
  callback: function (data) {
    WriteCharacteristicReq(data)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### gattServer.unsubscribeDescriptorWrite()


server 端取消订阅描述符写请求事件。


##### 无参数


##### 返回值


##### 示例


```

const gattServer = bluetooth.BLE.createGattServer()
gattServer.unsubscribeDescriptorWrite()
```

复制代码
#### gattServer.subscribeConnectStateChange(OBJECT)


server 端订阅 BLE 连接状态变化事件。


##### OBJECT 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 回调此函数 |
| fail | Function | 否 | 失败回调。 |


##### callback 返回值:


| 类型 | 说明 |
| --- | --- |
| [BLEConnectChangedState](#bleconnectchangedstate) | 描述 Gatt profile 连接状态 。 |


##### BLEConnectChangedState


描述 Gatt profile 连接状态 。


| 参数名 | 类型 | 可读 | 可写 | 描述 |
| --- | --- | --- | --- | --- |
| deviceId | string | 是 | 否 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | [ProfileConnectionState](#profileconnectionstate) | 是 | 是 | 表示 BLE 连接状态的枚举。 |


##### ProfileConnectionState


枚举，蓝牙设备的 profile 连接状态。


| 名称 | 默认值 | 说明 |
| --- | --- | --- |
| STATE\_DISCONNECTED | 0 | 表示 profile 已断连。 |
| STATE\_CONNECTING | 1 | 表示 profile 正在连接。 |
| STATE\_CONNECTED | 2 | 表示 profile 正在连接。 |
| STATE\_DISCONNECTING | 3 | 表示 profile 正在断连。 |


##### 示例


```

function Connected(BLEConnectChangedState) {
  let deviceId = BLEConnectChangedState.deviceId
  let status = BLEConnectChangedState.state
}

let gattServer = bluetooth.BLE.createGattServer()
gattServer.subscribeConnectStateChange({
  callback: function (data) {
    Connected(data)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### gattServer.unsubscribeConnectStateChange()


server 端取消订阅 BLE 连接状态变化事件。


##### 无参数


##### 无返回值


##### 示例


```

const gattServer = bluetooth.BLE.createGattServer()
gattServer.unsubscribeConnectStateChange()
```

复制代码


---


<!-- 文档 29: js-api/system/brightness/.md -->


## 屏幕亮度

## 屏幕亮度

更新时间：2023-11-08 11:11:17


### 接口声明


```

{ "name": "blueos.hardware.display.brightness" }
```

复制代码
### 导入模块


```

import brightness from '@blueos.hardware.display.brightness' 或 const brightness = require('@blueos.hardware.display.brightness')
```

复制代码
### 接口定义


#### brightness.getValue(OBJECT)


获得当前屏幕亮度值


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| value | Integer | 屏幕亮度，取值范围 0-255 |


##### 示例：


```

brightness.getValue({
  success: function (data) {
    console.log(`handling success, value = ${data.value}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### brightness.getValueSync()


同步获得当前屏幕亮度值


##### 参数


无


##### 返回值


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| value | Number | 屏幕亮度，取值范围 0-255 |


##### 示例


```

const value = brightness.getValueSync()
```

复制代码
#### brightness.setValue(OBJECT)


设置当前屏幕亮度值


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Integer | 是 | 屏幕亮度，取值范围 0-255 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


##### 示例：


```

brightness.setValue({
  value: 100,
  success: function () {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### brightness.getMode(OBJECT)


获得当前屏幕亮度模式


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| mode | Integer | 0 为手动调节屏幕亮度,1 为自动调节屏幕亮度 |


##### 示例：


```

brightness.getMode({
  success: function (data) {
    console.log(`handling success, mode = ${data.mode}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### brightness.setMode(OBJECT)


设置当前屏幕亮度模式


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | Integer | 是 | 0 为手动调节屏幕亮度,1 为自动调节屏幕亮度 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


##### 示例：


```

brightness.setMode({
  mode: 1,
  success: function () {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### brightness.setKeepScreenOn(OBJECT)


设置是否保持常亮状态


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keepScreenOn | Boolean | 是 | 是否保持屏幕常亮 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


##### 示例：


```

brightness.setKeepScreenOn({
  keepScreenOn: true,
  success: function () {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### brightness.wakeScreenOn(OBJECT)


点亮或熄灭屏幕


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| screenOn | Boolean | 是 | 是否点亮 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


##### 示例：


```

brightness.wakeScreenOn({
  screenOn: true,
  success: function () {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### brightness.subscribe(OBJECT)


监听当前屏幕亮度数据。如果多次调用，仅最后一次调用生效


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 监听前屏幕亮度数据回调函数的执行 |
| fail | Function | 否 | 失败回调 |


###### callback 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| value | Number | 屏幕亮度，取值范围 0-255 |


##### 示例：


```

brightness.subscribe({
  callback: function (data) {
    console.log(`handling success, data = ${data.value}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### brightness.unsubscribe()


取消监听屏幕亮度数据


##### 参数：


无


##### 示例：


```

brightness.unsubscribe()
```

复制代码


---


<!-- 文档 30: js-api/system/cipher/.md -->


## 密码算法

## 密码算法

更新时间：2025-04-27 20:44:09


### 接口声明


```

{ "name": "blueos.security.cipher" }
```

复制代码
### 导入模块


```

import cipher from '@blueos.security.cipher' 或 const cipher = require('@blueos.security.cipher')
```

复制代码
### 接口定义


#### cipher.rsa(OBJECT)


RSA 加解密。


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | String | 是 | 加解密类型，两个可选值：encrypt：加密，decrypt： 解密 |
| text | String | 是 | 待加密或解密的文本内容。待加密的文本内容应该是一段普通文本，长度不能超过 keySize / 8 - 66，其中 keySize 是秘钥的长度（例如秘钥长度为 1024 时，text 不能超过 62 个字节）。待解密的文本内容应该是经过 base64 编码的一段二进制值。base64 编码使用默认风格，下同 |
| key | String | 是 | 加密或解密使用到的 RSA 密钥，经过 base64 编码后生成的字符串。加密时 key 为公钥，解密时 key 为私钥 |
| transformation | String | 否 | RSA 算法的填充项，默认为"RSA/None/OAEPwithSHA-256andMGF1Padding" |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| text | String | 经过加密或解密后生成的文本内容。加密后内容是经过 base64 编码的一段二进制值，解密后内容是一段普通文本。如果解密后的内容不能转化为 utf-8 字符串会出错 |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 202 | 输入参数错误。 |


##### 示例：


```

//加密
cipher.rsa({
  action: 'encrypt',
  //待加密的文本内容
  text: 'hello',
  //base64编码后的加密公钥
  key:
    'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDc7GR2MrfAoefES+wrs1ns2afT\n' +
    'eJXSfIkEHfPXG9fVFjaws1ho4KcZfsxlA0+SXvc83f2SVGCuzULmM2lxxRCtcUN/\n' +
    'h7SoaYEeluhqFimL2AEjfSwINHCLqObJkcjCfoZpE1JCehPiDOJsyT50Auc08h/4\n' +
    'jHQfanyC1nc62LqUCQIDAQAB',
  success: function (data) {
    console.log(`handling success: ${data.text}`)
  },
  fail: function (data, code) {
    console.log(`### cipher.rsa fail ### ${code}: ${data}`)
  },
})

//解密：
cipher.rsa({
  action: 'decrypt',
  //待解密的内容，是base64编码后的一段二进制值，解密后是文本内容“hello”
  text:
    'CUg3tTxTIdpCfreIxIBdws3uhd5qXLwcrVl3XDnQzZFVHyjVVCDHS16rjopaZ4C5xU2Tc8mSDzt7\n' +
    'gp9vBfSwi7bMtSUvXG18DlncsKJFDkJpS5t0PkpS9YrJXrY80Gpe+ME6+6dN9bjgqMljbitDdBRf\n' +
    'S/ZWNI4Q8Q0suNjNkGU=',
  //base64编码后的解密私钥
  key:
    'MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBANzsZHYyt8Ch58RL\n' +
    '7CuzWezZp9N4ldJ8iQQd89cb19UWNrCzWGjgpxl+zGUDT5Je9zzd/ZJUYK7NQuYz\n' +
    'aXHFEK1xQ3+HtKhpgR6W6GoWKYvYASN9LAg0cIuo5smRyMJ+hmkTUkJ6E+IM4mzJ\n' +
    'PnQC5zTyH/iMdB9qfILWdzrYupQJAgMBAAECgYEAkibhH0DWR13U0gvYJeD08Lfd\n' +
    'Sw1PMHyquEqIcho9Yv7bF3LOXjOg2EEGPx09mvuwXFgP1Kp1e67XPytr6pQQPzK7\n' +
    'XAPcLPx80R/ZjZs8vNFndDOd1HgD3vSVmYQarNzmKi72tOUWMPevsaFXPHo6Xx3X\n' +
    '8x0wYb7XuBsQguRctTECQQD7GWX3JUiyo562iVrpTDPOXsrUxmzCrgz2OZildxMd\n' +
    'Pp/PkyDrx7mEXTpk4K/XnQJ3GpJNi2iDSxDuPSAeJ/aPAkEA4Tw4+1Z43S/xH3C3\n' +
    'nfulYBNyB4si6KEUuC0krcC1pDJ21Gd12efKo5VF8SaJI1ZUQOzguV+dqNsB/JUY\n' +
    'OFfX5wJAB1dKv9r7MR3Peg6x9bggm5vx2h6i914XSuuMJupASM6X5X2rrLj+F3yS\n' +
    'RHi9K1SPyeOg+1tkBtKfABgRZFBOyQJAbuTivUSe73AqTKuHjB4ZF0ubqgEkJ9sf\n' +
    'Q2rekzm9dOFvxjZGPQo1qALX09qATMi1ZN376ukby8ZAnSafLSZ64wJBAM2V37go\n' +
    'Sj44HF76ksRow8gecuQm48NCTGAGTicXg8riKog2GC9y8pMNHAezoR9wXJF7kk+k\n' +
    'lz5cHyoMZ9mcd30=',
  success: function (data) {
    console.log(`handling success: ${data.text}`)
  },
  fail: function (data, code) {
    console.log(`### cipher.rsa fail ### ${code}: ${data}`)
  },
})
```

复制代码
#### cipher.aes(OBJECT)


AES 加解密,支持分段加密


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | String | 是 | 加解密类型，两个可选值：encrypt：加密，decrypt：解密 |
| text | String | 是 | 待加密或解密的文本内容。待加密的文本内容应该是一段普通文本。待解密的文本内容应该是经过 base64 编码的一段二进制值。base64 编码使用默认风格，下同 |
| key | String | 是 | 加密或解密使用到的密钥，经过 base64 编码后生成的字符串。密钥长度可以是 128 bit，192 bit 或 256 bit。 |
| transformation | String | 否 | AES 算法的加密模式和填充项，默认为"AES/CBC/PKCS5Padding" |
| iv | String | 否 | AES 加解密的初始向量，经过 base64 编码后的字符串，默认值为 key 值 |
| ivOffset | Integer | 否 | AES 加解密的初始向量偏移，默认值为 0 |
| ivLen | Integer | 是 | AES 加解密的初始向量字节长度，取值和 iv 长度对应，iv 长度 128 bit，192 bit 或 256 bit 分别对应取值为 16，24，32 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| text | String | 经过加密或解密后生成的文本内容。加密后内容是经过 base64 编码的一段二进制值，解密后内容是一段普通文本。如果解密后的内容不能转化为 utf-8 字符串会出错（CODE：200） |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 200 | 一般性错误，在加解密出错时会返回此错误 |
| 202 | 参数错误 |


##### 示例：


```

//加密
cipher.aes({
  action: 'encrypt',
  //待加密的文本内容
  text: 'hello',
  //base64编码后的密钥
  key: 'NDM5Qjk2UjAzMEE0NzVCRjlFMkQwQkVGOFc1NkM1QkQ=',
  transformation: 'AES/CBC/PKCS5Padding',
  //transformation: 'ECB', // ECB类型加密
  ivOffset: 0,
  ivLen: 32,
  success(data) {
    console.log(`handling success: ${data.text}`)
  },
  fail(data, code) {
    console.log(`code=${code},data=${data}`)
  },
})

//解密：
cipher.aes({
  action: 'decrypt',
  //待解密的内容，是base64编码后的一段二进制值
  text: '1o0kf2HXwLxHkSh5W5NhzA==',
  //base64编码后的密钥
  key: 'NDM5Qjk2UjAzMEE0NzVCRjlFMkQwQkVGOFc1NkM1QkQ=',
  transformation: 'AES/CBC/PKCS5Padding',
  ivOffset: 0,
  ivLen: 32,
  success(data) {
    console.log(`handling success: ${data.text}`)
  },
  fail(data, code) {
    console.log(`code=${code},data=${data}`)
  },
})
```

复制代码
#### cipher.base64(OBJECT)


base64 编解码。


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | String | 是 | 加解密类型，两个可选值：encrypt：加密，decrypt：解密 |
| text | String | 是 | 待加密或解密的文本内容。待加密的文本内容应该是一段普通文本。 |


##### 返回值：


| 类型 | 说明 |
| --- | --- |
| String | 经过 base64 加密或解密后生成的文本内容。 |


##### 示例：


```

//加密
const base64text = cipher.base64({
  action: 'encrypt',
  text: 'hello',
})
console.log(base64text)

//解密：
const text = cipher.base64({
  action: 'decrypt',
  text: base64text,
})
console.log(text)
```

复制代码
#### cipher.crc32(OBJECT)


crc32 加密


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | Buffer | String | 是 | 加密内容 |


##### 返回值：


| 类型 | 说明 |
| --- | --- |
| Number | crc32 加密结果 |


##### 示例：


```

const res = cipher.crc32({
  content: new Uint8Array([1, 2]),
})
console.log(res)
```

复制代码
#### cipher.hash(OBJECT)


求 hash 值


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algorithm | String | 是 | hash 算法，可选 md5,sha256。 |
| content | Buffer | String | 是 | 加密内容。 |


##### 返回值：


| 类型 | 说明 |
| --- | --- |
| String | 返回 hash 计算结果 |


##### 示例：


```

const res = cipher.hash({
  algorithm: 'md5',
  content: 'hello',
})
console.log(res)
```

复制代码


---


<!-- 文档 31: js-api/system/communicationOverview/.md -->


## 概述

## 概述

更新时间：2023-10-29 18:27:39


蓝河应用通信能力为应用提供了丰富的通信工具，从本地设备到远程服务器，从文件传输到实时通信，从蓝牙到网络状态监测，为应用提供了多样化的数据传输和通信渠道。这使开发者能够构建更多样化的应用，实现应用内外的数据传输和通信。


### 子模块介绍


| 模块 | 简述 |
| --- | --- |
| 蓝牙 | 该模块允许应用与附件的蓝牙设备进行通信，实现设备间的数据传输和互动 |
| 上传下载 | 该模块支持应用上传和下载各种文件数据，有助于实现文件传输和数据同步 |
| 数据请求 | 该模块允许应用向远程服务器发送请求，获取数据或与服务器进行交互。这是应用与后端服务通信的核心功能 |
| websocket | 该模块提供了实时双向通信的能力，使应用能够实时传递数据和事件 |
| 网络状态 | 该模块帮助应用监测当前网络连接状态，包括是否连接、网络类型等，有助于应用根据网络条件调整行为 |


---


<!-- 文档 32: js-api/system/console/.md -->


## 日志打印

## 日志打印

更新时间：2024-06-28 10:21:20


### 概述


日志打印模块用于帮助开发者在应用开发和调试过程中记录和分析信息，有利于错误排查和性能优化。


### 接口声明


无需声明


### 导入模块


无需导入


### 接口定义


#### console.debug/log/info/warn/error(message)


打印一段文本。


##### 参数：


| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | String | 是 | 要打印的文本，也可以是格式化文本，规则与浏览器的 console 相同 |


备注：本接口只支持普通打印，不支持内容样式定义等其他操作。


##### 示例：


```

console.log('log:我是log')
console.debug('debug:我是debug')
console.info('info:我是info')
console.warn('warn:我是warn')
console.error('error:我是error')
```

复制代码


---


<!-- 文档 33: js-api/system/device/.md -->


## 设备信息

## 设备信息

更新时间：2025-03-31 14:41:09


### 接口声明


```

{ "name": "blueos.hardware.deviceInfo" }
```

复制代码
### 导入模块


```

import device from '@blueos.hardware.deviceInfo' 或 const device = require('@blueos.hardware.deviceInfo')
```

复制代码
##### 开发者需要在 manifest.json 里面配置权限：


```

{
  "permissions": [{ "name": "watch.permission.DEVICE\_INFO" }]
}
```

复制代码
### 接口定义


#### device.getInfo(OBJECT)


获取设备信息


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| brand | String | 设备品牌 |
| manufacturer | String | 设备生产商 |
| model | String | 设备型号 |
| product | String | 设备代号 |
| osType | String | 操作系统名称 |
| osVersionName | String | 操作系统版本名称 |
| osVersionCode | Integer | 操作系统版本号 |
| platformVersionName | String | 运行平台版本名称 |
| platformVersionCode | Integer | 运行平台版本号 |
| language | String | 系统语言 |
| deviceName | String | 设备名称 |
| hardwareVersion | String | 硬件版本 |
| softwareVersion | String | 软件版本 |
| region | String | 系统地区 |
| screenWidth | Integer | 屏幕宽 |
| screenHeight | Integer | 屏幕高 |
| windowWidth | Integer | 可使用窗口宽度 |
| windowHeight | Integer | 可使用窗口高度 |
| statusBarHeight | Integer | 状态栏高度 |
| screenDensity | Float | 设备的屏幕密度 |
| vendorOsName | String | 系统的名称，如 BlueOS |
| vendorOsVersion | String | 蓝河应用的版本号 |
| cutout | Array | 针对异形屏(比如刘海屏、水滴屏和开孔屏)返回异形区域的位置大小。Array 中每个 item 表示一个异形区域的描述。item 参数：left:cutout 左边界距离屏幕左边距离top:cutout 上边界距离屏幕上边距离right:cutout 右边界距离屏幕右边距离bottom:cutout 下边界距离屏幕下边距离cutout 的坐标描述以竖屏为基准。即在横屏和竖屏下获取的 cutout 参数描述都是一样的。 |
| deviceType | String | 当前蓝河应用引擎的设备类型，手表版为'watch' |
| screenRefreshRate | Float | 获取屏幕显示刷新率(获取帧率可能不为 60, 90, 144 等标准帧率) |


##### 示例：


```

device.getInfo({
  success: function (ret) {
    console.log(`handling success， brand = ${ret.brand}`)
  },
})
```

复制代码
#### device.getInfoSync()


同步获取设备信息


##### 参数


无


##### 返回值


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| deviceInfo | Object | 当前设备信息,deviceInfo 参数信息如上 device.getInfo success 返回值 |


##### 示例


```

const deviceInfo = device.getInfoSync()
```

复制代码
#### device.getApiLevel(OBJECT)


获取系统支持的支持API Level


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | (apiLevel: number) => void | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 类型 | 说明 |
| --- | --- |
| number | 系统支持的支持API Level |


##### 示例


```

device.getApiLevel({
  success(apiLevel) {
    console.log(`apiLevel=${apiLevel}`)
  },
  fail() {}
})
```

复制代码
#### device.getApiLevelSync()


同步获取系统支持的支持API Level


##### 参数


无


##### 返回值


| 类型 | 说明 |
| --- | --- |
| number | 系统支持的支持API Level |


##### 示例


```

const apiLevel = device.getApiLevelSync();
console.log(`apiLevel=${apiLevel}`)
```

复制代码
#### device.getRegionSync()


同步获取设备地区信息


##### 参数


无


##### 返回值


| 类型 | 说明 |
| --- | --- |
| string | CN 中国ID 印度尼西亚TH 泰国MY 马来西亚SG 新加坡PH 菲律宾ZA 南非CO 哥伦比亚TR 土耳其RU 俄罗斯 |


##### 示例


```

const region = device.getRegionSync()
console.log('region is', region)
```

复制代码
#### device.getRegion()


异步获取设备地区信息


##### 参数：


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| success | 否 | Function | 成功回调 |
| fail | 否 | Function | 失败回调 |


##### success 返回值:


| 类型 | 说明 |
| --- | --- |
| string | CN 中国ID 印度尼西亚TH 泰国MY 马来西亚SG 新加坡PH 菲律宾ZA 南非CO 哥伦比亚TR 土耳其RU 俄罗斯 |


##### 示例：


```

device.getRegion({
  success: function (region) {
    console.log('region is', region)
  },
})
```

复制代码
#### device.getPeerDeviceInfo(OBJECT)


获取连接手机的信息


##### 参数：


| 属性 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| success | 否 | Function | 成功回调 |
| fail | 否 | Function | 失败回调 |


##### success 返回值:


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| brand | String | 设备品牌 |
| osType | String | 操作系统名称 |


##### fail 返回值:


##### 示例：


```

device.getPeerDeviceInfo({
  success: function (ret) {
    console.log(`handling success， brand = ${ret.brand}`)
  },
})
```

复制代码
#### device.getId(OBJECT)


批量获取设备标识


##### 权限要求


获取手表状态


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | Array | 是 | 支持 device、mac、user、advertising 四种类型，可提供一至多个 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


按照传入的 type 返回对应的 id，未在 type 中出现的 id 类型不会返回


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| device | String | 设备唯一标识。 |
| mac | String | 设备的 mac 地址。 |
| user | String | 用户唯一标识。 |
| advertising | String | 广告唯一标识 |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 400 | 拒绝授予权限 |
| 402 | 权限错误（未声明该权限） |


##### 示例：


```

device.getId({
  type: ['device', 'mac'],
  success: function (data) {
    console.log(`handling success: ${data.device}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}, errorMsg=${data}`)
  },
})
```

复制代码
#### device.getDeviceId(OBJECT)


获取设备唯一标识


##### 权限要求


获取手表状态


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| deviceId | String | 设备唯一标识。 |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 400 | 拒绝授予权限 |
| 402 | 权限错误（未声明该权限） |


```

device.getDeviceId({
  success: function (data) {
    console.log(`handling success: ${data.deviceId}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### device.getSerial(OBJECT)


获取设备序列号


##### 权限要求


获取手表状态


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| serial | String | 设备序列号 |


```

device.getSerial({
  success: function (data) {
    console.log(`handling success: ${data.serial}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### device.getTotalStorage(OBJECT)


获取存储空间的总大小


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| totalStorage | Number | 存储空间的总大小，单位是 Byte。 |


```

device.getTotalStorage({
  success: function (data) {
    console.log(`handling success: ${data.totalStorage}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### device.getAvailableStorage(OBJECT)


获取存储空间的可用大小


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| availableStorage | Number | 存储空间的可用大小，单位是 Byte。 |


```

device.getAvailableStorage({
  success: function (data) {
    console.log(`handling success: ${data.availableStorage}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### device.getDeviceICCID(OBJECT)


获取卡识别码


##### 参数


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| iccid | String | 卡识别码 |


```

device.getDeviceICCID({
  success: function (data) {
    console.log(`handling success: ${data.iccid}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### device.getCpuInfo(OBJECT)


返回 CPU 信息


##### 参数


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| cpuInfo | String | CPU 信息。 |


```

device.getCpuInfo({
  success: function (data) {
    console.log(`handling success: ${data.cpuInfo}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### device.isSupported(name: string)


断硬件设备能力是否支持


##### 参数


| 类型 | 必填 | 说明 |
| --- | --- | --- |
| String | 是 | 支持的硬件能力枚举，见下文【硬件设备能力枚举】 |


###### 返回值


| 类型 | 说明 |
| --- | --- |
| Boolean | 是否支持，true 支持，false 不支持 |


###### 示例


```

const isSupported = device.isSupported('sys.modem.support')
```

复制代码
#### device.getFeatureList(OBJECT)


获取全部硬件功能列表


##### 参数


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 类型 | 说明 |
| --- | --- |
| Array<string> | 获取全部硬件功能列表，见下文【硬件设备能力枚举】 |


###### 示例


```

device.getFeatureList({
  success: function (data) {
    console.log(`handling success: ${data}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}, errorMsg=${data}`)
  },
})
```

复制代码


| 类型 | 说明 |
| --- | --- |
| Array<string> | 硬件设备支持的功能列表 |


### 硬件设备能力枚举


| 枚举值 | 说明 |
| --- | --- |
| sys.modem.support | modem 功能 |
| sys.sensor.ecg.support | ecg 功能 |


---


<!-- 文档 34: js-api/system/event/.md -->


## 公共事件

## 公共事件

更新时间：2023-12-21 13:49:50


公共事件提供了多应用间数据传递和事件交互的能力。


### 接口声明


```

{ "name": "blueos.app.event.eventManager" }
```

复制代码
### 导入模块


```

import event from '@blueos.app.event.eventManager' 或 const event = require('@blueos.app.event.eventManager')
```

复制代码
### 接口定义


#### event.publish(OBJECT)


发布公共事件


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventName | String | 是 | 事件名称, [公共事件保留名称](#%E5%85%AC%E5%85%B1%E4%BA%8B%E4%BB%B6%E4%BF%9D%E7%95%99%E7%B1%BB%E5%9E%8B)被系统占用，请勿使用 |
| options | Object | 否 | 事件参数 |


###### options 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | Object | 否 | 事件参数 |
| permissions | Array<String> | 否 | 订阅者的权限, 拥有权限的包才能收到发送的事件 |


##### 示例：


```

event.publish({
  eventName: 'myEventName',
  options: {
    params: { age: 10, name: 'peter' },
    permissions: ['com.example.demo'],
  },
})
```

复制代码
#### event.subscribe(OBJECT)


订阅公共事件


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventName | String | 是 | 事件名称 |
| callback | Function | 是 | 事件回调 |


###### callback 返回值：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | Object | 否 | 事件参数 |
| package | String | 否 | 事件推送者包名 |


##### 返回值：


| 类型 | 必填 | 说明 |
| --- | --- | --- |
| Number | 是 | 事件 id |


##### 示例：


```

const evtId = event.subscribe({
  eventName: 'myEventName',
  callback: function (res) {
    if (res.package === 'com.example.demo') {
      console.log(res.params)
    }
  },
})
console.log(evtId)
```

复制代码
#### event.unsubscribe(OBJECT)


取消订阅公共事件


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | Number | 是 | 订阅 id |


##### 示例：


```

event.unsubscribe({ id: 1 })
```

复制代码
#### 系统支持的公共事件


| 系统公共事件名称 | 订阅者所需权限 | 说明 |
| --- | --- | --- |
| usual.event.SHUTDOWN | 无 | 即将关机 |
| usual.event.BATTERY\_CHANGED | 无 | 电量改变，参数：level:0.0 - 1.0 之间 |
| usual.event.BATTERY\_LOW | 无 | 低电事件 |
| usual.event.BATTERY\_OKAY | 无 | 充满电事件 |
| usual.event.SCREEN\_OFF | 无 | 灭屏事件 |
| usual.event.SCREEN\_AOD | 无 | AOD 事件 |
| usual.event.SCREEN\_ON | 无 | 亮屏事件 |
| usual.event.PACKAGE\_ADDED | 无 | 新安装应用，参数：package:com.xxx.xxx |
| usual.event.PACKAGE\_REPLACED | 无 | 应用安装更新，参数：package:com.xxx.xxx |
| usual.event.PACKAGE\_REMOVED | 无 | 应用卸载，参数：package:com.xxx.xxx |
| usual.event.DISCHARGING | 无 | 停止充电 |
| usual.event.CHARGING | 无 | 开始充电 |
| usual.event.OTA\_TRANSFER | 无 | ota 开始传输 |
| usual.event.OTA\_INSTALL | 无 | ota 开始安装 |


---


<!-- 文档 35: js-api/system/fastlz/.md -->


## 解压缩

## 解压缩

更新时间：2025-04-29 11:37:34


### 接口声明


```

{ "name": "blueos.util.fastlz" }
```

复制代码
### 导入模块


```

import fastlz from '@blueos.util.fastlz' 或 const fastlz = require('@blueos.util.fastlz')
```

复制代码
### 接口定义


#### fastlz.decompress(OBJECT)


解压文件


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcUri | String | 是 | 源文件的 uri，不能是 tmp 类型的 uri |
| dstUri | String | 是 | 目标目录的 uri 必须是完整的文件名 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |


##### 示例：


```

fastlz.decompress({
  srcUri: 'internal://files/test1',
  dstUri: 'internal://files/test2',
  success: function () {
    console.log(`handling success`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码


---


<!-- 文档 36: js-api/system/fetch/.md -->


## 数据请求

## 数据请求

更新时间：2024-10-11 11:55:18


### 接口声明


```

{ "name": "blueos.network.fetch" }
```

复制代码
### 导入模块


```

import fetch from '@blueos.network.fetch' 或 const fetch = require('@blueos.network.fetch')
```

复制代码
### 接口定义


#### fetch.fetch(OBJECT)


获取网络数据


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | String | 是 | 资源 url |
| data | String/Object/ArrayBuffer | 否 | 请求的参数，可以是字符串，或者是 js 对象、arraybuffer 对象。参考 `data与Content-Type关系` 部分 |
| header | Object | 否 | 请求的 header，会将其所有属性设置到请求的 header 部分。User-Agent 设置在版本开始支持。示例：{"Accept-Encoding": "gzip, deflate","Accept-Language": "zh-CN,en-US;q=0.8,en;q=0.6"} |
| method | String | 否 | 默认为 GET，可以是：OPTIONS，GET，HEAD，POST，PUT，DELETE，TRACE，CONNECT |
| responseType | String | 否 | 支持返回类型是 text，json，file，arraybuffer，默认会根据服务器返回 header 中的 Content-Type 确定返回类型，详见 `success返回值`。 |
| timeout | Number | 否 | 超时时间，单位 ms，默认值为 7000 |
| success | Function | 否 | 成功返回的回调函数 |
| fail | Function | 否 | 失败的回调函数，可能会因为权限失败 |
| complete | Function | 否 | 结束的回调函数（调用成功、失败都会执行） |


##### data 与 Content-Type 关系


| data | Content-Type | 说明 |
| --- | --- | --- |
| String | 不设置 | Content-Type 默认为 text/plain，data 值作为请求的 body |
| String | 任意 Type | data 值作为请求的 body |
| Object | 不设置 | Content-Type 默认为 application/x-www-form-urlencoded，data 按照 url 规则进行 encode 拼接作为请求的 body |
| Object | application/x-www-form-urlencoded | data 按照 url 规则进行 encode 拼接作为请求的 body |
| Object | application/x-www-form-urlencoded 之外的任意 type | 会将 data 转为字符串作为请求的 body |
| ArrayBuffer | 不设置 | Content-Type 默认为 application/octet-stream，data 值作为请求的 body |
| ArrayBuffer | 任意 Type | data 值作为请求的 body |


###### success 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| code | Integer | 服务器状态 code |
| data | String/Object /ArrayBuffer | 参考 `responseType与success中data关系` 部分 |
| headers | Object | 服务器 response 的所有 header |


###### responseType 与 success 中 data 关系：


| responseType | data | 说明 |
| --- | --- | --- |
| 无 | String | 服务器返回的 header 中 type 是 text/\*或 application/json、application/javascript、application/xml，值是文本内容，否则是存储的临时文件的 uri，临时文件如果是图片或者视频内容，可以将图片设置到 image 或 video 控件上显示 |
| text | String | 返回普通文本 |
| json | Object | 返回 js 对象 |
| file | String | 返回存储的临时文件的 uri |
| arraybuffer | ArrayBuffer | 返回 ArrayBuffer 对象 |


##### 示例：


```

fetch.fetch({
  url: 'http://www.example.com',
  responseType: 'text',
  success: function (response) {
    console.log(`the status code of the response: ${response.code}`)
    console.log(`the data of the response: ${response.data}`)
    console.log(`the headers of the response: ${JSON.stringify(response.headers)}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, errMsg = ${data}`)
    console.log(`handling fail, errCode = ${code}`)
  },
})
```

复制代码


---


<!-- 文档 37: js-api/system/generatecertificatethumbprint/.md -->


## 生成签名证书指纹

## 生成签名证书指纹

更新时间：2024-01-10 16:04:30


开发者通过**JDK**的**Keytool**工具以及签名文件，导出**SHA256**指纹。


### windows


1. 执行 CMD 命令打开命令行工具，执行 cd 命令进入 keytool.exe 所在的目录（以下样例为 JDK 安装在 C 盘的 Program Files 目录）。


```

  cd C:\Program Files\Java\jdk\bin
```

复制代码
2. 执行命令 `keytool -list -v -keystore \<keystore-file\>`，按命令行提示进行操作。`\<keystore-file\>`为应用签名证书的完整路径。例如：


```

  keytool -list -v -keystore C:\TestApp.jks
```

复制代码
3. 根据结果获取对应的 SHA256 指纹。


![windowsSHA256](/c301ef1e1909585101d5106c752a8d6f/windowsSHA256.png)


### macOS


1. 打开 Terminal 终端。


![macOSTerminal](/e22774e8b3878b67d0253aa5d750bd9f/macOSTerminal.png)


2. 执行命令 `keytool -list -v -keystore \<keystore-file\>`，按命令行提示进行操作。`\<keystore-file\>`为应用签名证书的完整路径。例如：


```

  keytool -list -v -keystore /Users/admin/Downloads/HmsDemo.jks
```

复制代码
3. 根据结果获取对应的 SHA256 指纹。


![macOSSHA256](/16720dd49f62d60febf7af53f7f975d9/macOSSHA256.png)


---


<!-- 文档 38: js-api/system/geolocation/.md -->


## 地理位置

## 地理位置

更新时间：2024-08-13 15:19:43


### 接口声明


```

{ "name": "blueos.hardware.location.location" }
```

复制代码
### 导入模块


```

import geolocation from '@blueos.hardware.location.location' 或 const geolocation = require('@blueos.hardware.location.location')
```

复制代码
### 接口定义


#### geolocation.getLocation(OBJECT)


获取地理位置


##### 权限要求


精确设备定位


##### 开发者需要在 manifest.json 里面配置权限：


```

{
  "permissions": [{ "name": "watch.permission.LOCATION" }]
}
```

复制代码
##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | Number | 否 | 设置超时时间，单位是 ms，默认值为 30000。在权限被系统拒绝或者定位设置不当的情况下，有可能永远不能返回结果，因而需要设置超时。超时后会使用 fail 回调 |
| coordType | String | 否 | 坐标系类型，可选值可通过 getSupportedCoordTypes 获取，默认为 wgs84 |
| success | Function | 是 | 成功回调 |
| fail | Function | 否 | 失败回调，原因可能是用户拒绝 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| longitude | Number | 经度 |
| latitude | Number | 纬度 |
| accuracy | Number | 精确度 |
| time | Number | 时间 |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 400 | 拒绝授予权限 |
| 402 | 权限错误（未声明该权限） |


##### 示例：


```

geolocation.getLocation({
  success: function (data) {
    console.log(`handling success: longitude = ${data.longitude}, latitude = ${data.latitude}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}, errorMsg=${data}`)
  },
})
```

复制代码
#### geolocation.subscribe(OBJECT)


监听地理位置。如果多次调用，仅最后一次调用生效


##### 权限要求


精确设备定位


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reserved | Boolean | 否 | 是否持久化订阅，默认为 false。机制：设置为 true，页面跳转，不会自动取消订阅，需手动取消订阅 |
| coordType | String | 否 | 坐标系类型，可选值可通过 getSupportedCoordTypes 获取，默认为 wgs84 |
| callback | Function | 是 | 每次位置信息发生变化，都会被回调 |
| fail | Function | 否 | 失败回调，原因可能是用户拒绝 |


###### callback 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| longitude | Number | 经度 |
| latitude | Number | 纬度 |
| accuracy | Number | 精确度 |
| time | Number | 时间 |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 400 | 拒绝授予权限 |
| 402 | 权限错误（未声明该权限） |


##### 示例：


```

geolocation.subscribe({
  callback: function (data) {
    console.log(`handling success: longitude = ${data.longitude}, latitude = ${data.latitude}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}, errorMsg=${data}`)
  },
})
```

复制代码
#### geolocation.unsubscribe()


取消监听地理位置


##### 参数：


无


##### 示例：


```

geolocation.unsubscribe()
```

复制代码
#### geolocation.getSupportedCoordTypes()


获取支持的坐标系类型


##### 参数：


无


##### 返回值：


字符串数组。当前支持的坐标系类型，如['wgs84']


##### 示例：


```

const types = geolocation.getSupportedCoordTypes()
```

复制代码


---


<!-- 文档 39: js-api/system/hardware/.md -->


## 概述

## 概述

更新时间：2024-01-26 10:30:32


蓝河应用的基础硬件能力模块旨在为应用提供访问和控制设备的基础硬件功能。该模块使应用能够与设备硬件进行互动，为开发者提供了强大的工具，以满足应用特定功能要求。


### 子模块介绍


| 模块 | 简述 |
| --- | --- |
| 地理位置 | 该模块允许应用获取设备的地理位置信息，包括经度、纬度和定位精度，以支持位置相关的应用功能 |
| 振动 | 该模块提供了控制设备振动的功能，使应用能够在需要时触发振动反馈。 |
| 屏幕管理 | 提供获取熄屏时间能力 |
| 传感器 | 该模块提供了访问设备内置传感器（如加速度计、陀螺仪等）的功能，以支持应用的传感器驱动功能 |
| 电量信息 | 该模块提供了获取设备电池状态和电量信息的能力 |
| 屏幕亮度 | 该模块允许应用调整和获取设备屏幕的亮度，以满足用户需求和环境条件。 |
| 设备信息 | 该模块提供了获取设备硬件信息的功能，包括设备型号、操作系统版本等，以帮助应用适配和识别设备特性 |


---


<!-- 文档 40: js-api/system/inputmethod/.md -->


## 输入法

## 输入法

更新时间：2024-07-05 18:02:47


### 接口声明


```

{ "name": "blueos.service.inputMethod" }
```

复制代码
### 导入模块


```

import inputmethod from '@blueos.service.inputMethod' 或 const inputmethod = require('@blueos.service.inputMethod')
```

复制代码
### 接口定义


#### inputmethod.setInput()


输入法应用向页面的 [<input>](/component/table/input) 组件写入数据，仅输入法应用才会用到此功能


##### 参数：


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| value | String | 输入法录入的数据 |


##### 返回值：


无


##### 示例：


```

inputmethod.setInput({
  value: 'hello vivo watch',
})
```

复制代码
### 如何调起输入法


#### 1. 选择输入法类型


`input` 组件 `type` 属性可以控制拉起输入法类型


- text: 手写输入法
- speak: 语音输入法


```

<template>
  <input type="text" value="inputValue" onchange="textChange" />
</template>
<script>
 export default {
 data: {
 inputValue: '',
 },
 textChange({ value }) {
 this.inputValue = value
 },
 }
</script>
```

复制代码
#### 2.禁止 input 输入法自动拉起


若调用者仅需要展示文本，而不希望自动拉起输入法，可以在 `input` 组件上设置属性 `readonly="readonly"`


```

<template>
  <input type="text" value="inputValue" readonly="readonly" />
</template>
<script>
 export default {
 data: {
 inputValue: 'hello',
 },
 }
</script>
```

复制代码
#### 3.任意组件拉起输入法


1. 增加类型为 `text` 或者 `speak` 的 `input` 组件，并将其隐藏 `show="false"`, `input`组件位置可以是任意的。
2. `input` 组件的 `change` 事件回调用于调用者接收输入法返回的数据。
3. 在其他需要调用输入法的组件的 `click` 事件中调用 `input` 组件的 `focus` 方法
4. 若有多个组件需要启动输入法，只需要新增一个 `input` 组件，在对应的组件的 `click` 方法中标识是哪个组件拉起输入法。


```

<template>
  <div>
    <text onclick="btnClick">{{inputValue}}</text>
    <input show="false" id="ipt" type="text" onchange="textChange" />
  </div>
</template>
<script>
 export default {
 data: {
 inputValue: '',
 },
 textChange({ value }) {
 this.inputValue = value
 },
 btnClick() {
 this.$element('ipt').focus()
 },
 }
</script>
```

复制代码


---


<!-- 文档 41: js-api/system/media/.md -->


## 多媒体

## 多媒体

更新时间：2025-08-13 20:11:57


### 接口声明


```

{ "name": "blueos.media.audio.mediaManager" }
```

复制代码
### 导入模块


```

import media from '@blueos.media.audio.mediaManager' 或 const media = require('@blueos.media.audio.mediaManager')
```

复制代码
### media.createAudioPlayer(OBJECT)


创建音频播放的实例。


**参数**


| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamType | [StreamType](#streamtype) | 否 | 音量策略，默认值为 music |
| contentType | [ContentType](#contenttype) | 否 | 音频后处理类型，默认值为 music |
| streamUsage | [StreamUsage](#streamusage) | 否 | 音频类型，默认值为 music |


**返回值：** [AudioPlayer](#audioplayer)


**示例：**


```

const audioPlayer = media.createAudioPlayer({
  streamType: "music",
  contentType: "music",
  streamUsage: "music"
})
```

复制代码
### media.createAudioTrack(OBJECT)


创建音频流式播放的实例


**参数**


| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamType | [StreamType](#streamtype) | 否 | 音量策略，默认值为 music |
| contentType | [ContentType](#contenttype) | 否 | 音频后处理类型，默认值为 music |
| streamUsage | [StreamUsage](#streamusage) | 否 | 音频类型，默认值为 music |
| sampleRateInHz | number | 否 | 采样率，单位赫兹，可选值为：8000、 16000；默认值为 16000 |
| channelConfig | number | 否 | 捕获音频的声道数目，1：单声道，2：立体声；默认值为 1 |
| audioFormat | number | 否 | 样本的分辨率，单位 bit，可选值为： 8、16；默认值为 16 |


**返回值：** [AudioTrack](#audiotrack)


**示例：**


```

const audioTrack = media.createAudioTrack()
```

复制代码
### media.createAudioRecord(OBJECT)


创建录音实例


**权限要求**： 录音


**开发者需要在 manifest.json 里面配置权限：**


```

{
  "permissions": [{ "name": "blueos.permission.RECORD" }]
}
```

复制代码
**参数**


| 属性名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sampleRateInHz | number | 否 | 采样率，单位赫兹，可选值为：8000、 16000；默认值为 16000 |
| channelConfig | number | 否 | 音频的声道数目，1：单声道，2：立体声；默认值为 1 |
| audioFormat | number | 否 | 样本的分辨率，单位 bit，可选值为： 8、16；默认值为 16 |


**返回值：** [AudioRecorder](#audiorecorder)


**示例：**


```

const audioRecorder = media.createAudioRecord({
  sampleRateInHz: 16000,
  channelConfig: 1,
  audioFormat: 16
})
```

复制代码
### AudioPlayer


#### play()


开始播放音频


**参数：** 无


**示例：**


```

audioPlayer.src = 'xxx'
// play 方法调用无需等待 src 加载完成
audioPlayer.play()
```

复制代码
#### pause()


暂停播放音频


**参数：** 无


**示例：**


```

audioPlayer.pause()
```

复制代码
#### stop()


停止音频播放，可以通过 play 重新播放音频


**参数：** 无


**示例：**


```

audioPlayer.stop()
```

复制代码
#### release()


释放音频资源


**参数：** 无


**示例：**


```

audioPlayer.release()
```

复制代码
#### src


字符串属性；可读可写属性，声明该属性会指定播放的音频媒体 uri。


**示例：**


```

audioPlayer.src = "internal://files/a.mp3"
```

复制代码
#### currentTime


读取 `currentTime` 属性将返回一个双精度浮点值，用以标明以秒为单位的当前音频的播放位置，设置 `currentTime` 将设置当前的播放位置。


**示例：**


```

audioPlayer.currentTime = 100.0
```

复制代码
#### duration `只读`


这是一个双精度浮点数，指明了音频在时间轴中的持续时间（总长度），以秒为单位。如果元素上没有媒体，或者媒体是不可用的，那么会返回 `NaN`。


**示例：**


```

const duration = audioPlayer.duration;
console.log(duration)
```

复制代码
#### state `只读`


读取 `state` 属性可获取当前音频的播放状态。分别为：分别为`play,'pause','stop','idle'


```

const state = audioPlayer.state;
console.log(state)
```

复制代码
#### playcount


整型数值，控制音频的循环播放。playcount = 1 或 playcount = 0：不开启循环; playcount >1：开启循环，且循环指定的次数; playcount = -1：开启循环，且循环无限次数。


**示例：**


```

audioPlayer.playcount = -1;
```

复制代码
#### onPlay


在音频 play 后的回调事件。


**示例：**


```

audioPlayer.onPlay = () => {
  console.log("play")
}
```

复制代码
#### onPause


在音频 pause 后的回调事件


**示例：**


```

audioPlayer.onPause = () => {
  console.log("pause")
}
```

复制代码
#### onStop


在音频 stop 后的回调事件


**示例：**


```

audioPlayer.onStop = () => {
  console.log("stop")
}
```

复制代码
#### onEnded


播放结束时的回调事件


**示例：**


```

audioPlayer.onEnded = () => {
  console.log("ended")
}
```

复制代码
#### onError


播放发生错误时的回调事件


**回调返回：**


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| data | string | 错误说明 |
| code | [ErrorCode](#errorcode) | 错误码 |


**示例：**


```

audioPlayer.onError = (data, code) => {
  console.log(`data = ${data} code = ${code}`)
}
```

复制代码
#### onTimeUpdate


在 `currentTime` 属性更新时会触发的回调事件


**示例：**


```

audioPlayer.onTimeUpdate = () => {
  console.log("timeUpdate")
}
```

复制代码
#### onDurationChange


在 `duration` 属性更新时被触发的回调事件


**示例：**


```

audioPlayer.onDurationChange = () => {
  console.log("durationChange")
}
```

复制代码
#### onPrevious


音乐面板点击上一首按钮时触发


**示例：**


```

audioPlayer.onPrevious = () => {
  console.log("播放上一首")
}
```

复制代码
#### onNext


音乐面板点击下一首按钮时触发


**示例：**


```

audioPlayer.onNext = () => {
  console.log("播放下一首")
}
```

复制代码
#### onLoadedData


第一次获取到音频数据的回调事件


**示例：**


```

audioPlayer.onLoadedData = () => {
  console.log("loadedData")
}
```

复制代码
#### onInterrupt


音频打断事件，当前音频被其他有相同音频类型的音频抢夺时，被停止或者恢复的通知。或者当前音频被当外部设备操作打断的通知。


**回调返回：**


| 类型 | 说明 |
| --- | --- |
| [InterruptAction](#interruptaction) | 打断事件信息 |


**示例：**


```

audioPlayer.onInterrupt = function (interruptAction) {
  console.log(interruptAction.interruptHint)
}
```

复制代码
### AudioTrack


#### play()


开始播放音频


**参数：** 无


**示例：**


```

audioTrack.play()
```

复制代码
#### write(OBJECT)


写入音频数据。


> 
> 请确保在调用 `write()` 之前先调用 `play()`，否则写入的数据不会被处理或播放。
> 
> 
> 


**参数**


| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 写入的二进制音频数据 |
| success | Function | 否 | 成功函数，通过该回调函数通知写入的情况 |
| fail | Function | 否 | 失败函数 |


**success 返回值：**


| 类型 | 说明 |
| --- | --- |
| number | 表示写入成功的字节数，若返回的字节数为0 ，表示音频缓冲区已写满，建议等待后再次写入。 |


**fail 返回值：**


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | 写入失败 |


**示例：**


```

audioTrack.write({
  buffer: new ArrayBuffer(16),
  success(writtenBytes) {
    console.log(`written success writtenBytes=${writtenBytes}`)
  },
  fail(data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### pause()


暂停播放音频


**参数：** 无


**示例：**


```

audioTrack.pause()
```

复制代码
#### stop()


停止音频播放，可以通过 play 重新播放音频


**参数：** 无


**示例：**


```

audioTrack.stop()
```

复制代码
#### release()


释放音频资源


**参数：** 无


**示例：**


```

audioTrack.release()
```

复制代码
#### state `只读`


读取该属性可获得播放状态，分别为'play', 'pause', 'stop'


**示例：**


```

let state = audioTrack.state
console.log(state)
```

复制代码
#### onPlay


在音频 play 后的回调事件


**示例：**


```

audioTrack.onPlay = () => {
  console.log('play')
}
```

复制代码
#### onStop


在音频 stop 后的回调事件


**示例：**


```

audioTrack.onStop = () => {
  console.log('stop')
}
```

复制代码
#### onPause


在音频 pause 后的回调事件


**示例**：


```

audioTrack.onPause = () => {
  console.log('pause')
}
```

复制代码
#### onError


播放发生错误时的回调事件


**回调返回：**


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| data | string | 错误说明 |
| code | [ErrorCode](#errorcode) | 错误码 |


**示例：**


```

audioTrack.onError = (data, code) => {
  console.log(`data = ${data} code = ${code}`)
}
```

复制代码
#### onInterrupt


音频打断事件，当前音频被其他有相同音频类型的音频抢夺时，被停止或者恢复的通知。或者当前音频被当外部设备操作打断的通知。


**回调返回：**


| 类型 | 说明 |
| --- | --- |
| [InterruptAction](#interruptaction) | 打断事件信息 |


**示例：**


```

audioPlayer.onInterrupt = function (interruptAction) {
  console.log(interruptAction.interruptHint)
}
```

复制代码
### AudioRecorder


#### start(OBJECT)


开始录音，并在录音结束后生成音频文件。


**参数：**


| 属性名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 需要输出到文件的 uri |
| success | Function | 是 | 成功的回调 |
| fail | Function | 是 | 失败的回调 |
| complete | Function | 是 | 执行结束后的回调 |


**success 返回值：**


| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| uri | String | 录音文件的存储路径 |


**示例：**


```

audioRecorder.start({
  uri: 'internal://cache/file.mp3',
  success: function (data) {
    console.log(`handling success: ${data.uri}`)
  },
  fail: function (data, code) {},
})
```

复制代码
#### read(OBJECT)


开始录音，录音的过程中实时返回音频内容。


注意：read 也是开始录音，不要再调用 start。


**参数：**


| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 否 | 回调函数 |


**callback 返回值：**


| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 录音内容 |


**示例：**


```

audioRecorder.read({
  callback(buffer) {
    console.log('buffer.byteLength: ' + buffer.byteLength)
  },
})
```

复制代码
#### stop()


停止录音。


**参数：** 无


**示例：**


```

audioRecorder.stop()
```

复制代码
#### release()


释放录音资源。


**参数：** 无


**示例：**


```

audioRecorder.release()
```

复制代码
#### onError


录音发生错误时的回调事件


**回调返回：**


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| data | string | 错误说明 |
| code | [ErrorCode](#errorcode) | 错误码 |


**示例：**


```

audioRecorder.onError = (data, code) => {
  console.log(`data = ${data} code = ${code}`)
}
```

复制代码
#### onStart


录音开始时的回调事件


**示例：**


```

audioRecorder.onStart = () => {
  console.log(`start`)
}
```

复制代码
#### onStop


录音停止时的回调事件


**示例：**


```

audioRecorder.onStop = () => {
  console.log(`stop`)
}
```

复制代码
### StreamUsage


音频类型枚举值 ，取值为 `string` 类型，默认值为`music`。用于对音频冲突的仲裁，多个相同的`streamUsage`音频同时播放时，系统只会保留一个，其他的会被打断。


| 取值 | 权限限制 | 说明 |
| --- | --- | --- |
| system | 仅系统应用可用 | 系统消息 |
| ring | 仅系统应用可用 | 电话响铃或短信提示 |
| music | 无 | 媒体 |
| voicecall | 仅系统应用可用 | 通话 |
| alarm | 仅系统应用可用 | 闹钟 |
| notification | 仅系统应用可用 | 通知 |
| game | 仅系统应用可用 | 游戏 |
| tts | 仅系统应用可用 | 文本语音播报 |
| sportbroadcast | 仅系统应用可用 | 运动播报 |
| navigation | 仅系统应用可用 | 导航 |


### ContentType


音频后处理枚举值，取值为 `string` 类型，默认值为`music`。系统会根据不同的 `contentType` 对声音进行优化处理。


| 取值 | 说明 |
| --- | --- |
| speech | 语音播报 |
| music | 音乐播放 |
| movie | 视频播放/电视节目 |
| sonification | 按键音/游戏中的短音提示/拟音 |


### StreamType


音量策略枚举值，取值为 `string` 类型，默认值为`music`。系统可以通过不同的 `streamType` 来管理音频的音量，例如：播放音乐设置为 `music`，消息提示音设置为 `ring` 。


| 名称 | 权限限制 | 说明 |
| --- | --- | --- |
| system | 仅系统应用可用 | 系统消息 |
| ring | 仅系统应用可用 | 电话响铃或短信提示 |
| music | 无 | 媒体 |
| voicecall | 仅系统应用可用 | 通话 |
| alarm | 仅系统应用可用 | 闹钟 |
| notification | 仅系统应用可用 | 通知 |
| bluetoothsco | 仅系统应用可用 | 蓝牙通话 |
| tts | 仅系统应用可用 | 文本语音播报 |
| sportbroadcast | 仅系统应用可用 | 运动播报 |
| force | 仅系统应用可用 | 忽视静音策略，强制最大音量播放 |


### InterruptAction


音频打断对象


| 属性 | 类型 | 说明 |
| --- | --- | --- |
| interruptHint | number | 1 - 音频恢复 （如：来电恢复）2 - 音频暂停，可以恢复 （如：来电打断）3 - 音频停止，不会再恢复（如：彻底停止）4 - 音频被拒绝（如：来电时播放音乐） |
| actionType | number | 事件返回类型。0 - 被音频抢夺，焦点触发事件1 - 音频被外部设备打断事件，如蓝牙耳机连接。 |


**示例：**


```

{
  "interruptHint": 2,
  "actionType": 0
}
```

复制代码
### ErrorCode


错误码的枚举，枚举值的类型为 number


| 枚举值 | 对应的 data 信息 | 说明 |
| --- | --- | --- |
| 201 | No Permission | 表示无权限执行此操作，需要申请权限或者用户授权。 |
| 202 | Invalid Parameters | 参数无效 。 |
| 100001 | Insufficient Memory or Service Limit Reached | 表示系统内存不足或服务数量达到上限 。 |
| 100002 | Operation Not Allowed | 表示当前状态不允许或无权执行此操作 。 |
| 100003 | I/O error. | 表示出现IO错误。 |
| 100004 | System or Network Timeout | 表示系统或网络响应超时 。录音暂无此错误。 |
| 100005 | Service Process Terminated | 表示服务进程死亡。 |
| 100006 | Unsupported Format | 表示不支持当前媒体资源的格式。 |
| 100007 | Audio interrupted. | 表示音频焦点被抢占 。 |


---


<!-- 文档 42: js-api/system/multimediaOverview/.md -->


## 概述

## 概述

更新时间：2023-10-29 18:27:39


蓝河应用多媒体能力支持音频业务的开发，提供音频相关的功能，主要包括音频播放、音频流式播放、录音、音量管理等。


### 子模块介绍


| 模块 | 简述 |
| --- | --- |
| 音频 | 提供音频播放能力 |
| 多媒体 | 提供音频播放、音频流式播放、录音能力 |
| 音频管理 | 提供音量设置，音量获取、监听等音频管理能力 |
| 录音 | 提供录音能力 |


---


<!-- 文档 43: js-api/system/network/.md -->


## 网络状态

## 网络状态

更新时间：2024-10-11 11:55:18


### 接口声明


```

{ "name": "blueos.network.networkManager" }
```

复制代码
### 导入模块


```

import network from '@blueos.network.networkManager' 或 const network = require('@blueos.network.networkManager')
```

复制代码
### 接口定义


#### network.getType(OBJECT)


获取网络类型


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调，可能是因为缺乏权限 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| type | String | 网络类型，可能的值为 2g，3g，4g，wifi，none，5g，bluetooth，others |


##### 示例：


```

network.getType({
  success(data) {
    console.log(`handling success: ${data.type}`)
  },
})
```

复制代码
#### network.subscribe(OBJECT)


监听网络连接状态。如果多次调用，仅最后一次调用生效


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reserved | Boolean | 否 | 是否持久化订阅，默认为 false。机制：设置为 true，页面跳转，不会自动取消订阅，需手动取消订阅 |
| callback | Function | 否 | 每次网络发生变化，都会被回调 |
| fail | Function | 否 | 失败回调，可能是因为缺乏权限 |


###### callback 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| type | String | 网络类型，可能的值为 2g，3g，4g，wifi，none，5g，bluetooth，others |


##### 示例：


```

network.subscribe({
  callback: (data) => {
    console.log('handling callback')
  },
})
```

复制代码
#### network.unsubscribe()


取消监听网络连接状态


##### 参数：


无


##### 示例：


```

network.unsubscribe()
```

复制代码
#### network.getSimOperators(OBJECT)


获取 Sim 卡的运营商信息，即将废弃，改用 @blueos.telephony.simManager.getSimOperators()


##### 权限要求


电话权限


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| operators | Array | SIM 卡列表信息 |
| size | Number | Sim 卡数量 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 201 | 用户拒绝，获取电话权限失败 |
| 207 | 用户拒绝并勾选不再询问复选框 |
| 1001 | 未插入 sim 卡 |
| 1002 | 获取运营商信息失败 |


###### SIM 卡列表项参数：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| operator | String | 返回 Sim 卡的运营商信息运营商信息说明：此处统一返回 MCC+MNC，即移动国家代码 + 移动网络代码；中国移动：46000，46002，46004，46007；中国联通：46001，46006，46009；中国电信：46003，46005，46011； [其余 MCC+MNC](https://www.mcc-mnc.com/ ) |
| slotIndex | Number | 卡槽序号 |


##### 示例：


```

network.getSimOperators({
  success(data) {
    console.log(`size: ${data.size}`)
    for (const i in data.operators) {
      console.log(`operator: ${data.operators[i].operator},
 slotIndex:${data.operators[i].slotIndex},
 isDefaultDataOperator:${data.operators[i].isDefaultDataOperator},`)
    }
  },
  fail(data, code) {
    console.log(`handling fail, code = ${code}, errorMsg=${data}`)
  },
})
```

复制代码


---


<!-- 文档 44: js-api/system/notification/.md -->


## 消息通知

## 消息通知

更新时间：2024-09-02 20:54:40


### 接口声明


```

{ "name": "blueos.app.notification.notificationManager" }
```

复制代码
### 导入模块


```

import notification from '@blueos.app.notification.notificationManager' 或 const notification = require('@blueos.app.notification.notificationManager')
```

复制代码
### 接口定义


#### notification.publish(OBJECT)


发布通知


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [Notification](#Notification) | 是 | 消息通知对象 |
| success | Function | 是 | 成功的回调 |
| fail | Function | 是 | 失败的回调 |
| complete | Function | 是 | 执行结束后的回调 |


###### Notification


说明如下：


| 参数名 | 类型 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- | --- |
| icon | string | 是 | - | 通知小图标，应用下以 src 为根目录的图片的绝对路径 |
| id | number | 否 | - | 应用通知的唯一 id |
| appName | string | 否 | - | 应用名称 |
| contentType | number | 是 | - | 正文类型。 1：普通文本通知类型。 2：图片通知类型 |
| content | [Content](#Content) | 是 | - | 通知内容 与 contentType 对应 |
| channel | number | 是 | - | 通知来源 , 1：PHONE；2：WATCH\_APP |
| platform | string | 否 | - | 消息渠道来源 (PHONE 时) iOS | Andriod |
| deliveryTime | number | 是 | - | 通知发送时间，格式为毫秒时间戳 |
| actionButtons | Array<[ActionButton](#ActionButton)> | 否 | - | 通知按钮，最多两个按钮 |
| largeIcon | string | 否 | - | 通知大图标，应用下以 src 为根目录的图片的绝对路径 |
| isUnremovable | boolean | 否 | false | 是否不可清除 |
| badge | number | 否 | - | 数字角标(消息合并情况下) |
| appBundleName | string | 否 | - | 应用包名 ，格式 com.xxx.xxx，该字段的值应由 native 填充 |
| group | string | 否 | - | 消息分组 |
| extraInfo | {[key: string]: any} | 否 | - | 扩展参数 |


###### Content


普通文本通知类型


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 普通文本通知标题 |
| text | string | 是 | 普通文本通知内容 |
| additionalText | string | 否 | 可选参数，普通文本通知附加信息 |


图片通知类型


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 通知标题 |
| text | string | 是 | 通知内容 |
| additionalText | string | 否 | 可选参数，通知附加信息 |
| briefText | string | 是 | 图片文本通知简略内容 |
| expandedTitle | string | 是 | 图片通知扩展标题 |
| picture | string | 是 | 图片通知的图片，应用下以 src 为根目录的图片的绝对路径 |


###### ActionButton


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 是 | 按钮标题 |
| action | [Action](#Action) | 是 | 点击按钮时触发的动作 |
| extras | {[key: string]: any} | 否 | 扩展参数 |


###### Action


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| triggerMethod | string | 否 | 定义按钮点击触发的回调函数, 需要在 app.ux 中定义 |
| prameters | {[key: string]: any} | 否 | 自定义参数，供回调函数使用 |


##### 示例：


```

notification.publish({
  request: {
    icon: '/assets/images/icon.png',
    contentType: 1,
    content: {
      title: '收件通知',
      text: '门口xx收件，收件码：XXX',
    },
    channel: 1,
    deliveryTime: Date.now(),
  },
  success: function () {},
  fail: function () {},
  complete: function () {},
})
```

复制代码
#### notification.remove(OBJECT)


清除消息通知


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](#Query) | 是 | 清除的查询条件，如果条件为空则全部清除 |
| success | Function | 是 | 成功的回调 |
| fail | Function | 是 | 失败的回调 |
| complete | Function | 是 | 执行结束后的回调 |


###### Query 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 否 | 应用通知的唯一 id |
| group | string | 否 | 通知的分组 |


##### 示例：


```

notification.remove({
  query: {
    group: 'group1',
  },
  success: function () {},
  fail: function () {},
  complete: function () {},
})
```

复制代码


---


<!-- 文档 45: js-api/system/package/.md -->


## 包管理

## 包管理

更新时间：2025-10-09 11:25:10


### 接口声明


```

{ "name": "blueos.package.packageManager" }
```

复制代码
### 导入模块


```

import packageManager from '@blueos.package.packageManager' 或 const packageManager = require('@blueos.package.packageManager')
```

复制代码
### 接口定义


#### hasInstalled()


检测应用是否存在


##### 参数


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| package | String | 是 | 应用包名，如:com.vivo.music |
| moduleName | string | type 为 widget 时必填 | 卡片的 moduleName，manifest 中 widget 的 key，如：widgets/widget |
| type | "widget" | "package" | 否 | 默认值为 package，package 表示普通应用，widget 表示卡片 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


##### success 返回值


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| result | boolean | 应用是否存在 |


##### 示例


```

packageManager.hasInstalled({
  package: 'com.hap.app',
  moduleName: 'widgets/widget1',
  type: 'widget',
  success(data: { result: boolean }) {
    console.log(`handling success: ${data.result}`)
  },
  fail(data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### getCustomData()


读取当前应用在 manifest 中定义的 customData


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |


###### success 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| data | Record<string, string> | 开发者在 manifest 中定义的 customData |


##### 示例：


```

packageManager.getCustomData({
  success(response) {
    console.log(`handling success: ${response.data}`)
  },
  fail(data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码


---


<!-- 文档 46: js-api/system/pagestack/.md -->


## 页面栈管理

## 页面栈管理

更新时间：2024-10-11 11:55:18


### 接口声明


```

{ "name": "blueos.app.appmanager.pageStack" }
```

复制代码
### 导入模块


```

 import pagestack from '@blueos.app.appmanager.pageStack' 或 const pagestack = require('@blueos.app.appmanager.pageStack')
```

复制代码
### 接口定义


#### pagestack.getAppStacks(OBJECT)


获取应用页面栈信息


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| package | Array|String | 否 | 应用包名。 默认不传获取所有应用的页面栈信息 或 ['com.vivo.app1','com.vivo.app2'] 或 'com.vivo.app1' |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |


##### success 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| appStackPages | `Array<Object>` | 返回调用方页面栈信息 |


##### 所有应用 appStackPages 数据格式示例：


```

appStackPages：[
 {
   appInfo:{zIndex:1,package:'com.vivo.app'},
   pages:[{pageId:1,path:'pages/index/index'}]
 },
 null,
 null
]
```

复制代码
###### 根据传入应用包名的顺序返回页面栈信息


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| appInfo | Object | 应用信息 |
| pages | `Array<Object>` | 应用页面栈信息 |


某个应用 appInfo 参数详细说明


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| zIndex | Number | 所属应用的层级 |
| package | String | 应用包名 |


某个应用 pages 参数详细说明


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| pageId | Number | 页面的 id |
| path | String | 页面的路径 |


##### 示例：


```

pagestack.getAppStacks({
  package: ['com.vivo.app1', 'com.vivo.app2'],
  success: function (data) {
    const [app1, app2] = data.appStackPages
    //获取某个应用页面栈里面的某个页面id
    let paths1 = [app1 && app1.pages[0].path, app1 && app1.pages[1].path]
    let paths2 = [app2 && app2.pages[0].path, app2 && app2.pages[1].path]
    let pageIds1 = [app1 && app1.pages[0].pageId, app1 && app1.pages[1].pageId]
    let pageIds2 = [app2 && app2.pages[0].pageId, app2 && app2.pages[1].pageId]
    let package1 = app1 && app1.appInfo.package
    let package2 = app2 && app2.appInfo.package
    //根据页面id或页面路径关闭指定页面
    pagestack.close({
      pageList: [
        {
          package: package1, //是
          pageIds: pageIds1, //否
          paths: paths1, //否
        },
        {
          package: package2,
          pageIds: pageIds2,
          paths: paths2,
        },
      ],
      success: function () {},
      fail: function (data, code) {
        console.log(`handling fail,code = ${code}`)
      },
      complete: function () {
        console.log(`handling complete`)
      },
    })
    console.log(`handling success, pages = ${pages}`)
  },
  fail: function (data, code) {
    console.log(`handling fail,code = ${code}`)
  },
  complete: function () {
    console.log(`handling complete`)
  },
})
```

复制代码
#### pagestack.close(OBJECT)


关闭页面


##### 参数


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageList | `Array<Object>` | 是 | 关闭应用的配置项 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |


##### pageList 参数详细


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| package | String | 是 | 应用包名 |
| pageIds | Array | 否 | 页面 id |
| paths | Array | 否 | 页面路径 |


##### 示例：


```

pagestack.close({
  pageList: [
    {
      package: 'com.vivo.app',
      pageIds: [1],
      paths: ['/pages/index/index'],
    },
  ],
  success: function () {},
  fail: function (data, code) {
    console.log(`handling fail,code = ${code}`)
  },
  complete: function () {
    console.log(`handling complete`)
  },
})
```

复制代码


---


<!-- 文档 47: js-api/system/peaceOverview/.md -->


## 概述

## 概述

更新时间：2023-10-29 18:27:39


蓝河应用安全模块旨在确保应用程序的数据和用户信息得到有效的保护，以防止未经授权的访问和数据泄漏。


### 子模块介绍


| 模块 | 简述 |
| --- | --- |
| 权限管理 | 提供全面的权限控制和管理功能，以确保应用的安全性和隐私保护 |
| 密码算法 | 为应用提供了安全数据加密和解密的功能，以确保用户的敏感信息得到保护 |


---


<!-- 文档 48: js-api/system/permission/.md -->


## 权限管理

## 权限管理

更新时间：2024-10-11 11:55:18


### 权限列表


#### watch.permission.LOCATION


**说明：** 位置信息


**模块：** @blueos.hardware.geolocation


- geolocation.getLocation(OBJECT)
- geolocation.subscribe(OBJECT)
- geolocation.unsubscribe()


**错误码：**


- 400 : 拒绝授予权限
- 402: 权限错误（未声明该权限）


#### watch.permission.STEP\_COUNTER


**说明：** 计步传感器


**模块：** @blueos.hardware.sensor


- sensor.subscribeStepCounter(OBJECT)


**错误码：**


- 400 : 拒绝授予权限
- 402: 权限错误（未声明该权限）


#### watch.permission.DEVICE\_INFO


**说明：** 设备信息


**模块：** @blueos.hardware.device


- device.getId(OBJECT)
- device.getDeviceId(OBJECT)
- device.getSerial(OBJECT)


**错误码：**


- 400: 拒绝授予权限
- 402: 权限错误（未声明该权限）


#### watch.permission.RECORD


**说明：** 录音


**模块 1：** @blueos.multimedia.record


- record.start(OBJECT)
- record.stop(OBJECT)
- record.release(OBJECT)


**模块 2：** @blueos.media.audio.mediaManager


- media.createAudioRecord()


**错误码：**


- 400: 拒绝授予权限
- 401: 敏感权限不能在后台运行
- 402: 权限错误（未声明该权限）


#### watch.permission.BLUETOOTH


**说明：** 允许使用设备蓝牙


**模块 1：** @blueos.communication.bluetooth.bluetooth / @vivo.bluetooth


- bluetooth.getBindState()
- bluetooth.startBind(OBJECT)
- bluetooth.confirmBind(OBJECT)
- bluetooth.cancelBind(OBJECT)
- bluetooth.startDevicesDiscovery(OBJECT)
- bluetooth.onDevicefound = function(data)
- bluetooth.stopDevicesDiscovery(OBJECT)
- bluetooth.getConnectedDevices(OBJECT)
- bluetooth.getPairedDevices(OBJECT)
- bluetooth.createConnection(OBJECT)
- bluetooth.closeConnection (OBJECT)
- bluetooth.pair(OBJECT)
- bluetooth.unpair(OBJECT)
- bluetooth.subscribeBind(OBJECT)
- bluetooth.clearBindData(OBJECT)
- bluetooth.replyPhone(OBJECT)
- bluetooth.onadapterstatechange = function(data)


**模块 2：** @blueos.bluetooth.ble


- createGattClientDevice
- createGattServer
- getConnectedBLEDevices
- getLeMaximumAdvertisingDataLength
- startBLEScan
- stopBLEScan
- subscribeBLEDeviceFind
- unsubscribeBLEDeviceFind


**错误码：**


- 400 : 拒绝授予权限,
- 402: 权限错误（未声明该权限）


#### watch.permission.READ\_HEALTH\_DATA


**说明：** 读取健康数据


**模块：** @blueos.health.healthManager / @vivo.health


- health.getRecentSamples(Object)
- health.subscribeSample(Object)
- health.unsubscribeSample(Object)
- health.getTodayStatistic(Object)
- health.subscribeTodayStatistic(Object)
- health.unsubscribeTodayStatistic(Object)


**错误码：**


- 400 : 拒绝授予权限,
- 402: 权限错误（未声明该权限）


#### watch.permission.PLACE\_CALL


**说明：** 拨打电话


**模块：** @blueos.telephony.call


**错误码：**


- 400 : 拒绝授予权限,
- 402: 权限错误（未声明该权限）


#### watch.permission.SEND\_MESSAGES


**说明：** 发送短信


**模块：** @blueos.telephony.sms


**错误码：**


- 400 : 拒绝授予权限,
- 402: 权限错误（未声明该权限）


---


<!-- 文档 49: js-api/system/phoneOverview/.md -->


## 概述

## 概述

更新时间：2023-10-31 16:42:47


蓝河应用的电话能力模块的多功能性使其成为实现通信和互动的强大工具。它为应用提供了多种通信方式，可以通过短信进行信息传递以及通过电话进行语音通话，满足不同用户需求。这对于社交应用、通讯工具、客户服务和多种应用场景都具有广泛的适用性。


#### 子模块介绍


| 模块 | 简述 |
| --- | --- |
| 短信 | 提供了短信服务集成和短信功能实现支持 |
| 打电话 | 提供了电话通信支持，以满足用户的通话需求 |


---


<!-- 文档 50: js-api/system/prompt/.md -->


## 弹窗

## 弹窗

更新时间：2023-10-30 10:12:45


### 接口声明


```

{ "name": "blueos.window.prompt" }
```

复制代码
### 导入模块


```

import prompt from '@blueos.window.prompt' 或 const prompt = require('@blueos.window.prompt')
```

复制代码
### 接口定义


#### prompt.showToast(OBJECT)


显示 Toast


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | String | 是 | 要显示的文本 |
| duration | Number | 否 | 0 为短时，1 为长时，默认 0 |


##### 示例：


```

prompt.showToast({
  message: 'message',
})
```

复制代码


---


<!-- 文档 51: js-api/system/record/.md -->


## 录音

## 录音

更新时间：2024-09-02 14:53:40


### 接口声明


```

{ "name": "blueos.media.audio.audioRecorder" }
```

复制代码
### 导入模块


```

import record from '@blueos.media.audio.audioRecorder' 或 const record = require('@blueos.media.audio.audioRecorder')
```

复制代码
### 接口定义


#### record.start(OBJECT)


开始录音。默认录制为 PCM 格式，16000 采样率，16bit 位宽，2 通道。


##### 权限要求


录音


##### 开发者需要在 manifest.json 里面配置权限：


```

{
  "permissions": [{ "name": "watch.permission.RECORD" }]
}
```

复制代码
##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 是 | 成功的回调 |
| fail | Function | 是 | 失败的回调 |
| complete | Function | 是 | 执行结束后的回调 |


###### success 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| uri | String | 录音文件的存储路径，在应用的缓存目录中 |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 400 | 拒绝授予权限 |
| 401 | 敏感权限不能在后台运行 |
| 402 | 权限错误（未声明该权限） |


##### 示例：


```

record.start({
  success: function (data) {
    console.log(`handling success: ${data.uri}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}, errorMsg=${data}`)
  },
})
```

复制代码
#### record.stop(OBJECT)


停止录音。


##### 参数：


无


##### 示例：


```

record.stop()
```

复制代码

#### record.release(OBJECT)


释放录音资源。


##### 参数：


无


##### 示例：


```

record.release()
```

复制代码
#### 事件


| 名称 | 描述 |
| --- | --- |
| Error | 录音发生错误时的回调事件 |
| Start | 录音开始时的回调事件 |
| Stop | 录音停止时的回调事件 |


##### 示例：


```

record.onError = function () {
  console.log(`audio error`)
}
```

复制代码


---


<!-- 文档 52: js-api/system/request/.md -->


## 上传下载

## 上传下载

更新时间：2025-08-13 20:11:57


### 接口声明


```

{ "name": "blueos.network.request" }
```

复制代码
### 导入模块


```

import request from '@blueos.network.request' 或 const request = require('@blueos.network.request')
```

复制代码
### 接口定义


#### request.upload(OBJECT)


上传文件


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | String | 是 | 资源 url |
| header | Object | 否 | 请求的 header，会将其所有属性设置到请求的 header 部分。 |
| method | String | 否 | 默认为 POST，可以是： POST, PUT |
| files | Array | 是 | 需要上传的文件列表，使用 multipart/form-data 方式提交 |
| data | Array | 否 | HTTP 请求中其他额外的 form data |
| success | Function | 否 | 成功返回的回调函数 |
| fail | Function | 否 | 失败的回调函数 |
| complete | Function | 否 | 结束的回调函数（调用成功、失败都会执行） |


**files 参数 ：**


files 参数是一个 file 对象的数组，file 对象的结构如下：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filename | String | 否 | multipart 提交时，header 中的文件名 |
| name | String | 否 | multipart 提交时，表单的项目名，默认 file |
| uri | String | 是 | 只能为应用沙箱内 internal 目录 |
| type | String | 否 | 文件的 Content-Type 格式，默认会根据 filename 或者 uri 的后缀获取 |


**data 参数 ：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | String | 是 | form 元素的名称。 |
| value | String | 是 | form 元素的值。 |


**success 返回值：**


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| code | Integer | 服务器状态 code |
| data | String | 如果服务器返回的 header 中 type 是 text/\*或 application/json、application/javascript、application/xml，值是文本内容，否则是存储的临时文件的 uri 临时文件如果是图片或者视频内容，可以将图片设置到 image 或 video 控件上显示 |
| headers | Object | 服务器 response 的所有 header |


**示例：**


```

request.upload({
  url: 'http://www.example.com',
  files: [
    {
      uri: 'internal://xxx/xxx/test',
      name: 'file1',
      filename: 'test.png',
    },
  ],
  data: [
    {
      name: 'param1',
      value: 'value1',
    },
  ],
  success: function (data) {
    console.log('handling success')
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### request.download(OBJECT)


下载文件


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | String | 是 | 资源 url |
| header | String | 否 | 请求的 header，会将其所有属性设置到请求的 header 部分。 |
| description | String | 否 | 下载描述，会用于通知栏标题。默认为文件名 |
| filename | String | 否 | 在下载文件时，可以提供文件名或文件 URI。当输入文件 URI（internal://xxx）时，可定义下载路径；而若输入文件名，则会默认保存至缓存目录（internal://cache/）。若未提供文件信息，系统将从网络请求或 URL 中获取文件名。 |
| success | Function | 否 | 成功返回的回调函数 |
| fail | Function | 否 | 失败的回调函数 |
| complete | Function | 否 | 结束的回调函数（调用成功、失败都会执行） |


**success 返回值：**


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| token | String | 下载的 token，根据此 token 获取下载状态 |


**fail 返回错误代码：**


| 错误码 | 说明 |
| --- | --- |
| 302 | 存储空间不足 |


**示例：**


```

request.download({
  url: 'http://www.example.com',
  success: function (data) {
    console.log(`handling success${data.token}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### request.abortDownload(OBJECT)


中断下载任务


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | String | 是 | download 接口返回的 token |
| success | Function | 否 | 成功返回的回调函数 |
| fail | Function | 否 | 失败的回调函数 |
| complete | Function | 否 | 结束的回调函数（调用成功、失败都会执行） |


**success 返回值：**


无


**fail 返回错误代码：**


| 错误码　 | 说明 |
| --- | --- |
| 1000 | 中断失败 |
| 1001 | 下载任务不存在 |


**示例：**


```

request.abortDownload({
  token: '123',
  success: function (data) {
    console.log(`abortDownload success`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### request.onDownloadComplete(OBJECT)


监听下载任务


**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | String | 是 | download 接口返回的 token |
| success | Function | 否 | 成功返回的回调函数 |
| fail | Function | 否 | 失败的回调函数 |
| complete | Function | 否 | 结束的回调函数（调用成功、失败都会执行） |


**success 返回值：**


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| uri | String | 下载文件的 uri（默认情况下该文件处于应用缓存目录。如果文件类型为图片或者视频且要求用户可以在相册等应用内查看，则需要将该文件转存至公共目录，参考 media 接口中的方法实现即可） |


**fail 返回错误代码：**


| 错误码　 | 说明 |
| --- | --- |
| 1000 | 下载失败 |
| 1001 | 下载任务不存在 |


**示例：**


```

request.onDownloadComplete({
  token: '123',
  success: function (data) {
    console.log(`handling success${data.uri}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码


---


<!-- 文档 53: js-api/system/router/.md -->


## 页面路由

## 页面路由

更新时间：2024-01-10 16:04:30


### 接口声明


无需声明


### 导入模块


```

import router from '@blueos.app.appmanager.router' 或 const router = require('@blueos.app.appmanager.router')
```

复制代码
### 接口定义


#### router.push(OBJECT)


跳转到应用内的某个页面。


##### 参数：


| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | String | 是 | 要跳转到的 uri，可以是下面的格式：1. 以"/"开头的应用内页面的路径；例：/about。2. 以非"/"开头的应用内页面的名称；例：About。3. 特殊的，如果 uri 的值是"/"，则跳转到 path 为"/"的页，没有则跳转到首页 |
| params | Object | 否 | 跳转时需要传递的数据；跳转到蓝河应用页面时，参数可以在目标页面中通过`this.param1`的方式使用，param1 为 json 中的参数名，param1 对应的值会统一转换为 String 类型。 |
| transition | Object | 否 | 设置当前跳转的转场动画，优先级高于 `router.setTransition` |


##### transition 参数说明


| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| forward | Object | 否 | 路由进入页面时的动效 |
| back | Object | 否 | 路由返回页面时的动效 |


##### forward、back 参数说明


| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exit | [TransitionAnimation](#transitionanimation) | 否 | 即将退出的页面动画 |
| enter | [TransitionAnimation](#transitionanimation) | 否 | 即将出现的页面动画 |


##### 示例：


- 应用内切换页面


	- path 切换
	
	
	
	```

	router.push({
	  uri: '/about',
	  params: {
	    testId: '1',
	  },
	})
	```

	复制代码
	- name 切换
	
	
	
	```

	// open page by name
	router.push({
	  uri: 'About',
	  params: {
	    testId: '1',
	  },
	})
	```

	复制代码
- 打开另一个应用


	- 指定 deeplink 打开
	
	
	
	```

	router.push({
	  uri: 'hap://app/com.vivo.bind/pages/bindmain?key=value',
	})
	```

	复制代码


#### router.replace(OBJECT)


跳转到应用内的某个页面，当前页面无法返回


##### 参数：


| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | String | 是 | 要跳转到的 uri，可以是下面的格式：1. 以"/"开头的应用内页面的路径；例：/about。
2. 以非"/"开头的应用内页面的名称;例：About。
3. 特殊的，如果 uri 的值是"/"，则跳转到 path 为"/"的页，没有则跳转到首页
 |
| params | Object | 否 | 跳转时需要传递的数据，参数可以在目标页面中通过`this.param1`的方式使用，param1 为 json 中的参数名，param1 对应的值会统一转换为 String 类型。 |


##### 示例：


```

router.replace({
  uri: '/test',
  params: {
    testId: '1',
  },
})
```

复制代码
#### router.back()


返回上一页面


##### 示例：


```

// A页面，open page by name
router.push({
  uri: 'B',
})
// B页面，open page by name
router.push({
  uri: 'C',
})
// C页面，open page by name
router.push({
  uri: 'D',
})
// D页面，open page by name
router.push({
  uri: 'E',
})
// E页面返回至D页面
router.back()
// D页面返回至C页面
router.back()
```

复制代码
#### router.clear()


清空所有历史页面记录，仅保留当前页面（即保留栈顶页面）


##### 参数：


无


##### 示例：


```

router.clear()
```

复制代码
#### router.getState()


获取当前页面状态


##### 返回参数：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| index | Number | 当前页面在页面栈中的位置 |
| name | String | 当前页面的名称 |
| path | String | 当前页面的路径 |


##### 示例：


```

const page = router.getState()
console.log(`page index = ${page.index}`)
console.log(`page name = ${page.name}`)
console.log(`page path = ${page.path}`)
```

复制代码
#### router.setTransition(OBJECT)


设置应用默认转场动画


##### 参数：


| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| forward | Object | 否 | 路由进入页面时的动效 |
| back | Object | 否 | 路由返回页面时的动效 |


##### forward、back 参数说明：


| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exit | [TransitionAnimation](#transitionanimation) | 否 | 即将退出的页面动画 |
| enter | [TransitionAnimation](#transitionanimation) | 否 | 即将出现的页面动画 |


##### 示例：


```

router.setTransition({
  forward: {
    enter: 'fadeIn',
    exit: 'fadeOut',
  },
  back: {
    enter: 'fadeIn',
    exit: 'fadeOut',
  },
})
```

复制代码
#### TransitionAnimation


支持别名内置动画


##### 动效别名表


系统提供内置动画，类型为 String。


| 别名 | 适用情况 | 描述 |
| --- | --- | --- |
| slideInLeft | 打开页面 | 左侧滑入 |
| slideOutRight | 关闭页面 | 右侧滑出 |
| fadeIn | 打开页面 | 淡入 |
| fadeOut | 关闭页面 | 淡出 |
| none | 打开/关闭页面 | 无动效，瞬间显示/瞬间隐藏 |
| zoomIn | 打开/关闭页面 | 放大 |
| zoomOut | 打开/关闭页面 | 缩小 |


---


<!-- 文档 54: js-api/system/schedule/.md -->


## 定时任务

## 定时任务

更新时间：2024-09-14 16:42:27


### 接口声明


```

{ "name": "blueos.app.appmanager.schedule" }
```

复制代码
### 导入模块


```

import schedule from '@blueos.app.appmanager.schedule' 或 const schedule = require('@blueos.app.appmanager.schedule')
```

复制代码
### 接口定义


#### schedule.scheduleJob(OBJECT)


设置定时任务


###### 参数：


| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | Number | 是 | `1` 硬件时间，`2` 真实时间流逝，前者可以通过修改系统时间触发`triggerMethod`，后者要通过真实时间的流逝，即使在休眠状态，时间也会被计算 |
| timeout | long | 是 | 若 `type` 为 `1`，则为首次执行时间的时间戳，即从 1970/01/01 00:00:00 GMT 到当前时间的毫秒数；若 `type` 为 `2`，则为当前时间距离首次执行时间的间隔，单位毫秒。 |
| triggerMethod | String | 是 | app.ux 中定义的方法名，由后台拉起时调用 |
| interval | long | 否 | 周期性执行的间隔，毫秒为单位，不传就不重复执行 |
| params | Object | 否 | 任务参数 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


##### 说明


1. 首次执行时间可设置为过去的时间
2. 若首次执行时间为过去时间，已过期的任务将不会被执行，未过期的任务仍然会被执行


##### 返回值：


| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| id | Integer | 底层分配唯一的 ID |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| -27 | 定时任务已满 |
| -28 | 已注册 |


##### 示例：


```

// xx.ux
schedule.scheduleJob({
  type: 1,
  timeout: new Date('2050-10-01 09:00:00').getTime(),
  interval: 1000,
  triggerMethod: 'scheduleFunc',
  params: {
    color: 'red',
  },
  success: function (data) {
    console.log(`handling success, scheduleId = ${data.id}`)
  },
  fail: function (data, code) {
    console.log(`handling fail,code = ${code}`)
  },
  complete: function () {
    console.log(`handling complete`)
  },
})

// app.ux
export default {
  scheduleFunc(params) {
    console.log(`background processing color = ${params.color}`)
  },
}
```

复制代码
#### schedule.cancel(id: Integer)


取消定时任务


##### 参数：


| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| id | Integer | 底层分配唯一的 ID |


##### 返回值：


| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| value | Boolean | true：成功； false：失败； |


##### 示例：


```

schedule.cancel(1)
```

复制代码


---


<!-- 文档 55: js-api/system/screen/.md -->


## 屏幕管理

## 屏幕管理

更新时间：2023-12-25 11:01:05


### 接口声明


```

{ "name": "blueos.hardware.display.screen" }
```

复制代码
### 导入模块


```

import screen from '@blueos.hardware.display.screen' 或 const screen = require('@blueos.hardware.display.screen')
```

复制代码
### 接口定义


#### screen.getScreenOffTime()


获取熄屏时间


###### 参数：


无


##### 返回值：


| 类型 | 说明 |
| --- | --- |
| Number | 1-999 秒 |


##### 示例：


```

screen.getScreenOffTime()
```

复制代码
#### screen.getAodStatus()


获取 AOD 状态


> 
> AOD：Always on Display，即不点亮整块屏幕的情况下，控制屏幕局部亮起，将一些重要的信息一直显示在屏幕上。
> 
> 
> 


##### 参数：


无


##### 返回值：


| 类型 | 说明 |
| --- | --- |
| Number | 0: AOD 关闭; 1: AOD 打开 |


##### 示例：


```

screen.getAodStatus()
```

复制代码


---


<!-- 文档 56: js-api/system/sensor/.md -->


## 传感器

## 传感器

更新时间：2024-11-21 17:51:08


### 接口声明


```

{ "name": "blueos.hardware.sensor.sensor" }
```

复制代码
### 导入模块


```

import sensor from '@blueos.hardware.sensor.sensor' 或 const sensor = require('@blueos.hardware.sensor.sensor')
```

复制代码
### 接口定义


#### sensor.subscribeAccelerometer(OBJECT)


订阅加速度传感器数据，如果多次调用，仅最后一次调用生效


**说明：**


- 加速度是重力加速度和设备自身运动加速度的矢量叠加
- 当设备静止或做匀速直线运动时，返回的加速度值表示重力加速度。


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| interval | String | 否 | 监听加速度数据回调函数的执行频率，默认 normal |
| callback | Function | 是 | 加速度感应数据变化后会回调此函数。 |
| fail | Function | 否 | 失败回调 |


###### callback 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| x | Number | x 轴加速度 |
| y | Number | y 轴加速度 |
| z | Number | z 轴加速度 |


interval 的合法值：


| 值 | 说明 |
| --- | --- |
| game | 适用于更新游戏的回调频率，在 20ms/次 左右 |
| ui | 适用于更新 UI 的回调频率，在 60ms/次 左右 |
| normal | 普通的回调频率，在 200ms/次 左右 |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 1000 | 当前设备不支持重力感应传感器 |


##### 示例：


```

sensor.subscribeAccelerometer({
  callback: function (ret) {
    console.log(`handling callback, x = ${ret.x}, y = ${ret.y}, z = ${ret.z}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### sensor.unsubscribeAccelerometer()


取消监听重力感应数据


##### 参数：


无


##### 示例：


```

sensor.unsubscribeAccelerometer()
```

复制代码
#### sensor.subscribeCompass(OBJECT)


监听罗盘数据。如果多次调用，仅最后一次调用生效


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 罗盘数据变化后会回调此函数。 |
| fail | Function | 否 | 失败回调 |


###### callback 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| direction | Number | 表示设备的 y 轴和地球磁场北极之间的角度，当面朝北，角度为 0；朝南角度为 π；朝东角度 π/2；朝西角度-π/2 |
| accuracy | Number | 精度 |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 1000 | 当前设备不支持罗盘传感器 |


| 值 | 说明 |
| --- | --- |
| 3 | 高精度 |
| 2 | 中等精度 |
| 1 | 低精度 |
| -1 | 不可信，传感器失去连接 |
| 0 | 不可信，原因未知 |


##### 示例：


```

sensor.subscribeCompass({
  callback: function (ret) {
    console.log(`handling callback, direction = ${ret.direction}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### sensor.unsubscribeCompass()


取消监听罗盘数据


##### 参数：


无


##### 示例：


```

sensor.unsubscribeCompass()
```

复制代码
#### sensor.subscribeStepCounter(OBJECT)


监听计步传感器数据。如果多次调用，仅最后一次调用生效。


##### 开发者需要在 manifest.json 里面配置权限：


```

{
  "permissions": [{ "name": "watch.permission.STEP\_COUNTER" }]
}
```

复制代码
##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 计步传感器数据变化后会回调此函数。 |
| fail | Function | 否 | 失败回调 |


###### callback 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| steps | Number | 计步传感器当前累计记录的步数。每次手表重启，这个值就会从 0 开始重新计算。 |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 1000 | 当前设备不支持计步传感器 |


##### 示例：


```

sensor.subscribeStepCounter({
  callback: function (ret) {
    console.log(`handling callback, steps = ${ret.steps}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### sensor.unsubscribeStepCounter()


取消监听计步传感器数据。


##### 参数：


无


##### 示例：


```

sensor.unsubscribeStepCounter()
```

复制代码
#### sensor.subscribeOnBodyState(OBJECT)


监听设备佩戴状态传感器数据。如果多次调用，仅最后一次调用生效。


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 穿戴状态改变后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


###### callback 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| value | boolean | 是否已佩戴。 |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 1000 | 当前设备不支持佩戴状态传感器 |


```

sensor.subscribeOnBodyState({
  callback: function (ret) {
    console.log('get on-body state value:' + ret.value)
  },
  fail: function (data, code) {
    console.log('Subscription failed. Code: ' + code + '; Data: ' + data)
  },
})
```

复制代码
#### sensor.unsubscribeOnBodyState()


取消监听设备佩戴状态。


##### 参数：


无


##### 示例：


```

sensor.unsubscribeOnBodyState()
```

复制代码
#### sensor.getOnBodyState(OBJECT)


获取设备佩戴状态。


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |


###### callback 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| value | boolean | 是否已佩戴。 |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 1000 | 当前设备不支持佩戴状态传感器 |


```

sensor.getOnBodyState({
  success: function (ret) {
    console.log('on body state: ' + ret.value)
  },
  fail: function (data, code) {
    console.log('Subscription failed. Code: ' + code + '; Data: ' + data)
  },
})
```

复制代码
#### sensor.subscribeGyroscope(OBJECT)


监听陀螺仪传感器数据。如果多次调用，仅最后一次调用生效。


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 陀螺仪传感器数据改变后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


###### callback 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| x | Number | x 轴坐标 |
| y | Number | y 轴坐标 |
| z | Number | z 轴坐标 |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 1000 | 当前设备不支持陀螺仪传感器 |


##### 示例：


```

sensor.subscribeGyroscope({
  callback: function (ret) {
    console.log(`handling callback, x = ${ret.x}, y = ${ret.y}, z = ${ret.z}`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### sensor.unsubscribeGyroscope()


取消监听陀螺仪数据。


##### 参数：


无


##### 示例：


```

sensor.unsubscribeGyroscope()
```

复制代码
#### sensor.subscribeBarometer(OBJECT)


监听气压传感器数据。如果多次调用，仅最后一次调用生效。


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 气压传感器数据改变后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


###### callback 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| pressure | Number | 气压值，单位：帕斯卡。 |


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 1000 | 当前设备不支持气压传感器 |


```

sensor.subscribeBarometer({
  callback: function (ret) {
    console.log('get data value:' + ret.pressure)
  },
  fail: function (data, code) {
    console.log('Subscription failed. Code: ' + code + '; Data: ' + data)
  },
})
```

复制代码
#### sensor.unsubscribeBarometer()


取消监听气压传感器。


##### 参数：


无


##### 示例：


```

sensor.unsubscribeBarometer()
```

复制代码
#### sensor.subscribeWristLift(OBJECT)


监听抬腕。如果多次调用，仅最后一次调用生效。


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 抬腕后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


###### callback 返回值：


无


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 1000 | 当前设备不支持 |


```

sensor.subscribeWristLift({
  callback: function () {
    console.log('wrist lift')
  },
  fail: function (data, code) {
    console.log('Subscription failed. Code: ' + code + '; Data: ' + data)
  },
})
```

复制代码
#### sensor.unsubscribeWristLift()


取消监听监听抬腕。


##### 参数：


无


##### 示例：


```

sensor.unsubscribeWristLift()
```

复制代码
#### sensor.subscribeContinuousWristTurn(OBJECT)


监听连续转腕。如果多次调用，仅最后一次调用生效。


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 连续转腕变后的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |


###### callback 返回值：


无


###### fail 返回错误代码


| 错误码 | 说明 |
| --- | --- |
| 1000 | 当前设备不支持 |


```

sensor.subscribeContinuousWristTurn({
  callback: function () {
    console.log('continuous wrist turn')
  },
  fail: function (data, code) {
    console.log('Subscription failed. Code: ' + code + '; Data: ' + data)
  },
})
```

复制代码
#### sensor.unsubscribeContinuousWristTurn()


取消监听连续转腕。


##### 参数：


无


##### 示例：


```

sensor.unsubscribeContinuousWristTurn()
```

复制代码


---


<!-- 文档 57: js-api/system/settings/.md -->


## 系统设置

## 系统设置

更新时间：2024-09-02 14:53:40


### 接口声明


```

{ "name": "blueos.service.settings" }
```

复制代码
### 导入模块


```

import settings from '@blueos.service.settings'
```

复制代码
### 在工程里面的 manifest 文件中配置如下内容


#### 申请权限


```

{
  "permissions": [{ "name": "watch.permission.SETTINGS" }]
}
```

复制代码
### 接口定义


#### settings.getValue(OBJECT)


获取设置


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | String | 是 | 相应设置的字段名 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| key | String | 相应设置的字段名 |
| value | String/Object/Array 等 JS 原生对象 | 相应设置的值 |


##### 示例：


```

settings.getValue({
  key: 'brightness',
  success: function (data) {
    console.log(data.key + ': ' + data.value)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### settings.getValueSync(String)


同步获取设置


##### 参数


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | String | 是 | 相应设置的字段名 |


##### 返回值


| 参数值 | 类型 | 说明 |
| --- | --- | --- |
| value | String/Object/Array 等 JS 原生对象 | 相应设置的值 |


##### 示例


```

const value = settings.getValueSync('brightness')
```

复制代码
##### 设置相关的字段


###### brightness 屏幕亮度


| 字段名 | 类型 | 功能 | 说明 |
| --- | --- | --- | --- |
| brightness | Number | 系统屏幕亮度值设置 | 取值范围 0-255 |


```

{
  brightness: 60
}
```

复制代码
###### wearHand 佩戴手


| 字段名 | 类型 | 功能 | 说明 |
| --- | --- | --- | --- |
| wearHand | String | 佩戴手设置 | `L`: 左手， `R`: 右手 |


```

{
  wearHand: 'R'
}
```

复制代码
###### raiseWristSwitch 抬腕监听开关


注意: 此处的监听仅代表用户感知的监听设置，和真实的监听无关


| 字段名 | 类型 | 功能 | 说明 |
| --- | --- | --- | --- |
| raiseWristSwitch | Boolean | 抬腕监听开关设置 | `true`: 开启抬腕监听， `false`: 关闭抬腕监听 |


```

{
  raiseWristSwitch: true
}
```

复制代码
###### raiseWristSensitivity 抬腕监听灵敏度


注：灵敏度改变会影响 sensor 接口监听的灵敏度


| 字段名 | 类型 | 功能 | 说明 |
| --- | --- | --- | --- |
| raiseWristSensitivity | String | 抬腕监听灵敏度设置 | `H`: 高灵敏度， `M`: 标准灵敏度 |


```

{
  raiseWristSensitivity: `H`
}
```

复制代码
###### silentMode 静音模式


| 字段名 | 类型 | 功能 | 说明 |
| --- | --- | --- | --- |
| silentMode | Boolean | 静音模式设置 | `true`: 开启静音模式， `false`: 关闭静音模式 |


```

{
  silentMode: false
}
```

复制代码
###### flipScreen 屏幕翻转


| 字段名 | 类型 | 功能 | 说明 |
| --- | --- | --- | --- |
| flipScreen | Boolean | 屏幕翻转设置 | `true`: 翻转到正向， `false`: 翻转到反向 |


```

{
  flipScreen: false
}
```

复制代码


---


<!-- 文档 58: js-api/system/short-message-service/.md -->


## 短信

## 短信

更新时间：2025-02-17 09:59:02


在蓝河系统中，我们提供了 Deeplink 链接来使您可以快速打开短信服务所对应的页面。


我们已经为短信服务功能提供了 Deeplink 链接，具体链接为 `hap://app/com.vivo.mms/pages/entry`。


该 Deeplink 链接的页面拉取是通过 Router 调用来实现的，您可以方便地打开短信服务页面并进行相关操作。


### 示例


以下是一个演示示例，为您展示如何通过调用 Deeplink 链接来实现轻松发送短信的操作过程：


```

<template>
  <text @click="sendMessage">发短信</text>
</template>
<script>
 import router from '@blueos.app.appmanager.router'
 export default {
 sendMessage () {
 router.push({
 uri: `hap://app/com.vivo.mms/pages/entry`,
 })
 }
 }
</script>
```

复制代码


---


<!-- 文档 59: js-api/system/simManager/.md -->


## sim 卡管理

## sim 卡管理

更新时间：2024-10-11 11:55:18


### 接口声明


```

{ "name": "blueos.telephony.simManager" }
```

复制代码
### 导入模块


```

import simManager from '@blueos.telephony.simManager' 或 const simManager = require('@blueos.telephony.simManager')
```

复制代码
### 接口定义


#### simManager.getSimOperators(OBJECT)


获取 Sim 卡的运营商信息


##### 权限要求


电话权限


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### success 返回值：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| operators | Array | SIM 卡列表信息 |
| size | Number | Sim 卡数量 |


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 201 | 用户拒绝，获取电话权限失败 |
| 207 | 用户拒绝并勾选不再询问复选框 |
| 1001 | 未插入 sim 卡 |
| 1002 | 获取运营商信息失败 |


###### SIM 卡列表项参数：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| operator | String | 返回 Sim 卡的运营商信息运营商信息说明：此处统一返回 MCC+MNC，即移动国家代码 + 移动网络代码；中国移动：46000，46002，46004，46007；中国联通：46001，46006，46009；中国电信：46003，46005，46011； [其余 MCC+MNC](https://www.mcc-mnc.com/ ) |
| slotIndex | Number | 卡槽序号 |


##### 示例：


```

simManager.getSimOperators({
  success(data) {
    console.log(`size: ${data.size}`)
    for (const i in data.operators) {
      console.log(`operator: ${data.operators[i].operator},
 slotIndex:${data.operators[i].slotIndex},
 isDefaultDataOperator:${data.operators[i].isDefaultDataOperator},`)
    }
  },
  fail(data, code) {
    console.log(`handling fail, code = ${code}, errorMsg=${data}`)
  },
})
```

复制代码


---


<!-- 文档 60: js-api/system/softwareOverview/.md -->


## 概述

## 概述

更新时间：2023-10-31 19:37:39


蓝河应用的基础软件能力为应用提供了基础的软件功能支持，包括系统设置、输入法、解压缩、解包和序列化等，可以帮助开发者更加高效、快速地进行软件开发和计算机操作


### 子模块介绍


| 模块 | 简述 |
| --- | --- |
| 系统设置 | 提供获取系统设置能力 |
| 输入法 | 为输入法应用提供向 input 组件写入数据能力 |
| 解压缩 | 提供解压本地文件能力 |
| 解包 | 提供解包能力 |
| 序列化 | 提供序列化数据，反序列化数据能力 |


---


<!-- 文档 61: js-api/system/systemapp/.md -->


## 应用上下文

## 应用上下文

更新时间：2025-10-09 11:25:10


### 接口声明


无需声明


### 导入模块


```

import app from '@blueos.app.context'
// 或 const app = require('@blueos.app.context')
```

复制代码
### 接口定义


#### app.getInfo()


获取当前应用信息


##### 参数：


无


##### 返回值


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| packageName | String | 应用包名 |
| icon | String | 应用图标路径 |
| name | String | 应用名称 |
| versionName | String | 应用版本名称 |
| versionCode | Integer | 应用版本号 |


##### 示例：


```

console.log(JSON.stringify(app.getInfo()))
```

复制代码

```

// console 值打印
{
  // 应用包名
  "packageName": "com.example.demo",
  // 应用名称
  "name": "demo",
  // 应用版本名称
  "versionName": "1.0.0",
  // 应用版本号
  "versionCode": 1,
  // 应用图片
  "icon": "/Common/logo.png"
}
```

复制代码
#### app.loadLibrary(name: string)


加载静态库，需要与厂商合作


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | String | 是 | lib 库名称 |


##### 返回值


静态库加载结果


##### 示例：


```

import app from '@blueos.app.context'
const testApp = app.loadLibrary('test\_app')

testApp.on('js\_task\_callback', () => {
  // callback action
})
```

复制代码
#### app.terminate()


退出当前应用


##### 参数:


无


##### 返回值：


无


##### 示例：


```

app.terminate()
```

复制代码


---


<!-- 文档 62: js-api/system/tar/.md -->


## 解包

## 解包

更新时间：2023-11-08 11:11:17


### 接口声明


```

{ "name": "blueos.util.tar" }
```

复制代码
### 导入模块


```

import tar from '@blueos.util.tar' 或 const fastlz = require('@blueos.util.tar')
```

复制代码
### 接口定义


#### 注：“蓝河应用平台参数” 表示开发蓝河应用必填参数


#### tar.untar(OBJECT)


解包


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcUri | String | 是 | 源文件的 uri，不能是 tmp 类型的 uri |
| dstUri | String | 是 | 目标目录的 uri，不能是应用资源路径和 tmp 类型的 uri |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


###### 备注：


srcUri 和 dstUri 路径采用的是 file\_feature 协议，由于是私有接口，是可以跨包读取的。internal:// 原本的路径解析为: /sdcard/internal/rpk 包名，但在解压缩去掉了包名的限制，实际得到的路径是： /sdcard/internal/


###### fail 返回错误代码：


| 错误码 | 说明 |
| --- | --- |
| 202 | 参数错误 |
| 300 | I/O 错误 |


##### 示例：


```

tar.untar({
  srcUri: 'internal://cache/test.tar',
  dstUri: 'interval://files/untar/',
  success: function () {
    console.log(`handling success`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码


---


<!-- 文档 63: js-api/system/telephony-service/.md -->


## 电话

## 电话

更新时间：2025-02-17 09:59:02


在蓝河系统中，您可以通过 Deeplink 链接来打开电话服务相应页面。


我们为电话服务提供了 Deeplink 链接，具体链接为 `hap://app/com.vivo.call/pages/callMenu`。


并且 Deeplink 的页面拉取是通过 Router 调用来实现的，方便您快速地进行操作。


### 示例


以下是一个示例，展示了如何使用 Deeplink 链接调用电话功能，简单易懂、易于操作：


```

<template>
  <text @click="call">打电话</text>
</template>
<script>
 import router from '@blueos.app.appmanager.router'
 export default {
 call () {
 router.push({
 uri: `hap://app/com.vivo.call/pages/callMenu`,
 })
 }
 }
</script>
```

复制代码


---


<!-- 文档 64: js-api/system/vibrator/.md -->


## 振动

## 振动

更新时间：2024-08-13 15:19:43


### 接口声明


```

{ "name": "blueos.hardware.vibrator.vibrator" }
```

复制代码
### 导入模块


```

import vibrator from '@blueos.hardware.vibrator.vibrator' 或 const vibrator = require('@blueos.hardware.vibrator.vibrator')
```

复制代码
### 接口定义


#### vibrator.vibrate(OBJECT)


触发振动


##### 参数：


| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | String | 否 | 振动模式，`long` 表示长振动，`short` 表示短振动。默认为 `long` |


##### 示例：


```

vibrator.vibrate({
  mode: 'long',
})
```

复制代码
#### vibrator.start(OBJECT)


开始振动


###### 参数：


| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| priority | Number | 是 | 振动优先级 0-8，数字越小优先级越高 |
| duration | Number | 是 | 振动持续时间(单位 ms) |
| interval | Number | 是 | 振动间隔时间(单位 ms) |
| count | Number | 是 | 振动次数 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |
| complete | Function | 否 | 执行结束后的回调 |


##### success 返回值：


| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| id | Number | 底层分配唯一的 ID 并返回给调用者 |


##### 示例：


```

vibrator.start({
  priority: 1,
  duration: 1000,
  interval: 1000,
  count: 10,
  success: function (data) {
    console.log(`handling success, id = ${data.id}`)
  },
  fail: function () {
    console.log(`handling fail`)
  },
  complete: function () {
    console.log(`handling complete`)
  },
})
```

复制代码
#### vibrator.stop(Number)


停止振动


##### 参数：


| 类型 | 必填 | 说明 |
| --- | --- | --- |
| Number | 是 | 底层分配唯一的 ID |


##### 返回值：


| 类型 | 说明 |
| --- | --- |
| Boolean | true:成功; false:失败; |


##### 示例：


```

vibrator.stop(1)
```

复制代码
#### vibrator.getSystemDefaultMode()


获取系统默认振动模式


##### 参数：


无


##### 返回值：


| 类型 | 说明 |
| --- | --- |
| Number | 0:关闭振动; 1:标准振动; 2:加强振动 |


##### 示例：


```

vibrator.getSystemDefaultMode()
```

复制代码


---


<!-- 文档 65: js-api/system/websocket/.md -->


## websocket

## websocket

更新时间：2023-12-25 11:01:05


### 接口声明


```

{ "name": "blueos.network.webSocket" }
```

复制代码
### 导入模块


```

import websocketfactory from '@blueos.network.webSocket' 或 const websocketfactory = require('@blueos.network.webSocket')
```

复制代码
### 接口定义


#### 方法


#### websocketfactory.create(OBJECT)


创建 websocket 实例


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | String | 是 | 请求 url， 必须是 wss 或 ws 协议 |
| header | Object | 否 | 请求头，header 中不能设置 Referer |
| protocols | StringArray | 否 | 子协议组 |


##### 返回值：


| 类型 | 描述 |
| --- | --- |
| `WebSocket` | 返回一个 WebSocket 对象，请参考 [WebSocket](#websocket) 对象 |


##### 示例：


```

ws = websocketfactory.create({
  url: 'ws://test:8088',
  header: {
    'content-type': 'application/json',
  },
  protocols: ['protocol'],
})
```

复制代码


---


### WebSocket


WebSocket 对象提供了用于创建和管理 WebSocket 连接，以及可以通过该连接发送和接收数据的 API。


### 方法


#### WebSocket.send(OBJECT)


向服务器发送数据


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | String | ArrayBuffer | 是 | 发送的消息 |
| success | Function | 否 | 成功回调 |
| fail | Function | 否 | 失败回调 |


##### 示例：


```

ws.send({
  data: 'send message',
  success: function () {
    console.log(`send success`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
#### WebSocket.close(OBJECT)


关闭当前连接


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | Number | 否 | 关闭链接的状态号 ，默认 1000 |
| reason | String | 否 | 关闭的原因 |
| success | Function | 否 | 接口调用成功的回调函数 |
| fail | Function | 否 | 接口调用失败的回调函数 |


##### 示例：


```

ws.close({
  code: 1000,
  reason: 'close as normal',
  success: function () {
    console.log(`close success`)
  },
  fail: function (data, code) {
    console.log(`handling fail, code = ${code}`)
  },
})
```

复制代码
### 属性


#### WebSocket.onOpen


用于指定连接成功后的回调函数


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 否 | 打开连接回调 |


##### 示例：


```

ws.onOpen = function () {
  console.log(`connect open`)
}
```

复制代码
#### WebSocket.onMessage


用于指定当从服务器接受到信息时的回调函数


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 否 | 服务器返回消息事件回调 |


##### callback 参数：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| data | String | ArrayBuffer | 监听器接收到的消息，消息类型与发送类型一致 |


##### 示例：


```

ws.onMessage = function (data) {
  console.log(`message is ${data.data}`)
}
```

复制代码
#### WebSocket.onClose


用于指定连接关闭后的回调函数


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 否 | 关闭连接事件回调。 |


##### callback 参数：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| code | Number | 服务器返回关闭的状态码。 |
| reason | String | 服务器返回的关闭原因。 |
| wasClean | Boolean | 是否正常关闭。 |


##### 示例：


```

ws.onClose = function (data) {
  console.log(
    `onclose:data.code = ${data.code}, data.reason = ${data.reason}, data.wasClean = ${data.wasClean}`
  )
}
```

复制代码
#### WebSocket.onError


用于指定连接失败后的回调函数


##### 参数：


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 否 | 连接错误回调 |


##### callback 参数：


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| data | String | 监听器接收到的消息。 |


##### 示例：


```

ws.onError = function (data) {
  console.log(`onerror data.data = ${data.data}`)
}
```

复制代码


---


<!-- 文档 66: js-api/system/widget-manager/.md -->


## widgetManager

## widgetManager

更新时间：2025-10-09 21:26:28


widgetProvider 通过 widgetManager 来刷新 卡片 UI 页面中的 uiData 数据，widgetManager 也可以用于主应用刷新 uidata 的数据。


详细参考 [widgetProvider 开发](/reference/widget/widget-provider/)


**接口声明**


```

{ "name": "blueos.app.widgetManager" }
```

复制代码
### updateUiData


更新卡片 ui 数据


**入参**


| 属性 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| instanceId | number | string | 是 | widget 实例 id |
| uiData | Record<string, unknown> | 否 | 传递的数据 |


**返回值：** 无


**示例：**


```

import widgetManager from '@blueos.app.widgetManager'

export default {
  onWidgetEvent(instanceId, event) {
    console.log(`instanceId=${instanceId}, event=${JSON.stringify(event)}`)
    widgetManager.updateUiData({
      instanceId: instanceId,
      uiData: { cityName: `Shenzhen ${event.title}` },
    })
  },
}
```

复制代码


---


<!-- 文档 67: js-api/system/widget-provider/.md -->


## widgetProvider

## widgetProvider

更新时间：2025-10-09 21:26:28


widgetProvider 是轻卡的核心组成部分，它负责执行轻卡页面的逻辑，并与轻卡页面进行数据传递。


详细参考 [widgetProvider 开发](/reference/widget/widget-provider/)


### onWidgetCreate


当卡片在入口被创建时触发


**参数：**


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 卡片实例 id |
| widgetInfo | [WidgetInfo](#widgetinfo) | 卡片信息 |


**示例：**


```

export default {
  onWidgetCreate(id, widgetInfo) {
    console.log(`卡片被创建`)
  },
}
```

复制代码
### onWidgetUpdate


定时或定点条件满足时，卡片请求提供方刷新卡片


**参数：**


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 卡片实例 id |
| widgetInfo | [WidgetInfo](#widgetinfo) | 卡片信息 |


**示例：**


```

export default {
  onWidgetUpdate(id, widgetInfo) {
    console.log(`卡片需要更新`)
  },
}
```

复制代码
### onWidgetEvent


当卡片页面触发 Action 的 message 事件时被调用


**参数：**


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 卡片实例 id |
| event | [WidgetEventInfo](#widgeteventinfo) | 事件信息 |


**示例：**


```

export default {
  onWidgetEvent(id, event) {
    console.log(`收到 message 事件`)
  },
}
```

复制代码
### onConfigurationChanged


监听系统语言改变


| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| event | Object | 应用配置发生变化的事件 |


event 参数：


| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| type | String | 应用配置发生变化的原因类型，支持的 type 值如下所示 |


event 中`type` 现在支持的参数值如下：


| 参数值 | 描述 |
| --- | --- |
| locale | 应用语言、地区变化而发生改变 |


**示例：**


```

export default {
  onConfigurationChanged(id, evt) {
    if (event && event.type && event.type === 'locale') {
      console.log('locale or language changed!')
    }
  },
}
```

复制代码
### onWidgetDestroy


销毁卡片时触发，提供方可以做对应的释放


**参数：**


| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 卡片实例 id |


**示例：**


```

export default {
  onWidgetDestroy(id) {
    console.log(`卡片销毁`)
  },
}
```

复制代码
### 参数类型说明


#### WidgetInfo


widgetProvider 生命周期入参，描述卡片信息。


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instanceId | string | 是 | 卡片运行时实例的 id。 |
| package | string | 是 | 卡片包名，可用于校验卡片。 |
| path | string | 是 | 卡片路径，可用于校验卡片。 |
| sha256 | string | 否 | 卡片数字签名，可用于校验卡片是否合法。 |
| host | string | 是 | 卡片入口的包名，用于提供方做不同策略。 |
| scene | string | 否 | 卡片展示方场景标识 |
| version | number | 否 | 卡片版本 |
| extra | Record<string, any> | 否 | 如果卡片入口加载卡片 Uri 有携带额外数据，此时会携带额外的数据到提供方。 |


#### WidgetEventInfo


widgetProvider 生命周期入参，描述卡片页面的 Action 事件信息。


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instanceId | string | 是 | 卡片运行时实例的 id。 |
| package | string | 是 | 卡片包名，可用于校验卡片。 |
| path | string | 是 | 卡片路径，可用于校验卡片。 |
| sha256 | string | 否 | 卡片数字签名，可用于校验卡片是否合法。 |
| host | string | 是 | 卡片入口的包名，用于提供方做不同策略。 |
| scene | string | 否 | 卡片展示方场景标识 |
| version | number | 否 | 卡片版本。 |
| extra | Record<string, any> | 否 | 如果卡片入口加载卡片 Uri 有携带额外数据，此时会携带额外的数据到提供方。 |
| event | [Event](#event) | 是 | event 事件对象。 |


#### Event


描述 Action 事件参数


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | string | 是 | action 名，对应 data 中 actions 里的某个响应动作 |
| params | Record<string, any> | 否 | 开发者在事件响应动作设置的参数 |


---
