-- Selects cities from database
SELECT * FROM hbtn_0d_usa.cities WHERE hbtn_0d_usa.cities.stateid = (SELECT states.id FROM STATES WHERE name = california);
