import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------- 共被引矩阵构建函数 ----------------------
def build_co_citation_matrix(ref_series, ref_sep="; "):
    """
    从参考文献字段构建共被引矩阵
    :param ref_series: 文献的参考文献列（CR字段）
    :param ref_sep: 参考文献分隔符
    :return: 共被引矩阵C, 引用矩阵R
    """
    # 1. 拆分参考文献，构建引用关系表
    ref_list = []
    for idx, refs in ref_series.dropna().items():
        for r in refs.split(ref_sep):
            if r.strip():  # 过滤空值
                ref_list.append({"citing_paper": idx, "cited_ref": r.strip()})
    df_ref = pd.DataFrame(ref_list)
    
    # 2. 构建引用矩阵R（行：施引文献，列：被引文献）
    R = df_ref.pivot_table(
        index="citing_paper",
        columns="cited_ref",
        aggfunc="size",
        fill_value=0
    )
    
    # 3. 计算共被引矩阵C = R.T @ R
    C = R.T @ R
    return C, R

# ---------------------- 主函数：运行共被引分析 ----------------------
if __name__ == "__main__":
    # 读取数据
    df = pd.read_csv("data/processed/normalized_data_complete.csv")
    
    # 1. 构建共被引矩阵
    C, R = build_co_citation_matrix(df["CR"])
    
    # 2. 保存结果
    C.to_csv("outputs/co_citation_matrix.csv", encoding="utf-8-sig")
    print("✅ Lesson7 共被引矩阵构建完成！")
    print(f"📊 共被引矩阵维度：{C.shape[0]} 个被引文献 × {C.shape[1]} 个被引文献")
    print(f"📊 引用矩阵维度：{R.shape[0]} 个施引文献 × {R.shape[1]} 个被引文献")
