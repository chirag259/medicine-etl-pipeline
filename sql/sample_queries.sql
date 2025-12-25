 --View sample medicines
SELECT * 
FROM medicines 
LIMIT 10;

--Count total medicines
SELECT COUNT(*) AS total_medicines
FROM medicines;

--Find medicines by name (search)
SELECT medicine_id, name, price
FROM medicines
WHERE name LIKE '%Paracetamol%';

--Get all discontinued medicines
SELECT medicine_id, name, manufacturer
FROM medicines
WHERE is_discontinued = TRUE;

--Medicines by type (allopathy / ayurvedic etc.)
SELECT medicine_id, name, type
FROM medicines
WHERE type = 'allopathy';

--Medicines within a price range
SELECT name, price
FROM medicines
WHERE price BETWEEN 50 AND 200
ORDER BY price ASC;

--Top 10 most expensive medicines
SELECT name, price
FROM medicines
ORDER BY price DESC
LIMIT 10;

--Medicines with missing salt composition
SELECT medicine_id, name
FROM medicines
WHERE salt_composition IS NULL;

--Medicines with side effects listed
SELECT name, side_effects
FROM medicines
WHERE side_effects IS NOT NULL;


--Count medicines per manufacturer
SELECT manufacturer, COUNT(*) AS medicine_count
FROM medicines
GROUP BY manufacturer
ORDER BY medicine_count DESC;

-- Find medicines containing a specific salt
SELECT name, salt_composition
FROM medicines
WHERE salt_composition LIKE '%Azithromycin%';

--Medicines with drug interactions
SELECT name, drug_interactions
FROM medicines
WHERE drug_interactions IS NOT NULL
  AND drug_interactions != '';

--Average price of medicines by type
SELECT type, AVG(price) AS avg_price
FROM medicines
GROUP BY type;

