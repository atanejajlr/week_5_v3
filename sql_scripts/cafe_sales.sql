CREATE TABLE products (
  
  prod_id INT AUTO_INCREMENT PRIMARY KEY,
  prod_name VARCHAR(50),
  prod_price DECIMAL (5,2)
  
  );
  
  CREATE TABLE couriers (
  
  driver_id INT AUTO_INCREMENT PRIMARY KEY,
  driver_name VARCHAR(50),
  driver_phone VARCHAR(50)
  
  );
  

  CREATE TABLE customers (
  
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_name VARCHAR(50),
  customer_address VARCHAR(1000),
  customer_phone VARCHAR(50)
  
  );
  
  CREATE TABLE status (
  
  status_id INT AUTO_INCREMENT PRIMARY KEY,
  order_status VARCHAR(50)
  
  );
  
  CREATE TABLE orders (
  
  order_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id INT,
  status_id INT,
  driver_id INT,
  FOREIGN KEY(customer_id) REFERENCES customers(customer_id) ON DELETE SET NULL,
  FOREIGN KEY(driver_id) REFERENCES couriers(driver_id) ON DELETE SET NULL,
  FOREIGN KEY(status_id) REFERENCES status(status_id) ON DELETE SET NULL
  
  );
  
  CREATE TABLE order_items (
  
  item_id INT AUTO_INCREMENT PRIMARY KEY,
  order_id INT,
  prod_id INT,
  prod_qty INT,
  FOREIGN KEY(order_id) REFERENCES orders(order_id) ON DELETE SET NULL,
  FOREIGN KEY(prod_id) REFERENCES products(prod_id) ON DELETE SET NULL
  
  );
  
  
INSERT INTO products (prod_name, prod_price)
VALUES
    ("Coke Zero", 2.0)
    , ("Sprite", 1.80)
    , ("Diet Lemonade", 2.20)
    , ("Small Bowl of Chips", 3.40)
    , ("Veggie Burger with Chips", 6.50);
  
  
  INSERT INTO couriers (driver_name, driver_phone)
VALUES
    ("John", "0789887334")
    , ("Tim", "0789887156")
    , ("Sahil", "07754123892")
    , ("Jim", "0789887112")
    , ("Mary", "0769887479");
    
INSERT INTO customers (customer_name, customer_address, customer_phone)
VALUES
    ("Cynthia D'Souza", "4, Broadway House, Broadstone, Dorset BH18 8AX", "0789127334")
    , ("Dolly Menezes", "6, Alvaston Road, Derby DE24 8PZ", "0779137334")
    , ("Ian Chambers", "2, Babington Court, Derby DE24 8PZ", "07755123992")
    , ("Sanjay Paharia", "14, Babington Court, Derby DE24 8PZ", "07741718023")
    , ("Mary Kentish", "19, Avon Road, Laemington Spa,  CV33 9TS", "0769667479");
    
INSERT INTO status (order_status)
VALUES
    ("Accepted")
    , ("Preparing")
    , ("Ready")
    , ("Waiting for driver")
    , ("Shipped")
    , ("Delivered");
    
INSERT INTO orders (customer_id, status_id, driver_id)
VALUES
     (1, 2, 2),
     (2, 1, 3),
     (3, 3, 2),
     (4, 1, 1),
     (5, 2, 3);
   
INSERT INTO order_items (order_id, prod_id, prod_quantity)
VALUES
     (1, 2, 3),
     (1, 3, 4),
     (1, 1, 5),
     (2, 1, 2),
     (2, 2, 4),
     (3, 1, 4),
     (3, 3, 1),
     (4, 2, 2),
     (5, 1, 6),
     (5, 2, 3),
     (5, 3, 4),
     (5, 4, 1);

  DROP TABLE IF EXISTS products;
  DROP TABLE IF EXISTS couriers; 
  DROP TABLE IF EXISTS customers;
  DROP TABLE IF EXISTS orders;
  DROP TABLE IF EXISTS order_items;
  DROP TABLE IF EXISTS status;