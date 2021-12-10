from google.cloud import bigquery
import sql
from pgsql import query

if __name__ == '__main__':

    client = bigquery.Client()

    '''
    query = client.query(
        """
        SELECT *
        FROM `bigquery-public-data.stackoverflow.posts_questions`
        ORDER BY view_count DESC
        LIMIT 10;
        """
    )
    for row in query.result():
        print(row)

    '''
    # testing
    print(query(sql.return_table))