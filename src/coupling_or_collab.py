import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os

# ===================== 0. 清空旧结果 =====================
for f in ["outputs/keyword_centrality.csv", "outputs/keyword_network.png"]:
    if os.path.exists(f):
        os.remove(f)

# ===================== 1. 读取数据 =====================
df = pd.read_csv(
    "data/processed/normalized_data_complete.csv",
    engine="python",
    on_bad_lines="skip"
)

# ===================== ⭐ 2. 修复关键词列（关键！） =====================
def fix_keywords(row):
    val = str(row.get("keywords", ""))
    
    # 情况1：正常关键词
    if ";" in val:
        return val
    
    # 情况2：从 abstract 找
    abstract = str(row.get("abstract", ""))
    if ";" in abstract:
        return abstract
    
    # 情况3：遍历整行（修复版）
    for v in row.values:
        v = str(v)
        if ";" in v and len(v) < 200:
            return v
    
    return None

df["keywords_fixed"] = df.apply(fix_keywords, axis=1)

print("="*50)
print("📊 修复后关键词示例：")
print(df["keywords_fixed"].dropna().head(3).tolist())
print("="*50)

# ===================== 3. 构建关键词共现网络 =====================
G = nx.Graph()

for keywords in df["keywords_fixed"].dropna():
    kw_list = [k.strip().lower() for k in keywords.split(";")]
    kw_list = [k for k in kw_list if k]

    for i in range(len(kw_list)):
        for j in range(i + 1, len(kw_list)):
            if G.has_edge(kw_list[i], kw_list[j]):
                G[kw_list[i]][kw_list[j]]["weight"] += 1
            else:
                G.add_edge(kw_list[i], kw_list[j], weight=1)

# ===================== ⭐ 4. 过滤弱连接（重要！） =====================
MIN_WEIGHT = 2

G = nx.Graph(
    (u, v, d) for u, v, d in G.edges(data=True)
    if d["weight"] >= MIN_WEIGHT
)

# 删除孤立节点
G.remove_nodes_from(list(nx.isolates(G)))

# ===================== 5. 计算中心性 =====================
degree = nx.degree_centrality(G)

df_result = pd.DataFrame({
    "keyword": list(degree.keys()),
    "degree": list(degree.values())
}).sort_values("degree", ascending=False)

df_result.to_csv("outputs/keyword_centrality.csv", index=False)

# ===================== 6. 绘图 =====================
plt.figure(figsize=(12, 8), dpi=100)
pos = nx.spring_layout(G, seed=42, k=0.5)

node_sizes = [v * 3000 for v in degree.values()]
edge_widths = [G[u][v]["weight"] * 0.5 for u, v in G.edges()]

nx.draw_networkx_nodes(G, pos, node_size=node_sizes)
nx.draw_networkx_edges(G, pos, width=edge_widths)
nx.draw_networkx_labels(G, pos, font_size=8)

plt.title("RISC-V Keyword Co-occurrence Network")
plt.axis("off")

plt.savefig("outputs/keyword_network.png", dpi=300)
plt.close()

# ===================== 7. 输出 =====================
print("✅ 关键词网络分析完成！")
print(f"🔑 关键词数量：{G.number_of_nodes()}")
print(f"🔗 共现关系：{G.number_of_edges()}")

print("\n🏆 Top 5 核心关键词：")
print(df_result.head(5).to_string(index=False))