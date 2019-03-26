import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_cli, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_cli) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_cli, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_cli) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_cli, **k):

    @staticmethod
    def POST_DELETE(id_cli, **k):
    '''

    def GET(self, id_cli, **k):
        message = None # Error message
        id_cli = config.check_secure_val(str(id_cli)) # HMAC id_cli validate
        result = config.model.get_clientes(int(id_cli)) # search  id_cli
        result.id_cli = config.make_secure_val(str(result.id_cli)) # apply HMAC for id_cli
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_cli, **k):
        form = config.web.input() # get form data
        form['id_cli'] = config.check_secure_val(str(form['id_cli'])) # HMAC id_cli validate
        result = config.model.delete_clientes(form['id_cli']) # get clientes data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_cli = config.check_secure_val(str(id_cli))  # HMAC user validate
            id_cli = config.check_secure_val(str(id_cli))  # HMAC user validate
            result = config.model.get_clientes(int(id_cli)) # get id_cli data
            result.id_cli = config.make_secure_val(str(result.id_cli)) # apply HMAC to id_cli
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/clientes') # render clientes delete.html 
