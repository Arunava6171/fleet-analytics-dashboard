import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Autonomous Fleet Telemetry Hub", layout="wide")

@st.cache_data
def load_data():
    cols = ["unit", "cycle", "op_setting_1", "op_setting_2", "op_setting_3"] + [f"sensor_{i}" for i in range(1, 22)]
    df = pd.read_csv("train_FD001.txt", sep=r"\s+", header=None, names=cols)
    max_cycles = df.groupby("unit")["cycle"].max().reset_index()
    max_cycles.columns = ["unit", "max_cycle"]
    df = df.merge(max_cycles, on="unit")
    df["RUL"] = df["max_cycle"] - df["cycle"]
    df["sensor_11_rolling_avg"] = df.groupby("unit")["sensor_11"].transform(lambda x: x.rolling(window=10, min_periods=1).mean())
    df["sensor_11_zscore"] = df.groupby("unit")["sensor_11_rolling_avg"].transform(lambda x: (x - x.mean()) / x.std())
    df["anomaly_flag"] = df["sensor_11_zscore"].apply(lambda z: 1 if abs(z) > 2.5 else 0)
    df["health_status"] = df["RUL"].apply(lambda x: "CRITICAL" if x < 30 else ("WARNING" if x < 75 else "HEALTHY"))
    return df

try:
    df = load_data()
    st.title("Autonomous Fleet Sensor Anomaly & Maintenance Hub")
    selected_unit = st.sidebar.selectbox("Select Engine Unit", df["unit"].unique())
    engine_df = df[df["unit"] == selected_unit]
    latest_cycle = engine_df.iloc[-1]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Current Cycle", int(latest_cycle["cycle"]))
    col2.metric("Remaining Useful Life (RUL)", int(latest_cycle["RUL"]))
    col3.metric("Health Status", str(latest_cycle["health_status"]))
    col4.metric("Anomalies Detected", int(engine_df["anomaly_flag"].sum()))

    st.subheader(f"Telemetry Degradation Profile for Engine Unit #{selected_unit}")
    fig, ax = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    sns.lineplot(data=engine_df, x="cycle", y="sensor_11_rolling_avg", ax=ax[0], color="blue", label="Sensor 11 (Temp)")
    ax[0].set_ylabel("Sensor Avg Temp")
    sns.lineplot(data=engine_df, x="cycle", y="sensor_11_zscore", ax=ax[1], color="purple", label="Z-Score")
    ax[1].axhline(2.5, color="red", linestyle="--", label="Anomaly Threshold (+2.5)")
    ax[1].set_ylabel("Z-Score")
    ax[1].set_xlabel("Operational Cycle")
    st.pyplot(fig)
except FileNotFoundError:
    st.error("Missing train_FD001.txt file in directory.")
