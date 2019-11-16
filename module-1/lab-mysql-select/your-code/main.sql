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


--Second exercise
--select author_id, last_name, first_name, publisher, title_count
select a.au_id as AUTHOR_ID, a.au_lname as LAST_NAME, a.au_fname as FIRST_NAME, p.pub_name as PUBLISHER, count(t.title)
from authors a left join titleauthor ta on a.au_id = ta.au_id
inner join titles t on ta.title_id = t.title_id
left join publishers p on t.pub_id = p.pub_id
group by AUTHOR_ID, LAST_NAME, FIRST_NAME, PUBLISHER
order by AUTHOR_ID DESC, count(t.title) asc

-- Prueba del 2
select sum(Titles_num) 
from (
select a.au_id as AUTHOR_ID, a.au_lname as LAST_NAME, a.au_fname as FIRST_NAME, p.pub_name as PUBLISHER, count(t.title) as Titles_num
from authors a left join titleauthor ta on a.au_id = ta.au_id
inner join titles t on ta.title_id = t.title_id
left join publishers p on t.pub_id = p.pub_id
group by AUTHOR_ID, LAST_NAME, FIRST_NAME, PUBLISHER)


-- Exercise 3
select a.au_id AUTHOR_ID, a.au_lname as LAST_NAME, a.au_fname as FIRST_NAME, t.title, sum(s.qty) as TOTAL
from authors a left join titleauthor ta on a.au_id = ta.au_id
inner join titles t on ta.title_id = t.title_id
left join sales s on t.title_id = s.title_id
group by AUTHOR_ID
order by TOTAL DESC
limit 3

-- but this is not working because there are titles which are repeated in the table titleauthor.

-- Exercise 4
select a.au_id AUTHOR_ID, a.au_lname as LAST_NAME, a.au_fname as FIRST_NAME, t.title, CASE WHEN sum(s.qty) IS NULL THEN 0 ELSE sum(s.qty) END as TOTAL
from authors a left join titleauthor ta on a.au_id = ta.au_id
left join titles t on ta.title_id = t.title_id
left join sales s on t.title_id = s.title_id
group by AUTHOR_ID
order by TOTAL DESC

