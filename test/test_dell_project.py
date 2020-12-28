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
    username = "administrator"
    password = "root"
    app.project.open_project_page()
    old_project = app.soap.get_list_projects(username, password)
    project = random.choice(old_project)
    app.project.delete_project_by_name(project.name)
    new_project = app.soap.get_list_projects(username, password)
    old_project.remove(project)
    assert sorted(old_project, key=Configurations_Project.id_or_max) == sorted(new_project,key=Configurations_Project.id_or_max)

#    assert len(app.soap.get_list_of_projects(username, password)) == len(new_project)
#    assert len(old_project) - 1 == len(new_project)
