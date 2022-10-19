from suppliers_table_form import *


def main():
    # выгружаю данные в список словарей
    suppliers_dict_list = make_suppliers_dicts()

    with open('suppliers_table.sql', 'w', encoding='utf-8') as file:

        # удаляю таблицу suppliers, если такая уже есть
        file.write(f"""-- drop table\nDROP TABLE IF EXISTS suppliers;\n\n""")

        # создаю таблицу suppliers
        file.write(f"""--Name: suppliers; Type: TABLE; Schema: public; Owner: -; Tablespace:\nCREATE TABLE IF NOT EXISTS suppliers (
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
        );\n\n""")

        # заполняю данными таблицу suppliers
        file.write("""-- Data for Name: suppliers; Type: TABLE DATA; Schema: public; Owner: -\n""")

        i = 1
        for dt in suppliers_dict_list:
            file.write(f"""INSERT INTO suppliers (
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
            VALUES({i}, 
            '{dt['company_name'].replace("'", "_")}', 
            '{dt['contact'].split(', ')[0]}', 
            '{dt['contact'].split(', ')[1]}', 
            '{dt['address'].split('; ')[0]}',
            '{dt['address'].split('; ')[1]}',
            '{dt['address'].split('; ')[2]}',
            '{dt['address'].split('; ')[3]}',
            '{dt['address'].split('; ')[4].replace("'", "_")}'
             )
            ;\n""")
            i += 1

        # добавляю дополнительную колонку fk_suppliers в таблицу products
        file.write("""\n-- Name: products; Type: Column; Schema: -; Owner: -\n""")
        file.write("""ALTER TABLE products ADD COLUMN fk_suppliers INTEGER;\n""")

        # добавляю поле suppliers_id в таблицу products и заполняю его
        i = 1
        file.write("""-- Update data for Name: products\n""")

        for dt in suppliers_dict_list:
            dt['id'] = i
            product = [p.replace("'", "''") for p in dt['products']]
            file.write(f"""UPDATE products SET fk_suppliers = {dt['id']} WHERE product_name IN ('{"', '".join(product)}');\n""")
            i += 1

        # добавляю первичные ключи
        file.write("""\n-- Name: suppliers; Type: Column; Schema: -; Owner: -\n""")
        file.write("""ALTER TABLE ONLY suppliers ADD CONSTRAINT pk_suppliers PRIMARY KEY (suppliers_id);\n""")

        # добавляю внешний ключ
        file.write("""\n-- Name: fk_suppliers; Type: Constraint; Schema: -; Owner: -\n""")

        file.write("""ALTER TABLE ONLY products ADD CONSTRAINT fk_suppliers FOREIGN KEY (fk_suppliers) REFERENCES suppliers;\n""")


if __name__ == "__main__":
    main()
