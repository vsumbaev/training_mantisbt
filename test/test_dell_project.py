import random
from model.Project import Configurations_Project

'''удаление проекта в mantis'''
def test_dell_project(app, db):
    project = Configurations_Project(name="project",
                      description="project-description")
    app.session.login("administrator", "root")
    app.project.open_project_page()
    if len(db.get_project_list()) == 0:
        app.project.create_project(project)
    app.project.open_project_page()
    old_project = db.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_name(project.name)
    new_project = db.get_project_list()
    assert len(old_project) - 1 == len(new_project)