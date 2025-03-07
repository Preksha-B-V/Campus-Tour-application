from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Sample Faculty Data
faculty_data ={ "Computer Science": [
        {"name": "Prabhakar", "M.Tech": "PhD ", "7979878789": "prabhakar@cmr.edu.in"},
        {"name": "Prof. Priyanka", "B.Tech in CSE": "M.Tech in CS", "9875646767": "priyanka@cmr.edu.in"}
    ],
    "Electrical Engineering": [
        {"name": "Dr. Brijesh Mishra", "MS": "PhD", "876987694": "brijesh.mishra@cmr.edu.in"}
    ],
    "Mechanical Engineering": [
        {"name": "Dr. Anup", "MS in Mechanical engineering": "8766747394": "anup@cmr.edu.in"}
    ],
    "Civil Engineering": [
        {"name": "Prof. Manohar k", "M.Tech in Civil": "876987694": "manohar@cmr.edu.in"}
    ]
}

# Sample Events Data
events = [
    {"title": "Orientation Day", "start": "2025-03-15", "For First year students": "Block A, Room 401"},
    {"title": "Tech Fest", "start": "2025-03-07", "description": "Block C, SSCS, Room 203"},
    {"title": "Annual Sports Meet", "start": "2025-05-10", "Sports for Health": "Sports Ground"}
]

# Sample User Reviews
reviews = []


@app.route("/")
def home():
    return render_template("index.html")


# API to handle login authentication
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("preksha.bv@cmr.edu.in")
    password = data.get("12334")
    role = data.get("Student")

    if email and password and role:
        return jsonify({"status": "success", "message": f"Welcome, {role}!"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid credentials!"}), 400


# API to get faculty list for a department
@app.route("/get_faculty", methods=["GET"])
def get_faculty():
    department = request.args.get("department")
    return jsonify(faculty_data.get(department, []))


# API to add a faculty member
@app.route("/add_faculty", methods=["POST"])
def add_faculty():
    data = request.json
    department = data.get("department")
    name = data.get("name")
    education = data.get("education")
    contact = data.get("contact")

    if department and name and education and contact:
        faculty_data[department].append({"name": name, "education": education, "contact": contact})
        return jsonify({"message": "Faculty added successfully!"}), 200
    else:
        return jsonify({"message": "Invalid faculty data!"}), 400


# API to remove a faculty member
@app.route("/remove_faculty", methods=["POST"])
def remove_faculty():
    data = request.json
    department = data.get("department")
    index = data.get("index")

    if department in faculty_data and 0 <= index < len(faculty_data[department]):
        faculty_data[department].pop(index)
        return jsonify({"message": "Faculty removed successfully!"}), 200
    else:
        return jsonify({"message": "Invalid faculty data!"}), 400


# API to fetch upcoming events
@app.route("/get_events", methods=["GET"])
def get_events():
    return jsonify(events)


# API to handle user reviews
@app.route("/submit_review", methods=["POST"])
def submit_review():
    data = request.json
    review_text = data.get("review")

    if review_text:
        reviews.append(review_text)
        return jsonify({"message": "Review submitted successfully!"}), 200
    else:
        return jsonify({"message": "Invalid review data!"}), 400


# API to get submitted reviews
@app.route("/get_reviews", methods=["GET"])
def get_reviews():
    return jsonify(reviews)


if __name__ == "__main__":
    app.run(debug=True)
