USE hr;

-- Wyświetl imiona, nazwiska oraz pensje pracowników, nadaj im aliasy.
SELECT first_name AS Imię, last_name AS Nazwisko, salary AS Pensja FROM employees;



-- Wyświetl strukturę tabeli departments.
SHOW COLUMNS FROM departments;



-- Wyświetl zawartość tabeli regions.
SELECT * FROM regions;



-- Wyświetl imiona i nazwiska pracowników w jednej kolumnie.
SELECT CONCAT_WS(' ', first_name, last_name) AS Pracownik FROM employees;



-- Wyświetl alfabetyczną listę pracowników.
SELECT first_name AS Imię, last_name AS Nazwisko FROM employees 
ORDER BY first_name ASC;



-- Wyświetl nazwiska i pensje pracowników w porządku malejącym wg pensji.
SELECT first_name AS Imię, last_name AS Nazwisko, salary AS Pensja FROM employees
ORDER BY salary DESC;



-- Wyświetl imiona, nazwiska i pensje pracowników w porządku rosnącym wg pensji i malejącym wg nazwisk.
SELECT first_name AS Imię, last_name AS Nazwisko, salary AS Pensja FROM employees
ORDER BY salary ASC, last_name DESC;



-- Wyświetl listę nazwisk. W wyniku nie mogą pojawić się duplikaty nazwisk.
SELECT DISTINCT last_name FROM employees
ORDER BY last_name;


/*
Popraw następujace zapytania: A:select * from countri; B:select department_name, from employees; 
C:select hire_date as data zatrudnienia from employees; D:select name nazwisko pracownika from employees.
*/
-- A
SELECT * FROM countries;

-- B
SELECT department_name FROM departments;

-- C
SELECT hire_date AS "Data zatrudnienia" FROM employees;

-- D
SELECT last_name AS "Nazwisko pracownika" FROM employees;



-- Wyświetl imię, nazwisko oraz datę zatrudnienia wszystkich pracowników, których pensja nie znajduje się w przedziale [4000, 12 000]. Wyniki posortuj rosnąco wg pensji.
SELECT first_name AS Imię, last_name AS Nazwisko, hire_date AS "Data zatrudnienia", salary AS Pensja FROM employees
WHERE salary NOT BETWEEN 4000 AND 12000
ORDER BY salary;



-- Wyświetl dane osób o identyfikatorach 100, 102, 105 i 107.
SELECT * FROM employees
WHERE employee_id IN (100, 102, 105, 107);



-- Wyświetl nazwiska pracowników, którzy zarabiają poniżej 3000.
SELECT last_name AS Nazwisko, salary AS Pensja FROM employees
WHERE salary < 3000;



-- Wyświetl imiona i nazwiska pracowników, których pensja znajduje się w przedziale [3000, 8 000].
SELECT first_name AS Imię, last_name AS Nazwisko, salary AS Pensja FROM employees
WHERE salary BETWEEN 3000 AND 8000;



-- Wyświetl bez duplikatów identyfikatory stanowisk z tabeli employees.
SELECT DISTINCT employee_id FROM employees;



-- Wyświetl nazwisko, pensję i premię pracowników, których nazwisko zaczyna się na literę ‘M’.
SELECT last_name AS Nazwisko, salary AS Pensja, ROUND((commission_pct * salary),2) AS Premia FROM employees
WHERE commission_pct IS NOT NULL AND last_name LIKE 'M%';



-- Wyświetl imiona i nazwiska pracowników zatrudnionych w oddziale o identyfikatorze 60.
SELECT first_name AS Imię, last_name AS Nazwisko, department_id AS "Numer departamentu" FROM employees
WHERE department_id = 60;



-- Wyświetl dane pracowników, którzy nie mają premii.
SELECT * FROM employees
WHERE commission_pct IS NULL;



-- Wyświetl imiona i nazwiska pracowników, których druga litera imienia to ‘e’.
SELECT first_name AS Imię, last_name AS Nazwisko FROM employees
WHERE first_name LIKE '_e%';



-- Wyświetl bez duplikatów identyfikatory oddziałów z tabeli employees.
SELECT DISTINCT department_id FROM employees;



-- Wyświetl imiona, nazwiska i pensje pracowników, którzy mają pensję powyżej 9000.
SELECT first_name AS Imię, last_name AS Nazwisko, salary AS Pensja FROM employees
WHERE salary > 9000;



