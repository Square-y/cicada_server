## 用户

[TOC]

### 一、用户注册

```python
URL:http://127.0.0.1:5000/register
```

1、请求方式

```python
POST
```

2、请求格式

```python
{
    'username':'HUANGJIANFANG',
    'password01':'1028111x',
    'password02':'1028111x'
    'mail':'huang111x@163.com',
    'phone': '18211111111'
}
```

3.响应格式



```python
{
    'retCode':'000',
    'retMsg':'用户注册成功'
}
```

4.数据库结构

user表

| 字段     | 类型    | 是否必填 | 备注       |
| -------- | ------- | -------- | ---------- |
| id       | int     | 否       | 序号，主键 |
| username | varchar | 是       | 用户名     |
| password | varchar | 是       | 密码       |

count表

| 字段    | 类型    | 是否必填 | 备注     |
| ------- | ------- | -------- | -------- |
| user_id | int     | 是       | 用户id   |
| mail    | varchar | 是       | 用户邮箱 |

### 二、用户登录

```python
URL:http://127.0.0.1:5000/login
```

1、请求方式

```python
POST
```

2、请求格式

```python
{
    'username':'',
    'password': '',
    'email':''
}
```

3、响应格式

登录成功，则将token放在header里

```python
{
    'retCode':'000',
    'reMsg':'登录成功'
}
```

### 三、获取用户信息

```python
URL:http://127.0.0.1:5000/user
```

1、请求类型

```python
GET
```

2、请求格式

```python
无
```

3、响应格式

```python
{
    "mail":"",
    "username":"",
    "sign":""
}
```

### 四、修改用户信息

```python
URL:http://127.0.0.1:5000/user
```

1、请求类型

```python
POST
```

2、请求格式

```python
{
    "mail":"",
    "username":"",
    "sign":""
}
```

3、响应格式

```python
{
    'retCode':'000',
    'reMsg':'修改成功'
}
```



