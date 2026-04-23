def run_check(cursor, check):
    cursor.execute(check["query"])
    result = cursor.fetchone()[0]

    status = "PASS" if result == check["expected"] else "FAIL"

    return {
        "check_name": check["name"],
        "result": result,
        "expected": check["expected"],
        "status": status
    }