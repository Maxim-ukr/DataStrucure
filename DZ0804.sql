-- ¾ Кафедри (Departments)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор кафедри.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Фінансування (Financing). Фонд фінансування кафедри.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Назва (Name). Назва кафедри.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
CREATE TABLE DEPARTMENTS(
	ID SERIAL PRIMARY KEY NOT NULL,
	FINANCING FLOAT NOT NULL CHECK(FINANCING >= 0) DEFAULT 0,
	NAME VARCHAR(100) NOT NULL CHECK(NAME != '') UNIQUE
)

INSERT INTO DEPARTMENTS (FINANCING, NAME) VALUES
(120000, 'Кардіологія'),
(85000, 'Неврологія'),
(150000, 'Хірургія'),
(95000, 'Педіатрія'),
(110000, 'Гастроентерологія');

-- ¾ Факультети(Faculties)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор факультету.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Декан (Dean). Декан факультету.
-- ▷ Тип даних — varchar(255).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнім.
-- ■ Назва (Name). Назва факультету.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
CREATE TABLE FACULTIES(
	ID SERIAL PRIMARY KEY NOT NULL,
	DEAN VARCHAR(255) NOT NULL CHECK(DEAN != ''),
	NAME VARCHAR(100) NOT NULL CHECK(NAME != '') UNIQUE
)

INSERT INTO FACULTIES (DEAN, NAME) VALUES
('Олена Іваненко', 'Медичний факультет №1'),
('Андрій Сидорчук', 'Медичний факультет №2'),
('Тетяна Коваль', 'Фармацевтичний факультет'),
('Ігор Бондар', 'Стоматологічний факультет'),
('Марина Литвин', 'Педіатричний факультет'),
('Юрій Шевченко', 'Факультет післядипломної освіти'),
('Оксана Романюк', 'Факультет медсестринства');

-- ¾ Групи (Groups)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор групи.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва групи.
-- ▷ Тип даних — varchar(10).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
-- ■ Рейтинг (Rating). Рейтинг групи.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 0 до 5.
-- ■ Курс (Year). Курс (рік), на якому навчається група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 5.
CREATE TABLE GROUPS(
	ID SERIAL PRIMARY KEY NOT NULL,
	NAME VARCHAR(10) NOT NULL CHECK(NAME != '') UNIQUE,
	RATING INT NOT NULL CHECK(RATING BETWEEN 0 AND 5),
	YEAR INT NOT NULL CHECK(RATING BETWEEN 1 AND 5)
	)

INSERT INTO GROUPS (NAME, RATING, YEAR) VALUES
('М-101', 4, 1),
('М-102', 5, 1),
('М-201', 3, 2),
('М-202', 4, 2),
('М-301', 2, 3),
('М-302', 3, 3),
('М-401', 5, 4),
('М-402', 4, 4),
('М-501', 5, 5),
('М-502', 3, 5);

-- ¾ Викладачі(Teachers)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- викладача.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
--  Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Дата працевлаштування (EmploymentDate). Дата працевлаштування викладача.
-- ▷ Тип даних — date.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше 01.01.1990.
-- ■ Асистент (IsAssistant). Чи є викладач асистентом.
-- ▷ Тип даних — bit. - НЕПРОПУСТИЛО БІТ - ПОМІНЯВ НА ІНТ І ДОДАВ ПЕРЕВІРКУ НА 1 ЧИ 0
-- ▷ Не містить null-значення.
-- ▷ Значення за замовчуванням — 0.
-- ■ Професор (IsProfessor). Чи є викладач професором.
-- ▷ Тип даних — bit.- НЕПРОПУСТИЛО БІТ - ПОМІНЯВ НА ІНТ І ДОДАВ ПЕРЕВІРКУ НА 1 ЧИ 0
-- ▷ Не містить null-значення.
-- ▷ Значення за замовчуванням — 0.
-- ■ Ім’я (Name). Ім’я викладача.
-- ▷ Тип даних — nvarchar(max). - НЕПРОПУСТИЛО НВАРЧАР - ПОМІНЯВ НА ВАРЧАР 255
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.
-- ■ Посада (Position). Посада викладача.
-- ▷ Тип даних — varchar(max). - НЕПРОПУСТИЛО ВАРЧАР МАКС ПОМІНЯВ НА 255
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ■ Надбавка (Premium). Надбавка викладача.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Ставка (Salary). Ставка викладача.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути меншою або дорівнювати 0.
-- ■ Прізвище (Surname). Прізвище викладача.
-- ▷ Тип даних — varchar(max).  - НЕПРОПУСТИЛО ВАРЧАР МАКС ПОМІНЯВ НА 255
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.
CREATE TABLE TEACHERS(
	ID SERIAL NOT NULL PRIMARY KEY,
 	EMPLOYMENTDATE DATE NOT NULL CHECK(EMPLOYMENTDATE > '1990-01-01'),
 	ISASSISTANT INT NOT NULL DEFAULT 0 CHECK(ISASSISTANT BETWEEN 0 AND 1),
	ISPROFESSOR INT NOT NULL DEFAULT 0 CHECK(ISPROFESSOR BETWEEN 0 AND 1),
	NAME VARCHAR(255) NOT NULL CHECK(NAME != ''),
	POSITION VARCHAR(255) NOT NULL CHECK(POSITION != ''),
	PREMIUM FLOAT NOT NULL CHECK(PREMIUM >= 0) DEFAULT 0,
	SALARY FLOAT NOT NULL CHECK(SALARY > 0),
	SURNAME VARCHAR(255) NOT NULL CHECK(SURNAME != '')
)

