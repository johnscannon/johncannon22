from flask import Flask, render_template, request, redirect, url_for # type: ignore

app = Flask(__name__)

# In-memory storage for simplicity (replace with a database in production)
job_postings = [
    {"title": "Software Engineer Intern", "company": "TechCorp", "description": "Develop and test software.", "status": "Pending Approval"},
    {"title": "Web Developer", "company": "Webify", "description": "Design and maintain websites.", "status": "Approved"},
]
student_applications = []

@app.route("/")
def home():
    return render_template("index.html", jobs=job_postings)

@app.route("/submit_job", methods=["POST"])
def submit_job():
    if request.method == "POST":
        # Retrieve form data
        job_title = request.form["job_title"]
        company = request.form["company_name"]
        description = request.form["job_description"]
        contact = request.form["contact"]
        
        # Add the job to the in-memory job postings
        job_postings.append({"title": job_title, "company": company, "description": description, "status": "Pending Approval"})
        return redirect(url_for("home"))

@app.route("/student_apply", methods=["POST"])
def student_apply():
    if request.method == "POST":
        # Retrieve form data
        student_name = request.form["student_name"]
        student_email = request.form["student_email"]
        job_title = request.form["job"]
        cover_letter = request.form["cover_letter"]
        
        # Store application in memory
        student_applications.append({
            "name": student_name,
            "email": student_email,
            "job": job_title,
            "cover_letter": cover_letter,
        })
        return redirect(url_for("home"))

@app.route("/applications")
def view_applications():
    return render_template("applications.html", applications=student_applications)

if __name__ == "__main__":
    app.run(debug=True)
