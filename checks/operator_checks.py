OPERATOR_CHECKS = [
    {
        "name": "ORPHAN_OPERATOR",
        "query": """
            SELECT COUNT(*) FROM (
                SELECT o.ebnk_cst_pltfrm_id
                FROM m_bb_operator_merged o
                WHERE NOT EXISTS (
                    SELECT 1
                    FROM m_en_chanl_info_merged m
                    WHERE m.ebnk_cst_pltfrm_id = o.ebnk_cst_pltfrm_id
                )
            ) t
        """,
        "expected": 0
    }
]