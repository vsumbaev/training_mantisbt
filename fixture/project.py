
class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_in_project(self, Project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(Project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(Project.description)

#    def save_project(self):
#        wd = self.app.wd
#        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def dell_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def delete_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text(name).click()
        self.dell_project()
        self.dell_project()

    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//input[@type='submit' and @value='Create New Project']").click()
        self.fill_in_project(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()