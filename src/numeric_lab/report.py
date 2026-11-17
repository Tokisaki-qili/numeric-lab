"""报表：把跑出来的数字变成人能读的 Markdown。"""


def render_report(metrics: dict, out_path) -> None:
    """生成报告，写入 out_path。

    TODO(N5)：结构固定为四块
      # 数值模拟报告
      ## 1. 参数（卡池/成长/经济，写明来源文件）
      ## 2. 核心指标（6 个：平均抽数、P50、P90、L90 累计经验、缺口日、30 天缺口）
      ## 3. 结论（3 条，每条"参数 → 数字 → 一句话"）
      ## 4. 复现方式（命令 + 种子 + 参数版本）
    """
    raise NotImplementedError("N5")
