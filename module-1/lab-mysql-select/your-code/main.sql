-- LAB-MYSQL-SELECT

-- The inner joint could be left join, but there are authors without titles, they haven't published anything I guess
select a.au_id, a.au_lname, a.au_fname, t.title, p.pub_name
from authors a left join titleauthor ta on a.au_id = ta.au_id
inner join titles t on ta.title_id = t.title_id
left join publishers p on t.pub_id = p.pub_id
order by t.title_id

-- Testing it's OK. Result 1 must be equal to Result 2
--Result 1
select count(a.au_id)
from authors a left join titleauthor ta on a.au_id = ta.au_id
inner join titles t on ta.title_id = t.title_id
left join publishers p on t.pub_id = p.pub_id
--Result 2
SELECT count(au_id)
from titleauthor ta




