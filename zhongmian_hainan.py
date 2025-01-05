"""
中免海南商城
name: 中免海南
定时规则
cron: 30 9 * * *

变量：
ZHONGMIAN_CK: 必填，多账号使用 @ 隔开，如 'token1@token2'

捉 https://service.cdfhnms.com 域名下请求，token在header中
"""

import os
import json
import requests

split_token = '@'
version = '1.0.0'

print(f'🎉 中免海南商城免税店 🎉')
print(f'🎉 版本: {version} 🎉')
print(f'🎉 作者: todrfu 🎉')
print(f'🎉 更新时间: 2025-01-04 🎉')

print('\n============📣初始化📣============\n')

TOKEN_NAME = 'ZHONGMIAN_TOKEN'


# 发送通知消息
def send_notification_message(message):
    try:
        from notify import send

        send('中免海南商城免税店', message)
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

    url = 'https://service.cdfhnms.com/api/inc/signin/submit'
    headers = {
        'terminalId': '11',
        'stockId': '6868',
        'appToken': None,
        # 不校验，此处随便写的
        'openid': 'oKweDiDTiEz7Eq9xkOjxggrCSwXTC',
        'cloudType': None,
        'subsiteId': '10',
        'txfp': None,
        'appVersion': '10.10.52',
        'warehouseId': '10',
        'nativeVersion': '10.10.45',
        'channelType': 'big_frontend_weapp',
        'appTerminalId': None,
        'token': token,
        'apiVersion': '2.0',
        # 不校验，此处随便写的
        'anonymousId': '1735573443718-8522633-01ceb6bf2cbd116-28733585',
        'Appkey': '850226', 
        'clickId': None,
        # 不校验，此处随便写的
        'fpp': '8423cda43ab57aa1fda86446e5cdc063-1735704528162',
        # 不校验，此处随便写的
        'unique': 'weapp-2024123023440378011214825364258085293',
        'txfpCode': None,
        'content-type': 'application/json',
        'channelId': None
    }

    response = requests.get(url, headers=headers)
    
    try:
        data = response.json()
        message = data.get('message')
    except json.JSONDecodeError:
        print("响应不是有效的JSON格式")
        return
    
    if (data.get('code') == 0):
        msg = f'🎉 签到成功 🎉 '
    else:
        msg = f'🎉 签到异常: {message} 🎉'

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
            sign_in(token)
        except Exception as e:
            print(f'🎉 签到失败: {e} 🎉')


if __name__ == '__main__':
    main()
