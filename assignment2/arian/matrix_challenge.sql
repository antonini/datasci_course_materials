create table C as select a.row as row, b.col_num as col_num, sum(a.value * b.value) as value
    from a, b where a.col_num = b.row
    group by a.row, b.col_num;

 select * from
(
select row_num, col_num,value from a
*
select row_num, col_num,value from b
)
where row_num = 2
and col_num = 3



-- 

create table C as select a.row as row, b.col_num as col_num, sum(a.value * b.value) as value
    from a, b where a.col_num = b.row
    group by a.row, b.col_num;

 select * from
(
select row_num, col_num,value from a
*
select row_num, col_num,value from b
)
where row_num = 2
and col_num = 3