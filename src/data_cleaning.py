import pandas as pd

def clean_policy_data(df):
    df["policy_start_date"] = pd.to_datetime(df["policy_start_date"])
    df["policy_end_date"] = pd.to_datetime(df["policy_end_date"])
    df = df[df["policy_end_date"] > df["policy_start_date"]]
    return df


def clean_claims_data(df):
    df["accident_date"] = pd.to_datetime(df["accident_date"])
    df = df[df["claim_amount"] >= 0]
    return df


def clean_payment_data(df):
    df["payment_date"] = pd.to_datetime(df["payment_date"])
    return df
