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
    "validate_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoiMTIzNDU2QHFxLmNvbSIsInZhbGlkYXRlX2NvZGUiOiIyOTY0ODYiLCJleHAiOjE1OTkwNDI1ODh9.kYH7VgjYY3RtYEdIwp3LtXxwhm8o-nN_ujIXHLQAR_c"
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
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMzU2ZGJmZWUtMDYxYi00YjEzLWE2YjEtZWE5MWY2MmQzMzUzIiwicm9sZV9pZCI6IlVTRVIiLCJleHAiOjE1OTkyMTUyMTl9.CAN4Y-zXGUvIIcCDVgCvp3oY_5DfnL27Ia7d_oZ49qA",
    "user_id": "356dbfee-061b-4b13-a6b1-ea91f62d3353"
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
    "created_at": "2020-09-02T10:26:45.615525",
    "description": "产品1的介绍",
    "manager_id": "bc7bf2d6-2292-4511-ae6a-53a2d8ac2afa",
    "name": "产品1",
    "price": 1.1,
    "product_id": "85710367-56ad-48e1-ade1-7ba5cdc2d97a"
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
        "created_at": "2020-09-02T10:26:45.615000",
        "description": "4",
        "manager_id": "87859102-2a1a-4943-b037-51e187ccb170",
        "name": "4",
        "price": 1.100000023841858,
        "product_id": "24687165-a2d9-423b-87c3-3ea617e752e3"
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
    "nickname": "tester",
    "role_id": "USER",
    "user_id": "0837ebba-7ede-4554-bd2d-2d275e11eb0f"
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

正确响应: 
```json
{
  "ok": true,
  "result": {}
}
```
