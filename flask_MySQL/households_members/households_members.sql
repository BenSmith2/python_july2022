SELECT *
FROM dojos;

SET SQL_SAFE_UPDATES = 0;

SELECT *
FROM ninjas;

INSERT INTO dojos (name)
VALUES ("austin"),("nepal"),("mariana trench");

DELETE FROM dojos WHERE dojos.created_at > 2022-07-14;