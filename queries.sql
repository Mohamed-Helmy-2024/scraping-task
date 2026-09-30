DROP TABLE IF EXISTS books;
CREATE TABLE books (
    title TEXT,
    price REAL,
    rating INTEGER,
    in_stock TEXT,
    url TEXT
);

.mode csv
.import --skip 1 books.csv books

-- 1. Average price for each rating
SELECT
    rating,
    ROUND(AVG(price), 2) AS average_price
FROM books
GROUP BY rating
ORDER BY rating;

-- 2. The 5 most expensive books rated 4 or 5
SELECT
    title,
    price,
    rating
FROM books
WHERE rating IN (4, 5)
ORDER BY price DESC
LIMIT 5;

-- 3. How many books are out of stock, per rating
SELECT
    rating,
    SUM(in_stock = 'False') AS out_of_stock
FROM books
GROUP BY rating
ORDER BY rating;