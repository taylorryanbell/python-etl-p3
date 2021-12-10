from google.cloud import bigquery
import sql
import pgsql

if __name__ == '__main__':

    client = bigquery.Client()

    # bigquery
    query = client.query('''
        SELECT geo_id, state, county, change AS sales_vector FROM (
            SELECT
                geo_id, sub_region_1 AS state, sub_region_2 AS county, AVG(retail_and_recreation_percent_change_from_baseline) AS change
            FROM
                bigquery-public-data.census_bureau_acs.county_2017_1yr
            JOIN
                bigquery-public-data.covid19_google_mobility.mobility_report ON geo_id || '.0' = census_fips_code
            WHERE
                median_rent < 2000
                AND median_age < 30
            GROUP BY
                geo_id, state, county
        )
        WHERE change > -15
    ''')

    # Create Schema and Table
    pgsql.query(sql.create_schema_and_table)

    # Run query and insert results into table
    for row in query.result():
        row_list = []
        for item in row:
            row_list.append(item)
        pgsql.query(sql.insert_results, row_list)
