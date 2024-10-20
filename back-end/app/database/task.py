from app.database import get_db #We import the function to get database from app/database

def output_formatter(results): #takes a list of database query results as input
    out = [] #empty list to store the formatted results
    for result in results: #iterates over each result in the input list
        res = {  #creates a dictionary with keys corresponding to the column names in the database table and values extracted from the current result tuple
            "id": result[0],
            "name": result[1],
            "summary": result[2],
            "description": result[3],
            "is_done": result[4]
        }
        out.append(res) #appends the formatted dictionary res to the out list.
    return out #returns the list of formatted dictionaries

def scan():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE is_done=0", ()) #executes sql query to select all rows from the task table where is_done column is 0 indicating incomplete tasks
    results = cursor.fetchall() #fetches all the results from query and stores them in the "results" variable.
    return output_formatter(results) #return formatted results after the scan

def select_by_id(task_id):
    conn = get_db() #connects to db
    cursor = conn.execute("SELECT * FROM task WHERE id=?", (task_id, )) #executes query search looking for a specific ID  
    result = cursor.fetchall() #stores task with ID #N in results
    if result: #if there are results do:
        return output_formatter(result)[0] #format the result and return it
    return {} #else, return an empty list (no "else" needed here)



#INSERT UPADTE AND DELETE ARE NOT YET USED


def insert(task_data): #defines a function to insert a new task into the database
    task_tuple = ( #creates task_tuple containing values for name, summary, description columns
        task_data.get("name"), 
        task_data.get("summary"),
        task_data.get("description")
    )
    # define sql statement for inserting a new row into the task table:
    statement = """  
    INSERT INTO task (
        name, 
        summary,
        description
    ) VALUES (?, ?, ?)
    """ #(?) indicates the value will be placed later, these are placeholders.
    conn = get_db() #connect to database
    conn.execute(statement, task_tuple) #execute runs the INSERT statement with task_tuple as the argument, the ? are replaced with the task's name, summary, description 
    conn.commit() #after INSERT you must commit() to save the changes.

def update_by_id(task_data, task_id): #function is provided with the task's data and its ID
    task_tuple = (
        task_data.get("name"),
        task_data.get("summary"),
        task_data.get("description"),
        task_data.get("is_done"),
        task_id
    )
    # SETs placeholders for the task with the selected ID
    statement = """
    UPDATE task SET
        name=?,
        summary=?,
        description=?,
        is_done=?
    WHERE id=?
    """
    conn = get_db() #connects to database
    conn.execute(statement, task_tuple) #executes the statement with the new task_data, updating it
    conn.commit() #updates database

def delete_by_id(task_id): #function is provided with the task id
    conn = get_db() #connects to db
    conn.execute("DELETE FROM task WHERE id=?", (task_id, )) #executes delete statement in one line
    conn.commit() #updates database
