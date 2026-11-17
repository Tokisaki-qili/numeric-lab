# 测试

每个 ticket 的断言数量写在 [TICKETS.md](../TICKETS.md) 里，测试自己写，别用 `assert True` 凑数。

跑测试：

```bash
python -m pytest -q
```

建议每个模块一个文件：`test_gacha.py`、`test_growth.py`、`test_economy.py`。

必须覆盖的三类输入：**正常值 / 边界值 / 坏值**。

- 正常值：抽 1000 次，平均抽数在合理区间
- 边界值：`pulls=0`、`level=1`、`level=max_level`
- 坏值：概率为负、等级为 0、配置缺字段（应报 `ConfigError` 而不是崩）
