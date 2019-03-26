import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_cli, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_cli) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_cli, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_cli) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_cli, **k):

    @staticmethod
    def POST_EDIT(id_cli, **k):
        
    '''

    def GET(self, id_cli, **k):
        message = None # Error message
        id_cli = config.check_secure_val(str(id_cli)) # HMAC id_cli validate
        result = config.model.get_clientes(int(id_cli)) # search for the id_cli
        result.id_cli = config.make_secure_val(str(result.id_cli)) # apply HMAC for id_cli
        return config.render.edit(result, message) # render clientes edit.html

    def POST(self, id_cli, **k):
        form = config.web.input()  # get form data
        form['id_cli'] = config.check_secure_val(str(form['id_cli'])) # HMAC id_cli validate
        # edit user with new data
        result = config.model.edit_clientes(
            form['id_cli'],form['nombre'],form['ap_p'],form['ap_m'],form['telefono'],form['email'],
        )
        if result == None: # Error on udpate data
            id_cli = config.check_secure_val(str(id_cli)) # validate HMAC id_cli
            result = config.model.get_clientes(int(id_cli)) # search for id_cli data
            result.id_cli = config.make_secure_val(str(result.id_cli)) # apply HMAC to id_cli
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/clientes') # render clientes index.html
