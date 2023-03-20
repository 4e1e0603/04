# %%
import polars as pl

# Eager API
## Load tabular data from CSV to data frame.
## Explore data

# %%
df = pl.read_csv("https://j.mp/iriscsv")

# FAIL see https://github.com/pola-rs/polars/issues/1051
df = df[df["sepal_length"] > 5].groupby("species").sum()

# %%
df

# %%
print(df.head())

print(df.tail())

print(len(dv))
# %%