-- Wyświetl imiona, nazwiska i pensje powiększone o 20% pracowników zatrudnionych w oddziale o identyfikatorze 50. 
SELECT first_name AS Imię, last_name AS Nazwisko, salary AS "Pensja podstawowa", salary + salary * 0.2 AS "Pensja +20%", department_id AS "Numer departamentu" FROM employees
WHERE department_id = 50;



-- Wyświetl dane oddziałów o identyfikatorze lokalizacji większym od 1500.
SELECT * FROM departments
WHERE location_id > 1500;



-- Wyświetl nazwy krajów posortowane w porządku rosnącym.
SELECT DISTINCT country_id AS "Nazwa kraju" FROM locations
ORDER BY country_id ASC;



-- Wyświetl dane pracowników, których zarobki mieszczą się w przedziale [6 000; 8 000] (podaj dwa rozwiązania).
SELECT * FROM employees
WHERE salary BETWEEN 6000 AND 8000;

SELECT * FROM employees
WHERE salary > 6000 AND salary < 8000;



-- Wyświetl nazwy oddziałów, dla których nie wprowadzono kierownika.
SELECT department_name AS "Nazwa departamentu" FROM departments
WHERE manager_id IS NULL;



-- Wyświetl dane pracowników, uporządkowane malejąco wg pensji.
SELECT * FROM employees
ORDER BY salary DESC;



-- Wyświetl dane pracowników oddziału o identyfikatorze 60 uporządkowaną malejąco wg pensji.
SELECT * FROM employees
WHERE department_id = 60
ORDER BY salary DESC;



-- Wyświetl dane pracowników oddziałów o identyfikatorach 50, 60, 100 (podaj dwa rozwiązania).
SELECT * FROM employees
WHERE department_id IN (50, 60, 100);

SELECT * FROM employees
WHERE department_id = 50 OR department_id = 60 OR department_id = 100;



-- Wyświetl dane pracowników o identyfikatorach oddziałów 70, 80, 110, dla których pensja nie znajduje się w przedziale [5 000; 9 000]. Wyniki posortuj wg pensji.
SELECT * FROM employees
WHERE employee_id IN (70, 80, 110) AND salary BETWEEN 5000 AND 9000
ORDER BY salary;



-- Wyświetl imiona, nazwiska, daty zatrudnienia i pensje pracowników zatrudnionych na stanowisku ST_CLERK, których data zatrudnienia nie przypada na lata 1996-1998.
SELECT first_name AS Imię, last_name AS Nazwisko, hire_date AS "Data zatrudnienia", salary AS Pensja FROM employees
WHERE job_id = 'ST_CLERK' AND YEAR(hire_date) BETWEEN 1996 AND 1998;



-- Wyświetl dane prezesa.
SELECT * FROM employees
WHERE manager_id IS NULL;



-- Wyświetl imiona pracowników bez powtórzeń. Wyniki posortuj rosnąco.
SELECT DISTINCT first_name AS Imię FROM employees
ORDER BY first_name;



-- Wyświetl nazwy oddziałów, dla których drugą literą w nazwie nie jest 'o'.
SELECT department_name AS "Nazwa departamentu" FROM departments
WHERE department_name NOT LIKE '_o%';



-- Wyświetl dane pracowników, których email kończy się literą 's' i są zatrudnieni w oddziałach o identyfikatorach 90, 110.
SELECT * FROM employees
WHERE email LIKE '%s' AND department_id IN (90, 110);



-- Wyświetl dane oddziałów, dla których identyfikator lokalizacji jest różny od 1700.
SELECT * FROM departments
WHERE location_id != 1700;



-- Wyświetl różne imiona pracowników rozpoczynające się na literę K lub A. Wyniki posortuj rosnąco.
SELECT DISTINCT first_name AS Imię FROM employees
WHERE first_name LIKE 'K%' OR first_name LIKE 'A%'
ORDER BY first_name;



-- Wyświetl imiona, nazwiska i pensje powiększone o 20% pracowników zatrudnionych w oddziałach o identyfikatorach 50, 60 i 80.
SELECT first_name AS Imię, last_name AS Nazwisko, salary AS Pensja, ROUND((salary + salary * 0.2),2) AS "Pensja + 20%", department_id AS "Numer departamentu" FROM employees
WHERE department_id IN (50, 60, 80);



