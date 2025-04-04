# Write your MySQL query statement below
select tday.id from Weather tday
join Weather yday
on tday.recordDate = Date_ADD(yday.recordDate, interval 1 day)
where tday.temperature > yday.temperature