# 自用青龙面板脚本

## 🚀 订阅方式

### 方式一：通过青龙面板订阅（推荐）

1. 登录青龙面板
2. 进入 **订阅管理** → **新建订阅**
3. 填写以下信息：

```
名称: qinglong-scripts
类型: 公开仓库
链接: https://github.com/todrfu/qinglong-scripts
分支: main
白名单: .*\.py$
黑名单: notify\.py$
依赖文件: notify.py,requirements.txt
```

4. 点击 **确定** 保存
5. 点击 **运行** 执行订阅，脚本将自动拉取并创建定时任务

### 方式二：通过命令订阅

在青龙面板的 **定时任务** 中新建任务，执行以下命令：

```bash
ql repo https://github.com/todrfu/qinglong-scripts.git ".*\.py$" "notify\.py$" "notify.py|requirements.txt" "main"
```

## 📋 依赖安装

脚本依赖的 Python 包已列在 `requirements.txt` 中，青龙面板会自动安装。主要依赖：

- `requests` - HTTP 请求库

## ⚠️ 免责声明

本项目仅供学习交流使用，不得用于商业用途。

如果本项目中使用的任何内容侵犯了您的权益，请及时联系删除相关内容。
