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
    "validate_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoiMTIzNDU2QHFxLmNvbSIsInZhbGlkYXRlX2NvZGUiOiIwMTc1MTMiLCJleHAiOjE1OTg5NjAwMDN9.6TVq3R4DVCdVdb_-Y88XyCh-KMA5z0ROxUCXjCxPySI"
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
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMThlYzZmOGEtNTBmMi00OTZlLWI2NTEtYzUyMWI4MDg4NDI4Iiwicm9sZV9pZCI6IlVTRVIiLCJleHAiOjE1OTkxMzI2MzR9.R98p1B3YN00ukEueQ3vTV0KXbXe9Luse9NL8POYVWro",
    "user_id": "18ec6f8a-50f2-496e-b651-c521b8088428"
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
    "created_at": "2020-09-01T11:30:21.391147",
    "description": "产品1的介绍",
    "manager_id": "71d21f79-9114-47da-8da9-6e717a6e9d6c",
    "name": "产品1",
    "price": 1.1,
    "product_id": "eba1007e-acd3-4741-8437-e1768f6e8890"
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
        "created_at": "2020-09-01T11:30:21.391000",
        "description": "4",
        "manager_id": "371d460e-9d89-4fbc-9744-d8c32ed44f23",
        "name": "4",
        "price": 1.100000023841858,
        "product_id": "5d861bf7-7a3b-424f-96ba-9c1e33b24567"
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
    "user_id": "c40fd12d-2008-4329-b463-f750553e9a6c"
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
