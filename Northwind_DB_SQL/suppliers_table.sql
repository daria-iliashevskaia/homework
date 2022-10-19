-- drop table
DROP TABLE IF EXISTS suppliers;

--Name: suppliers; Type: TABLE; Schema: public; Owner: -; Tablespace:
CREATE TABLE IF NOT EXISTS suppliers (
        suppliers_id INTEGER NOT NULL,
        company_name VARCHAR (80),
        contact_name VARCHAR (80),
        contact_title VARCHAR (80),
        ad_country VARCHAR (80),
        ad_state VARCHAR (80),
        ad_index text,
        ad_city VARCHAR (80),
        ad_street VARCHAR (80),
        phone VARCHAR (80),
        fax VARCHAR (80),
        homepage VARCHAR (80)
        );

-- Data for Name: suppliers; Type: TABLE DATA; Schema: public; Owner: -
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(1, 
            'Exotic Liquids', 
            'Charlotte Cooper', 
            'Purchasing Manager', 
            'UK',
            '',
            'EC1 4SD',
            'London',
            '49 Gilbert St.'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(2, 
            'New Orleans Cajun Delights', 
            'Shelley Burke', 
            'Order Administrator', 
            'USA',
            'LA',
            '70117',
            'New Orleans',
            'P.O. Box 78934'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(3, 
            'Grandma Kelly_s Homestead', 
            'Regina Murphy', 
            'Sales Representative', 
            'USA',
            'MI',
            '48104',
            'Ann Arbor',
            '707 Oxford Rd.'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(4, 
            'Tokyo Traders', 
            'Yoshi Nagase', 
            'Marketing Manager', 
            'Japan',
            '',
            '100',
            'Tokyo',
            '9-8 Sekimai Musashino-shi'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(5, 
            'Cooperativa de Quesos _Las Cabras_', 
            'Antonio del Valle Saavedra', 
            'Export Administrator', 
            'Spain',
            'Asturias',
            '33007',
            'Oviedo',
            'Calle del Rosal 4'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(6, 
            'Mayumi_s', 
            'Mayumi Ohno', 
            'Marketing Representative', 
            'Japan',
            '',
            '545',
            'Osaka',
            '92 Setsuko Chuo-ku'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(7, 
            'Pavlova, Ltd.', 
            'Ian Devling', 
            'Marketing Manager', 
            'Australia',
            'Victoria',
            '3058',
            'Melbourne',
            '74 Rose St. Moonie Ponds'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(8, 
            'Specialty Biscuits, Ltd.', 
            'Peter Wilson', 
            'Sales Representative', 
            'UK',
            '',
            'M14 GSD',
            'Manchester',
            '29 King_s Way'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(9, 
            'PB Knäckebröd AB', 
            'Lars Peterson', 
            'Sales Agent', 
            'Sweden',
            '',
            'S-345 67',
            'Göteborg',
            'Kaloadagatan 13'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(10, 
            'Refrescos Americanas LTDA', 
            'Carlos Diaz', 
            'Marketing Manager', 
            'Brazil',
            '',
            '5442',
            'Sao Paulo',
            'Av. das Americanas 12.890'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(11, 
            'Heli Süßwaren GmbH & Co. KG', 
            'Petra Winkler', 
            'Sales Manager', 
            'Germany',
            '',
            '10785',
            'Berlin',
            'Tiergartenstraße 5'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(12, 
            'Plutzer Lebensmittelgroßmärkte AG', 
            'Martin Bein', 
            'International Marketing Mgr.', 
            'Germany',
            '',
            '60439',
            'Frankfurt',
            'Bogenallee 51'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(13, 
            'Nord-Ost-Fisch Handelsgesellschaft mbH', 
            'Sven Petersen', 
            'Coordinator Foreign Markets', 
            'Germany',
            '',
            '27478',
            'Cuxhaven',
            'Frahmredder 112a'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(14, 
            'Formaggi Fortini s.r.l.', 
            'Elio Rossi', 
            'Sales Representative', 
            'Italy',
            '',
            '48100',
            'Ravenna',
            'Viale Dante, 75'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(15, 
            'Norske Meierier', 
            'Beate Vileid', 
            'Marketing Manager', 
            'Norway',
            '',
            '1320',
            'Sandvika',
            'Hatlevegen 5'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(16, 
            'Bigfoot Breweries', 
            'Cheryl Saylor', 
            'Regional Account Rep.', 
            'USA',
            'OR',
            '97101',
            'Bend',
            '3400 - 8th Avenue Suite 210'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(17, 
            'Svensk Sjöföda AB', 
            'Michael Björn', 
            'Sales Representative', 
            'Sweden',
            '',
            'S-123 45',
            'Stockholm',
            'Brovallavägen 231'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(18, 
            'Aux joyeux ecclésiastiques', 
            'Guylène Nodier', 
            'Sales Manager', 
            'France',
            '',
            '75004',
            'Paris',
            '203, Rue des Francs-Bourgeois'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(19, 
            'New England Seafood Cannery', 
            'Robb Merchant', 
            'Wholesale Account Agent', 
            'USA',
            'MA',
            '02134',
            'Boston',
            'Order Processing Dept. 2100 Paul Revere Blvd.'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(20, 
            'Leka Trading', 
            'Chandra Leka', 
            'Owner', 
            'Singapore',
            '',
            '0512',
            'Singapore',
            '471 Serangoon Loop, Suite #402'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(21, 
            'Lyngbysild', 
            'Niels Petersen', 
            'Sales Manager', 
            'Denmark',
            '',
            '2800',
            'Lyngby',
            'Lyngbysild Fiskebakken 10'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(22, 
            'Zaanse Snoepfabriek', 
            'Dirk Luchte', 
            'Accounting Manager', 
            'Netherlands',
            '',
            '9999 ZZ',
            'Zaandam',
            'Verkoop Rijnweg 22'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(23, 
            'Karkki Oy', 
            'Anne Heikkonen', 
            'Product Manager', 
            'Finland',
            '',
            '53120',
            'Lappeenranta',
            'Valtakatu 12'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(24, 
            'G_day, Mate', 
            'Wendy Mackenzie', 
            'Sales Representative', 
            'Australia',
            'NSW',
            '2042',
            'Sydney',
            '170 Prince Edward Parade Hunter_s Hill'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(25, 
            'Ma Maison', 
            'Jean-Guy Lauzon', 
            'Marketing Manager', 
            'Canada',
            'Québec',
            'H1J 1C3',
            'Montréal',
            '2960 Rue St. Laurent'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(26, 
            'Pasta Buttini s.r.l.', 
            'Giovanni Giudici', 
            'Order Administrator', 
            'Italy',
            '',
            '84100',
            'Salerno',
            'Via dei Gelsomini, 153'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(27, 
            'Escargots Nouveaux', 
            'Marie Delamare', 
            'Sales Manager', 
            'France',
            '',
            '71300',
            'Montceau',
            '22, rue H. Voiron'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(28, 
            'Gai pâturage', 
            'Eliane Noz', 
            'Sales Representative', 
            'France',
            '',
            '74000',
            'Annecy',
            'Bat. B 3, rue des Alpes'
             )
            ;
INSERT INTO suppliers (
            suppliers_id, 
            company_name, 
            contact_name, 
            contact_title, 
            ad_country,
            ad_state,
            ad_index,
            ad_city,
            ad_street
            )
            VALUES(29, 
            'Forêts d_érables', 
            'Chantal Goulet', 
            'Accounting Manager', 
            'Canada',
            'Québec',
            'J2S 7S8',
            'Ste-Hyacinthe',
            '148 rue Chasseur'
             )
            ;
-- Update data for Name: products
UPDATE products SET fk_suppliers = 1 WHERE product_name IN ('Chang', 'Aniseed Syrup');
UPDATE products SET fk_suppliers = 2 WHERE product_name IN ('Chef Anton''s Cajun Seasoning', 'Chef Anton''s Gumbo Mix', 'Louisiana Fiery Hot Pepper Sauce', 'Louisiana Hot Spiced Okra');
UPDATE products SET fk_suppliers = 3 WHERE product_name IN ('Grandma''s Boysenberry Spread', 'Uncle Bob''s Organic Dried Pears', 'Northwoods Cranberry Sauce');
UPDATE products SET fk_suppliers = 4 WHERE product_name IN ('Mishi Kobe Niku', 'Ikura', 'Longlife Tofu');
UPDATE products SET fk_suppliers = 5 WHERE product_name IN ('Queso Cabrales', 'Queso Manchego La Pastora');
UPDATE products SET fk_suppliers = 6 WHERE product_name IN ('Konbu', 'Tofu', 'Genen Shouyu');
UPDATE products SET fk_suppliers = 7 WHERE product_name IN ('Pavlova', 'Alice Mutton', 'Carnarvon Tigers', 'Vegie-spread', 'Outback Lager');
UPDATE products SET fk_suppliers = 8 WHERE product_name IN ('Chai', 'Teatime Chocolate Biscuits', 'Sir Rodney''s Marmalade', 'Sir Rodney''s Scones', 'Scottish Longbreads');
UPDATE products SET fk_suppliers = 9 WHERE product_name IN ('Gustaf''s Knäckebröd', 'Tunnbröd');
UPDATE products SET fk_suppliers = 10 WHERE product_name IN ('Guaraná Fantástica');
UPDATE products SET fk_suppliers = 11 WHERE product_name IN ('NuNuCa Nuß-Nougat-Creme', 'Gumbär Gummibärchen', 'Schoggi Schokolade');
UPDATE products SET fk_suppliers = 12 WHERE product_name IN ('Rössle Sauerkraut', 'Thüringer Rostbratwurst', 'Wimmers gute Semmelknödel', 'Rhönbräu Klosterbier', 'Original Frankfurter grüne Soße');
UPDATE products SET fk_suppliers = 13 WHERE product_name IN ('Nord-Ost Matjeshering');
UPDATE products SET fk_suppliers = 14 WHERE product_name IN ('Gorgonzola Telino', 'Mascarpone Fabioli', 'Mozzarella di Giovanni');
UPDATE products SET fk_suppliers = 15 WHERE product_name IN ('Geitost', 'Gudbrandsdalsost', 'Flotemysost');
UPDATE products SET fk_suppliers = 16 WHERE product_name IN ('Sasquatch Ale', 'Steeleye Stout', 'Laughing Lumberjack Lager');
UPDATE products SET fk_suppliers = 17 WHERE product_name IN ('Inlagd Sill', 'Gravad lax', 'Röd Kaviar');
UPDATE products SET fk_suppliers = 18 WHERE product_name IN ('Côte de Blaye', 'Chartreuse verte');
UPDATE products SET fk_suppliers = 19 WHERE product_name IN ('Boston Crab Meat', 'Jack''s New England Clam Chowder');
UPDATE products SET fk_suppliers = 20 WHERE product_name IN ('Singaporean Hokkien Fried Mee', 'Ipoh Coffee', 'Gula Malacca');
UPDATE products SET fk_suppliers = 21 WHERE product_name IN ('Rogede sild', 'Spegesild');
UPDATE products SET fk_suppliers = 22 WHERE product_name IN ('Zaanse koeken', 'Chocolade');
UPDATE products SET fk_suppliers = 23 WHERE product_name IN ('Maxilaku', 'Valkoinen suklaa', 'Lakkalikööri');
UPDATE products SET fk_suppliers = 24 WHERE product_name IN ('Manjimup Dried Apples', 'Filo Mix', 'Perth Pasties');
UPDATE products SET fk_suppliers = 25 WHERE product_name IN ('Tourtière', 'Pâté chinois');
UPDATE products SET fk_suppliers = 26 WHERE product_name IN ('Gnocchi di nonna Alice', 'Ravioli Angelo');
UPDATE products SET fk_suppliers = 27 WHERE product_name IN ('Escargots de Bourgogne');
UPDATE products SET fk_suppliers = 28 WHERE product_name IN ('Raclette Courdavault', 'Camembert Pierrot');
UPDATE products SET fk_suppliers = 29 WHERE product_name IN ('Sirop d''érable', 'Tarte au sucre');

-- Name: products; Type: Column; Schema: -; Owner: -
ALTER TABLE products ADD COLUMN fk_suppliers INTEGER;

-- Name: suppliers; Type: Column; Schema: -; Owner: -
ALTER TABLE ONLY suppliers ADD CONSTRAINT pk_suppliers PRIMARY KEY (suppliers_id);

-- Name: fk_suppliers; Type: Constraint; Schema: -; Owner: -
ALTER TABLE ONLY products ADD CONSTRAINT fk_suppliers FOREIGN KEY (fk_suppliers) REFERENCES suppliers;
