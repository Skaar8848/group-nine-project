# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# 设置中文字体（避免图表中文乱码）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取去重后的数据（你的文件名是“去重后数据.csv”）
FILE_PATH = "去重后数据.csv"
df = pd.read_csv(FILE_PATH, encoding='utf-8-sig')  # 解决中文乱码

# ===================== 1. 时间分布分析（核心） =====================
# 清洗年份字段，转为数字格式
df["PY"] = pd.to_numeric(df["PY"], errors="coerce")
# 按年份统计文献数量
year_count = df["PY"].value_counts().sort_index()

# 绘制时间趋势折线图
plt.figure(figsize=(12, 6))
year_count.plot(kind="line", color="#2E86AB", linewidth=3, marker='o', markersize=6)
plt.title("RISC-V领域文献发表时间趋势（2017-2026）", fontsize=14, pad=20)
plt.xlabel("发表年份", fontsize=12)
plt.ylabel("文献数量", fontsize=12)
plt.grid(alpha=0.3, linestyle='--')
plt.xticks(year_count.index, rotation=0)  # 显示所有年份
plt.tight_layout()
plt.savefig("time_trend.png", dpi=300, bbox_inches="tight")
plt.close()
print("✅ 生成时间趋势图：time_trend.png")

# ===================== 2. 高频关键词分析 =====================
# 提取关键词（KW字段），拆分多关键词
if "KW" in df.columns:
    # 拆分分号分隔的关键词，去除空值
    keywords = df["KW"].str.split("; ").explode().dropna()
    # 过滤无意义的停用词
    stop_words = ["the", "and", "of", "in", "for", "with", "a", "to", "on", "is"]
    keywords_clean = [kw.strip() for kw in keywords if kw.strip() not in stop_words and len(kw.strip())>2]
    # 统计Top10高频关键词
    top10_keywords = Counter(keywords_clean).most_common(10)
    
    # 绘制关键词柱状图
    plt.figure(figsize=(12, 6))
    kw_names = [k[0] for k in top10_keywords]
    kw_counts = [k[1] for k in top10_keywords]
    plt.bar(kw_names, kw_counts, color="#A23B72", alpha=0.8)
    plt.title("RISC-V领域高频关键词（Top10）", fontsize=14, pad=20)
    plt.xlabel("关键词", fontsize=12)
    plt.ylabel("出现次数", fontsize=12)
    plt.xticks(rotation=45, ha="right")  # 旋转标签避免重叠
    plt.tight_layout()
    plt.savefig("top10_keywords.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("✅ 生成高频关键词图：top10_keywords.png")
else:
    print("⚠️ 无KW字段，跳过关键词分析")

# ===================== 3. 核心作者分析 =====================
if "AU" in df.columns:
    # 统计Top10核心作者（发表文献数）
    top10_authors = df["AU"].value_counts().head(10)
    
    # 绘制作者柱状图
    plt.figure(figsize=(12, 6))
    top10_authors.plot(kind="bar", color="#F18F01", alpha=0.8)
    plt.title("RISC-V领域核心作者（Top10）", fontsize=14, pad=20)
    plt.xlabel("作者", fontsize=12)
    plt.ylabel("发表文献数", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("core_authors.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("✅ 生成核心作者图：core_authors.png")
else:
    print("⚠️ 无AU字段，跳过作者分析")

# ===================== 输出统计结果（用于报告） =====================
print("\n===== Lesson4 核心统计结果 =====")
print(f"1. 总文献数：{len(df)} 篇")
print(f"2. 时间范围：{int(year_count.index.min())} - {int(year_count.index.max())} 年")
print(f"3. 最高产年份：{year_count.idxmax()} 年（{year_count.max()} 篇）")
if "KW" in df.columns and len(keywords_clean)>0:
    print(f"4. 最热门关键词：{top10_keywords[0][0]}（{top10_keywords[0][1]} 次）")
if "AU" in df.columns:
    print(f"5. 核心作者：{top10_authors.index[0]}（{top10_authors.iloc[0]} 篇）")

print("\n🎉 所有可视化图表已生成！可直接用于Lesson4分析报告。")