import pandas as pd

# Filter by country code
def filter_country(pdf, country="USA"):
    pdf = pdf[pdf.iso_code == country]
    return pdf
    
# Pivot by indicator and fill missing values
def pivot_and_clean(pdf, fillna):
    pdf["value"] = pd.to_numeric(pdf["value"])
    pdf = pdf.fillna(fillna).pivot_table(values="value", columns = "indicator", index = "date")
    return pdf

def clean_spark_cols(pdf):
    pdf.columns = pdf.columns.str.replace(" ", "_")
    return pdf

def index_to_col(df, colname):
    df[colname] = df.index
    return df