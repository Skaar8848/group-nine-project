# -*- coding: utf-8 -*-
import pandas as pd

# 你的文件
FILE_PATH = "wos_riscv_2015-2026_raw.ris"

# 读取RIS
def read_ris(file):
    ris_data = []
    entry = {}
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if line.startswith("TY"):
                if entry:
                    ris_data.append(entry)
                entry = {}
            if line.startswith("ER"):
                ris_data.append(entry)
                entry = {}
            if " - " in line:
                parts = line.split(" - ", 1)
                if len(parts) == 2:
                    entry[parts[0].strip()] = parts[1].strip()
    return pd.DataFrame(ris_data)

# 运行
df = read_ris(FILE_PATH)
total = len(df)

# 去重
df_dedup = df.drop_duplicates(subset=["DO", "TI"], keep="first")
duplicates = total - len(df_dedup)

# 保存去重后的文件 👇👇👇
df_dedup.to_csv("去重后数据.csv", index=False, encoding="utf-8-sig")

# 输出结果
print("====== 完成 ======")
print(f"原始：{total}")
print(f"重复：{duplicates}")
print(f"去重后：{len(df_dedup)}")
print("✅ 去重文件已生成：去重后数据.csv")