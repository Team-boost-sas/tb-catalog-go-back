def autenticar():
    token = request.json['token']
    payload = verificar_token(token)
    if payload is not None:

        usuario_id = payload['sub']
        email = payload['email']
        companies = payload['companies']

        for company in companies:
            name = company.get('name')
            if not name or len(name) < 3: # no se cual validacion de nombre utilizar 
                raise ValueError('El campo "name" es inválido')
            role = company.get('role')
            if not role or role not in ['admin', 'user']:
                raise ValueError('El campo "role" es inválido')
            status = company.get('status')
            if not status or status not in ['active', 'inactive']:
                raise ValueError('El campo "status" es inválido')
            
        return 'Autenticación exitosa'
    else:
        return 'Token invalido'

def verificar_token(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # El token ha expirado
    except jwt.InvalidTokenError:
        return None  # El token no es válido