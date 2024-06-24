# mtavari aplikacia
# routebi
# methods

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

#es daabrunebs getit ubralod yvela monacems
@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)


#id-it daabrunebs shesabamis monacemebs 
@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = next((course for course in courses if course['course_id'] == course_id), None)
    if course:
        return jsonify(course)
    return jsonify({"error": "Course not found"})

@app.route('/courses/<int:course_id>', methods=['PUT']) # cvlilebistvis gvinda put method
def update_course(course_id):
    # es ubralod 'erroristvis', tu gvinda ki, tu ara-ara :)))
    '''
    if request.content_type != 'application/json': 
        return jsonify({"error": "Unsupported Media Type"})
    '''

    updated_data = request.json
    course = next((course for course in courses if course['course_id'] == course_id), None)
    if course:
        course.update(updated_data)
        return jsonify(course)
    return jsonify({"error": "Course not exists"})

if __name__ == '__main__':
    app.run(debug=True)

# gavxsnit command prompts da amit shevcvlit, mere gadavamowmebt mainc get - it
# curl -X PUT -H "Content-Type: application/json" -d "{\"Description\": \"BTULinux\"}" http://127.0.0.1:5000/courses/2
