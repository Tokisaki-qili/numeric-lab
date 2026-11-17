"""数据结构：配置在内存里的样子。

规矩：这里**只存值**，不做业务校验（校验集中在 loader.py）。
"""

from dataclasses import dataclass, field


@dataclass
class GachaConfig:
    name: str
    rate5: float
    rate4: float
    hard_pity: int
    soft_pity_start: int
    soft_pity_step: float
    ten_pull_guarantee4: bool = False


# TODO(N0-2)：照 GachaConfig 的写法，补下面三个。
#
# GrowthConfig:  base / exponent / max_level / weights(dict) / attrs_at_level_1(dict) / attrs_per_level(dict)
# DropTable:     name / items(list[dict])，每个 item 有 name、rarity、weight
# EconomyConfig: stamina / stamina_per_run / exp_per_run / gold_per_run /
#                daily_quest_gold / daily_quest_exp / gacha_cost_per_pull /
#                level_up_gold_per_level / start_gold / team_size
#
# 每个配置都要能从 dict 构造，并且字段名与 config/*.yaml 一一对应。
