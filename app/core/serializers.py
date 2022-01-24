from tkinter.tix import CheckList
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.db.models import fields
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from .models import M4, OT, Act_Ot, Act_Ot_Codigo, Act_Ot_Tipo, Actividad_Mantenimiento, Almacen, Checklist_Aspecto, Checklist_Aspecto_Copiado, Checklist_Equipo, Checklist_Instruccion, Chk, Chk_Aspecto, Chk_Equipo, Chk_Instruccion, Codigo_Falla, Devolucion, Equipo, Equipo_Categoria_Icono, Equipo_Tarea, Equipo_Tarea_Parte, Evento, Frecuencia, Herramienta, Instalacion, Instalacion_Icono, Instruccion, Inventario_Ajuste, Inventario_Vale, Jornada, Cliente, Mecanismo_Falla, Modelo_Icono, Modo_Deteccion, Orden_Archivos, Orden_Subestatus, Orden_Trabajo_Checklist, Orden_Trabajo_Completa, Orden_Trabajo_Estatus, Orden_Trabajo_Parte, Orden_Trabajo_Prioridad, Orden_Trabajo_Ruta, Orden_Trabajo_Ruta_Set_Point, Orden_Trabajo_Tipo, Orden_trabajo_Revisada, Parte_Detalle, Parte_Detalle_Surtido, Parte_Estatus, Proveedor, CentroCosto, Departamento, EstatusUsuario, Historial_Turno, Idioma, Puesto, Rca, Rca_Accion_Preventiva, Rca_Preventive_Status, Rca_Status, Rca_Tipo_Accion, Ruta, Ruta_Condicion, Ruta_Condicion_Unidad, Ruta_Equipo, Ruta_Equipo_Componente, Ruta_Estatus, Ruta_Set_Point, Ruta_Set_Point_Operador, Scope, Stock, Stock_Ajuste, Stock_Detalle, Stock_Entrada, Tarea_Instruccion, Tarea_Orden_Trabajo, Tiempo_Unidad, Tipo_Cambio, Tipo_Programa, Tipo_Rol, Rol, Usuario_Revisar
from .models import Departamento_Turno, Turno, Puesto, Usuario, Contacto_Proveedor, Unidad, Inventario_Categoria, Cliente, JornadaHoras
from .models import Equipo_Categoria_Estatus, Equipo_Categoria, Clase_Equipo, Modelo, Equipo_Estatus
from .models import Herramienta_Movimiento, Herramienta_Historial, Inventario, Inventario_Tipo, Tipo_Instruccion


class JornadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jornada
        fields = '__all__'
        
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
        depth = 1

class Contacto_ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto_Proveedor
        fields = '__all__'
        depth = 2

class CentroCostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroCosto
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'


class Tipo_RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Rol
        fields = '__all__'


class ScopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scope
        fields = '__all__'


class EstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstatusUsuario
        fields = '__all__'


class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = '__all__'


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
        depth = 1


class Departamento_TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento_Turno
        fields = '__all__'
        depth = 1


class PuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puesto
        fields = '__all__'
        depth = 2


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        depth = 2


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'username')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class JornadaHorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = JornadaHoras
        fields = '__all__'
        depth = 1
        
class Historial_TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial_Turno
        fields = '__all__'
        depth = 4


class Usuario_Lat_Lng_Serializer(serializers.Serializer):

    lat = serializers.CharField(max_length=40, allow_blank=False)
    lng = serializers.CharField(max_length=40, allow_blank=False)

    class Meta:
        fields = ('Lat', 'lng')
        
class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = '__all__'

class Inventario_CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario_Categoria
        fields = '__all__'
        depth = 1


#Clase para relacionar llave y valor en formato JSON 
#para generar un conjunto de unidades[um, km, m... n+1] ,
#el valor de generate debe ser True, para que tenga efecto
class setup_Serializer(serializers.Serializer):  

    generar_unidades = serializers.BooleanField(required=True)
    generar_categorias = serializers.BooleanField(required=True)
    generar_equipo_categoria_estatus = serializers.BooleanField(required=True)
    generar_equipo_categoria = serializers.BooleanField(required=True)
    generar_clase_equipo = serializers.BooleanField(required=True)
    generar_modelo_icono = serializers.BooleanField(required=True)
    generar_equipo_categoria_icono = serializers.BooleanField(required=True)
    generar_instalacion_icono = serializers.BooleanField(required=True)
    generar_equipo_estatus = serializers.BooleanField(required=True)
    generar_herramienta_movimiento = serializers.BooleanField(required=True)
    generar_orden_subestatus = serializers.BooleanField(required=True)
    generar_orden_trabajo_estatus = serializers.BooleanField(required=True)

    class Meta:

        fields = ('generar_unidades, generar_categorias, generar_equipo_categoria_estatus, generar_equipo_categoria, generar_clase_equipo, generar_modelo_icono, generar_equipo_categoria_icono,generar_instalacion_icono, generar_equipo_estatus, generar_herramienta_movimiento','generar_orden_subestatus', 'generar_orden_trabajo_estatus' )


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        depth = 2

class EquipoCategoriaEstatusSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Equipo_Categoria_Estatus
        fields = '__all__'

class EquipoCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo_Categoria
        fields = '__all__'

class ClaseEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase_Equipo
        fields = '__all__'
        depth = 2

class ModeloIconoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo_Icono
        fields = '__all__'

class EquipoCategoriaIconoSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Equipo_Categoria_Icono
        fields = '__all__'
        depth = 2

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'
        depth = 3

class InstalacionIconoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instalacion_Icono
        fields = '__all__'

class InstalacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instalacion
        fields = '__all__'
        depth = 2

class EquipoEstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo_Estatus
        fields = '__all__'

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'
        depth = 4

class HerramientaMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Herramienta_Movimiento
        fields = '__all__'


class HerramientaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Herramienta
        fields = '__all__'
        depth = 4

class HerramientaHistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Herramienta_Historial
        fields = '__all__'
        depth = 2

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'
        depth = 2

class InventarioTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario_Tipo
        fields = '__all__'
        depth = 2

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
        depth = 2

class StockDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock_Detalle
        fields = '__all__'
        depth = 2

class StockEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock_Entrada
        fields = '__all__'
        depth = 2

class StockAjusteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock_Ajuste
        fields = '__all__'
        depth = 2

class ParteEstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parte_Estatus
        fields = '__all__'

class InventarioValeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario_Vale
        fields = '__all__'
        depth = 2

class InventarioAjusteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario_Ajuste
        fields = '__all__'
        depth = 2

class ParteDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parte_Detalle
        fields = '__all__'
        depth = 2

class ParteDetalleSurtidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parte_Detalle_Surtido
        fields = '__all__'  
        depth = 2

class DevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devolucion
        fields = '__all__'
        depth = 2

class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = '__all__'
        depth = 1

class OrdenTrabajoTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden_Trabajo_Tipo
        fields = '__all__'

class OrdenTrabajoPrioridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden_Trabajo_Prioridad
        fields = '__all__'

class OrdenTrabajoEstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden_Trabajo_Estatus
        fields = '__all__'

class OrdenSubestatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden_Subestatus
        fields = '__all__'

class OTSerializer(serializers.ModelSerializer):
    class Meta:
        model = OT
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class TareaOrdenTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea_Orden_Trabajo
        fields = '__all__'

class OrdenTrabajoParteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden_Trabajo_Parte
        fields = '__all__'

class TipoCambioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Cambio
        fields = '__all__'

class OrdenArchivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden_Archivos
        fields = '__all__'
        
class AtcOtTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Act_Ot_Tipo
        fields = '__all__'

class AtcOtCodigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Act_Ot_Codigo
        fields = '__all__'


class ActOtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Act_Ot
        fields = '__all__'

class FrecuenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frecuencia
        fields = '__all__'

class TipoProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Programa
        fields = '__all__'

class EquipoTareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo_Tarea
        fields = '__all__'

class TipoInstruccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Instruccion
        fields = '__all__'

class TiempoUnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiempo_Unidad
        fields = '__all__'

class InstruccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruccion
        fields = '__all__'

class TareaInstruccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea_Instruccion
        fields = '__all__'

class EquipoTareaParteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo_Tarea_Parte
        fields = '__all__'

class MecanismoFallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mecanismo_Falla
        fields = '__all__'

class CodigoFallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codigo_Falla
        fields = '__all__'

class M4Serializer(serializers.ModelSerializer):
    class Meta:
        model = M4
        fields = '__all__'


class OrdenTrabajoCompletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden_Trabajo_Completa
        fields = '__all__'

class RcaTipoAccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rca_Tipo_Accion
        fields = '__all__'

class RcaStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rca_Status
        fields = '__all__'

class RCASerializer(serializers.ModelSerializer):
    class Meta:
        model = Rca
        fields = '__all__'

class RcaPreventiveStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rca_Preventive_Status
        fields = '__all__'

class RcaAccionPreventivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rca_Accion_Preventiva
        fields = '__all__'

class ModoDeteccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modo_Deteccion
        fields = '__all__'

class ActividadMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad_Mantenimiento
        fields = '__all__'

class UsuarioRevisarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_Revisar
        fields = '__all__'

class OrdenTrabajoRevisadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden_trabajo_Revisada
        fields = '__all__'

class RutaEstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta_Estatus
        fields = '__all__'

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'

class RutaEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta_Equipo
        fields = '__all__'

class RutaCondicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta_Condicion
        fields = '__all__'

class RutaCondicionUnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta_Condicion_Unidad
        fields = '__all__'

class RutaEquipoComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta_Equipo_Componente
        fields = '__all__'

class RutaSetPointOperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta_Set_Point_Operador
        fields = '__all__'

class RutaSetPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta_Set_Point
        fields = '__all__'

class OrdenTrabajoRutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden_Trabajo_Ruta
        fields = '__all__'

class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = '__all__'

class ChecklistEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist_Equipo
        fields = '__all__'

class OrdenTrabajoRutaSetPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden_Trabajo_Ruta_Set_Point
        fields = '__all__'

class ChecklistAspectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist_Aspecto
        fields = '__all__'

class ChecklistInstruccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist_Instruccion
        fields = '__all__'

class ChecklistAspectoCopiadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist_Aspecto_Copiado
        fields = '__all__'

class ChkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chk
        fields = '__all__'

class ChkEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chk_Equipo
        fields = '__all__'

class ChkAspectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chk_Aspecto
        fields = '__all__'

class ChkInstruccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chk_Instruccion
        fields = '__all__'

class OrdenTrabajoChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden_Trabajo_Checklist
        fields = '__all__'
