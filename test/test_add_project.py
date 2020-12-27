from model.Project import Configurations_Project
'''добавление проекта в mantis'''
def test_add_project(app, db):
    project = Configurations_Project(name="project",
                      description="project-description")
    app.session.login("administrator", "root")
#    old_project = db.get_project_list()
    app.project.create_project(project)
    new_project = db.get_project_list()
    username = "administrator"
    password = "root"
    assert len(app.soap.get_list_of_projects(username, password)) == len(new_project)
#    assert len(old_project) == len(new_project) - 1