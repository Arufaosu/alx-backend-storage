-- implement a trigger that decreases the quantity
CREATE TRIGGER after_orders_insert
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name; 
