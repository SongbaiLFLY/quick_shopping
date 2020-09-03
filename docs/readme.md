[readme.md](readme.md)

## 1 发送验证码
**请求**: 

| 方法名 | 参数 | 描述 |
| --- | --- | --- |
| path | `/v1/account/send_code` | - |
| method | `POST` | - |
| body | `account_id（必填）` | 帐号 |

正确响应: 
```json
{
  "ok": true,
  "result": {
    "validate_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoiMTIzNDU2QHFxLmNvbSIsInZhbGlkYXRlX2NvZGUiOiI0NTYzMzkiLCJleHAiOjE1OTkxMzA1Mjh9.i9sqP10YDGYLW4-QFkfjk5QaiUbNcw4KIPMiC3mQY7w"
  }
}
```
验证码已经发送: 
```json
{
  "error_type": "code_already_sent",
  "message": "验证码已经发送",
  "ok": false
}
```

## 2 创建帐号
**请求**: 

| 方法名 | 参数 | 描述 |
| --- | --- | --- |
| path | `/v1/account` | - |
| method | `POST` | - |
| body | `account_id（必填）` | 邮箱 |
| body | `password(密码)` | 密码 |
| body | `validate_token` | token |
| body | `validate_code` | 验证码 |

正确响应: 
```json
{
  "ok": true,
  "result": {}
}
```
帐号已存在: 
```json
{
  "error_type": "account_already_exist",
  "message": "该账号已经存在，请登录",
  "ok": false
}
```

## 3 登录帐号
**请求**: 

| 方法名 | 参数 | 描述 |
| --- | --- | --- |
| path | `/v1/login` | - |
| method | `POST` | - |
| body | `account_id（必填）` | 邮箱 |
| body | `password（必填）` | 密码 |

正确响应: 
```json
{
  "ok": true,
  "result": {
    "role_id": "USER",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYTc2NmM2MzItMGIzMy00NjcwLWIwZGEtMWM1ZjJhMjEyNGI4Iiwicm9sZV9pZCI6IlVTRVIiLCJleHAiOjE1OTkzMDMxNTl9.5JROy-gaKY6TDtm8mLIJZO7WMevD1Ovsj8Ad6DGeuIw",
    "user_id": "a766c632-0b33-4670-b0da-1c5f2a2124b8"
  }
}
```
密码错误: 
```json
{
  "error_type": "password_wrong",
  "message": "密码错误",
  "ok": false
}
```

## 4 创建一个产品
**请求**: 

| 方法名 | 参数 | 描述 |
| --- | --- | --- |
| path | `/v1/product` | - |
| method | `POST` | - |
| header | `Authorization` | 用户 Token |
| body | `manager_id（必填）` | manager_ID |
| body | `name（必填）` | 产品名 |
| body | `price` | 价格 |
| body | `description` | 产品介绍 |

正确响应: 
```json
{
  "ok": true,
  "result": {
    "created_at": "2020-09-03T10:52:25.822320",
    "description": "产品1的介绍",
    "manager_id": "e30c4c81-bf7f-474d-bd67-1d36a62340a9",
    "name": "产品1",
    "price": 1.1,
    "product_id": "4f2ebb8c-e060-4f00-8e44-763e30846717"
  }
}
```

## 5 查询产品
**请求**: 

| 方法名 | 参数 | 描述 |
| --- | --- | --- |
| path | `/v1/product/manager/{manager_id}` | - |
| method | `GET` | - |
| header | `Authorization` | 用户 Token |

正确响应: 
```json
{
  "ok": true,
  "result": {
    "products": [
      {
        "created_at": "2020-09-03T10:52:25.822000",
        "description": "4",
        "manager_id": "2ccdcfe9-9f5e-4bf0-8830-4b0a0b79791c",
        "name": "4",
        "price": 1.100000023841858,
        "product_id": "cae99c90-6ad0-4e8d-9289-b6e8056733c4"
      }
    ]
  }
}
```

## 6 创建个人资料
**请求**: 

| 方法名 | 参数 | 描述 |
| --- | --- | --- |
| path | `v1/profile` | - |
| method | `POST` | - |
| body | `user_id(必填)` | 用户id |
| body | `nickname(必填)` | 用户昵称 |
| body | `gender` | 性别 |
| body | `role_id` | 角色id |

正确响应: 
```json
{
  "ok": true,
  "result": {}
}
```

## 7 获取个人资料
**请求**: 

| 方法名 | 参数 | 描述 |
| --- | --- | --- |
| path | `/v1/profile/{user_id}` | - |
| method | `GET` | - |

正确响应: 
```json
{
  "ok": true,
  "result": {
    "avatar": "",
    "gender": 0,
    "nickname": "tester",
    "role_id": "MANAGER",
    "user_id": "a5f16be9-ae36-4380-aff0-b882648736b2"
  }
}
```

## 8 更新个人资料
**请求**: 

| 方法名 | 参数 | 描述 |
| --- | --- | --- |
| path | `/v1/profile/{user_id}` | - |
| method | `PUT` | - |
| body | `nickname` | 昵称 |
| body | `gender` | 性别 |
| body | `user_id` | 用户id |
| body | `avatar` | 头像 |

正确响应: 
```json
{
  "ok": true,
  "result": {}
}
```

## 9 获取所有商家
**请求**: 

| 方法名 | 参数 | 描述 |
| --- | --- | --- |
| path | `/v1/profile/user/manager` | - |
| method | `GET` | - |

正确响应: 
```json
{
  "ok": true,
  "result": {
    "managers": [
      {
        "avatar": "",
        "gender": 0,
        "nickname": "tester",
        "role_id": "MANAGER",
        "user_id": "ddab74cc-f3aa-48b4-b6b7-30ffed604e13"
      }
    ]
  }
}
```