-- Wyświetl lokalizacje dla których nie wprowadzono kodu pocztowego.
SELECT * FROM locations
WHERE postal_code IS NULL;



-- Wyświetl dane oddziałów o identyfikatorze lokalizacji większym od 2000.
SELECT * FROM departments
WHERE location_id > 2000;



-- Wyświetl miasta nie znajdujące się w prowicji oraz których nazwy rozpoczynają się na literę T i B.
SELECT city AS Miasto FROM locations
WHERE state_province IS NULL AND city LIKE 'V%' OR city LIKE 'L%';



-- Wyświetl minimalne i maksymalne pensje dla poszczególnych stanowisk.
SELECT job_title AS "Nazwa stanowiska", MIN(min_salary) AS Minimalne, MAX(max_salary) AS Maksymalne FROM jobs
GROUP BY job_title;



-- Wyświetl nazwy stanowisk minimalne pensje i minimalne pensje powiększone o 10%. Wyniki posortuj wg minimalnej pensji.
SELECT job_title AS "Nazwa stanowiska", MIN(min_salary) + MIN(min_salary) * 0.1 AS "Minimalne +10%", MAX(max_salary) + MAX(max_salary) * 0.1 AS "Maksymalne +10%" FROM jobs
GROUP BY job_title
ORDER BY MIN(min_salary) + MIN(min_salary) * 0.1 DESC;



-- Wyświetl nazwy stanowisk i różnice pomiędzy maksymalnymi i minimalnymi pensjami (nadaj kolumnie alias ROZNICA). Wyniki posortuj wg różnicy.
SELECT job_title AS "Nazwa stanowiska", MAX(min_salary) + MIN(min_salary) AS Różnica FROM jobs
GROUP BY job_title
ORDER BY Różnica DESC;



-- Wyświetl bez duplikatów identyfikatory lokalizacji z tabeli DEPARTMENTS.
SELECT DISTINCT location_id FROM departments;



-- Wyświetl nazwy regionów posortowane w porządku rosnącym.
SELECT region_name FROM regions
ORDER BY region_name;



-- Wyświetl minimalną i maksymalną pensję dla stanowisk o nazwie rozpoczynającej się od ’Sale’.
SELECT job_title AS Stanowisko, min_salary AS Minimalna, max_salary AS Maksymalna FROM jobs
WHERE job_title LIKE 'Sale%';



-- Wyświetl średnią pensję osób zatrudnionych na stanowisku IT_PROG.
SELECT ROUND(AVG(salary),2) AS "Średnia pensja" FROM employees
WHERE job_id = 'IT_PROG';



-- Wyświetl średnią, minimalną i maksymalną pensję pracowników.
SELECT ROUND(MAX(salary),2) AS "Maksymalna pensja", ROUND(MIN(salary),2) AS "Minimalna pensja", ROUND(AVG(salary),2) AS "Średnia pensja" FROM employees;



-- Wyświetl sumę, średnią, minimalną i maksymalną pensję pracowników, których przełożonym nie jest prezes.
SELECT ROUND(MAX(salary),2) AS "Maksymalna pensja", ROUND(MIN(salary),2) AS "Minimalna pensja", ROUND(AVG(salary),2) AS "Średnia pensja" FROM employees
WHERE manager_id IS NOT NULL AND manager_id != 100;




-- Wyświetl zestawienie pokazujące sumy zarobków dla poszczególnych stanowisk.
SELECT job_id AS Stanowisko, SUM(salary) AS "Suma zarobków" FROM employees
GROUP BY job_id;



-- Wyświetl zestawienie pokazujące liczbę pracowników dla poszczególnych stanowisk.
SELECT job_id AS Stanowisko, COUNT(job_id) AS "Liczba pracowników" FROM employees
GROUP BY job_id;



/*
Wyświetl zestawienie pokazujące średnie zarobków dla poszczególnych stanowisk, ale tylko dla tych na których jest zatrudnionych co najmniej 
trzech pracowników. W wyniku powinna pojawić się również liczba pracowników zatrudnionych na poszczególnych stanowiskach.
*/
SELECT job_id AS Stanowisko, AVG(salary) AS "Średnia zarobków", COUNT(job_id) AS "Liczba pracowników" FROM employees
GROUP BY job_id
HAVING COUNT(job_id) >= 3;



