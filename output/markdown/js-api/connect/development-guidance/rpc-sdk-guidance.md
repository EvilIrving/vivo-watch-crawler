---
title: vivo 智能终端设备 SDK
url: https://developers-watch.vivo.com.cn/api/connect/development-guidance/rpc-sdk-guidance/
---

# vivo 智能终端设备 SDK

# vivo 智能终端设备 SDK

更新时间：2025-07-23 09:40:34


## 开发准备，申请 appid


#### 1. 申请 app 开发者接入，接入地址：[vivo 开放平台](https://dev.vivo.com.cn/)，已有账号则无需申请，直接登录


#### 2. 申请账号后，注册对应的 app，取到 appid


## SDK 集成


```

implementation files('libs/device-rpc.aar')
```

复制代码
## 初始化


```

 // 在 app 恰当的时候初始化，如果需要拉起并发送到通知，建议放 application 里面。
 DeviceRpcManager.getInstance().init(getApplicationContext(), String encryStr,InitCallBack initCallBack);
```

复制代码
#### encryStr:需联系 vivo 对接人员获取（[xiaoming.ling@vivo.com](mailto:xiaoming.ling@vivo.com)），请提供包名、appid


#### InitCallBack:鉴权结果回调


#### manifest 中添加 meta 数据，固定格式和名称，用于设备查询 app 功能信息


```

<meta-data android:name="health.device.manager.version" android:value="1" />
<meta-data android:name="appid" android:value="开发平台申请的appid" />
```

复制代码
## 三方 APP 协议参考设计


三方 App 除了获取“运动健康功能版本号”，“读取设备对应功能版本号”外，通常需要使用接口<给设备发送 Request 数据>跟手机交换数据，为了区分不同 Request 数据类型，建议使用如下 Json 格式


```

{
     "type":"type\_xxxx"
     "data":{}
}
```

复制代码
#### 对应的 Response 数据类型，建议使用如下 Json 格式：


```

{
     "code"：0
     "result":{}
}
```

复制代码
#### 其中


- type 指定数据类型，不同的业务对应不同的类型，用于对端区分数据，作相应处理
- data 数据，不同业务有不同的数据
- code 对端的业务执行结果
- result 结果依赖不同的 type 而不同


## SDK 下载


[vivo 智能终端设备 SDK](https://h5.vivo.com.cn/health/rpcsdk/new/device-rpc.aar)


## API 参考


[手机侧](/api/connect/mobile-side/)


## 隐私政策


[隐私政策](/api/connect/development-guidance/privacy-policy/)
