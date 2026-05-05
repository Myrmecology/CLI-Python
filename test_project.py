from project import add_task, complete_task, delete_task


# ---------------------------
# TESTS FOR add_task
# ---------------------------
def test_add_task(monkeypatch):
    monkeypatch.setattr("project.save_tasks", lambda tasks: None)
    tasks = []
    result = add_task(tasks, "Buy groceries")
    assert result == True
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Buy groceries"
    assert tasks[0]["done"] == False


def test_add_task_empty(monkeypatch):
    monkeypatch.setattr("project.save_tasks", lambda tasks: None)
    tasks = []
    result = add_task(tasks, "   ")
    assert result == False
    assert len(tasks) == 0


# ---------------------------
# TESTS FOR complete_task
# ---------------------------
def test_complete_task(monkeypatch):
    monkeypatch.setattr("project.save_tasks", lambda tasks: None)
    tasks = [{"title": "Buy groceries", "done": False}]
    result = complete_task(tasks, 0)
    assert result == True
    assert tasks[0]["done"] == True


def test_complete_task_invalid(monkeypatch):
    monkeypatch.setattr("project.save_tasks", lambda tasks: None)
    tasks = []
    result = complete_task(tasks, 5)
    assert result == False


# ---------------------------
# TESTS FOR delete_task
# ---------------------------
def test_delete_task(monkeypatch):
    monkeypatch.setattr("project.save_tasks", lambda tasks: None)
    tasks = [{"title": "Buy groceries", "done": False}]
    result = delete_task(tasks, 0)
    assert result == "Buy groceries"
    assert len(tasks) == 0


def test_delete_task_invalid(monkeypatch):
    monkeypatch.setattr("project.save_tasks", lambda tasks: None)
    tasks = []
    result = delete_task(tasks, 5)
    assert result == None