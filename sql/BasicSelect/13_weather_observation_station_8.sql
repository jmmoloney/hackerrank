SELECT DISTINCT CITY
FROM STATION
WHERE (CITY LIKE 'a%' AND (CITY LIKE '%a'
                            OR CITY LIKE '%i'
                            OR CITY LIKE '%e'
                            OR CITY LIKE '%o'
                            OR CITY LIKE '%u'))
    OR (CITY LIKE 'o%' AND (CITY LIKE '%a'
                            OR CITY LIKE '%i'
                            OR CITY LIKE '%e'
                            OR CITY LIKE '%o'
                            OR CITY LIKE '%u'))
    OR (CITY LIKE 'i%' AND (CITY LIKE '%a'
                            OR CITY LIKE '%i'
                            OR CITY LIKE '%e'
                            OR CITY LIKE '%o'
                            OR CITY LIKE '%u'))
    OR (CITY LIKE 'e%' AND (CITY LIKE '%a'
                        OR CITY LIKE '%i'
                        OR CITY LIKE '%e'
                        OR CITY LIKE '%o'
                        OR CITY LIKE '%u'))
    OR (CITY LIKE 'u%' AND (CITY LIKE '%a'
                        OR CITY LIKE '%i'
                        OR CITY LIKE '%e'
                        OR CITY LIKE '%o'
                        OR CITY LIKE '%u'))