-- Wyświetl zestawienie imion wraz z liczbą ich powtórzeń. Wyniku powinny pojawić się tylko imiona powtarzające się. Posortuj je malejąco wg liczby wystąpień.
SELECT first_name AS Imię, COUNT(first_name) AS "Ilość wystąpień" FROM employees
GROUP BY first_name
HAVING COUNT(first_name) > 1
ORDER BY COUNT(first_name) DESC;



-- Wyświetl oddziały, w których średnia pensja jest wyższa od 9000.
SELECT department_id AS "Numer oddziału", ROUND(AVG(salary),2) AS "Średnia pensja" FROM employees
GROUP BY department_id
HAVING AVG(salary) > 9000;



-- Wyświetl różnicę pomiędzy maksymalną i minimalną pensją w poszczególnych działach.
SELECT department_id AS "Numer oddziału", MAX(salary) - MIN(salary) AS Różnica FROM employees
GROUP BY department_id;




-- Wyświetl najwyższą pensję wśród pracowników podlegających każdemu z kierowników. Wyniki posortuj według identyfikatorów kierowników.
SELECT manager_id AS "Numer kierownika", MAX(salary) AS "Maksymalna pensja" FROM employees
GROUP BY manager_id
ORDER BY manager_id;



-- Wyświetl maksymalną pensję dla każdego działu. Wyniki posortuj wg maksymalnej pensji.
SELECT department_id AS "Nazwa departamentu", MAX(salary) AS "Maksymalna pensja" FROM employees
GROUP BY department_id
ORDER BY MAX(salary);



-- Wyświetl liczbę pracowników oraz liczbę niepowtarzających się pensji dla każdego działu.
SELECT department_id AS "Numer oddziału", COUNT(job_id) AS "Ilość pracowników", ROUND(AVG(DISTINCT salary),2) AS "Średnia pensja działu bez powtarzających się" FROM employees
GROUP BY department_id;



-- Wyświetl średnią pensję dla każdego działu bez powtarzających się pensji.
SELECT department_id, ROUND(AVG(DISTINCT salary),2) FROM employees
GROUP BY department_id;



-- Wyświetl maksymalną pensję dla działów o identyfikatorach 50,60 i 100.
SELECT department_id AS "Numer oddziału", MAX(salary) AS "Maksymalna pensja" FROM employees
GROUP BY department_id
HAVING department_id IN(50, 60, 100);



-- Wyświetl minimalną pensję dla każdego działu. W obliczeniach uwzględnij tylko osoby które nie mają litery ‘o’ w nazwisku.
SELECT department_id AS "Numer oddziału", MIN(salary) AS "Minimalna pensja" FROM employees
WHERE last_name NOT LIKE '%o%'
GROUP BY department_id;



-- Wyświetl minimalną i maksymalną pensję dla każdego działu, ale tylko dla działów, w których zatrudnionych jest mniej niż pięciu pracowników.
SELECT department_id AS "Numer departamentu", MIN(salary) AS "Pensja minimalna", MAX(salary) AS "Pensja maksymalna", COUNT(*) AS "Ilość pracowników" FROM employees
GROUP BY department_id
HAVING COUNT(*) < 5;



-- Sprawdź, czy identyfikatory oddziałów w tabeli DEPARTMENTS są unikalne.
SELECT department_id AS "Numer departamentu", COUNT(department_id) AS "Ilość wystąpień" FROM departments
GROUP BY department_id
HAVING COUNT(department_id) > 1;



-- Wyświetl najwcześniejszą i najpóźniejszą datę zatrudnienia pracowników w poszczególnych działach. Wyniki posortuj wg identyfikatora oddziału.
SELECT department_id AS "Numer departamentu", MIN(hire_date) AS Najwcześniej, MAX(hire_date) AS Najpóźniej FROM employees
GROUP BY department_id
ORDER BY department_id; 



/*
Wyświetl liczbę pracowników zatrudnionych na poszczególnych stanowiskach. W wyniku uwzględnij tylko stanowiska na których jest 
zatrudnionych więcej niż 10-ciu pracowników.
*/
SELECT job_id AS Stanowisko, COUNT(job_id) AS "Ilość pracowników" FROM employees
GROUP BY job_id
HAVING COUNT(job_id) > 10;



