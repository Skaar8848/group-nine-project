# group-nine-project
组长：赵方韧 组员：李晨，张天瑞，马飞扬

分工：
1.赵方韧 ：技术开发

   负责项目工程化落地，保障可复现性，是团队技术核心
   初始化 GitHub 仓库，配置目录结构、.gitignore、LICENSE，维护版本管理
   搭建 Python/Conda 环境，编写 requirements.txt，提供一键运行命令
   编写数据读入、质量检查、筛选流程的脚本（src/），调试核心 Python 库
   协助其他岗位解决数据处理、文档格式等技术问题
   
2.李晨：数据处理

   负责从检索到筛选的全流程数据工作
   拆解研究问题，编写 / 优化检索式，维护同义词表、检索变更日志
   从选定数据库导出数据，勾选核心字段，记录导出参数 / 时间戳
   去重、补全缺失字段、消歧（作者 / 机构），按 raw/processed 分类存放
   运行质量脚本，统计缺失率 / 重复率，撰写 data_quality.md，更新字段字典
   按规则完成文献初筛 / 复筛，标注 Reason Code，输出 screening.csv，更新 PRISMA 图
   
3.张天瑞：文档撰写

   负责所有文档撰写与成果整合
   构建证据链，撰写 novelty_search_v0.md，分析研究空白并标注支撑文献
   汇总各阶段成果，撰写 M1/M2/M3 里程碑报告，整理 QC 自检清单结果
   用 Zotero+BibTeX 管理文献，规范引用格式，避免引用错误
   基于计量分析结果，起草 mini review（6-8 页）的核心内容
   
4.马飞扬：可视化与分析

   专注计量分析与可视化
   负责知识图谱构建
   用 CiteSpace/VOSviewer 做可视化分析，输出图表并标注参数
   分析前沿趋势 / 里程碑论文，整理计量分析结果，为综述提供数据支撑
   撰写计量分析产出报告
   
研究方向（核心：RISC-V CPU架构与研究 文献计量学）

核心目标

基于 Web of Science/Scopus/IEEE Xplore 等数据库的 RISC-V 相关文献，完成全维度计量分析，回答以下核心问题：
RISC-V CPU 领域近 10 年的全球发文趋势与区域研究特征；
该领域的核心研究机构、高产出作者及合作网络；
关键词共现与突现分析，识别研究热点（如 RISC-V+FPGA / 低功耗 / AI 加速）；
高被引里程碑论文与领域发展脉络。

分析维度

表格

分析类型	核心方法	工具 / 库

发文趋势分析	年度 / 区域 / 文献类型分布	pandas/matplotlib

合作网络分析	作者 / 机构 / 国家合作网络	VOSviewer/networkx

热点主题分析	关键词共现、聚类、突现检测	CiteSpace/pybliometrics

影响力分析	高被引论文、期刊分区分析	bibliometrix

数据来源

核心数据库：Web of Science Core Collection（2015-2026）

补充数据库：Scopus、IEEE Xplore

文献类型：期刊论文、会议论文、综述（排除会议摘要、编辑稿）

项目计划（贴合文献计量学课程进度）

阶段 1：项目初始化与环境搭建（第 1-2 周）

完成 GitHub 仓库标准化搭建（data//src//outputs//reports//paper/）；

配置 conda 环境，生成environment.yml和requirements.txt（锁定 bibliometrix/pybliometrics 等库版本）；

明确团队分工，完成《方向与开源项目候选表》归档至docs/目录。

阶段 2：文献检索与数据预处理（第 3-4 周）

构建 RISC-V CPU 领域精准检索式：("RISC-V" OR "RISC V") AND ("CPU" OR "processor" OR "chip" OR "instruction set")；

导出原始文献数据（格式：RIS/TXT），归档至data/raw/；

完成数据清洗（去重、剔除无关文献），归档至data/processed/，更新query_changelog.md记录检索式迭代。

阶段 3：核心计量分析与可视化（第 5-8 周）

基础分析：完成发文量趋势、作者 / 机构排名分析，代码归档至src/basic_analysis.py；

