from flask import render_template, Blueprint,request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Job, User, db

views = Blueprint("views", __name__, template_folder="template")

@views.route("/", methods=['GET','POST'])
@login_required     #You can't get to the home page unless you're logged in
def home():
    if request.method == "POST":
        company = request.form.get("company")
        position = request.form.get("position")
        status = request.form.get("status")
        job_type = request.form.get("job_type")
        location = request.form.get("location")
        link = request.form.get("link")
        notes = request.form.get("notes")

        new_job = Job(
        company=company,
        position=position,
        status=status,
        job_type=job_type,
        location=location,
        link=link,
        notes=notes,
        user_id=current_user.id
    )
        db.session.add(new_job)
        db.session.commit()
        flash("Job added successfully!", "success")
        #return redirect(url_for("views.dashboard"))

    return render_template("home.html", user=current_user)



