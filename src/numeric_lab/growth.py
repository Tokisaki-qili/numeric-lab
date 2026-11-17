"""成长曲线。公式见 docs/公式与口径.md 第 3 节。"""

from .model import GrowthConfig


def exp_to_next(cfg: GrowthConfig, level: int) -> int:
    """从 level 升到 level+1 需要的经验：round(base * level ** exponent)。

    TODO(N3-1)：level 超出 [1, max_level] 抛 ValueError。
    """
    raise NotImplementedError("N3-1")


def cumulative_exp(cfg: GrowthConfig, level: int) -> int:
    """从 1 级升到 level 级的累计经验 = Σ_{k=1}^{level-1} exp_to_next(k)。

    TODO(N3-1)：level = 1 时返回 0。
    """
    raise NotImplementedError("N3-1")


def combat_power(cfg: GrowthConfig, level: int) -> float:
    """战力 = Σ attr(level) × weight。

    TODO(N3-2)：attr = attrs_at_level_1 + attrs_per_level × (level-1)
    """
    raise NotImplementedError("N3-2")
