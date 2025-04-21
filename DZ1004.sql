-- ¾ Куратори (Curators)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор куратора.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ім’я (Name). Ім’я куратора.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.
-- ■ Прізвище (Surname). Прізвище куратора.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.
CREATE TABLE CURATORS(
	ID SERIAL NOT NULL PRIMARY KEY,
	NAME VARCHAR(255) NOT NULL CHECK(NAME != ''),
	SURNAME VARCHAR(255) NOT NULL CHECK(NAME != '')
)

INSERT INTO CURATORS (NAME, SURNAME) VALUES
('Ольга', 'Мельник'),
('Андрій', 'Шевченко'),
('Ірина', 'Коваль'),
('Максим', 'Гончар'),
('Світлана', 'Ткаченко');

-- ¾ Кафедри (Departments)
-- ТРЕБА ДОДАТИ
-- ■ Ідентифікатор факультету (FacultyId). Факультет, до складу
-- якого належить кафедра.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення. -- В ЗВЯЗКУ З ТИМ, ЩО НЕ ДОЗВОЛЯЄ ДОДАТИ У ВЖЕ ЗАПОВНЕНУ ТАБЛИЦЮ - ДОДАВ ЗНАЧЕННЯ ЗА ЗАМОВЧУВАННЯМ 1, ПОТІМ ПРИБРАВ 
-- 				ТА ЗРОБИВ ДВА АПДЕЙТА
-- ▷ Зовнішній ключ.
ALTER TABLE DEPARTMENTS
ADD COLUMN FACULTYID INT NOT NULL REFERENCES FACULTIES(ID)

UPDATE DEPARTMENTS
SET FACULTYID = 3
WHERE ID = 2

UPDATE DEPARTMENTS
SET FACULTYID = 2
WHERE ID = 3

UPDATE DEPARTMENTS
SET FINANCING = 140000
WHERE ID = 1

SELECT *
FROM DEPARTMENTS


-- ¾ Факультети (Faculties)
-- ДОДАТИ:
-- ■ Фінансування (Financing). Фонд фінансування факультету.
-- ▷ Тип даних — DECIMAL(10, 2).
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
ALTER TABLE FACULTIES
ADD COLUMN FINANCING DECIMAL(10, 2) NOT NULL CHECK(FINANCING >= 0) DEFAULT 0

UPDATE FACULTIES
SET FINANCING = 140000
WHERE ID = 1

SELECT *
FROM FACULTIES

-- ¾ Групи (Groups)
-- ДОДАТИ
-- ■ Ідентифікатор кафедри (DepartmentId). Кафедра, до складу
-- якої належить група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення. - В ЗАПОВНЕНІЙ ТАБЛИЦІ НЕ СПРАЦЮВАЛО - ЗРОБИВ БЕЗ, ЗАПОВНИВ ВРУЧНУ СЕТОМ
-- ▷ Зовнішній ключ.
ALTER TABLE GROUPS
ADD COLUMN DEPARTMENTID INT REFERENCES DEPARTMENTS(ID)

UPDATE GROUPS
SET DEPARTMENTID = 2
WHERE ID BETWEEN 1 AND 5

UPDATE GROUPS
SET DEPARTMENTID = 1
WHERE ID BETWEEN 6 AND 10


SELECT *
FROM GROUPS


-- ¾ Групи та куратори (GroupsCurators)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор групи та
-- куратора.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ідентифікатор куратора (CuratorId). Куратор.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.  
-- ▷ Зовнішній ключ.
-- ■ Ідентифікатор групи (GroupId). Група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ
CREATE TABLE GROUPSCURATORS(
	CURATORID INT NOT NULL REFERENCES CURATORS(ID),
	GROUPID INT NOT NULL REFERENCES GROUPS(ID),	
	PRIMARY KEY(CURATORID, GROUPID)
	)

INSERT INTO GROUPSCURATORS(
	CURATORID,
	GROUPID)
VALUES 
(1, 1),
(1, 3),
(2, 2),
(2, 4),
(3, 5),
(3, 7),
(4, 6),
(4, 8),
(5, 9),
(5, 10)

SELECT *
FROM GROUPS

SELECT *
FROM CURATORS


-- ¾ Групи та лекції (GroupsLectures)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор групи та
-- лекції.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ідентифікатор групи (GroupId). Група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.
-- ■ Ідентифікатор лекції (LectureId). Лекція.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.
CREATE TABLE GROUPSELECTURES(
	ID INT NOT NULL PRIMARY KEY,
	GROUPEID INT NOT NULL REFERENCES GROUPS(ID),
	LECTUREID INT NOT NULL REFERENCES LECTURES(ID)
	)
	
INSERT INTO GROUPSELECTURES (ID, GROUPEID, LECTUREID) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10);

