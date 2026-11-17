"""命令行入口。

约定：所有子命令都接受配置路径参数，核心逻辑调用其他模块，这里只做参数解析和打印。
"""

import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="numeric_lab", description="数值模拟器")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_info = sub.add_parser("info", help="打印配置参数")
    p_info.add_argument("--gacha", default="config/gacha.yaml")
    p_info.add_argument("--growth", default="config/growth.yaml")

    p_gacha = sub.add_parser("gacha", help="抽卡模拟")
    p_gacha.add_argument("--config", default="config/gacha.yaml")
    p_gacha.add_argument("--pulls", type=int, default=100000)
    p_gacha.add_argument("--seed", type=int, default=42)

    p_growth = sub.add_parser("growth", help="成长曲线")
    p_growth.add_argument("--config", default="config/growth.yaml")

    p_eco = sub.add_parser("economy", help="经济循环")
    p_eco.add_argument("--config", default="config/economy.yaml")
    p_eco.add_argument("--days", type=int, default=30)

    p_rep = sub.add_parser("report", help="生成报告")
    p_rep.add_argument("--out", default="docs/report.md")

    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)

    # TODO(N0-1)：info 子命令
    # TODO(N1-1)：gacha 子命令（打印平均抽数、理论值、差值百分比）
    # TODO(N3-1)：growth 子命令（打印 L1/L40/L80/L90 累计经验）
    # TODO(N4-1)：economy 子命令（打印缺口日、30 天缺口）
    # TODO(N5)：report 子命令
    print(f"[todo] 子命令 {args.cmd} 还没实现，见 TICKETS.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
