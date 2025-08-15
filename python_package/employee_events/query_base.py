# Import any dependencies needed to execute sql queries
# YOUR CODE HERE
import pandas as pd
from sqlite3 import connect

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
# YOUR CODE HERE
class QueryBase:

    # Create a class attribute called `name`
    # set the attribute to an empty string
    # YOUR CODE HERE
    name=""

    # Define a `names` method that receives
    # no passed arguments
    # YOUR CODE HERE
    def name(self):    
        # Return an empty list
        # YOUR CODE HERE
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    # YOUR CODE HERE
    def event_counts(self, id):

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        # YOUR CODE HERE
        qry = f"""
            SELECT event_date, 
                   SUM(positive_events) AS total_positive_events, 
                   SUM(negative_events) AS total_negative_events
            FROM {self.name} 
            WHERE id = {id}
            GROUP BY event_date
            ORDER BY event_date
        """

        # Execute the query and return the results as a DataFrame
        with connect('employee_events.db') as conn:
            return pd.read_sql_query(qry, conn)
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        # YOUR CODE HERE

        qry = f"""
            SELECT note_date, note
            FROM notes 
            WHERE employee_id = {id}
        """
        
        # Execute the query and return the results as a DataFrame
        with connect('employee_events.db') as conn:
            return pd.read_sql_query(qry, conn)