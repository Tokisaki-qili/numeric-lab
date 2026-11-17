"""读配置 + 校验字段。

规矩：所有"配置有问题"的报错都在这里抛，错误信息必须带文件名和字段名。
"""

from pathlib import Path

import yaml


class ConfigError(Exception):
    """配置契约错误：文件缺字段、类型不对、YAML 语法坏。属性：path / field。"""

    def __init__(self, message: str, path: str = "", field: str = ""):
        super().__init__(message)
        self.path = path
        self.field = field


def load(path) -> dict:
    """读 YAML，返回 dict。

    TODO(N0-1)：实现下面几步
      1. 文件不存在 → ConfigError（含路径）
      2. YAML 解析失败 → ConfigError（含行号）
      3. 顶层必须是 dict
      4. 缺 version → ConfigError(field="version")
    """
    raise NotImplementedError("N0-1")


def load_gacha(path) -> "GachaConfig":
    """load 之后转成 model.GachaConfig，缺字段在这里报。

    TODO(N0-1)：必填字段 rate5 / hard_pity / soft_pity_start / soft_pity_step，
    缺任何一个抛 ConfigError，信息里要有字段名。
    """
    raise NotImplementedError("N0-1")
