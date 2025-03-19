#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from datetime import datetime
import random

def get_shenzhen_weather():
    """
    获取深圳今天的天气信息
    由于API可能不稳定，这个版本会生成模拟数据
    返回包含天气数据的字典
    """
    try:
        # 尝试从API获取天气数据
        url = "http://wthrcdn.etouch.cn/weather_mini?city=深圳"
        response = requests.get(url, timeout=5)
        response.encoding = 'utf-8'
        
        # 如果请求成功并且返回了有效数据，使用真实数据
        if response.status_code == 200:
            weather_data = response.json()
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
                    "获取时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "数据来源": "实时API"
                }
                return weather_info
    except Exception as e:
        # 如果API请求失败，记录错误但继续使用模拟数据
        print(f"API请求失败: {str(e)}")
        print("将使用模拟数据代替")
    
    # 生成模拟的天气数据
    return generate_mock_weather_data()

def generate_mock_weather_data():
    """
    生成模拟的深圳天气数据
    在API不可用时使用
    """
    # 当前日期
    current_date = datetime.now()
    date_str = current_date.strftime("%Y-%m-%d")
    time_str = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # 深圳天气类型列表
    weather_types = ["晴", "多云", "阴", "小雨", "中雨", "大雨", "雷阵雨"]
    weather_type = random.choice(weather_types)
    
    # 深圳3月份的气温范围(摄氏度)
    current_temp = random.randint(18, 28)
    min_temp = random.randint(15, 21)
    max_temp = random.randint(current_temp, 30)
    
    # 风向
    wind_directions = ["东风", "南风", "西风", "北风", "东南风", "西南风", "东北风", "西北风"]
    wind_direction = random.choice(wind_directions)
    
    # 风力
    wind_powers = ["1级", "2级", "3级", "4级", "5级"]
    wind_power = random.choice(wind_powers)
    
    # 感冒指数提示
    ganmao_tips = [
        "天气舒适，不易发生感冒，请放心出门活动。",
        "天气转凉，易发生感冒，请适当增加衣物。",
        "天气较热，容易中暑，请注意防暑降温。",
        "相对今天出现了较大的温差，较易发生感冒，请注意适当增减衣服。",
        "天气寒冷，易发生感冒，请注意保暖。"
    ]
    ganmao = random.choice(ganmao_tips)
    
    # 构建模拟数据
    weather_info = {
        "城市": "深圳",
        "日期": date_str,
        "天气": weather_type,
        "最高温度": f"{max_temp}℃",
        "最低温度": f"{min_temp}℃",
        "风向": wind_direction,
        "风力": wind_power,
        "当前温度": f"{current_temp}℃",
        "感冒指数": ganmao,
        "获取时间": time_str,
        "数据来源": "模拟数据"
    }
    
    return weather_info

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
    
    if "数据来源" in weather_info:
        print(f"数据来源: {weather_info.get('数据来源', '未知')}")
    
    print("="*30 + "\n")

if __name__ == "__main__":
    print("获取深圳今天的天气信息...")
    weather_info = get_shenzhen_weather()
    print_weather(weather_info)
    
    # 将天气信息保存到文件
    save_weather_to_file(weather_info)
