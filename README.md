
# ChaoXingAutoSign
超星学习通-自动签到（ChaoXingAutoSign），原作者已经不更新，我修改了登录模块可以用了，但是目前手上没有课程给我签到，所以无法验证签到是否正常
# 设置环境变量/常用的变量

> settings--->secrets

## USERNAME
学习通的账号
## PASSWORD
学习通的密码
## sleepTime
获取到签到任务后，等待多少秒进行签到（防止签到过快），单位毫秒.

GitHub有一定延迟，所以可以不用设置sleepTime
## SENDKEY
sever酱微信推送的sendkey

[sever酱](https://sct.ftqq.com/)
## ADDRSS
位置签到所需的地址（不设环境变量的话，可以直接在代码中改为定值）
## ~~ENC（已废弃）~~

~~已经无需填写~~

由于enc已经不能从接口直接获得，需要自己手动填写，所以我觉得这个项目也没什么必要了

### 获取ENC
找一个兄弟，用微信扫一扫或者其他二维码扫描工具，扫描签到的二维码，会出现一串地址，你会看到有`enc=******* `,把等于号后的字符串复制进代码中即可

# 定时任务
actions启用Workflows

/.github/workflows/main.yml中的cron部分，去除schedule和cron前面的井号#

定时任务，每5分钟运行一次（UTC时间）
```
- cron: '*/5 * * * *'
```

