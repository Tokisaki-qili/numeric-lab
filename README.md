# numeric-lab 数值实验室

把抽卡、掉落、成长、经济四条规则写成参数配置，用 Python 模拟出玩家视角的数字：**多少抽出金、多少天毕业、资源缺口第几天出现**。

目标是用可复现、能对账的数字，替代策划手里的 Excel 试算表——这也是数值策划每天在做的事。

> **状态：Sprint 0（骨架）。** 配置与口径文档已就位，代码按 [TICKETS.md](TICKETS.md) 逐个实现。
> 参数取自二游常见量级，仅用于练习与作品展示，**不代表任何公司真实配置**。

## 目标岗位

数值策划（实习）

## 目录结构

```
numeric-lab/
├── README.md               # 本文件：给面试官看的说明
├── TICKETS.md              # 任务板：分阶段、验收标准、面试问题
├── config/                 # 参数（代码只读这里，不许写死）
│   ├── gacha.yaml          # 卡池：基础概率、保底、软保底
│   ├── growth.yaml         # 等级经验与属性成长
│   ├── drop.yaml           # 掉落权重表
│   └── economy.yaml        # 每日产出/消耗
├── docs/
│   ├── 一分钟看懂.md        # 非技术版：这项目在干嘛
│   ├── 公式与口径.md        # 公式、模拟约定、容差
│   └── 人手试算.md          # 你手算的"标准答案"（N0-0 交付）
├── src/numeric_lab/
│   ├── model.py            # 数据结构（dataclass）
│   ├── loader.py           # 读配置 + 校验字段
│   ├── gacha.py            # 抽卡模拟
│   ├── growth.py           # 成长曲线
│   ├── economy.py          # 经济循环
│   ├── report.py           # 报表输出
│   └── cli.py              # 命令行入口
├── tests/                  # 测试（按 TICKETS 的断言写）
└── requirements.txt
```

## 怎么跑（实现后）

```bash
python -m numeric_lab.cli gacha  --config config/gacha.yaml --pulls 100000 --seed 42
python -m numeric_lab.cli growth --config config/growth.yaml
python -m numeric_lab.cli economy --config config/economy.yaml --days 30
python -m numeric_lab.cli report --out docs/report.md
```

## 三条纪律

1. **数字必须可复现**：固定随机种子，报告里写种子和参数版本。
2. **模拟必须对得上理论**：每个指标同时给理论值和模拟值，差超过 2% 先怀疑自己的代码。
3. **结论必须由数字推出**：报告里没有"我估计"，只有"跑了 N 次，得到 X"。

## 现在该干什么

从 [TICKETS.md](TICKETS.md) 的 Sprint 0 开始，先手算，再写代码。
