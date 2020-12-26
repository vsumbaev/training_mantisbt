import pymysql
from model.Project import Configurations_Project


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name , user=user , password=password, autocommit=True )

    def get_project_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, status, view_state, description from mantis_project_table")
            for row in cursor:
                (id,name,status,view_state,description) = row
                list.append(Configurations_Project(id=str(id), name=name, status=status, view=view_state, description=description))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()