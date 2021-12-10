# sql.py
# Create SQL queries to be run through pgAdmin database

create_schema_and_table = ('''
    DROP SCHEMA IF EXISTS petl3 CASCADE;
    CREATE SCHEMA IF NOT EXISTS petl3;
    
    DROP TABLE IF EXISTS petl3.viable_counties;
    CREATE TABLE IF NOT EXISTS petl3.viable_counties (
        geo_id INT PRIMARY KEY NOT NULL,
        state TEXT,
        county TEXT,
        sales_vector INT
    );
''')

return_table = ('''
    SELECT * FROM petl1.top_genres
    LIMIT 10;
''')

create_table_viable_counties = ('''
    DROP TABLE IF EXISTS petl3.viable_counties;
    
    CREATE TABLE IF NOT EXISTS petl3.viable_counties (
        geo_id INT PRIMARY KEY NOT NULL,
        state TEXT,
        county TEXT,
        sales_vector INT
    );
''')

insert_results = ('''
    INSERT INTO petl3.viable_counties
    VALUES (%s, %s, %s, %s);
''')