INSERT INTO TEACHERS (EMPLOYMENTDATE, ISASSISTANT, ISPROFESSOR, NAME, POSITION, PREMIUM, SALARY, SURNAME) VALUES
('2001-09-01', 1, 0, 'Олександр', 'Асистент', 1000, 18000, 'Петренко'),
('2005-02-15', 0, 1, 'Марина', 'Професор', 3000, 25000, 'Іваненко'),
('2010-06-10', 1, 0, 'Ігор', 'Асистент', 800, 15000, 'Сидорчук'),
('2003-11-20', 0, 1, 'Наталія', 'Професор', 4000, 28000, 'Коваль'),
('2008-04-05', 0, 1, 'Андрій', 'Доцент', 1500, 22000, 'Гриценко'),
('2015-09-01', 1, 0, 'Тетяна', 'Асистент', 900, 14500, 'Литвин'),
('1999-01-17', 0, 1, 'Юрій', 'Професор', 5000, 32000, 'Шевченко'),
('2017-03-20', 1, 0, 'Олена', 'Асистент', 700, 14000, 'Романюк'),
('2006-10-12', 0, 1, 'Богдан', 'Професор', 3500, 27000, 'Мельник'),
('2011-06-01', 0, 0, 'Ірина', 'Доцент', 1300, 21000, 'Захарченко'),
('2013-07-25', 1, 0, 'Дмитро', 'Асистент', 950, 16000, 'Савчук'),
('2002-02-18', 0, 1, 'Світлана', 'Професор', 3700, 26000, 'Кравець'),
('2016-10-10', 1, 0, 'Роман', 'Асистент', 870, 14200, 'Ткаченко'),
('2009-12-09', 0, 0, 'Ольга', 'Доцент', 1700, 22500, 'Федорчук'),
('2014-05-22', 1, 0, 'Євген', 'Асистент', 1100, 17500, 'Черниш');

-- ____________________________________________________________________________________________________________________
-- Для бази даних Академія створіть такі запити:
-- 1. Вивести таблицю кафедр, але розташувати її поля у зворотному порядку.

-- 2. Вивести назви груп та їх рейтинги з уточненнями до назв
-- полів відповідно до назви таблиці.
SELECT NAME AS GROUPE_NAME, RATING AS GROUPE_RATING
FROM GROUPS

-- 3. Вивести для викладачів їх прізвища, відсоток ставки по
-- відношенню до надбавки та відсоток ставки по відношенню до зарплати (сума ставки та надбавки).

-- 4. Вивести таблицю факультетів одним полем у такому форматі: «The dean of faculty [faculty] is [dean].».

-- 5. Вивести прізвища професорів, ставка яких перевищує 26000.
SELECT SURNAME
FROM TEACHERS
WHERE ISPROFESSOR = 1 AND SALARY > 26000

-- 6. Вивести назви кафедр, фонд фінансування яких менший,
-- ніж 11000 або більший за 100000.
SELECT *
FROM DEPARTMENTS
WHERE FINANCING < 11000 OR FINANCING > 100000

-- 7. Вивести назви факультетів, окрім факультету «Хірургія».
SELECT NAME
FROM DEPARTMENTS
WHERE NAME != 'Хірургія'

-- 8. Вивести прізвища та посади викладачів, які не є професорами.
SELECT SURNAME, POSITION
FROM TEACHERS
WHERE ISPROFESSOR != 1

-- 9. Вивести прізвища, посади, ставки та надбавки асистентів,
-- надбавка яких у діапазоні від 160 до 1000.
SELECT SURNAME, POSITION, SALARY, PREMIUM
FROM TEACHERS
WHERE ISASSISTANT = 1 AND PREMIUM BETWEEN 160 AND 1000

-- 10. Вивести прізвища та ставки асистентів.
SELECT SURNAME, SALARY
FROM TEACHERS
WHERE ISASSISTANT = 1

-- 11. Вивести прізвища та посади викладачів, які були прийняті
-- на роботу до 01.01.2000.
-- 12. Вивести назви кафедр, які в алфавітному порядку розміщені до кафедри «Software Development». Виведене поле
-- назвіть «Name of Department».
-- 13. Вивести прізвища асистентів із зарплатою (сума ставки
-- та надбавки) не більше 1200.
-- 14. Вивести назви груп 5-го курсу з рейтингом у діапазоні
-- від 2 до 4.

