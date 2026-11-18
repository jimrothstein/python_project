# from __future__ import annotations
# REF:
# https://www.youtube.com/watch?v=hCHucCkf-RI
import pandas as pd
import polars as pl
import pyarrow as pa
import narwhals as nw
from narwhals.typing import IntoFrame

# Each of pandas, polars ... has a different way to add 2 columns
# Use narwhals to extact data only, do calculation and print in desired form when done.
def agnostic_get_columns(df_native: IntoFrame) -> list[str]:
    df = nw.from_native(df_native)
    column_names = df.columns
    return column_names


data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df_pandas = pd.DataFrame(data)
df_polars = pl.DataFrame(data)
table_pa = pa.table(data)

print("pandas output")
print(agnostic_get_columns(df_pandas))

print("Polars output")
print(agnostic_get_columns(df_polars))

print("PyArrow output")
print(agnostic_get_columns(table_pa))


print(
    nw.from_native(df_pandas)
)
