select 
--distinct(doca.term) 
	SUM(doca.count * docb.count) as value
from 
	frequency doca
	JOIN frequency docb ON doca.term = docb.term and docb.docid = '17035_txt_earn'
 where 
 	doca.docid = '10080_txt_crude';


