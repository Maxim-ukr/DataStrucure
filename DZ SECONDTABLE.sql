SELECT *
FROM FV

-- Створіть наступні запити для бази даних з інформацією
-- про овочі та фрукти з попереднього домашнього завдання:
-- ■ Відображення усіх овочів з калорійністю, менше вказаної.
SELECT *
FROM FV
WHERE FV_TYPE = 'Овоч' AND CCAL < 30

-- ■ Відображення усіх фруктів з калорійністю у вказаному
-- діапазоні.
SELECT *
FROM FV
WHERE FV_TYPE = 'Фрукт' AND CCAL BETWEEN 40 AND 53

-- ■ Відображення усіх овочів, у назві яких є вказане слово.
-- Наприклад, слово: капуста.
SELECT *
FROM FV
WHERE FV_TYPE = 'Овоч' AND FV_NAME LIKE '%апуста'

-- ■ Відображення усіх овочів та фруктів, у короткому описі
-- яких є вказане слово. Наприклад, слово: гемоглобін.
SELECT *
FROM FV
WHERE OPIS LIKE '%втамін%'

-- ■ Показати усі овочі та фрукти жовтого або червоного
-- кольору.
SELECT *
FROM FV
WHERE COLOR = 'Жовтий' OR COLOR = 'Червоний'

-- Створіть наступні запити для бази даних з інформацією
-- про овочі та фрукти з попереднього домашнього завдання:
-- ■ Показати кількість овочів.
SELECT COUNT(FV_NAME) AS VEG_COUNT
FROM FV
WHERE FV_TYPE = 'Овоч'

-- ■ Показати кількість фруктів.
SELECT COUNT(FV_NAME) AS FR_COUNT
FROM FV
WHERE FV_TYPE = 'Фрукт'

-- ■ Показати кількість овочів та фруктів заданого кольору.
SELECT COUNT(FV_NAME) AS RED_COL
FROM FV
WHERE COLOR = 'Червоний'

-- ■ Показати кількість овочів та фруктів кожного кольору.
SELECT COLOR, COUNT(FV_NAME) AS COL_COUNT
FROM FV
GROUP BY COLOR

-- ■ Показати колір мінімальної кількості овочів та фруктів.
WITH COLOR_COUNT AS (
		SELECT COLOR, COUNT(FV_NAME) AS COL_COUNT
		FROM FV
		GROUP BY COLOR
)
SELECT COLOR
FROM COLOR_COUNT
WHERE COL_COUNT = (
	SELECT MIN(COL_COUNT)
	FROM COLOR_COUNT
	)

-- ■ Показати колір максимальної кількості овочів та фруктів.
WITH COLOR_COUNT AS (
		SELECT COLOR, COUNT(FV_NAME) AS COL_COUNT
		FROM FV
		GROUP BY COLOR
)
SELECT COLOR
FROM COLOR_COUNT
WHERE COL_COUNT = (
	SELECT MAX(COL_COUNT)
	FROM COLOR_COUNT
	)

-- ■ Показати мінімальну калорійність овочів та фруктів.
SELECT MIN(CCAL) AS MIN_CCAL
FROM FV

-- ■ Показати максимальну калорійність овочів та фруктів.
SELECT MAX(CCAL) AS MAX_CCAL
FROM FV

-- ■ Показати середню калорійність овочів та фруктів.
SELECT AVG(CCAL) AS AVG_fv
FROM FV

-- ■ Показати фрукт з мінімальною калорійністю.
SELECT *
FROM FV
WHERE CCAL = (
	SELECT MIN(CCAL)
	FROM FV
	WHERE FV_TYPE = 'Фрукт'
)

-- ■ Показати фрукт з максимальною калорійністю
SELECT *
FROM FV
WHERE CCAL = (
	SELECT MAX(CCAL)
	FROM FV
	WHERE FV_TYPE = 'Фрукт'
	)