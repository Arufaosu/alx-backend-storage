-- creates a function SafeDiv that divides 1st num by 2nd num
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	IF (b = 0)
	THEN RETURN (0);
	ELSE RETURN (a / b);
	END IF;
END $$
DELIMITER ;
