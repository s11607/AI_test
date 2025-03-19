# AI_test

这个仓库包含使用Python编写的各种测试脚本和实用工具。

## 文件列表

### 1. hello_world.py
一个简单的多语言"Hello World"程序，支持多种语言输出：
- 英语: "Hello, World!"
- 中文: "你好，世界！"
- 日语: "こんにちは世界！"

### 2. weather.py
深圳天气信息获取工具，具有以下功能：
- 尝试从中国天气网API获取深圳实时天气数据
- 当API不可用时，自动生成合理的模拟天气数据
- 显示当天天气状况，包括温度、风向和风力等信息
- 提供感冒指数等健康提示
- 将天气数据保存为JSON格式文件
- 显示数据来源（实时API或模拟数据）

## 如何使用

### hello_world.py
直接运行脚本以查看多语言问候语：
```bash
python hello_world.py
```

### weather.py
运行前需要安装依赖：
```bash
pip install requests
```

然后执行：
```bash
python weather.py
```

程序会显示深圳当前的天气信息，并将数据保存到同目录下的`shenzhen_weather.json`文件中。即使在网络不可用或API无法连接的情况下，程序也能提供合理的天气信息。

## 依赖项
- Python 3.x
- requests (用于weather.py)
- random (Python标准库，用于生成模拟数据)
- datetime (Python标准库，用于处理日期和时间)
- json (Python标准库，用于处理JSON数据)

## 许可
MIT