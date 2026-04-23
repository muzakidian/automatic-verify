CHANNEL_CHECKS = [
    {
        "name": "CIF_SPLIT",
        "query": """
            SELECT COUNT(*) 
            FROM m_en_chanl_info_merged
            WHERE ebnk_cst_pltfrm_id LIKE '%|%'
        """,
        "expected": 0
    },
    {
        "name": "DUPLICATE_CIF",
        "query": """
            SELECT COUNT(*) FROM (
                SELECT ebnk_cst_pltfrm_id
                FROM m_en_chanl_info_merged
                GROUP BY ebnk_cst_pltfrm_id
                HAVING COUNT(*) > 1
            ) t
        """,
        "expected": 0
    }
]