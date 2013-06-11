select distinct t1.docid from frequency t1, frequency t2
where t1.docid = t2.docid and t1.term = 'transactions' and t2.term = 'world';