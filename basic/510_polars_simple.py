# polars
# 510_simple_polar_examples.py

import polars as pl
import datetime as dt

pl.show_versions()

#--- if statement
if False : 
    fruit = pl.read_csv("fruit.csv")

    fruit.filter(
        (pl.col("weight") > 1000) & pl.col("is_round")
        ).write_parquet("fruit.parquet")



df = pl.DataFrame(
    {
        "name": ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"],
        "birthdate": [
            dt.date(1997, 1, 10),
            dt.date(1985, 2, 15),
            dt.date(1983, 3, 22),
            dt.date(1981, 4, 30),
        ],
        "weight": [57.9, 72.5, 53.6, 83.1],  # (kg)
        "height": [1.56, 1.77, 1.65, 1.75],  # (m)
    }
)

print(df)
df    # simple tibble-like


# --- Series (vector)
series = pl.Series("ints", [ 3, 4, 5])
print(series)


#--- another Dataframe
df = pl.DataFrame({
    "sales": series,
    "id": [41, 42, 43]
})
print(df)

#---Add line or row# field
df1 = df.with_row_index("line")
print(df)
print(df1)


#--- DataFrame to Lazy (opimize: filter 1st, drop columns,,, then query)
LazyDf = df.lazy() 
print(LazyDf)

#--- Lazy to df
df3 = LazyDf.collect()
print(df3)


#--- if data larger than memory
LazyDf.collect(engine="streaming")


#--- show optimization
LazyDf.explain()
LazyDf.show_graph()
