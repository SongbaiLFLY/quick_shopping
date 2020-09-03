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
    "validate_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoiMTIzNDU2QHFxLmNvbSIsInZhbGlkYXRlX2NvZGUiOiIzNDE3MjkiLCJleHAiOjE1OTkxMzAxMzl9.rwlfb-pm7OYg-Njvnj6RdYcW5Sgc7JqlmkKQHcxgdIg"
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
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiZWVkZjc5MmYtYmNhZi00Y2QyLWEzNmItZDQ5N2I4YWNjZTBjIiwicm9sZV9pZCI6IlVTRVIiLCJleHAiOjE1OTkzMDI3NzB9.UR34GvMjb7nuELVZSPf3CL5SSgaz_ppj2uQooYInxic",
    "user_id": "eedf792f-bcaf-4cd2-a36b-d497b8acce0c"
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
    "created_at": "2020-09-03T10:45:56.664702",
    "description": "产品1的介绍",
    "manager_id": "22108203-9a62-4c35-860f-9d20b49abdc3",
    "name": "产品1",
    "price": 1.1,
    "product_id": "4dbd290a-ddef-41e1-bbf2-08c4845837e2"
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
        "created_at": "2020-09-03T10:45:56.664000",
        "description": "4",
        "manager_id": "992bfcb9-ce3c-4cc0-b453-084fb4025ac5",
        "name": "4",
        "price": 1.100000023841858,
        "product_id": "7454c854-1117-4129-a7ff-96b77ab282a1"
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
    "user_id": "4cd8eb35-afb0-4ad8-a9a7-c4e2d6390251"
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
      {}
    ]
  }
}
```
