import web
import config
import json


class Api_clientes:
    def get(self, id_cli):
        try:
            # http://0.0.0.0:8080/api_clientes?user_hash=12345&action=get
            if id_cli is None:
                result = config.model.get_all_clientes()
                clientes_json = []
                for row in result:
                    tmp = dict(row)
                    clientes_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(clientes_json)
            else:
                # http://0.0.0.0:8080/api_clientes?user_hash=12345&action=get&id_cli=1
                result = config.model.get_clientes(int(id_cli))
                clientes_json = []
                clientes_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(clientes_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            clientes_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)

# http://0.0.0.0:8080/api_clientes?user_hash=12345&action=put&id_cli=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    # /api_clientes?user_hash=12345&action=put&nombre=nuevo&ap_p=nuevo&ap_m=nuevo&telefono=nuevo&email=nuevo
    def put(self, nombre,ap_p,ap_m,telefono,email):
        try:
            config.model.insert_clientes(nombre,ap_p,ap_m,telefono,email)
            clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_clientes?user_hash=12345&action=delete&id_cli=1

    def delete(self, id_cli):
        try:
            config.model.delete_clientes(id_cli)
            clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_clientes?user_hash=12345&action=update&id_cli=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
#api_clientes?user_hash=12345&action=update&id_cli=5&nombre=Jesus&ap_p=Calderon&ap_m=Hernandez&telefono=7713009035&email=pucca420@gmail.com
    def update(self, id_cli, nombre,ap_p,ap_m,telefono,email):
        try:
            config.model.edit_clientes(id_cli,nombre,ap_p,ap_m,telefono,email)
            clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            clientes_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_cli=None,
            nombre=None,
            ap_p=None,
            ap_m=None,
            telefono=None,
            email=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_cli=user_data.id_cli

            nombre=user_data.nombre

            ap_p=user_data.ap_p

            ap_m=user_data.ap_m

            telefono=user_data.telefono

            email=user_data.email

            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_cli)
                elif action == 'put':
                    return self.put(nombre,ap_p,ap_m,telefono,email)
                elif action == 'delete':
                    return self.delete(id_cli)
                elif action == 'update':
                    return self.update(id_cli, nombre,ap_p,ap_m,telefono,email)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
