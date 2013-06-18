select a.row_num as row, b.col_num as col_num, sum(a.value * b.value) as value
    from a, b where a.col_num = b.row_num
    group by a.row_num, b.col_num;