-- Wyświetl średnie pensje wypłacane w ramach poszczególnych stanowisk i liczbę pracowników zatrudnionych na danym etacie. Pomiń pracowników zatrudnionych w 2000 roku.
SELECT job_id AS "Nazwa stanowiska", ROUND(AVG(salary),2) AS "Średnia pensja", COUNT(job_id) AS "Ilość pracowników" FROM employees
WHERE YEAR(hire_date) != 2000
GROUP BY job_id;



-- Dla każdego kierownika wyświetl pensję najgorzej zarabiającego podwładnego.
SELECT manager_id AS "Kod kierownika", MIN(salary) AS "Minimalna pensja" FROM employees
GROUP BY manager_id;



-- Wyświetl średnie zarobki dla stanowisk ST_CLERK, ST_MAN.
SELECT job_id, ROUND(AVG(salary),2) FROM employees
GROUP BY job_id
HAVING job_id = 'ST_CLERK' OR job_id = 'ST_MAN';



-- Wyświetl liczbę oddziałów znajdujących się w poszczególnych lokalizacjach.
SELECT location_id AS "Kod lokalizacji", COUNT(location_id) AS "Ilość oddziałów" FROM departments
GROUP BY location_id;



-- Napisz zapytanie aby wyświetlić imię, nazwisko, numer działu i nazwę działu dla każdego pracownika.
SELECT e.first_name AS Imię, e.last_name AS Nazwisko, e.department_id AS "Numer departmentu", d.department_name AS "Nazwa depaertamentu"
FROM employees e
JOIN departments d
ON e.department_id = d.department_id;



-- Napisz zapytanie aby wyświetlić imię i nazwisko, departament, miasto i stan dla pracowników z departamentu IT.
SELECT e.first_name AS Imię, e.last_name AS Nazwisko, d.department_id AS "Numer departamentu", l.city AS Miasto, l.state_province AS "Stan"
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
JOIN locations l
ON d.location_id = l.location_id
WHERE e.department_id = 60;



-- Napisz zapytanie aby wyświetlić imię, nazwisko, numer działu i nazwę działu dla wszystkich pracowników z działu 80 lub 40.
SELECT e.first_name AS Imię, e.last_name AS Nazwisko, e.department_id AS "Numer departamentu", d.department_name AS "Nazwa departamentu"
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
WHERE e.department_id IN (40, 80);



-- Napisz zapytanie aby wyświetlić tych pracowników, którzy w posiadją litrę 'z' w imieniu, a także wyświetlić ich nazwisko, departament, miasto i stan.
SELECT e.last_name AS Nazwisko, d.department_name AS Departament, l.city AS Miasto, l.state_province AS Stan
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
JOIN locations l
ON d.location_id = l.location_id
WHERE e.first_name LIKE '%z%';



-- Napisz zapytanie aby wyświetlić wszystkie działy, w tym te, w których pracuje mniej niż 5 pracowników.
SELECT e.department_id AS "Numer departamentu", d.department_name AS Departament, COUNT(*) AS "Liczba pracowników" 
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
GROUP BY e.department_id
HAVING COUNT(*) < 5;



-- Napisz zapytanie aby wyświetlić imiona wszystkich pracowników, w tym imię ich menedżera.
SELECT e.first_name AS Pracownik, p.first_name AS Przełożony
FROM employees e
JOIN employees p
ON e.employee_id = p.manager_id;



-- Napisz zapytanie aby wyświetlić ID pracownika, nazwę pracy, liczbę dni przepracowanych dla wszystkich zadań w dziale 80.
SELECT e.employee_id AS "Numer pracownika", j.job_title AS Stanowisko, DATEDIFF(CURRENT_DATE(), e.hire_date) AS "Przepracowanych dni do dziś", e.department_id AS Departament
FROM employees e
JOIN jobs j
ON e.job_id = j.job_id
WHERE department_id = 80;



-- Napisz zapytanie aby wyświetlić nazwę działu, średnią pensję pracowników oraz liczbę pracowników zatrudnionych w każdym dziale, którzy otrzymali prowizję.
SELECT d.department_name AS Departament, ROUND(AVG(salary),2) AS "Średnia pensja", COUNT(commission_pct) AS "Liczba osób z prowizją"
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_id;



