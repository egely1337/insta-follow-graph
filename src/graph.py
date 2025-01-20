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
    ax.set_facecolor('white')
    plt.title(f"{os.getenv('TARGET_USERNAME')} follow graph")
    fig.set_size_inches(19.20, 10.80)
    fig.autofmt_xdate()
    fig.savefig(f"{os.getenv("TARGET_USERNAME")}-{datetime.datetime.now().strftime("%d-%m-%Y")}.png")
    return 0


if __name__ == "__main__":
    main()