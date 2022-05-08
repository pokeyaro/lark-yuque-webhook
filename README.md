# lark_yuque_webhook

### 1. 基础信息
- **昵称：** 小雀同学（飞书机器人）
- **应用：** *Yuque Assistant*
- **名片：** */help*
- **描述：** 将语雀的动态以 Webhook 方式推送给飞书机器人



### 2. 能力建设

- **可以陪你聊天：**

  - 你可以在群组中艾特:     @Bot + 描述

  - 也可以直接跟它私聊:     描述

    

- **消息推送能力：**

  - 发布内容 ✅

  - 更新内容 ✅

  - 发表评论 ✅

  - 更新评论 ✅

  - 回复评论 ✅

  - 评审状态 ❌

    

- **Tips：**

  - 目前除 '评审' 状态未 Hook 外，其它均已集成到飞书端。总之，还是希望语雀产研团队能多提供些 API 接口呀～




### 3. 开发者文档

- **开发文档说明：**

| 示例说明              | 网址链接                                                     |
| --------------------- | ------------------------------------------------------------ |
| 请求网址配置说明      | https://open.feishu.cn/document/ukTMukTMukTM/uYDNxYjL2QTM24iN0EjN/event-subscription-configure-/request-url-configuration-case |
| 发送消息 content 说明 | https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json#11e75d0 |
| 服务端错误码说明      | https://open.feishu.cn/document/ukTMukTMukTM/ugjM14COyUjL4ITN |


- **使用飞书接口：**

| 接口说明 | 网址链接 |
| -------------------------- | ------------------------------------------------------------ |
| 获取认证访问权限 | https://open.feishu.cn/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token |
| 发送消息                   | https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/create |
| 回复消息                   | https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/reply |
| 发送「仅你可见」的临时消息 | https://open.feishu.cn/document/ukTMukTMukTM/uETOyYjLxkjM24SM5IjN |
| 删除「仅你可见」的临时消息 | https://open.feishu.cn/document/ukTMukTMukTM/uITOyYjLykjM24iM5IjN |
| 获取机器人信息 | https://open.feishu.cn/document/ukTMukTMukTM/uAjMxEjLwITMx4CMyETM |
| 获取用户或机器人所在的群列表 | https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/chat/list |


- **工具类：**

| 工具网站     | 网址链接                                |
| ------------ | --------------------------------------- |
| 构建消息卡片 | https://open.feishu.cn/tool/cardbuilder |
| JSON在线转换 | https://www.huatools.com/json-dict/     |



### 4. 环境部署

- **前置条件：**

- - 注册飞书 APP 企业账号（免费无审核）。
  - 需要一个暴露在公网的 HTTP 服务：

- - - 购买云主机 + 域名申请 + 搭建 Nginx WEB 服务（付费）。
    - 腾讯云 FaaS 服务的 SCF 云函数 + API 网关（免费高额度）。
    - 使用内网穿透：如 Ngrok 工具，可让本地服务暴露在外网。

- **实施方案：**
  - 该工具使用 Flask + uWSGI + Nginx 进行部署。



### 5. 机器人截图

- **聊天：**

![image](https://user-images.githubusercontent.com/58482090/167250453-c5cf6d26-9b1d-4177-a173-65fb6e11365b.png)



- **消息推送：**

![image](https://user-images.githubusercontent.com/58482090/167250155-29127406-d143-4f26-886a-fba047a9870f.png)



- **小雀名片：**

![image](https://user-images.githubusercontent.com/58482090/167250194-afa278df-d471-4059-9a44-4e96dfa8e0c6.png)



### 6. 更新日志

- v1.0.0 更新机器人对话功能
- v1.0.1 配置路径调整
- v1.0.2 优化机器人消息处理能力, 删除了 Webhook 事件去重严谨判断逻辑
- v1.0.3 新增语雀 PC 端的 Webhook 消息获取, 包括文章与评论相关
- v1.0.4 配置文件新增 API 路由选择与机器人昵称定义
- v1.0.5 提高消息回复的敏捷与准确性
- v1.0.6 新增获取机器人所在的群组信息列表
- v1.0.7 新增语雀通知消息卡片
- v1.0.8 新增自动获取应用机器人基础信息接口
- v1.0.9 细节变更, 与 v1.1.0 同时发布
- v1.1.0 语雀 Wiki 库的变化 Webhook 给飞书, 并通过消息卡片实时发布到聊天群组中
- v1.1.1 小雀同学群聊 /help 名片已上线, 仅你可见
- v1.1.2 小雀同学的卡片交互响应功能已上线

