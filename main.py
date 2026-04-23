from db import get_connection
from checks.channel_checks import CHANNEL_CHECKS
from checks.operator_checks import OPERATOR_CHECKS
from utils.runner import run_check
from utils.reporter import save_report

def main():
    conn = get_connection()
    cursor = conn.cursor()

    all_checks = CHANNEL_CHECKS + OPERATOR_CHECKS

    results = []

    print("\n=== RUNNING DATA VALIDATION ===\n")

    for check in all_checks:
        try:
            res = run_check(cursor, check)
            results.append(res)
            print(f"{res['check_name']}: {res['status']} ({res['result']})")
        except Exception as e:
            print(f"{check['name']}: ERROR → {e}")

    cursor.close()
    conn.close()

    save_report(results)

if __name__ == "__main__":
    main()