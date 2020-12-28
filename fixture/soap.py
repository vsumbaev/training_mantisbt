from suds.client import Client
from suds import WebFault
from model.Project import Configurations_Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False


#    def get_list_of_projects(self, username, password):
#        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
#        return  client.service.mc_projects_get_user_accessible(username, password)

    def get_list_projects(self, username, password):
        client = Client(self.app.baseUrl + "/api/soap/mantisconnect.php?wsdl")
        list = client.service.mc_projects_get_user_accessible(username, password)
        project_list = []
        for i in list:
            id = i[0]
            name = i[1]
            description = i[7]
            project_list.append(
                Configurations_Project(id=str(id), name=name, description=description))
        return project_list
