import pandas as pd
import numpy as np

def build_cumulative_triangle(df):
    inc = df.pivot_table(
        index="accident_year",
        columns="development_year",
        values="incurred",
        aggfunc="sum"
    )
    return inc.cumsum(axis=1)


def calculate_factors(triangle):
    factors = []
    for i in range(triangle.shape[1] - 1):
        num = triangle.iloc[:, i+1].sum(skipna=True)
        den = triangle.iloc[:, i].sum(skipna=True)
        factors.append(num / den)
    return factors


def calculate_cdf(factors):
    cdf = [np.prod(factors[i:]) for i in range(len(factors))]
    cdf.append(1.0)
    return cdf


def estimate_ultimate(triangle, cdf):
    ult = {}
    for ay in triangle.index:
        dev = triangle.loc[ay].last_valid_index()
        ult[ay] = triangle.loc[ay, dev] * cdf[dev]
    return pd.Series(ult)
