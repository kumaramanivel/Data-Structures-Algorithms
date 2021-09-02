# Write your MySQL query statement below
SELECT FirstName, LastName, City, State
FROM person left join Address
ON Person.PersonID = Address.PersonID;