from flask import Flask
from flask import abort
import json as json
import database_connector
from database_connector import exec_sql_query

app = Flask(__name__)

@app.route('/sqli_good_dynamic_sql/<string:student_id>', methods=['GET'])
def get_task(student_id):
    result = exec_sql_query('get_student_stress_level_by_id_good_dynamic_sql ?', student_id)
    if result.empty:
        abort(404)

    return result.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