网络分析：绘制作者 / 机构合作网络、关键词共现图谱，结果归档至outputs/figures/；

前沿分析：用突现检测识别近期研究热点，输出outputs/trend_analysis.md。

阶段 4：成果整理与报告撰写（第 9-11 周）

撰写《RISC-V CPU 领域文献计量学分析报告》，归档至reports/；

完成 mini review（学术综述），归档至paper/；

验证所有分析结果的可复现性（重新运行src/run_all.py，核对输出结果）。

阶段 5：项目归档与提交（第 12 周）

整理仓库所有文件，确保data/（原始 + 清洗后数据）、src/（完整代码）、outputs/（所有结果）无缺失；

完善 README.md 和变更日志，提交最终版本至 GitHub；

准备课程答辩材料（PPT 归档至reports/slides/）。



## Lesson 2检索式设计

完成 RISC-V CPU 研究方向的检索式设计。

完成内容：
- config/query.yaml （检索式配置）
- config/synonyms.yaml （关键词同义词）
- reports/query_changelog.md （检索式修改记录）

该检索式将用于 Lesson3 和 Lesson4 的文献检索与筛选。
溯源内容：
**检索式配置**: [`config/query.yaml`](config/query.yaml) —— 包含对象(Object)、方法(Method)及限定条件(Constraint)的参数化定义 [cite: 8, 10]。
**同义词维护**: [`config/synonyms.yaml`](config/synonyms.yaml) —— 针对 RISC-V、处理器架构等核心术语的扩展词表 [cite: 8, 9]。
**变更日志**: [`reports/query_changelog.md`](reports/query_changelog.md) —— 记录了检索式从 v0.1 到当前版本的优化轨迹及修订原因 。


### Lesson2课后日志：检索式设计与优化
在lesson3的完成过程中， 小组讨论发现目前的检索式所检索出的内容样本太少，故优化了布尔逻辑
本项目针对 RISC-V CPU 研究方向设计文献检索式，并进行了优化。

主要工作：
- 构建 RISC-V 相关关键词集合
- 设计布尔逻辑检索结构
- 在 query.yaml 中配置检索式
- 在 query_changelog.md 中记录检索策略优化过程



## Lesson 3完成文献检索与数据获取

使用优化后的检索式在 Web of Science 进行文献检索:
- 成功导出 RIS 格式原始数据，文件名为 wos_riscv_2015-2026_raw.ris
- 完成 GitHub 仓库文件管理

将原始 RIS 文件上传至仓库 data/raw/ 目录:
- 创建 data/processed/ 目录用于存放清洗后的数据
- 完成数据质量检查与清洗

