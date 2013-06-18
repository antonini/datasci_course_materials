-- (a) select: Write a query that is equivalent to the following relational algebra expression.
-- σdocid=10398_txt_earn(frequency) 

SELECT count(*) FROM frequency where docid = "10398_txt_earn";

-- (b) select project: Write a SQL statement that is equivalent to the following relational algebra expression.
-- πterm( σdocid=10398_txt_earn and count=1(frequency))
SELECT count(term) FROM frequency where docid = "10398_txt_earn" and count = 1;

-- (c) union: Write a SQL statement that is equivalent to the following relational algebra expression. 
-- (Hint: you can use the UNION keyword in SQL)
-- πterm( σdocid=10398_txt_earn and count=1(frequency)) U πterm( σdocid=925_txt_trade and count=1(frequency))
SELECT count(*) FROM
(SELECT term FROM Frequency x WHERE docid = "10398_txt_earn" AND count = 1
UNION 
SELECT term FROM Frequency x WHERE docid = "925_txt_trade" AND count = 1
) x;

-- (d) count: Write a SQL statement to count the number of documents containing the word “parliament”
select count(*) from frequency where term = "parliament"

-- (e) big documents Write a SQL statement to find all documents
-- that have more than 300 total terms, including duplicate terms. 
-- (Hint: You can use the HAVING clause, or you can use a nested query. 
-- Another hint: Remember that the count column contains the term frequencies, 
-- and you want to consider duplicates.) (docid, term_count)
select count(*) from (select docid, sum(count) as total from frequency
group by docid)
where total > 300

-- (f) two words: Write a SQL statement to count the number of unique documents that contain both
-- the word 'transactions' and the word 'world'.
SELECT COUNT(*) from 
(SELECT docid FROM Frequency WHERE term = "transactions"
INTERSECT
SELECT docid FROM Frequency WHERE term = "world")