-- ¾ Лекції (Lectures)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор лекції.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Аудиторія (LectureRoom). Аудиторія, в якій проходить
-- лекція.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ■ Ідентифікатор предмета (SubjectId). Предмет, з якого читається лекція.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.
-- ■ Ідентифікатор викладача (TeacherId). Викладач, який веде
-- лекцію.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.
CREATE TABLE LECTURES(
	ID SERIAL NOT NULL PRIMARY KEY,
	LECTUREROOM VARCHAR(10) NOT NULL CHECK(LECTUREROOM != ''),
	SUBJECTID INT NOT NULL REFERENCES SUBJECTS(ID),
	TEACHERID INT NOT NULL REFERENCES TEACHERS(ID)
)

INSERT INTO LECTURES (LECTUREROOM, SUBJECTID, TEACHERID) VALUES
('101-A', 1, 1),
('102-B', 2, 2),
('103-C', 3, 3),
('104-D', 4, 4),
('105-E', 5, 5),
('106-F', 6, 6),
('107-G', 7, 7),
('108-H', 8, 8),
('109-I', 9, 9),
('110-J', 10, 10),
('201-A', 1, 11),
('202-B', 2, 12),
('203-C', 3, 13),
('204-D', 4, 14),
('205-E', 5, 15),
('206-F', 6, 1),
('207-G', 7, 2),
('208-H', 8, 3),
('209-I', 9, 4),
('210-J', 10, 5);

-- ¾ Предмети (Subjects)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор предмета.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва предмета.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
CREATE TABLE SUBJECTS(
	ID SERIAL NOT NULL PRIMARY KEY,
	NAME VARCHAR NOT NULL UNIQUE
)

INSERT INTO SUBJECTS (NAME) VALUES
('Анатомія'),
('Фізіологія'),
('Біохімія'),
('Фармакологія'),
('Патофізіологія'),
('Мікробіологія'),
('Гістологія'),
('Педіатрія'),
('Хірургія'),
('Терапія')

-- ______________________________________________

-- Завдання
-- -- 1. Виведіть усі можливі пари рядків викладачів і груп.
SELECT TEACHERS.NAME, TEACHERS.SURNAME, GROUPS.NAME
FROM GROUPSELECTURES
	JOIN GROUPS ON GROUPSELECTURES.GROUPEID = GROUPS.ID	
	JOIN LECTURES ON GROUPSELECTURES.LECTUREID = LECTURES.ID
	JOIN TEACHERS ON LECTURES.TEACHERID = TEACHERS.ID

-- 2. Виведіть назви факультетів, фонд фінансування кафедр
-- яких перевищує фонд фінансування факультету.
SELECT FACULTIES.NAME
FROM FACULTIES JOIN DEPARTMENTS ON DEPARTMENTS.FACULTYID = FACULTIES.ID
WHERE DEPARTMENTS.FINANCING > FACULTIES.FINANCING

-- 3. Виведіть прізвища кураторів груп і назви груп, які вони
-- курирують.
SELECT CURATORS.SURNAME, GROUPS.NAME
FROM GROUPSCURATORS 
	JOIN GROUPS ON GROUPSCURATORS.GROUPID = GROUPS.ID
	JOIN CURATORS ON GROUPSCURATORS.CURATORID = CURATORS.ID

-- 4. Виведіть імена та прізвища викладачів, які читають лекції
-- у групі «М-201».
SELECT TEACHERS.NAME, TEACHERS.SURNAME
FROM GROUPSELECTURES
	JOIN GROUPS ON GROUPSELECTURES.GROUPEID = GROUPS.ID	
	JOIN LECTURES ON GROUPSELECTURES.LECTUREID = LECTURES.ID
	JOIN TEACHERS ON LECTURES.TEACHERID = TEACHERS.ID
WHERE GROUPS.NAME = 'М-201'

-- 6. Виведіть назви кафедр і назви груп, які до них належать.
SELECT DEPARTMENTS.NAME, GROUPS.NAME
FROM DEPARTMENTS JOIN GROUPS ON DEPARTMENTS.ID = GROUPS.DEPARTMENTID

SELECT *
FROM DEPARTMENTS

SELECT *
FROM GROUPS


-- 7. Виведіть назви предметів, які викладає викладач «Samantha
-- Adams».

-- 8. Виведіть назви кафедр, на яких викладається дисципліна
-- «Database Theory».

-- 9. Виведіть назви груп, що належать до факультету «Computer
-- -- Science».

-- 10. Виведіть назви груп 5-го курсу, а також назви факультетів,
-- до яких вони належать.

-- 11. Виведіть повні імена викладачів і лекції, які вони читають
-- (назви предметів та груп). Зробіть відбір по тим лекціям,
-- які проходять в аудиторії «B103».