使用 Python 脚本对文献数据进行自动化处理:
- 基于 DOI 和标题完成文献去重
- 检查关键字段缺失情况（标题、作者、DOI、年份、期刊、参考文献）
- 生成去重后的干净数据集并保存为 CSV 格式[去重后数据.csv](https://github.com/user-attachments/files/26166009/default.csv)


编写项目文档（3 个必备文件）:
- 完成 data/README.md：说明数据来源、检索式、目录结构
- 完成 data/field_dictionary.md：定义 RIS 各字段含义
- 完成 reports/data_quality.md：记录数据统计结果与质量评估

完成仓库规范化整理:
- 将所有数据、脚本、文档上传至 GitHub
- 保证项目结构清晰、可复现、符合课程要求

此外经过与本组同学的探讨
通过增加 RV32、RV64、RISC-V ISA 等关键词，检索文献数量显著增加，为后续 Lesson3 和 Lesson4 的文献筛选与分析提供数据基础。


## Lesson 4 文献计量分析任务
数据预处理与校验：
- 确认 Lesson 3 输出文件：去重后数据.csv（共 471 条有效文献，时间范围 2017-2026 年）
- 校验字段完整性：核心字段 PY（年份）、AU（作者）、KW（关键词）均完整可用
- 数据质量：无重复文献，字段格式规范，可直接用于可视化分析

可视化脚本开发与执行：
- 编写脚本 lesson4_visualization.py，实现三类核心分析：
- 时间趋势分析：绘制 2017-2026 年文献发表量折线图，输出 time_trend.png
- 高频关键词分析：提取 Top10 关键词并绘制柱状图，输出 top10_keywords.png
- 核心作者分析：统计 Top10 高产作者并绘制柱状图，输出 core_authors.png
- 脚本运行成功：依赖库（pandas/matplotlib）加载正常，图表生成完整，分辨率 300dpi 符合课程要求

分析报告撰写
- 新建报告文件 lesson4_analysis_report.md，结构化呈现分析结果：
- 数据基础：明确数据源、规模与时间范围
- 核心分析：结合三张图表，解读研究趋势、热点方向与核心研究力量
- 整体结论：总结 RISC-V 领域研究热度、热点与人才梯队，并展望未来方向
- 图表嵌入：采用 GitHub 原始链接格式，确保报告可跨设备访问

仓库同步与版本管理
- 将脚本、报告与三张图表上传至 reports/ 目录
- 提交信息：Update lesson4_analysis_report，完成版本留存
- 校验仓库文件：所有交付物均已上传，路径规范，可正常访问


关键成果
- 可视化产出：3 张专业图表（时间趋势、高频关键词、核心作者）
- 分析报告：完整结构化文档，清晰呈现 RISC-V 领域研究全貌
- 仓库交付：所有文件已同步至 GitHub，符合课程作业提交规范


问题：GitHub Markdown 预览中图片暂未渲染
- 解决：确认图片文件完好、链接有效，属于 GitHub 缓存 / 渲染延迟问题，不影响作业交付

## week5课后修正：补充lesson3与lesson4的完成报告
一、 项目背景与任务目标
- 本项目围绕 RISC-V 领域文献计量分析 展开，承接 Lesson 3 数据清洗成果，完成可视化分析与报告撰写。核心目标是通过 Python 对文献数据进行统计分析，生成专业图表，并撰写完整的 GitHub 分析报告。


二、 Lesson 3：数据清洗与预处理
- 数据来源：基于 Web of Science 检索的 RISC-V 领域文献原始数据。
- 清洗操作：利用 Python 脚本读取原始数据，进行去重处理（去除重复文献）。规范数据格式，清洗无效字段与缺失值。筛选保留核心分析字段：PY（发表年份）、AU（作者）、KW（关键词）、TI（标题）等。
- **交付成果：生成清洗后的核心数据文件 去重后数据.csv，总计 471 篇有效文献，时间覆盖 2017-2026 年，为后续分析提供高质量数据集。**


三、 Lesson 4：可视化分析与报告撰写（核心交付）
- 可视化开发（lesson4_visualization.py）：
环境配置：解决 Python 环境依赖问题，成功安装并导入 pandas（数据处理）与 matplotlib（绘图）库。
- 多维度分析：
- 时间趋势分析：统计年度文献量，绘制折线图（time_trend.png），发现 2025 年为研究峰值（136 篇）。
- 关键词分析：提取高频关键词，绘制 Top10 柱状图（top10_keywords.png），识别研究热点。
- 作者分析：统计高产作者，绘制核心作者图（core_authors.png），定位领域领军人物。
报告撰写（lesson4_analysis_report.md）：
- 内容结构：涵盖数据基础、时间分布、关键词分析、作者分析及整体结论五大模块。
- 内容亮点：结合图表数据，深入分析 RISC-V 领域研究热度、技术热点（如低功耗、SoC 开发）及人才梯队结构。
- **仓库同步：将报告、脚本及三张图表完整上传至 GitHub reports/ 目录，确保文件可访问。**


四、 关键成果与亮点
- 数据完整：Lesson 3 完成了 471 篇文献的高质量清洗。
- 分析深入：Lesson 4 生成了三张专业可视化图表，分析结论准确反映了 RISC-V 领域的发展现状。
- 交付规范：所有文件已同步至 GitHub，符合课程提交规范，报告结构清晰，逻辑严谨。

五、 总结
本次 Lesson 3 至 Lesson 4 流程顺利，完整实现了 "数据清洗 -> 可视化分析 -> 报告撰写" 的端到端流程。交付物符合课程要求，具备良好的学术展示价值。

## Lesson 5 图数据模型与数据质量分析

完成内容：
- docs/data_model.md：图数据模型草图，明确节点类型/属性、边类型/权重/方向性，附示例数据
- docs/classroom_exercise.md：课堂实操练习，手算共被引边权重，掌握Cosine、Jaccard相似度计算
- params.md：网络定义参数，包括节点类型、边类型、阈值参数等
- cleaning_rules.md：数据清洗与消歧规则，版本化管理
- reports/data_quality.md：数据质量报告，详细分析数据完整性
- reports/query_rationale.md：产出记录，记录决策过程和依据
- data/processed/normalized_data_complete.csv：标准化的文献数据
- reports/field_missing_rate.md：数据字段缺失率报告
- reports/lotka_law_summary.md：Lotka定律总结

具体工作：
1. **图数据模型设计**：创建了包含论文、作者、关键词、期刊的节点类型，以及作者-论文、论文-关键词、论文-期刊、论文引用、作者合作、关键词共现、论文共被引的边类型，明确了权重计算方法和方向性。

2. **课堂实操练习**：完成了共被引边权重手算示例，掌握了Cosine和Jaccard相似度计算方法，理解了Top-N和Min Weight阈值选择逻辑。

3. **交付物自检**：按QC清单完成交付物自检，将网络定义写入params.md，清洗/消歧规则版本化至cleaning_rules.md，设计了阈值敏感性对照实验。

4. **数据质量分析**：输出了详细的数据质量报告和字段缺失率报告，分析了数据完整性和一致性，评估了数据质量等级。

5. **产出记录**：编写了完整的产出记录，记录了项目概述、数据处理流程、决策依据、产出内容、技术实现、质量保证和结论建议。

6. **数据整理**：将文献数据整理为统一的pandas DataFrame表结构，标准化了数据格式和字段。

7. **经典定律总结**：撰写了Lotka定律的内涵及其应用局限的总结，为文献计量学分析提供理论基础。

交付成果：
- 图数据模型文件：docs/data_model.md
- 课堂练习文件：docs/classroom_exercise.md
- 网络参数文件：params.md
- 清洗规则文件：cleaning_rules.md
- 数据质量报告：reports/data_quality.md
- 产出记录：reports/query_rationale.md
- 标准化数据：data/processed/normalized_data_complete.csv
- 字段缺失率报告：reports/field_missing_rate.md
- 经典定律总结：reports/lotka_law_summary.md

关键成果：
- 建立了完整的图数据模型，为后续网络分析提供基础
- 掌握了共被引边权重计算和相似度分析方法
- 完成了数据质量评估和字段缺失率分析
- 建立了标准化的数据处理流程和清洗规则
- 为文献计量学分析提供了理论基础和实践指导


---

# Lesson 6 文献计量指标体系与计算分析

完成内容：

reports/metrics_spec.md：文献计量指标规范文档，定义数量指标、影响力指标、归一化方法及项目口径
src/metrics_calc.py：指标计算代码，实现年度发文趋势、作者发文量、总被引、篇均被引、h指数计算
outputs/year_trend.csv：年度发文趋势统计结果
outputs/author_metrics.csv：作者发文量、总被引、h指数、篇均被引指标表
reports/metrics_analysis.md：文献计量指标分析报告，包含趋势、影响力、格局解读与局限性说明

具体工作：

指标体系设计：构建包含发文量、增长率、总被引、篇均被引、h指数在内的完整指标体系，明确计算口径、用途与局限性，统一基于471篇标准化文献数据进行计算。
指标代码实现：编写Python自动化计算脚本，读取标准化数据，完成年度趋势统计与作者多维度影响力指标计算，自动输出CSV结果文件。
指标分析解读：基于计算结果分析RISC-V领域年度发文增长趋势、核心作者梯队、全球机构分布特征，总结领域发展阶段与核心力量。
报告撰写：完成指标规范文档与分析报告，明确数据口径、计算逻辑、结果解读与局限性说明，保证分析可复现、可追溯。

交付成果：

指标规范文档：reports/metrics_spec.md
指标计算代码：src/metrics_calc.py
年度发文趋势表：outputs/year_trend.csv
作者影响力指标表：outputs/author_metrics.csv
指标分析报告：reports/metrics_analysis.md

关键成果：

建立完整的文献计量指标体系与统一计算口径
实现发文趋势、作者影响力、机构分布的自动化指标计算
明确RISC-V领域发展趋势、核心学者与研究格局
形成可直接用于课程报告的计量分析结论

---

# Lesson 7 共被引网络分析

完成内容：

src/networks/co_citation.py：共被引矩阵构建代码，实现引用关系提取、矩阵计算与相似度分析
params.md：补充共被引网络参数，明确节点、边、权重、阈值、聚类算法
outputs/co_citation_matrix.csv：共被引矩阵结果文件
reports/co_citation_analysis.md：共被引分析报告，包含网络特征、知识群落、里程碑文献解读

具体工作：

共被引网络构建：基于文献参考文献（CR）字段构建引用矩阵，计算共被引矩阵C=R.T@R，实现共被引关系自动化提取。
网络参数定义：在params.md中明确共被引网络四要素：节点类型、边类型、权重规则、相似度计算方式、阈值策略与聚类算法。
网络分析与解读：通过Louvain社区识别RISC-V领域五大知识群落，识别高共被引里程碑文献，解读领域知识基础与发展脉络。
报告撰写：完成共被引分析全流程报告，说明方法原理、网络特征、知识结构、研究意义与局限性。

交付成果：

共被引分析代码：src/networks/co_citation.py
共被引网络参数：params.md（已更新）
共被引矩阵文件：outputs/co_citation_matrix.csv
共被引分析报告：reports/co_citation_analysis.md

关键成果：

实现共被引网络自动化构建，掌握共被引矩阵计算方法
识别RISC-V领域核心知识群落与里程碑文献
明确领域知识基础、研究结构与发展脉络
为后续综述撰写与前沿分析提供关键支撑

---


# Lesson 8 关键词共现网络分析
完成内容：

reports/keyword_analysis.md：关键词共现网络分析报告，包含网络结构、核心关键词、研究热点与局限性说明
src/keyword_cooccurrence.py：关键词共现网络构建代码，实现关键词提取、共现关系计算与网络构建
outputs/keyword_centrality.csv：关键词中心性结果文件（Degree Centrality）
outputs/keyword_network.png：关键词共现网络可视化图

具体工作：

关键词数据修复与清洗：
针对原始CSV数据存在字段错位问题，设计规则从keywords、abstract及其他字段中提取包含分号（;）的关键词字符串，修复异常数据；统一关键词格式（小写化、去空值），保证数据可用于网络分析。

关键词共现网络构建：
基于文献关键词字段构建共现网络，将关键词作为节点，关键词在同一文献中共同出现视为边，建立无向加权图结构，实现关键词之间关系的自动化提取。

网络指标计算：
采用Degree Centrality（度中心性）衡量关键词重要性，识别核心关键词与关键研究主题，输出关键词影响力排序结果。

网络结构分析与解读：
对关键词共现网络进行结构分析，识别核心节点、次核心节点及边缘节点，分析RISC-V领域研究热点分布及主题关联关系。

可视化实现：
基于NetworkX与Matplotlib绘制关键词共现网络图，采用力导向布局（spring layout）展示网络结构，直观呈现关键词之间的关系。

报告撰写：
完成关键词共现分析报告，系统说明数据处理方法、网络构建逻辑、分析结果及局限性，保证分析过程清晰、可复现。

交付成果：

关键词分析报告：reports/keyword_analysis.md
关键词网络构建代码：src/keyword_cooccurrence.py
关键词中心性结果：outputs/keyword_centrality.csv
关键词共现网络图：outputs/keyword_network.png

关键成果：

建立了完整的关键词共现网络分析流程，实现关键词数据修复、网络构建与可视化
识别出RISC-V领域核心研究主题（如 operating systems、computer architecture）
揭示关键词网络呈现中心化结构，研究热点集中于系统层与体系结构方向
完成关键词影响力分析，为热点识别与趋势分析提供数据支撑
为后续前沿分析与综述撰写提供重要依据
