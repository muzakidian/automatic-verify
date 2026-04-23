import pandas as pd

def save_report(results):
    df = pd.DataFrame(results)
    df.to_csv("report.csv", index=False)
    print("\nReport saved to report.csv")