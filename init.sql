
CREATE TABLE sneaker (
    id SERIAL PRIMARY KEY,
    brand_name VARCHAR(100),
    name VARCHAR(100),
    description VARCHAR(100),
    size INTEGER,
    color VARCHAR(100),
    free_delivery BOOLEAN
);


INSERT INTO sneaker (brand_name,name,description,size,color,free_delivery )
SELECT 
    'brand_name ' || generate_series,
    'name ' || generate_series,
    'description' || generate_series ,
    (random() * 11)::integer,
    'color' || generate_series ,
    random() >= 0.5 as free_delivery
FROM generate_series(1, 10000000);