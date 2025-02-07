"""
通义万相
name: 通义万相
定时规则
cron: 30 9 * * *

变量：
TONGYI_COOKIE: 必填，多账号使用 @ 隔开，如 'cookie1@cookie2'
"""

import os
import json
import requests


version = '0.0.1'
app_name = '通义万相'
author = 'todrfu'
update_time = '2025-02-07'

print(f'🎉 {app_name} 🎉')
print(f'🎉 版本: {version} 🎉')
print(f'🎉 作者: {author} 🎉')
print(f'🎉 更新时间: {update_time} 🎉')

print('\n============📣初始化📣============\n')

TOKEN_NAME = 'TONGYI_COOKIE'


# 发送通知消息
def send_notification_message(message):
    try:
        from notify import send

        send(f'{app_name}', message)
    except Exception as e:
        if e:
            print('发送通知消息失败！')


def get_token():
    """
    获取用户token
    return:
        token: 用户token
    """

    token = os.getenv(TOKEN_NAME)
    return token

def sign_in(cookie):
    """
    签到
    params:
        token: 用户token
    """
    url = 'https://wanxiang.aliyun.com/wanx/api/common/inspiration/dailySignReward'
    headers = {
        'cookie': cookie,  # 改为字符串
        'priority': 'u=1, i',
        'x-platform': 'web',
        'content-type': 'application/json',
    }

    response = requests.post(url, json={}, headers=headers)
    
    try:
        data = response.json()
        message = data.get('message')
    except json.JSONDecodeError:
        print("响应不是有效的JSON格式")
        return
    
    if (data.get('httpCode') == 200):
        msg = f'🎉 签到成功 🎉 '
    else:
        msg = f'🎉 签到异常: {message} 🎉'

    print(msg)
    send_notification_message(msg)

def doTask():
    """
    开始执行任务
    """
    token = get_token()

    if not token:
        print(f'🎉 请设置{TOKEN_NAME}环境变量 🎉')
        exit(1)

    tokens = token.split('@')

    for token in tokens:
        # 其中一个出错后，继续执行下一个
        try:
            sign_in(token)
        except Exception as e:
            print(f'🎉 签到失败: {e} 🎉')


if __name__ == '__main__':
    doTask()