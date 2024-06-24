from flask import Flask, jsonify

app = Flask(__name__)

courses = [
    {
        "Description": "Python in AI",
        "course_id": 0,
        "name": "Python AI Certificate",
        "site": "btu.edu.ge"
    },
    {
        "Description": "CCNA",
        "course_id": 1,
        "name": "CCNA Certificate",
        "site": "netacad.com"
    },
    {
        "Description": "Linux",
        "course_id": 2,
        "name": "Linux Certificate",
        "site": "netdevgroup.com"
    }
]

@app.route('/', methods=['GET'])
def get_courses():
    return jsonify(courses)

@app.route('/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    global courses  # coursebze ro wvdoma mogvces 
    index_to_delete = None
    for index, course  in enumerate(courses):
        if course['course_id'] == course_id:
            index_to_delete = index
            break
    if index_to_delete:
        deleted_course = courses.pop(index_to_delete)
        return jsonify(f'deleted data with index {index_to_delete}')
    else:
        return jsonify('ravi rames izavs')

if __name__ == '__main__':
    app.run(debug=True)

# curl -X DELETE http://127.0.0.1:5000/<course_id>



   