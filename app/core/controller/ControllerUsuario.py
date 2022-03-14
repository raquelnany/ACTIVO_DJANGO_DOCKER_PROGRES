from django.contrib.auth.models import User
from ..serializers import UsuarioSerializer
from ..models import Puesto, Usuario, Rol, EstatusUsuario, Idioma

class ControllerUsuario:
    def crearUsuario(request):
        datosUsuario = request.data
        print(request.data)
        print(request)
        try:
            #usuarioRegistra =  Usuario.objects.get(p_nombre="administrador")    
            rol = Rol.objects.get(id_rol=datosUsuario['rol'])
            puesto = Puesto.objects.get(id_puesto=datosUsuario['puesto'])
            idioma = Idioma.objects.get(id_idioma=datosUsuario['idioma'])
            estatus = EstatusUsuario.objects.get(id_estatus=datosUsuario['estatus'])
            username = datosUsuario['username']
            
            # if  usuarioRegistra.rol.scope.id_scope >= rol.scope.id_scope:
            #     return {"Error":"No cuentas con los privilegios para registrar al usuario"}

            # if usuarioRegistra.rol.tipo_rol.id_tipo_rol >= rol.tipo_rol.id_tipo_rol:
            #     return {"Error":"No cuentas con los privilegios para registrar al usuario"}

            usuario_duplicado = Usuario.objects.filter(username=username)
            if usuario_duplicado.exists():
                 return {"Error":"El username ya existe en la base de datos"}
            
            
            UsuarioNuevo = Usuario.objects.create(
                username =username,
                p_nombre = datosUsuario['p_nombre'],
                p_apellido = datosUsuario['p_apellido'],
                s_apellido= datosUsuario['s_apellido'],
                email= datosUsuario['email'],
                telefono = datosUsuario['telefono'], 
                password = datosUsuario['password'],
                es_activo = datosUsuario['es_activo'],
                rol = rol,
                puesto = puesto,
                idioma = idioma,
                estatus = estatus,
            )

            userNuevo = User.objects.create(
                username = username,
                email = datosUsuario['email'],
                password =  datosUsuario['password'],
            )
                
        except Exception:
            return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_usuario': UsuarioNuevo.username}
       
    def listarUsuario(id_usuario=None):
        if id_usuario:
            try:
                queryset = Usuario.objects.get(id_usuario=id_usuario)
            except Usuario.DoesNotExist:
                return ({'result': 'No se encontró el usuario deseado'})
            serializer = UsuarioSerializer(queryset)
            return serializer.data
        else:
            queryset = Usuario.objects.all()
            serializer = UsuarioSerializer(queryset, many=True)
            return serializer.data

    def verPerfil(p_nombre=None):
        if p_nombre:
            try:
                queryset = Usuario.objects.get(p_nombre=p_nombre)
            except Usuario.DoesNotExist:
                return ({'result': 'No se encontró el usuario deseado'})
            serializer = UsuarioSerializer(queryset)
            return serializer.data
        else:
            return ({'result': 'Ingrese el nombre de usuario'})


    def modificarUsuario(request,id_usuario=None):
        if id_usuario:
            datosUsuario = request.data
            try:
                usuarioModificar = Usuario.objects.get(id_usuario=id_usuario)
            except Usuario.DoesNotExist:
                return ({'result': 'No se encontró el usuario deseado'})
            try:
                #usuarioRegistra =  Usuario.objects.get(p_nombre="administrador")    
                rol = Rol.objects.get(id_rol=datosUsuario['rol'])
                puesto = Puesto.objects.get(id_puesto=datosUsuario['puesto'])
                idioma = Idioma.objects.get(id_idioma=datosUsuario['idioma'])
                estatus = EstatusUsuario.objects.get(id_estatus=datosUsuario['estatus'])
                username = datosUsuario['username']
                
                # if  usuarioRegistra.rol.scope.id_scope >= rol.scope.id_scope:
                #     return {"Error":"No cuentas con los privilegios para registrar al usuario"}

                # if usuarioRegistra.rol.tipo_rol.id_tipo_rol >= rol.tipo_rol.id_tipo_rol:
                #     return {"Error":"No cuentas con los privilegios para registrar al usuario"}

                usuario_duplicado = Usuario.objects.filter(username=username).exclude(id_usuario=id_usuario)

                if usuario_duplicado.exists():
                    return {"Error":"El username ya existe en la base de datos"}
                
                usuarioModificar.username = username
                usuarioModificar.p_nombre = datosUsuario['p_nombre']
                usuarioModificar.p_apellido = datosUsuario['p_apellido']
                usuarioModificar.s_apellido= datosUsuario['s_apellido']
                usuarioModificar.email= datosUsuario['email']
                usuarioModificar.telefono = datosUsuario['telefono'] 
                usuarioModificar.password = datosUsuario['password']
                usuarioModificar.es_activo = datosUsuario['es_activo']
                usuarioModificar.rol = rol
                usuarioModificar.puesto = puesto
                usuarioModificar.idioma = idioma
                usuarioModificar.estatus = estatus
                
                usuarioModificar.save()
              
            except Exception:
                return {"estatus":"Error"}

            return {"estatus":"Ok", 'Usuario_modificado': usuarioModificar.username}
        else: 
            return {"result":"Ingrese el Id del usuario que desea modificar"}