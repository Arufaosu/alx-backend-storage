-- lists all bands with 'Glam rock' as their main style
SELECT
	band_name,
	(
		CASE
		WHEN split IS NULL THEN 2022
		ELSE split
		END - formed
	) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
