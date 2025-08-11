from flask_restful import Resource,Api
from flask import jsonify,Blueprint, request
from flask_login import current_user, login_required
from .models import db, Job

from supabase_client import supabase

job_bp = Blueprint("job", __name__)
api = Api(job_bp)


#@job.route("api/jobs", methods=["GET"])
class JobResource(Resource):
    def get(self):
        response = supabase.table("jobs").select("*").execute()
        return response.data, 200
    
    def post(self):
        data = request.get_json()
        required_fields = ["company", "position", "job_type", "location"]
        if not all(field in data for field in required_fields):
            return {"error": "Missing required fields"}, 400

        try:
            response = supabase.table("jobs").insert(data).execute()

            if not response.data:  # Supabase returns inserted rows in .data
                return {"error": "Failed to insert job"}, 500

            return {
                "message": "Job posted successfully",
                "job": response.data
            }, 201 
        
        except Exception as e:
            return {"error": str(e)}, 500
    

    def put(self, id):
        data = request.get_json()
        try:
            response = supabase.table("jobs").update(data).eq("id", id).execute()

            if not response.data:
                return {"error": "Job not found"}, 404

            return {"message": "Job updated successfully", "job": response.data}, 200
        except Exception as e:
            return {"error": str(e)}, 500

    def delete(self, id):
        try:
            response = supabase.table("jobs").delete().eq("id", id).execute()

            if not response.data:
                return {"error": "Job not found"}, 404

            return {"message": "Job deleted successfully", "deleted_job": response.data}, 200
        except Exception as e:
            return {"error": str(e)}, 500

