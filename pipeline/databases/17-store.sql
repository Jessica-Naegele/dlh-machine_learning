-- sql script that creates a trigger that decreases the quanitiy of an item ater adding a new order

DELIMITER //

CREATE TRIGGER IF NOT EXISTS store
AFTER INSERT ON orders
FOR EACH ROW 
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//

DELIMITER ;
