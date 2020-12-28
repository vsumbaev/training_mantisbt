from model.Project import Configurations_Project


'''добавление проекта в mantis'''
def test_add_project(app, db):
    project = Configurations_Project(name="1none-name1", description="1none-name1")
    app.session.login("administrator", "root")
    username = "administrator"
    password = "root"
    old_project = app.soap.get_list_projects(username, password)
    app.project.create_project(project)
    old_project.append(project)
    new_project = app.soap.get_list_projects(username, password)
    assert sorted(old_project, key=Configurations_Project.id_or_max) == sorted(new_project, key=Configurations_Project.id_or_max)

