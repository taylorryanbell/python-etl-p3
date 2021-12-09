# Setup

  1. Create a fork of the project
  2. Move the config file provided into your project foulder.
  3. At the top menu select ```Run -> Edit Configurations...```
      1. in the new window under ```Environment``` click the icon on the right side of the input box
      2. In the ```Environment Variables``` window click the plus button and add a new record with the name of ```GOOGLE_APPLICATION_CREDENTIALS``` and set the value to the file path of the config file you added to your project
  4. Install the ```google-cloud-bigquery``` package via ```pip``` or the pycharm UI.

# Example Query
```
from google.cloud import bigquery;

if __name__ == '__main__':
    client = bigquery.Client()
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
```
