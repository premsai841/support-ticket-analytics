from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "tickets.csv"


def main() -> None:
    df = pd.read_csv(INPUT)
    resolved = df[df["status"].eq("Resolved")].copy()
    resolved["sla_met"] = resolved["resolved_hours"] <= resolved["sla_hours"]

    print("Support Operations Report")
    print("=" * 26)
    print(f"Total tickets: {len(df)}")
    print(f"Open tickets: {df['status'].eq('Open').sum()}")
    print(f"Resolved tickets: {len(resolved)}")
    print(f"SLA compliance: {resolved['sla_met'].mean() * 100:.1f}%")
    print(f"Avg. resolution time: {resolved['resolved_hours'].mean():.1f} hours")
    print("\nTickets by category:")
    print(df["category"].value_counts().to_string())
    print("\nTickets by agent:")
    print(df["agent"].value_counts().to_string())


if __name__ == "__main__":
    main()
