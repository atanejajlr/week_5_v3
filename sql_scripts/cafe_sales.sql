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
    ("Coke Zero", 2.75)
    , ("Sprite", 1.95)
    , ("Diet Lemonade", 2.25)
    , ("Small Bowl of Chips", 3.65)
    , ("Veggie Burger with Chips", 6.75)
    , ("Cheese and Capsicum Pizza", 9.75)
    , ("Chicken Burger with Chips", 8.25)
    , ("Caffe Latte", 3.35)
    , ("Caffe Mocha", 4.75)
    , ("Fruit Cake with IceCream", 6.35)
    , ("Chice of IceCream", 4.75);
  
  
  INSERT INTO couriers (driver_name, driver_phone)
VALUES
    ("John", "07741719098")
    , ("Tim", "07741256713")
    , ("Sahil", "07741712456")
    , ("Jim", "07741719234")
    , ("Mary", "07712456712");
    
INSERT INTO customers (customer_name, customer_address, customer_phone)
VALUES
    ("Cynthia D'Souza", "Dorset, BH18 8AX", "07712456719")
    , ("Dolly Menezes", "Derby DE15 8PZ", "07791371334")
    , ("Ian Chambers", "Derby DE45 8PZ", "07741719356")
    , ("Sanjay Paharia", "Derby DE24 8PZ", "07741718023")
    , ("Linda Kentish", "Laemington Spa, CV33 9TS", "07696674792");
    
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
   
INSERT INTO order_items (order_id, prod_id, prod_qty)
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
     
SELECT * FROM products;
SELECT * FROM couriers;
SELECT * FROM orders;
SELECT * FROM customers;
SELECT * FROM order_items;

  DROP TABLE IF EXISTS products;
  DROP TABLE IF EXISTS couriers; 
  DROP TABLE IF EXISTS customers;
  DROP TABLE IF EXISTS orders;
  DROP TABLE IF EXISTS order_items;
  DROP TABLE IF EXISTS `status`;
  
  
SELECT orders.order_id, customers.customer_name, customers.customer_phone
, couriers.driver_name, couriers.driver_phone, products.prod_name,
order_items.prod_qty
FROM orders
INNER JOIN customers ON customers.customer_id = orders.order_id
INNER JOIN couriers ON couriers.driver_id = orders.driver_id
INNER JOIN order_items ON orders.order_id = order_items. order_id
INNER JOIN products ON products.prod_id = order_items.prod_id;


SELECT * FROM products;



SELECT driver_id FROM couriers
ORDER BY RAND()
LIMIT 1;  

SELECT orders.order_id, customers.customer_name,
SUM(products.prod_price * order_items.prod_qty)
FROM orders
INNER JOIN customers ON customers.customer_id = orders.order_id
INNER JOIN couriers ON couriers.driver_id = orders.driver_id
INNER JOIN order_items ON orders.order_id = order_items. order_id
INNER JOIN products ON products.prod_id = order_items.prod_id
GROUP BY orders.order_id
ORDER BY customers.customer_name;


