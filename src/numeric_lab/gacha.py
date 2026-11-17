"""抽卡模拟。公式见 docs/公式与口径.md 第 1 节。

约定：第 i 抽从 1 开始计数；返回的"第几抽"也是 1-based。
"""

import random

from .model import GachaConfig


def prob_at(cfg: GachaConfig, i: int) -> float:
    """第 i 抽出五星的概率 p_i。

    TODO(N1-1)：按文档实现分段：
      i <  soft_pity_start           → rate5
      soft_pity_start <= i < hard_pity → rate5 + step*(i - soft_pity_start + 1)
      i >= hard_pity                 → 1.0
    注意 cap 到 1.0。
    """
    raise NotImplementedError("N1-1")


def simulate_pulls(cfg: GachaConfig, n_pulls: int, seed: int = 42) -> list[int]:
    """抽 n_pulls 次，返回 [每次五星在第几抽]，没出记 0。

    TODO(N1-1)：
      - 用 random.Random(seed)，不要用全局 random（否则不可复现）
      - 一次抽卡 = 一抽；命中后计数器归零
      - n_pulls = 0 返回 []
    """
    raise NotImplementedError("N1-1")


def expected_pulls(cfg: GachaConfig) -> float:
    """期望抽数 E（理论值，闭式）。

    TODO(N1-2)：E = Σ i * P_i，P_i = p_i * Π_{j<i}(1-p_j)
    """
    raise NotImplementedError("N1-2")


def quantiles(cfg: GachaConfig) -> tuple[int, int]:
    """返回 (P50, P90)：累计概率首次达到 0.5 / 0.9 的抽数。

    TODO(N1-2)
    """
    raise NotImplementedError("N1-2")
