select count(*)  from (select docid  from frequency where term like 'parliament' group by docid) a;