-- Napisz zapytanie aby wyświetlić imię, nazwisko i numer działu dla pracowników, którzy pracują w tym samym dziale, co pracownik, który ma maila 'WTAYLOR'.
SELECT * FROM employees
WHERE email = 'WTAYLOR';

SELECT first_name AS Imie, last_name AS Nazwisko, department_id AS 'Numer departamentu' FROM employees
WHERE department_id = 50;



-- Napisz zapytanie aby wyświetlić imię, nazwisko dla wszystkich pracowników, którzy nie mają żadnego działu.
SELECT first_name AS Imię, last_name AS Nazwisko FROM employees
WHERE department_id IS NULL;



-- Wyświetl wszystkie nazwy regionów przyporządkowując je do nazw krajów.
SELECT r.region_name AS Region, c.country_name AS Kraj
FROM regions r
JOIN countries c
ON r.region_id = c.region_id;



-- Wyświetl różnicę pomiędzy najwyższymi a najniższymi zarobkami w departamencie “Finance”.
SELECT d.department_name AS Departament, ROUND(MAX(e.salary) - MIN(e.salary),2) AS Różnica
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
GROUP BY e.department_id
HAVING e.department_id = 100;



-- Wyświetl nazwiska pracowników oraz nazwiska ich przełożonych.
SELECT e.last_name AS Przełożony, p.last_name AS Pracownik
FROM employees e
JOIN employees p
ON e.employee_id = p.manager_id;



-- Wyświetl nazwiska pracowników oraz nazwy departamentów w których pracują.
SELECT e.last_name AS Pracownik, d.department_name AS Departament
FROM employees e
JOIN departments d
ON e.department_id = d.department_id;



-- Wyświetl nazwiska pracowników oraz nazwy regionów w których pracują.
SELECT e.last_name AS Pracownik, region_name AS Region
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
JOIN locations l
ON d.location_id = l.location_id
JOIN countries c
ON l.country_id = c.country_id
JOIN regions r
ON c.region_id = r.region_id;


-- Utwórz nową bazę o nazwie 'ksiegarnia'.
CREATE SCHEMA `ksiegarnia`;


USE ksiegarnia;

-- Utworz tabelę 'books' zawierającą książki, pola: title, author, published, isbn, category, page_count, publisher, price.
CREATE TABLE IF NOT EXISTS books (
	title VARCHAR(50),
    author VARCHAR(50),
    published DATE,
    isbn CHAR(17),
    category VARCHAR(50),
    page_count INT,
    publisher VARCHAR(50),
    price DECIMAL(10,2)
) ENGINE = INNODB;



-- Dodaj do tabeli numer kolumnę numer id z inkrementacją oraz primary key.
ALTER TABLE books
ADD COLUMN book_id INT AUTO_INCREMENT PRIMARY KEY;


-- Kolumna isbn nie może akceptować wartości NULL.
ALTER TABLE books
MODIFY isbn CHAR(17) NOT NULL;



-- Kolumna publisher powinna być wypełniane wartością ‘nieznana’ jeśli nie zostanie podana wartość w INSERT.
ALTER TABLE books
ALTER publisher SET DEFAULT 'nieznana';



-- Dodajemy kolumnę z liczbą sztuk książki 'in_stok' z wartością domyślną 0.
ALTER TABLE books
ADD COLUMN in_stock INT DEFAULT 0;



-- Popraw nazwę kolumny 'in_stok' na 'in_stock'.
ALTER TABLE books
CHANGE in_stok in_stock INT;

ALTER TABLE books
ALTER in_stock SET DEFAULT 0;



-- Dodaj rekordy
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('Spring w akcji. Wydanie IV', 'Craig Walls', '2017-08-13', '234-83-283-0849-1', 'programowanie java', 624, 'Helion', 89.00);
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('MySQL. Vademecum profesjonalisty', 'Paul DuBois', '2016-03-29', '246-83-246-8146-9', 'bazy danych', 1216, 'Helion', 149.00);
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('ORACLE-sql', 'Marek Mycha', '2016-08-13', '978-82-283-0849-8', 'programowanie sql', 454, 'Helion', 234.00);
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('ORACLE-administracja', 'Pawel Nowak', '2015-03-28', '918-83-246-8146-5', 'bazy danych', 16, 'Helion', 1349.00);
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('MS_SQL bazy', 'Luja Sliwa', '2013-01-13', '323-82-283-0849-7', 'bazy danych', 6224, 'Helion', 2354.00);
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('MS_SQL programowanie', 'Mariusz Oziebly', '2012-04-15', '234-83-246-8146-4', 'programowanie sql', 162, 'Helion', 319.00);
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('IBW', 'Adam Jakis', '2014-05-16', '345-83-246-8132-9', 'programowanie ibm', 262, 'Matrix', 198.00);
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('IBM-DB2', 'Agata Loy', '2011-01-10', '678-23-316-913-1', 'bazy danych', 762, 'Matrix', 18.00);



