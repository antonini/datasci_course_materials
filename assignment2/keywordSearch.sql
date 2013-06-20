
select 
--distinct(doca.term) 
	doca.docid,
	--'--------' as DIF,
	--docb.*
	SUM(doca.count * docb.count) as value
from 
	q_frequency doca
	JOIN q_frequency docb ON doca.term = docb.term and docb.docid = 'q'
 where 
 	doca.docid != 'q'

 	group by doca.docid order by 2 asc;


