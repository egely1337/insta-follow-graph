import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import dotenv
import os
import datetime

def main() -> int:
    # load .env
    dotenv.load_dotenv()
    df = pd.read_csv(f"{os.getenv("TARGET_USERNAME")}.csv")
    df["date"] = pd.to_datetime(df["date"], format="mixed")
    fig, ax = plt.subplots()
    ax.plot(df["date"], df["followers"])
    ax.plot(df["date"], df["followers"])
    fig.autofmt_xdate()
    fig.savefig(f"{os.getenv("TARGET_USERNAME")}-{datetime.datetime.now().strftime("%d-%m-%Y")}.png")
    return 0


if __name__ == "__main__":
    main()