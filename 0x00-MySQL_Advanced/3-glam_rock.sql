SELECT band_name, 
       IFNULL(DATEDIFF(2022, split, formed), 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
