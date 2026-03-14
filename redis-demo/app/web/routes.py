from flask import Blueprint, request, jsonify
from app.use_cases.task_service import TaskService
from app.infrastructure.redis_repository import RedisRepository

task_bp = Blueprint("task_bp", __name__)

_repository = RedisRepository()
_service = TaskService(_repository)

@task_bp.route("/task", methods=["POST"])
def create_task():
    payload = request.get_json(force=True) or {}

    task_id = payload.get("id")
    title = payload.get("title")

    try:
        task = _service.create_task(task_id, title)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify(task.to_dict()), 201

@task_bp.route("/task/<task_id>", methods=["GET"])
def get_task(task_id):
    task = _service.get_task(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task.to_dict()), 200
