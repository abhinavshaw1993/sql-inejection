from flask import Flask
from flask import abort
import json as json
from database_connector import exec_sql_query

app = Flask(__name__)

def query_generator(student_id):
    sql = "select * from stress_details where student_id = " + student_id
    stress_level = exec_sql_query(sql)

    return stress_level.to_json(orient='records')

@app.route('/sqli_query_gen_at_app/<string:student_id>', methods=['GET'])
def get_task(student_id):
    result = query_generator(student_id)
    if not result:
        abort(404)
    return result

if __name__ == '__main__':
    app.run(debug=True)
