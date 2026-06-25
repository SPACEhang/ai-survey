import json
import matplotlib.pyplot as plt
from collections import Counter

# 读取问卷数据
DATA_FILE = "data.json"
with open(DATA_FILE, "r", encoding="utf-8") as f:
    data_list = json.load(f)

if len(data_list) == 0:
    print("暂无问卷数据，请先填写问卷！")
else:
    # 1. 基础统计
    total = len(data_list)
    gender_list = [item["gender"] for item in data_list]
    ai_attitude_list = [item["like_ai"] for item in data_list]
    age_list = [int(item["age"]) for item in data_list]

    gender_count = Counter(gender_list)
    attitude_count = Counter(ai_attitude_list)
    avg_age = sum(age_list) / len(age_list)

    # 2. 打印文字分析报告
    print("="*50)
    print("问卷数据分析报告")
    print("="*50)
    print(f"总填写人数：{total} 人")
    print(f"平均年龄：{avg_age:.1f} 岁")
    print("\n【性别分布】")
    for g, num in gender_count.items():
        rate = num / total * 100
        print(f"{g}：{num}人，占比 {rate:.1f}%")
    print("\n【对AI发展态度分布】")
    for att, num in attitude_count.items():
        rate = num / total * 100
        print(f"{att}：{num}人，占比 {rate:.1f}%")
    print("="*50)

    # 3. 绘制两张统计图（饼图+柱状图）
    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文乱码
    plt.rcParams["axes.unicode_minus"] = False

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # 左图：性别饼图
    ax1.pie(gender_count.values(), labels=gender_count.keys(), autopct="%.1f%%", colors=["#66a3ff", "#ff99cc"])
    ax1.set_title("问卷填写者性别分布")

    # 右图：AI态度柱状图
    ax2.bar(attitude_count.keys(), attitude_count.values(), color="#44bb77")
    ax2.set_title("大众对AI发展态度统计")
    ax2.set_ylabel("人数")

    plt.tight_layout()
    plt.savefig("问卷统计图表.png", dpi=300)
    plt.show()
    print("\n图表已保存为：问卷统计图表.png")