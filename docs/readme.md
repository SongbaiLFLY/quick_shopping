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
    "validate_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoiMTIzNDU2QHFxLmNvbSIsInZhbGlkYXRlX2NvZGUiOiIwMzc4ODkiLCJleHAiOjE1OTkyMzI3NTJ9.uQjeq0vr7VbFL4acYbGheJS7DWqabgwWDL0llSKWoGw"
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
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMWE5NWZkNmEtYWUxMS00MmM2LTlkMjYtMDk5NmUwZjcwZDUzIiwicm9sZV9pZCI6IlVTRVIiLCJleHAiOjE1OTk0MDUzODN9.J4McdAow5PTD8oVUa3EmZ7oC0v_5Pqz1zANVCwuU1OI",
    "user_id": "1a95fd6a-ae11-42c6-9d26-0996e0f70d53"
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
    "created_at": "2020-09-04T15:16:09.817799",
    "description": "产品1的介绍",
    "manager_id": "51750507-ea50-4005-9290-6cbcf8b5849e",
    "name": "产品1",
    "price": 1.1,
    "product_id": "7d4c0b84-cab3-4048-9ad9-bc1aec0ebf89"
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
        "created_at": "2020-09-04T15:16:09.817000",
        "description": "4",
        "manager_id": "7523243d-46e5-4fc3-843c-09bba2039225",
        "name": "4",
        "price": 1.100000023841858,
        "product_id": "0c1b388b-4b1b-4b79-a050-b097dc23a508"
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
    "user_id": "d90386ca-0000-4139-ba0a-f3d186a57acd"
  }
}
```
