# 今日校园/辅导猫 API

**⚠️注意：本项目仅供学习交流使用，如作他用所承受的任何直接、间接法律责任一概与作者无关（下载使用即代表你同意上述观点）**

若无意侵犯到您的权益，请立即联系我删除相关内容

# 接口列表

* 登录接口 - `login.py`
* 同学列表接口 - `find_student.py`
* 同学圈动态接口 - `fresh_list.py`
* 同学圈热门动态接口 - `hot_fresh_list.py`
* 今日红人榜接口 - `hot_list.py`
* 其他接口随缘更新 🛏️💤

# 依赖库

* requests
* bs4
* Java 8 或者更新的环境，要保证命令行中执行 `jar` 是没问题的

# 登录接口使用说明

请打开 `config.py` 按照顺序依次操作

其中学校的参数可以 [在这里](https://www.cpdaily.com/v6/config/guest/tenant/list) 获取

或者参考项目中的 `tenant_list.json` 也行，但不保证是最新的

登录成功，拿到 sessionToken 后

将 `config.py` 的 sessionToken 填好，其他的接口就能用了（应该

# FAQ

## 这项目有啥用？

请开动你的小脑筋 🤦‍

## 为啥需要 Java 环境？

编码 iap，获取 ticket，详细请看 `login.py` 的第 3 阶段

## 项目里的 cpdaily-api-encoder.jar 开源吗？

https://github.com/jerryshell/cpdaily-api-encoder

# Screenshot

打码是因为敏感信息太多，看个意思就行了

## 登录

![login](./screenshot/login.jpg)

## 同学圈热门动态

![hot_fresh_list](./screenshot/hot_fresh_list.jpg)
