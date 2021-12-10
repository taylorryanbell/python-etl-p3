# SQL queries can be created here

create_schema = ('''
    DROP SCHEMA IF EXISTS petl3 CASCADE;
    CREATE SCHEMA IF NOT EXISTS petl3;
''')

return_table = ('''
    SELECT * FROM petl1.top_genres
    LIMIT 10;
''')