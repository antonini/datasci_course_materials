select count(*) from (select f.docid, sum(f.count) as sum_count
from frequency f group by docid) where sum_count > 300;