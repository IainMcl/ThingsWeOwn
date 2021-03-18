SELECT * 
  FROM "Item" AS i
FULL OUTER JOIN "Person" AS p
  ON p."Name" = i."ItemName"
FULL OUTER JOIN "House" AS h
  ON h."House_pk" = i."Room";
-- LEFT OUTER JOIN House h
--   ON h.HouseName = c.HouseName
-- RIGHT OUTER JOIN Person p
--   ON p.Name = i.Owner
--SELECT * FROM "Person";
