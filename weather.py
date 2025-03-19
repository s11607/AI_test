#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def get_shenzhen_weather():
    """
    获取深圳今天的天气信息
    返回包含天气数据的字典
    """
    # 使用天气API获取深圳天气
    url = "http://wthrcdn.etouch.cn/weather_mini?city=深圳"
    
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        
        # 检查请求是否成功
        if response.status_code == 200:
            weather_data = response.json()
            
            # 提取今天的天气信息
            if weather_data.get("status") == 1000:
                data = weather_data.get("data", {})
                today = data.get("forecast", [])[0] if data.get("forecast") else {}
                
                # 构建天气信息字典
                weather_info = {
                    "城市": data.get("city", "深圳"),
                    "日期": today.get("date", datetime.now().strftime("%Y-%m-%d")),
                    "天气": today.get("type", "未知"),
                    "最高温度": today.get("high", "").replace("高温 ", ""),
                    "最低温度": today.get("low", "").replace("低温 ", ""),
                    "风向": today.get("fengxiang", "未知"),
                    "风力": today.get("fengli", "").replace("<![CDATA[", "").replace("]]>", ""),
                    "当前温度": data.get("wendu", "未知") + "℃",
                    "感冒指数": data.get("ganmao", "未知"),
                    "获取时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                return weather_info
            else:
                return {"错误": "无法获取天气数据", "状态码": weather_data.get("status")}
        else:
            return {"错误": "请求失败", "状态码": response.status_code}
            
    except Exception as e:
        return {"错误": f"获取天气时出现异常: {str(e)}"}

def save_weather_to_file(weather_info, filename="shenzhen_weather.json"):
    """
    将天气信息保存到文件
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(weather_info, f, ensure_ascii=False, indent=4)
        print(f"天气信息已保存到 {filename}")
    except Exception as e:
        print(f"保存文件时出错: {str(e)}")

def print_weather(weather_info):
    """
    打印天气信息
    """
    print("\n" + "="*30)
    print(f"深圳天气信息 ({weather_info.get('获取时间', '未知时间')})")
    print("="*30)
    
    if "错误" in weather_info:
        print(f"获取天气失败: {weather_info.get('错误')}")
        return
        
    print(f"城市: {weather_info.get('城市', '深圳')}")
    print(f"日期: {weather_info.get('日期', '未知')}")
    print(f"天气: {weather_info.get('天气', '未知')}")
    print(f"当前温度: {weather_info.get('当前温度', '未知')}")
    print(f"温度范围: {weather_info.get('最低温度', '未知')} ~ {weather_info.get('最高温度', '未知')}")
    print(f"风向: {weather_info.get('风向', '未知')}")
    print(f"风力: {weather_info.get('风力', '未知')}")
    
    if "感冒指数" in weather_info:
        print(f"健康提示: {weather_info.get('感冒指数', '未知')}")
    
    print("="*30 + "\n")

if __name__ == "__main__":
    print("获取深圳今天的天气信息...")
    weather_info = get_shenzhen_weather()
    print_weather(weather_info)
    
    # 可选：将天气信息保存到文件
    save_weather_to_file(weather_info)
