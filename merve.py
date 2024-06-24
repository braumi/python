from flask import Flask, request, jsonify

app = Flask(__name__) #vqmnit aplikacias 
#listshi calke dictebad unda shevinaxot monacemebi
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


@app.route('/add', methods=['POST'])
def add_data():
    new_course = {
        "Description": "SQLserver",
        "course_id": 3,  # Assuming you want to auto-generate course_id
        "name": "SQLserver Certificate",
        "site": "mygreatlearning.com"
    }
    courses.append(new_course)
    return jsonify({"message": "Specific course added successfully", "course": new_course})

if __name__ == '__main__':
    app.run(debug=True)

# curl -X POST http://127.0.0.1:5000/add