from flask import render_template, url_for,Blueprint, flash, redirect
from flask_login import login_required, current_user
from .models import Job, User,db


dashboard = Blueprint("dashboard", __name__, template_folder="template")

@dashboard.route('/dashboard', methods=["GET"])
@login_required
def view_dashboard():
    user_id = current_user.id
    applications = Job.query.filter_by(user_id=user_id).all()
    return render_template('dashboard.html', applications=applications, user=current_user)



@dashboard.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_application(id):
    application = Job.query.get_or_404(id)

    if application.user_id != current_user.id:
        flash("Not authorized to delete this application.", category='error')
        return redirect(url_for('views.dashboard'))

    db.session.delete(application)
    db.session.commit()
    flash("Application removed.", category='success')
    return redirect(url_for('dashboard.view_dashboard'))