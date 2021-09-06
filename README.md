# ChaoXingAutoSign
超星学习通-自动签到（ChaoXingAutoSign）
# 设置环境变量/常用的变量

> settings--->secrets

## USERNAME
学习通的账号
## PASSWORD
学习通的密码
## sleepTime
获取到签到任务后，等待多少秒进行签到（防止签到过快），单位毫秒
## SENDKEY
sever酱微信推送的sendkey

(sever酱)[https://sct.ftqq.com/]
## ADDRESS
位置签到所需的地址（不设环境变量的话，可以直接在代码中改为定值）
## ENC
二维码签到所需要的参数，因为频繁变动，设置环境变量麻烦，可以直接在代码中改动
### 获取ENC
找一个兄弟，用微信扫一扫或者其他二维码扫描工具，扫描签到的二维码，会出现一串地址，你会看到有`enc=******* `,把等于号后的字符串复制进代码中即可

# 定时任务
自己看个人需要进行修改
