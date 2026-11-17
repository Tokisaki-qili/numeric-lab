"""经济循环。公式见 docs/公式与口径.md 第 4 节。"""

import random

from .model import EconomyConfig


def daily_income(cfg: EconomyConfig) -> dict:
    """一天的总产出：{'gold': ..., 'exp': ...，'runs': 体力能刷几次}。

    TODO(N4-1)：runs = stamina // stamina_per_run
    """
    raise NotImplementedError("N4-1")


def daily_cost(cfg: EconomyConfig, pulls_per_day: int = 0) -> dict:
    """一天的总消耗（示例：抽卡 + 升级）。

    TODO(N4-1)
    """
    raise NotImplementedError("N4-1")


def simulate_days(cfg: EconomyConfig, days: int = 30, players: int = 1000,
                  seed: int = 42) -> list[dict]:
    """模拟多名玩家 days 天，返回每人每天一条记录：

    {'player': 0.., 'day': 1..days, 'gold': 累计金币, 'exp': 累计经验}

    TODO(N4-1)：玩家之间的差异来自随机（比如每天抽卡次数）。
    """
    raise NotImplementedError("N4-1")


def find_shortage_day(records: list[dict], resource: str) -> int | None:
    """累计值首次 < 0 的那天，没有缺口返回 None。

    TODO(N4-2)
    """
    raise NotImplementedError("N4-2")
