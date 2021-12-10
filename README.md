# Setup

  1. Create a fork of the project
  2. Move the config file provided into your project folder.
  3. At the top menu select ```Run -> Edit Configurations...```
      1. in the new window under ```Environment``` click the icon on the right side of the input box
      2. In the ```Environment Variables``` window click the plus button and add a new record with the name of ```GOOGLE_APPLICATION_CREDENTIALS``` and set the value to the file path of the config file you added to your project
  4. Install the ```google-cloud-bigquery``` package via ```pip``` or the pycharm UI.
  5. Create a new schema in your pgsql database named ```petl3```

# Example BigQuery Query
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
# Project  
  The company want to open a new store, but needs us to use ```American Community Survey (ACS)``` data along with google's ```COVID-19 Community Mobility Reports```
  to find viable US counties to build the new location.
  
  Here is the criteria for viable counties.
  
      1. Median rent must be lower than $2000.
      2. The population must have a median age lower than 30 years.
      3. The mobility report's average retail and recreation baseline change for
          all the locations in the county must have a value greater than -15%.
    
  Store the viable counties in a table called ```viable_countys``` with the following structure.
  | Col Name      | Data Type |
  | ----------- | ----------- |
  | geo_id      | int       |
  | state   | text        |
  | county   | text        |
  | sales_vector   | int        |

# Hints
  - Use the following BigQuery tables to gather the data you need.
  
    ```bigquery-public-data.census_bureau_acs.county_2017_1yr```
    
    ```bigquery-public-data.covid19_google_mobility.mobility_report```
    
  - Lookup SQL ```GROUP BY``` and ```AVG``` and learn how to use them.
  
  
