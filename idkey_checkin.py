"""
IDKey 签到脚本
name: IDKey签到
定时规则
cron: 0 9 * * *

变量：
 IDKEY_TOKEN: 必填，多账号使用 @ 隔开，如 'token1@token2'

抓取 https://one.idkey.cc 域名下请求，token在header的authorization中
"""

import os
import json
import requests

split_token = '@'
version = '1.0.0'

print(f'🎉 IDKey 签到 🎉')
print(f'🎉 版本: {version} 🎉')
print(f'🎉 作者: todrfu 🎉')
print(f'🎉 更新时间: 2026-01-26 🎉')

print('\n============📣初始化📣============\n')

TOKEN_NAME = 'IDKEY_TOKEN'


# 发送通知消息
def send_notification_message(message):
    try:
        from notify import send

        send('IDKey 签到', message)
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


def sign_in(token):
    """
    签到
    params:
        token: 用户token
    """

    url = 'https://one.idkey.cc/api/user/checkin'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': token,
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'Referer': 'https://one.idkey.cc/'
    }

    response = requests.post(url, headers=headers)

    try:
        data = response.json()
        message = data.get('message', '')
    except json.JSONDecodeError:
        print("响应不是有效的JSON格式")
        print(f"响应内容: {response.text}")
        return

    if response.status_code == 200:
        # 根据实际响应判断成功或失败
        if data.get('code') == 0 or data.get('success') or 'success' in str(data).lower():
            msg = f'🎉 签到成功 🎉'
        else:
            msg = f'🎉 签到异常: {message or data} 🎉'
    else:
        msg = f'🎉 签到失败: HTTP {response.status_code} - {message or response.text} 🎉'

    print(msg)
    send_notification_message(msg)


def main():
    """
    开始执行任务
    """
    token = get_token()

    if not token:
        print(f'🎉 请设置{TOKEN_NAME}环境变量 🎉')
        exit(1)

    tokens = token.split(split_token)

    for token in tokens:
        # 其中一个出错后，继续执行下一个
        try:
            sign_in(token.strip())
        except Exception as e:
            print(f'🎉 签到失败: {e} 🎉')


if __name__ == '__main__':
    main()