-- Usuń wszystkie rekordy z tabeli books.
TRUNCATE TABLE books;



-- Utwórz tabele db_books, js_books i przekopiuj do nich wszystkie książki odpowiednio z kategorii ‘bazy danych’ oraz ‘programowanie java (pomijając kolumnę kategoria).
CREATE TABLE db_books
AS SELECT * FROM books 
WHERE category = 'bazy danych'; 

CREATE TABLE js_books
AS SELECT * FROM books
WHERE category = 'programowanie java';



/*
Utwórz dwie tabele: 'categories' i 'products' i dodaj do nich 2 kategorie i 4 produkty.
Każda kategoria posiada jeden lub więcej produktów, ale każdy produkt należy tylko do jednej kategorii.
*/
CREATE TABLE IF NOT EXISTS categories (
	cat_id INT AUTO_INCREMENT,
    cat_name VARCHAR(50),
    PRIMARY KEY (cat_id)
) ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS products (
	prod_id INT AUTO_INCREMENT,
    prod_name VARCHAR(50),
    cat_id INT,
	PRIMARY KEY (prod_id)
) ENGINE = INNODB;

INSERT INTO categories VALUES (DEFAULT, 'Monitory');
INSERT INTO categories VALUES (DEFAULT, 'Klawiatury');

INSERT INTO products VALUES (DEFAULT, 'LG Turbo 27"', 3);
INSERT INTO products VALUES (DEFAULT, 'Samsung Master 32"', 3);
INSERT INTO products VALUES (DEFAULT, 'Microsoft 800 + myszka', 2);
INSERT INTO products VALUES (DEFAULT, 'TechKey 32 klawisze', 2);

ALTER TABLE products
ADD CONSTRAINT prod_to_cat
FOREIGN KEY (cat_id) REFERENCES categories (cat_id)
ON DELETE NO ACTION;

ALTER TABLE products DROP FOREIGN KEY testowe_polaczenie;

DELETE FROM categories
WHERE cat_id = 1;

DELETE FROM products
WHERE prod_id IN (3, 4);



USE hr;
-- Dodaj indeks o nazwie first_last_name_idx na tabeli employees zakładając go na kolumnach first_name i last_name.
CREATE INDEX first_last_name
ON employees (first_name, last_name);



/*
Dodaj unikalny indeks o nazwie cn_idx na tabeli countries zakładając go na kolumnie country_name, dodaj 
duplikat państwa w kolumnie country_name i dodaj kolejny index cn_idx1 (sprawdź jaki komunikat zwrócił serwer bazydanych).
*/
CREATE UNIQUE INDEX cn_idx
ON countries (country_name);

INSERT INTO countries VALUES('DU', 'Argentina', 2);
-- Error code 1062: na kolumnie country_name istnieje index.

CREATE UNIQUE INDEX cn_idx1
ON countries (country_name);
-- Warning 1831: Duplikat indexu na tej samej tabeli, ale założył drugi index. 



-- Usuń index cn_idx1
DROP INDEX cn_idx1 ON countries;


/*
Utwórz  widok  o  nazwie  max_pensje  który  będzie  wyświetlał  nazwę  działu, maksymalną pensję pracowników oraz liczbę pracowników zatrudnionych w każdym
dziale, którzy otrzymali prowizję.
*/
CREATE VIEW max_pensje AS 
SELECT d.department_name AS Departament, ROUND(MAX(e.salary),2) AS "Maksymalna pensja", COUNT(e.employee_id) AS "Ilość pracowników"
FROM departments d
JOIN employees e
ON d.department_id = e.department_id
WHERE e.commission_pct IS NOT NULL
GROUP BY d.department_name;

SELECT * FROM max_pensje;
DROP VIEW max_pensje;
