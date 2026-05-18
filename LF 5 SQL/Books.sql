create Table books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100),
    price DECIMAL(10, 2),
    publication_year INTEGER,
    stock_quantity INTEGER
);

create Table customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100),
    registration_date DATE,
    country VARCHAR(50)
);

create Table orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    order_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

create Table order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    book_id INTEGER,
    quantity INTEGER,
    price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);


INSERT INTO books (title, author, price, publication_year, stock_quantity) VALUES
('Der Herr der Ringe', 'J.R.R. Tolkien', 24.99, 1954, 15),
('Harry Potter und der Stein der Weisen', 'J.K. Rowling', 19.99, 1997, 25),
('1984', 'George Orwell', 14.99, 1949, 12),
('Die Blechtrommel', 'Günter Grass', 18.50, 1959, 8),
('Das Zauberberg', 'Thomas Mann', 22.00, 1924, 10);


INSERT INTO customers (first_name, last_name, email, registration_date, country) VALUES
('Max', 'Müller', 'max.mueller@email.com', '2025-01-15', 'Deutschland'),
('Anna', 'Schmidt', 'anna.schmidt@email.com', '2025-02-20', 'Deutschland'),
('Klaus', 'Weber', 'klaus.weber@email.com', '2025-03-10', 'Österreich'),
('Eva', 'Fischer', 'eva.fischer@email.com', '2025-04-05', 'Schweiz');


INSERT INTO orders (customer_id, order_date, status) VALUES
(1, '2025-04-01', 'Delivered'),
(2, '2025-04-08', 'Pending'),
(3, '2025-04-15', 'Shipped');

INSERT INTO order_items (order_id, book_id, quantity, price) VALUES
(1, 1, 1, 24.99),
(1, 3, 1, 14.99),
(2, 2, 2, 19.99),
(2, 4, 1, 18.50),
(3, 5, 1, 22.00),
(3, 1, 1, 24.99);

select books.title, books.price, books.stock_quantity from books where price > 20;
select orders.customer_id, orders.order_date, orders.status from orders;
select order_items.order_id, order_items.book_id, order_items.quantity from order_items;
select order_items.order_id, (order_items.quantity * order_items.price) as total_price from order_items;
select sum(order_items.quantity * order_items.price) as total_revenue from order_items;
select books.title, sum(order_items.quantity * order_items.price) as total_revenue from books, order_items where books.book_id = order_items.book_id group by books.title;