from src.models import Task, User


def test_task_completed_flag():
    task = Task(title="Sample Task", completed=False)
    task.completed = True
    assert task.completed is True


def test_task_creation():
    task = Task(title="New Task", completed=False)
    assert task.title == "New Task"
    assert task.completed is False
    assert task.user_id is None


def test_task_user_assignment():
    user = User(name="Ola")
    task = Task(title="Assigned Task", user_id=1)
    task.user_id = user.id
    assert task.user_id == user.id
