import pandas as pd
import numpy as np

def calculate_exposure(start, end, obs_start, obs_end):
    overlap_start = max(start, obs_start)
    overlap_end = min(end, obs_end)
    days = max((overlap_end - overlap_start).days, 0)
    return days / 365.0


def cap_exposure(exp):
    return min(exp, 1.0)


def add_exposure(df, obs_start, obs_end):
    df["exposure"] = df.apply(
        lambda x: calculate_exposure(
            x["policy_start_date"],
            x["policy_end_date"],
            obs_start,
            obs_end
        ),
        axis=1
    )
    df["exposure"] = df["exposure"].apply(cap_exposure)
    return df
