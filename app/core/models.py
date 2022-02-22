import binascii
import os
from pyexpat import model
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Jornada(models.Model):
    id_jornada = models.AutoField(primary_key=True)
    anio = models.CharField(max_length=25, default="")
    mes = models.CharField(max_length=25, default="")
    horaInicio = models.TimeField()
    horaFinal = models.TimeField()
    
    def str(self):
        return super().str()

class CentroCosto(models.Model):
    id_centro_costo = models.AutoField(primary_key=True)
    codigo_centro_costo = models.BigIntegerField()
    nombre_centro_costo = models.CharField(max_length=25, default="")
    codigo_cc = models.BigIntegerField()
    
    def str(self):
        return super().str()

class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=25)

    def __str__(self):
        return super().__str__()


class Turno(models.Model):
    id_turno = models.AutoField(primary_key=True)
    nombre_turno = models.CharField(max_length=25)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return super().__str__()


class Tipo_Rol(models.Model):
    id_tipo_rol = models.AutoField(primary_key=True)
    nombre_tipo_rol = models.CharField(max_length=25)

    def __str__(self):
        return super().__str__()


class Scope(models.Model):
    id_scope = models.AutoField(primary_key=True)
    nombre_scope = models.CharField(max_length=25)

    def __str__(self):
        return super().__str__()


class EstatusUsuario(models.Model):
    id_estatus = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    activo = models.BooleanField()

    def __str__(self):
        return super().__str__()


class Idioma(models.Model):
    id_idioma = models.AutoField(primary_key=True)
    idioma = models.CharField(max_length=25, default="")
    idioma_en = models.CharField(max_length=25, default="")

    def __str__(self):
        return super().__str__()


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    tipo_rol = models.ForeignKey(Tipo_Rol, on_delete=models.SET_NULL, null=True)
    scope = models.ForeignKey(Scope, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()


class Departamento_Turno(models.Model):
    id_departamento_turno = models.AutoField(primary_key=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    turno = models.ForeignKey(Turno, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Puesto(models.Model):
    id_puesto = models.AutoField(primary_key=True)
    nombre_puesto = models.CharField(max_length=25)
    departamento_turno = models.ForeignKey(Departamento_Turno, on_delete=models.SET_NULL, null=True,
                                           )

    def __str__(self):
        return super().__str__()


# on_delete establecer eliminar en cascada
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, default="")
    p_nombre = models.CharField(max_length=25)
    p_apellido = models.CharField(max_length=25)
    s_apellido = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    password = models.CharField(max_length=15)
    es_activo=models.BooleanField(null=True)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    puesto = models.ForeignKey(Puesto, on_delete=models.SET_NULL, null=True)
    idioma = models.ForeignKey(Idioma, on_delete=models.SET_NULL, null=True)
    estatus = models.ForeignKey(EstatusUsuario, on_delete=models.SET_NULL, null=True)

class Historial_Turno(models.Model):
    id_historial_turno = models.AutoField(primary_key=True)
    milisegundos = models.CharField(max_length=25)
    fecha = models.DateField()
    turno = models.ForeignKey(Turno, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class JornadaHoras(models.Model):
    id_jornada_horas = models.AutoField(primary_key=True)
    jornada = models.ForeignKey(Jornada, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    dia = models.CharField(max_length=25, default="")
    hora = models.TimeField()
    
    def __str__(self):
        return super().__str__()

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    proveedor = models.CharField(max_length=25, default="")
    calle = models.CharField(max_length=25, default="")
    colonia = models.CharField(max_length=25, default="")
    cp = models.BigIntegerField()
    municipio = models.CharField(max_length=25, default="")
    estado = models.CharField(max_length=25, default="")
    pais = models.CharField(max_length=25, default="")
    razon_social = models.CharField(max_length=25, default="")
    rfc = models.BigIntegerField()
    pagina_web = models.CharField(max_length=25, default="")
    foto_proveedor = models.CharField(max_length=50)
    id_estatus_proveedor = models.ForeignKey(EstatusUsuario, on_delete=models.SET_NULL, null=True)
    numero_proveedor = models.BigIntegerField()
    moneda = models.CharField(max_length=25, default="")

    def __str__(self):
        return super().__str__()

class Contacto_Proveedor(models.Model):
    id_contacto_proveedor = models.AutoField(primary_key=True)
    contacto = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()


class Unidad(models.Model):
    id_unidad = models.AutoField(primary_key=True)
    unidad_es = models.CharField(max_length=25, default="")
    unidad_en = models.CharField(max_length=25, default="")
    siglas = models.CharField(max_length=25, default="")

    def str(self):
        return super().str()


class Inventario_Categoria(models.Model):
    id_inventario_categoria = models.AutoField(primary_key=True)
    inventario_categoria = models.CharField(max_length=120, default="")
    inventario_categoria_notas = models.CharField(max_length=500, default="")
    inventario_categoria_estatus = models.ForeignKey(EstatusUsuario, on_delete=models.SET_NULL, null=True)

    def str(self):
        return super().str()

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=45)
    calle = models.CharField(max_length=45)
    colonia = models.CharField(max_length=45)
    cp = models.BigIntegerField()
    municipio = models.CharField(max_length=45)
    estado = models.CharField(max_length=45)
    pais = models.CharField(max_length=45)
    razon_social = models.CharField(max_length=75)
    rfc = models.CharField(max_length=13)
    telefono = models.BigIntegerField()
    contacto = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    pagina_web = models.CharField(max_length=25)
    id_zona_horaria = models.IntegerField()
    foto_cliente = models.CharField(max_length=50)
    usar_inventario = models.IntegerField()
    alertas_email = models.IntegerField()
    registro = models.IntegerField()

    def __str__(self):
        return super().__str__()


class Equipo_Categoria_Estatus(models.Model):
    id_equipo_categoria_estatus = models.AutoField(primary_key=True)
    equipo_categoria_estatus_en = models.CharField(max_length=25)
    equipo_categoria_estatus_es = models.CharField(max_length=25)

    def __str__(self):
        return super().__str__()

class Equipo_Categoria(models.Model):
    id_equipo_categoria = models.AutoField(primary_key=True)
    equipo_categoria_en = models.CharField(max_length=60)
    equipo_categoria_es = models.CharField(max_length=60)
    equipo_categoria_clave_en = models.CharField(max_length=20)
    equipo_categoria_clave_es = models.CharField(max_length=20)
    estatus = models.ForeignKey(Equipo_Categoria_Estatus, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return super().__str__()

class Clase_Equipo(models.Model):
    id_clase_equipo = models.AutoField(primary_key=True)
    clase_equipo_en = models.CharField(max_length=45)
    clase_equipo_es = models.CharField(max_length=45)
    codigo_clase = models.BigIntegerField()
    equipo_categoria = models.ForeignKey(Equipo_Categoria, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return super().__str__()

class Modelo_Icono(models.Model):
    id_modelo_icono = models.AutoField(primary_key=True)
    modelo_icono_es = models.CharField(max_length=70)
    modelo_icono_en = models.CharField(max_length=70)
    
    def __str__(self):
        return super().__str__()

class Equipo_Categoria_Icono(models.Model):
    id_equipo_categoria_icono = models.AutoField(primary_key=True)
    equipo_categoria = models.ForeignKey(Equipo_Categoria, on_delete=models.SET_NULL, null=True)
    modelo_icono = models.ForeignKey(Modelo_Icono, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Modelo(models.Model):
    id_modelo = models.AutoField(primary_key=True)
    num_modelo = models.CharField(max_length=20)
    modelo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=254)
    fabricante = models.CharField(max_length=45)
    tipo_de_equipo = models.CharField(max_length=45)
    clase_equipo = models.ForeignKey(Clase_Equipo, on_delete=models.SET_NULL, null=True)
    icono = models.ForeignKey(Modelo_Icono, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Instalacion_Icono(models.Model):
    id_instalacion_icono = models.AutoField(primary_key=True)
    instalacion_icono_en = models.CharField(max_length=45)
    instalacion_icono_es = models.CharField(max_length=45)
  
    def __str__(self):
        return super().__str__()

class Instalacion(models.Model):
    id_instalacion = models.AutoField(primary_key=True)
    descripcion_instalacion = models.CharField(max_length=45)
    jerarquia_instalacion = models.CharField(max_length=45)
    padre_instalacion = models.CharField(max_length=45)
    foto_instalacion = models.CharField(max_length=45)
    lugar_instalacion = models.CharField(max_length=45)
    icono = models.ForeignKey(Instalacion_Icono, on_delete=models.SET_NULL, null=True)
    color = models.IntegerField()
    estatus_instalacion = models.ForeignKey(EstatusUsuario, on_delete=models.SET_NULL, null=True)
    horas = models.IntegerField()
    operadores = models.IntegerField()
      
    def __str__(self):
        return super().__str__()

class Equipo_Estatus(models.Model):
    id_equipo_estatus = models.AutoField(primary_key=True)
    equipo_estatus_en = models.CharField(max_length=45)
    equipo_estatus_es = models.CharField(max_length=45)
   
    def __str__(self):
        return super().__str__()

class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    numero_de_equipo = models.CharField(max_length=45)
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)
    estatus = models.ForeignKey(Equipo_Estatus, on_delete=models.SET_NULL, null=True)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.SET_NULL, null=True)
    centro_costos = models.ForeignKey(CentroCosto, on_delete=models.SET_NULL, null=True)
    criticidad = models.IntegerField()
    pasillo = models.CharField(max_length=45)
    equipo_caido = models.IntegerField()
    tiempo_muerto = models.CharField(max_length=20)
    fila = models.CharField(max_length=45)
    jerarquia = models.CharField(max_length=2)
    codigo_qr = models.CharField(max_length=255)
    codigo_barras = models.CharField(max_length=255)
    foto_equipo = models.CharField(max_length=60)
    icono =  models.ForeignKey(Modelo_Icono, on_delete=models.SET_NULL, null=True)
    num_pedimiento = models.CharField(max_length=20)
    garantia = models.CharField(max_length=50)
    fecha_compra = models.DateField()
    num_serie = models.CharField(max_length=200)
    horas_diarias = models.CharField(max_length=20)
    dlunes = models.IntegerField()
    dmartes = models.IntegerField()
    dmiercoles = models.IntegerField()
    djueves = models.IntegerField()
    dviernes = models.IntegerField()
    dsabado = models.IntegerField()
    ddomingo = models.IntegerField()
    comentarios = models.CharField(max_length=500)
    referencias =models.CharField(max_length=500)

    def __str__(self):
        return super().__str__()

class Herramienta_Movimiento(models.Model):
    id_herramienta_movimiento = models.AutoField(primary_key=True)
    herramienta_movimiento_en = models.CharField(max_length=75)
    herramienta_movimiento_es = models.CharField(max_length=75)
  
    def __str__(self):
        return super().__str__()


class Herramienta(models.Model):
    id_herramienta = models.AutoField(primary_key=True)
    herramienta= models.CharField(max_length=500)
    herramienta_codigo = models.CharField(max_length=50)
    herramienta_descripcion = models.CharField(max_length=1000)
    herramienta_marca = models.CharField(max_length=50)
    herramienta_modelo = models.CharField(max_length=50)
    herramienta_num_serie = models.CharField(max_length=50)
    herramienta_departamento = models.CharField(max_length=50)
    herramienta_proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    herramienta_usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    herramienta_registro = models.DateField()
    herramienta_estatus = models.ForeignKey(EstatusUsuario, on_delete=models.SET_NULL, null=True)
    herramienta_foto = models.CharField(max_length=120)
    herramienta_movimiento = models.ForeignKey(Herramienta_Movimiento, on_delete=models.SET_NULL, null=True)
    herramienta_costo = models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()

class Herramienta_Historial(models.Model):
    id_herramienta_historial = models.AutoField(primary_key=True)
    herramienta= models.ForeignKey(Herramienta, on_delete=models.SET_NULL, null=True)
    herramienta_movimiento = models.ForeignKey(Herramienta_Movimiento, on_delete=models.SET_NULL, null=True)
    fecha_movimiento = models.DateField()
    notas_herramienta = models.CharField(max_length=1000)
    solicitante = models.ForeignKey(Usuario , related_name='+', on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario , related_name='+', on_delete=models.SET_NULL, null=True)
    prestamo = models.IntegerField()

    def __str__(self):
        return super().__str__()

class Inventario_Tipo(models.Model):
    id_inventario_tipo = models.AutoField(primary_key=True)
    inventario_tipo_es = models.CharField(max_length=30)
    inventario_tipo_en = models.CharField(max_length=30)

    def __str__(self):
        return super().__str__()

class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    inventario = models.CharField(max_length=1000)
    descripcion_inventario = models.CharField(max_length=1000)
    codigo_inventario = models.CharField(max_length=50)
    estatus_inventario = models.ForeignKey(EstatusUsuario, on_delete=models.SET_NULL, null=True)
    prioridad_inventario = models.IntegerField()
    foto_inventario = models.CharField(max_length=200)
    inventario_categoria = models.ForeignKey(Inventario_Categoria, on_delete=models.SET_NULL, null=True)
    inventario_tipo = models.ForeignKey(Inventario_Tipo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.SET_NULL, null=True)
    inventario = models.ForeignKey(Inventario, on_delete=models.SET_NULL, null=True)
    cantidad_actual = models.IntegerField()
    punto_reorden = models.IntegerField()
    pasillo = models.CharField(max_length=50)
    columna = models.CharField(max_length=50)
    contenedor = models.CharField(max_length=50)
    user_stock = models.IntegerField()
    img_inventario = models.CharField(max_length=200)
    maxima = models.IntegerField()
    
    def __str__(self):
        return super().__str__()

class Stock_Detalle(models.Model):
    id_stock_detalle = models.AutoField(primary_key=True)
    inventario = models.ForeignKey(Inventario, on_delete=models.SET_NULL, null=True)
    cuenta = models.CharField(max_length=20)
    centro_costos = models.ForeignKey(CentroCosto, on_delete=models.SET_NULL, null=True)
    modelo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=50)
    notas_detalles = models.CharField(max_length=1000)
    unidad = models.ForeignKey(Unidad, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return super().__str__()


class Stock_Entrada(models.Model):
    id_stock_entrada = models.AutoField(primary_key=True)
    inventario = models.ForeignKey(Inventario, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    fecha_orden = models.DateField()
    fecha_recibido = models.DateField()
    orden_compra = models.CharField(max_length=50)
    cantidad_recibida = models.CharField(max_length=50)
    precio_unitario = models.CharField(max_length=50)
    embargado_a = models.IntegerField()
    user_entrada =  models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    cantidad_disponible = models.CharField(max_length=50)
    moneda = models.IntegerField()
    dolares = models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()

class Stock_Ajuste(models.Model):
    id_stock_ajuste = models.AutoField(primary_key=True)
    stock_entrada = models.ForeignKey(Stock_Entrada, on_delete=models.SET_NULL, null=True)
    usuario_ajuste = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    fecha_ajuste = models.DateField()
    orden_compra_1 = models.CharField(max_length=50)
    orden_compra_2 = models.CharField(max_length=50)
    proveedor_1 = models.ForeignKey(Proveedor, related_name='+', on_delete=models.SET_NULL, null=True)
    proveedor_2 = models.ForeignKey(Proveedor, related_name='+', on_delete=models.SET_NULL, null=True)
    cantidad_1 = models.CharField(max_length=50)
    cantidad_2 = models.CharField(max_length=50)
    cantidad_disponible_1 = models.CharField(max_length=50)
    cantidad_disponible_2 = models.CharField(max_length=50)
    precio_unitario_1 = models.CharField(max_length=50)
    precio_unitario_2 = models.CharField(max_length=50)
    moneda_1 = models.IntegerField()
    moneda_2 = models.IntegerField()
    dolares_1 = models.CharField(max_length=50)
    dolares_2 = models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()


class Parte_Estatus(models.Model):
    id_parte_estatus = models.AutoField(primary_key=True)
    parte_estatus_en  = models.CharField(max_length=30)
    parte_estatus_es = models.CharField(max_length=30)

    def __str__(self):
        return super().__str__()

class Inventario_Vale(models.Model):
    id_inventario_vale = models.AutoField(primary_key=True)
    nombre_vale  = models.CharField(max_length=20)
    inventario = models.ForeignKey(Inventario, on_delete=models.SET_NULL, null=True)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.SET_NULL, null=True)
    solicitante = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    cantidad_solicitada = models.CharField(max_length=50)
    cantidad_surtida = models.CharField(max_length=50)
    parte_estatus = models.ForeignKey(Parte_Estatus, on_delete=models.SET_NULL, null=True)
    fecha_surtido = models.DateField()
    fecha_solicitud  = models.DateField() 
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return super().__str__()

class Inventario_Ajuste(models.Model):
    id_inventario_ajuste = models.AutoField(primary_key=True)
    nombre_ajuste  = models.CharField(max_length=20)
    inventario = models.ForeignKey(Inventario, on_delete=models.SET_NULL, null=True)
    stock_entrada = models.ForeignKey(Stock_Entrada, on_delete=models.SET_NULL, null=True)
    solicitante = models.ForeignKey(Usuario, related_name='+', on_delete=models.SET_NULL, null=True)
    fecha_solicitud  = models.DateField() 
    fecha_aceptado = models.DateField()
    parte_estatus = models.ForeignKey(Parte_Estatus, on_delete=models.SET_NULL, null=True)
    aprobador = models.ForeignKey(Usuario ,related_name='+', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return super().__str__()

class Parte_Detalle(models.Model):
    id_parte_detalle = models.AutoField(primary_key=True)
    orden_trabajo_parte  = models.IntegerField()
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)
    stock_entrada = models.ForeignKey(Stock_Entrada, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    inventario_vale = models.ForeignKey(Inventario_Vale, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Parte_Detalle_Surtido(models.Model):
    id_parte_detalle_surtido = models.AutoField(primary_key=True)
    id_surtido_por  = models.IntegerField()
    id_orden_trabajo_parte = models.IntegerField()
    inventario_vale = models.ForeignKey(Inventario_Vale, on_delete=models.SET_NULL, null=True)
    fecha_surtido = models.DateField()
    hora_surtido  = models.TimeField()
    
    def __str__(self):
        return super().__str__()

class Devolucion(models.Model):
    id_devolucion = models.AutoField(primary_key=True)
    id_devuelto_por  = models.IntegerField()
    id_orden_trabajo_parte = models.IntegerField()
    inventario_vale = models.ForeignKey(Inventario_Vale, on_delete=models.SET_NULL, null=True)
    fecha_devuelto = models.DateField()
    hora_devuelto  = models.TimeField()
    def __str__(self):
        return super().__str__()

class Almacen(models.Model):
    id_almacen = models.AutoField(primary_key=True)
    descripcion_almacen = models.CharField(max_length=45)
    jerarquia_almacen = models.CharField(max_length=45)
    padre_almacen = models.CharField(max_length=45)
    foto_almacen = models.CharField(max_length=45)
    lugar_almacen  = models.CharField(max_length=45)
    icono = models.IntegerField()
    color = models.IntegerField()
    estatus_almacen = models.ForeignKey(EstatusUsuario, on_delete=models.SET_NULL, null=True)
   
    def __str__(self):
        return super().__str__()

class Orden_Trabajo_Tipo(models.Model):
    id_orden_trabajo_tipo = models.AutoField(primary_key=True)
    siglas_es = models.CharField(max_length=20)
    sigles_en = models.CharField(max_length=20)
    orden_trabajo_tipo_es = models.CharField(max_length=200)
    orden_trabajo_tipo_en = models.CharField(max_length=200)
   
    def __str__(self):
        return super().__str__()

class Orden_Trabajo_Prioridad(models.Model):
    id_orden_trabajo_prioridad = models.AutoField(primary_key=True)
    orden_trabajo_prioridad_es = models.CharField(max_length=200)
    orden_trabajo_prioridad_en = models.CharField(max_length=200)
   
    def __str__(self):
        return super().__str__()

class Orden_Subestatus(models.Model):
    id_orden_subestatus = models.AutoField(primary_key=True)
    orden_subestatus_es = models.CharField(max_length=120)
    orden_subestatus_en = models.CharField(max_length=120)
   
    def __str__(self):
        return super().__str__()

class Orden_Trabajo_Estatus(models.Model):
    id_orden_trabajo_estatus = models.AutoField(primary_key=True)
    orden_trabajo_estatus_es = models.CharField(max_length=120)
    orden_trabajo_estatus_en = models.CharField(max_length=120)
   
    def __str__(self):
        return super().__str__()

class OT(models.Model):
    id_ot = models.AutoField(primary_key=True)
    id_visible_ot = models.CharField(max_length=45)
    descipcion_ot = models.CharField(max_length=255)
    equipo_ot = models.ForeignKey(Equipo , on_delete=models.SET_NULL, null=True)
    id_requisitor_ot = models.ForeignKey(Usuario, related_name='+', on_delete=models.SET_NULL, null=True)
    id_cuenta = models.DateField()
    id_problema = models.BigIntegerField()
    id_causa = models.BigIntegerField()
    id_actividad = models.BigIntegerField()
    caido_ot = models.BigIntegerField()
    prioridad_ot = models.ForeignKey(Orden_Trabajo_Prioridad, on_delete=models.SET_NULL, null=True)
    tipo_de_trabajo_ot = models.BigIntegerField()
    estatus_ot = models.ForeignKey(Orden_Trabajo_Estatus, on_delete=models.SET_NULL, null=True)
    subestatus_ot = models.ForeignKey(Orden_Subestatus, on_delete=models.SET_NULL, null=True)
    responsable_ot = models.ForeignKey(Usuario,related_name='+', on_delete=models.SET_NULL, null=True)
    fecha_inicio_ot = models.DateField()
    fecha_estimada = models.DateField()
    fecha_fin_ot = models.DateField()
    tecnico_asignado = models.ForeignKey(Usuario, related_name='+', on_delete=models.SET_NULL, null=True)
    instr_trab_ot = models.CharField(max_length=1000)
    notas_ot = models.CharField(max_length=1000)
    trab_estimados = models.BigIntegerField()

    def __str__(self):
        return super().__str__()

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    tabla = models.CharField(max_length=70)
    id_registro = models.BigIntegerField()
    accion_en = models.CharField(max_length=50)
    fecha  = models.DateField()
    hora = models.TimeField()
    linux = models.CharField(max_length=20)
    bloque_es = models.CharField(max_length=20)
    accion_es = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255)
    bloque_en = models.CharField(max_length=20)

    def __str__(self):
        return super().__str__()

class Tarea_Orden_Trabajo(models.Model):
    id_tarea_orden_trabajo = models.AutoField(primary_key=True)
    id_tarea = models.IntegerField()
    orden_trabajo = models.ForeignKey(OT , on_delete=models.SET_NULL, null=True)
    fecha  = models.DateField()
    hora = models.TimeField()
    instrucciones = models.CharField(max_length=500)
    fecha_base = models.DateField()
    tiempo_estimado = models.CharField(max_length=10)
    ventana_cumplimiento = models.IntegerField()
    bloque_en = models.CharField(max_length=20)
    
    def __str__(self):
        return super().__str__()


class Orden_Trabajo_Parte(models.Model):
    id_orden_trabajo_parte = models.AutoField(primary_key=True)
    ot = models.ForeignKey(OT, on_delete=models.SET_NULL, null=True)
    inventario  = models.ForeignKey(Inventario, on_delete=models.SET_NULL, null=True)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.SET_NULL, null=True)
    solicitante = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    cantidad_solicitada = models.DateField()
    cantidad_surtida = models.CharField(max_length=10)
    parte_estatus = models.IntegerField()
    fecha_surtido = models.DateField()
    fecha_solicitud = models.DateField()

    def __str__(self):
        return super().__str__()

class Tipo_Cambio(models.Model):
    id_tipo_cambio = models.AutoField(primary_key=True)
    tipo_cambio = models.CharField(max_length=10)
    tipo_cambio_en = models.CharField(max_length=30)
    tipo_cambio_es = models.CharField(max_length=30)
    
    def __str__(self):
        return super().__str__()

class Orden_Archivos(models.Model):
    id_orden_archivos = models.AutoField(primary_key=True)
    nombre_archivo = models.CharField(max_length=50)
    archivo = models.CharField(max_length=70)
    fecha = models.DateField()
    comentarios = models.CharField(max_length=255)
    id_orden = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return super().__str__()


class Act_Ot_Tipo(models.Model):
    id_act_ot_tipo = models.AutoField(primary_key=True)
    act_ot_tipo_en = models.CharField(max_length=45)
    act_ot_tipo_es = models.CharField(max_length=45)
    
    def __str__(self):
        return super().__str__()

class Act_Ot_Codigo(models.Model):
    id_act_ot_codigo = models.AutoField(primary_key=True)
    act_ot_codigo_en = models.CharField(max_length=120)
    act_ot_codigo_es = models.CharField(max_length=120)
    act_clave = models.CharField(max_length=20)

    def __str__(self):
        return super().__str__()

class Frecuencia(models.Model):
    id_frecuencia = models.AutoField(primary_key=True)
    frecuencia_es = models.CharField(max_length=30)
    frecuencia_en = models.CharField(max_length=30)
    tiempo_es = models.CharField(max_length=30)
    tiempo_en = models.CharField(max_length=30)

    def __str__(self):
        return super().__str__()

class Tipo_Programa(models.Model):
    id_tipo_programa = models.AutoField(primary_key=True)
    tipo_programa_es = models.CharField(max_length=30)
    tipo_programa_en = models.CharField(max_length=30)

    def __str__(self):
        return super().__str__()

class Equipo_Tarea(models.Model):
    id_equipo_tarea = models.AutoField(primary_key=True)
    tarea = models.CharField(max_length=70)
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
    tipo =  models.ForeignKey(Act_Ot_Tipo, on_delete=models.SET_NULL, null=True)
    descripcion = models.CharField(max_length=20)
    realizar_activa = models.IntegerField()
    tipo_programa = models.ForeignKey(Tipo_Programa, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateField()
    frecuencia = models.ForeignKey(Frecuencia, on_delete=models.SET_NULL, null=True)
    estatus = models.ForeignKey(EstatusUsuario, on_delete=models.SET_NULL, null=True)
    cada = models.IntegerField()
    user = models.ForeignKey(Usuario, related_name='+', on_delete=models.SET_NULL, null=True)
    ultima_fecha = models.DateField()
    numero_trabajadores = models.IntegerField()
    usuario = models.ForeignKey(Usuario , related_name='+', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()


class Tipo_Instruccion(models.Model):
    id_tipo_instruccion = models.AutoField(primary_key=True)
    tipo_instruccion_es = models.CharField(max_length=70)
    tipo_instruccion_en = models.CharField(max_length=70)

    def __str__(self):
        return super().__str__()

class Tiempo_Unidad(models.Model):
    id_tiempo_unidad = models.AutoField(primary_key=True)
    unidad_es = models.CharField(max_length=30)
    unidad_en = models.CharField(max_length=30)

    def __str__(self):
        return super().__str__()

class Instruccion(models.Model):
    id_instruccion = models.AutoField(primary_key=True)
    instruccion = models.CharField(max_length=50)
    codigo = models.CharField(max_length=20)
    tipo = models.ForeignKey(Tipo_Instruccion, on_delete=models.SET_NULL, null=True)
    tiempo = models.CharField(max_length=20)
    unidad = models.ForeignKey(Tiempo_Unidad, on_delete=models.SET_NULL, null=True)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return super().__str__()


class Tarea_Instruccion(models.Model):
    id_tarea_instruccion = models.AutoField(primary_key=True)
    tarea =  models.ForeignKey(Tarea_Orden_Trabajo, on_delete=models.SET_NULL, null=True)
    instruccion =  models.ForeignKey(Instruccion, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    hora = models.TimeField()
    user =  models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    posicion =  models.IntegerField()

    def __str__(self):
        return super().__str__()


class Equipo_Tarea_Parte(models.Model):
    id_equipo_tarea_parte = models.AutoField(primary_key=True)
    parte =  models.ForeignKey(Orden_Trabajo_Parte, on_delete=models.SET_NULL, null=True)
    cantidad_solicitada =  models.IntegerField()
    tarea = models.ForeignKey(Tarea_Orden_Trabajo, on_delete=models.SET_NULL, null=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
    user =  models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    instalacion =  models.ForeignKey(Instalacion, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Mecanismo_Falla(models.Model):
    id_mecanismo_falla = models.AutoField(primary_key=True)
    mecanismo_falla_en = models.CharField(max_length=30)
    mecanismo_falla_es = models.CharField(max_length=30)
    mecanismo_falla_code = models.CharField(max_length=10)

    def __str__(self):
        return super().__str__()

class Codigo_Falla(models.Model):
    id_codigo_falla = models.AutoField(primary_key=True)
    codigo_falla_en = models.CharField(max_length=50)
    codigo_falla_es = models.CharField(max_length=50)
    codigo_falla_code = models.CharField(max_length=10)
    mecanismo_falla = models.ForeignKey(Mecanismo_Falla, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()


class M4(models.Model):
    id_4m = models.AutoField(primary_key=True)
    es_4m = models.CharField(max_length=50)
    en_4m = models.CharField(max_length=50)
   
    def __str__(self):
        return super().__str__()


class Act_Ot(models.Model):
    id_act_ot_codigo = models.AutoField(primary_key=True)
    ot = models.ForeignKey(OT, on_delete=models.SET_NULL, null=True)
    comentarios_act_ot = models.CharField(max_length=10)
    fecha_act_ot = models.DateField()
    hora_inicio_act = models.TimeField()
    fecha_act_ot_2 = models.DateField()
    hora_inicio_act_2 = models.TimeField()
    hora_fin_act =  models.TimeField()
    tipo_hora_act = models.IntegerField()
    codigo_paro_act = models.ForeignKey(Codigo_Falla , on_delete=models.SET_NULL, null=True)
    creador_act_ot = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    tiempo_muerto = models.IntegerField() 

    def __str__(self):
        return super().__str__()

class Modo_Deteccion(models.Model):
    id_modo_deteccion = models.AutoField(primary_key=True)
    modo_deteccion_en = models.CharField(max_length=50)
    modo_deteccion_es = models.CharField(max_length=50)
    modo_deteccion_code_en = models.CharField(max_length=50)
    modo_deteccion_code_es = models.CharField(max_length=50)
    def __str__(self):
        return super().__str__()

class Actividad_Mantenimiento(models.Model):
    id_actividad_mantenimiento = models.AutoField(primary_key=True)
    actividad_mantenimiento_en = models.CharField(max_length=30)
    actividad_mantenimiento_es = models.CharField(max_length=30)
    actividad_mantenimiento_code = models.CharField(max_length=10)
    def __str__(self):
        return super().__str__()

class Orden_Trabajo_Completa(models.Model):
    id_orden_trabajo_completa = models.AutoField(primary_key=True)
    orden_trabajo = models.ForeignKey(OT, on_delete=models.SET_NULL, null=True)
    cuenta_cc = models.CharField(max_length=20)
    mecanismo_falla =  models.ForeignKey(Mecanismo_Falla, on_delete=models.SET_NULL, null=True)
    codigo_falla = models.ForeignKey(Codigo_Falla, on_delete=models.SET_NULL, null=True)
    id_modo_deteccion =  models.IntegerField()
    id_actividad_mantenimiento =  models.IntegerField()
    modo_falla = models.CharField(max_length=50)
    notas =models.CharField(max_length=1000)
    trabajadores_reales = models.IntegerField()
    tiempo_real =  models.CharField(max_length=5)
    m4 =  models.ForeignKey(M4, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return super().__str__()


class Rca_Tipo_Accion(models.Model):
    id_rca_tipo_accion = models.AutoField(primary_key=True)
    rca_tipo_accion_en = models.CharField(max_length=50)
    rca_tipo_accion_en = models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()


class Rca_Status(models.Model):
    id_rca_status = models.AutoField(primary_key=True)
    rca_status_en = models.CharField(max_length=30)
    rca_status_en = models.CharField(max_length=30)

    def __str__(self):
        return super().__str__()


class Rca(models.Model):
    id_rca = models.AutoField(primary_key=True)
    ot = models.ForeignKey(OT, on_delete=models.SET_NULL, null=True)
    rca_causa = models.CharField(max_length=100)
    rca_tipo_accion = models.ForeignKey(Rca_Tipo_Accion, on_delete=models.SET_NULL, null=True)
    rca_status = models.ForeignKey(Rca_Status, on_delete=models.SET_NULL, null=True)
    rca_causa_raiz = models.CharField(max_length=100)

    def __str__(self):
        return super().__str__()


class Rca_Preventive_Status(models.Model):
    id_rca_status = models.AutoField(primary_key=True)
    rca_preventive_status_en = models.CharField(max_length=50)
    rca_preventive_status_en = models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()

class Rca_Accion_Preventiva(models.Model):
    id_rca_accion_preventiva = models.AutoField(primary_key=True)
    rca = models.ForeignKey(Rca, on_delete=models.SET_NULL, null=True)
    ot =models.ForeignKey(OT, on_delete=models.SET_NULL, null=True)
    rca_accion_preventiva = models.CharField(max_length=50)
    fecha_cumpliento = models.DateField()
    duenio = models.CharField(max_length=50)
    rca_preventive_status = models.ForeignKey(Rca_Preventive_Status, on_delete=models.SET_NULL, null=True)
    fecha_apertura = models.DateField()

    def __str__(self):
        return super().__str__()

class Usuario_Revisar(models.Model):
    id_usuario_revisar = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()


class Orden_trabajo_Revisada(models.Model):
    id_orden_trabajo_revisada = models.AutoField(primary_key=True)
    ot = models.ForeignKey(OT, on_delete=models.SET_NULL, null=True)
    calificacion_revisada = models.IntegerField()
    comentarios_revisada = models.CharField(max_length=1000)
    fecha_revisada = models.DateField()
    hora_revisada = models.TimeField()
    reviso = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Ruta_Estatus(models.Model):
    id_ruta_estatus = models.AutoField(primary_key=True)
    ruta_estatus_es = models.CharField(max_length=30)
    ruta_estatus_en = models.CharField(max_length=30)

    def __str__(self):
        return super().__str__()

class Ruta(models.Model):
    id_ruta = models.AutoField(primary_key=True)
    user_creador = models.ForeignKey(Usuario , related_name='+', on_delete=models.SET_NULL, null=True)
    user_modifico = models.ForeignKey(Usuario , related_name='+', on_delete=models.SET_NULL, null=True)
    ruta_estatus = models.ForeignKey(Ruta_Estatus , on_delete=models.SET_NULL, null=True)
    frecuencia = models.ForeignKey(Frecuencia , on_delete=models.SET_NULL, null=True)
    id_asignado = models.IntegerField()
    instalacion = models.ForeignKey(Instalacion, on_delete=models.SET_NULL, null=True)
    ruta = models.CharField(max_length=50)
    ruta_codigo = models.CharField(max_length=30)
    ruta_cada = models.IntegerField()
    ruta_modificado = models.CharField(max_length=10)
    tipo_ot = models.ForeignKey(Orden_Trabajo_Tipo, on_delete=models.SET_NULL, null=True)
    tipo_programa  = models.ForeignKey(Tipo_Programa, on_delete=models.SET_NULL, null=True)
    ruta_alcance = models.IntegerField()
    ruta_trabajadores = models.IntegerField()
    ruta_realizar_activo = models.IntegerField()
    tiempo_estimado = models.CharField(max_length=10)
    
    def __str__(self):
        return super().__str__()

class Ruta_Equipo(models.Model):
    id_ruta_equipo = models.AutoField(primary_key=True)
    ruta = models.ForeignKey(Ruta, on_delete=models.SET_NULL, null=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Ruta_Condicion(models.Model):
    id_ruta_condicion = models.AutoField(primary_key=True)
    ruta_condicion_en = models.CharField(max_length=30)
    ruta_condicion_es = models.CharField(max_length=30)

    def __str__(self):
        return super().__str__()

class Ruta_Condicion_Unidad(models.Model):
    id_ruta_condicion_unidad = models.AutoField(primary_key=True)
    ruta_condicion = models.ForeignKey(Ruta_Condicion, on_delete=models.SET_NULL, null=True)
    ruta_condicion_unidad_en = models.CharField(max_length=30)
    ruta_condicion_unidad_es = models.CharField(max_length=30)

    def __str__(self):
        return super().__str__()

class Ruta_Equipo_Componente(models.Model):
    id_ruta_equipo_componente = models.AutoField(primary_key=True)
    ruta_equipo = models.ForeignKey(Ruta_Equipo, on_delete=models.SET_NULL, null=True)
    componente = models.CharField(max_length=50)
    ruta_condicion =  models.ForeignKey(Ruta_Condicion, on_delete=models.SET_NULL, null=True)
    ruta_condicion_unidad =  models.ForeignKey(Ruta_Condicion_Unidad, on_delete=models.SET_NULL, null=True)
    puntos_componente = models.IntegerField()
    fecha_componente = models.DateField()
    ciclo = models.IntegerField()
    id_ciclo_condicion = models.IntegerField()
    ciclo_cantidad = models.IntegerField()

    def __str__(self):
        return super().__str__()


class Ruta_Set_Point_Operador(models.Model):
    id_ruta_set_point_operador = models.AutoField(primary_key=True)
    ruta_set_point_operador_es = models.CharField(max_length=20)
    ruta_set_point_operador_en = models.CharField(max_length=20)

    def __str__(self):
        return super().__str__()

class Ruta_Set_Point(models.Model):
    id_ruta_set_point = models.AutoField(primary_key=True)
    ruta_equipo_componente =  models.ForeignKey(Ruta_Equipo_Componente , on_delete=models.SET_NULL, null=True)
    ruta_set_point_operador =  models.ForeignKey(Ruta_Set_Point_Operador , on_delete=models.SET_NULL, null=True)
    ruta_set_point_1 = models.IntegerField()
    ruta_set_point_2 = models.IntegerField()

    def __str__(self):
        return super().__str__()


class Orden_Trabajo_Ruta(models.Model):
    id_orden_trabajo_ruta = models.AutoField(primary_key=True)
    orden_trabajo =  models.ForeignKey(OT , on_delete=models.SET_NULL, null=True)
    ruta =  models.ForeignKey(Ruta , on_delete=models.SET_NULL, null=True)
    equipo = models.ForeignKey(Equipo , on_delete=models.SET_NULL, null=True)
    id_componente = models.ForeignKey(Ruta_Equipo_Componente , on_delete=models.SET_NULL, null=True)
    componente =  models.CharField(max_length=50)
    condicion =   models.ForeignKey(Ruta_Condicion , on_delete=models.SET_NULL, null=True)
    unidad = models.ForeignKey(Unidad , on_delete=models.SET_NULL, null=True)
    puntos = models.IntegerField()
    ventana =  models.CharField(max_length=10)
    realizar_activo =  models.IntegerField()


    def __str__(self):
        return super().__str__()

class Checklist(models.Model):
    id_checklist = models.AutoField(primary_key=True)
    user_creador =  models.ForeignKey(Usuario , related_name='+', on_delete=models.SET_NULL, null=True)
    user_modificador = models.ForeignKey(Usuario , related_name='+', on_delete=models.SET_NULL, null=True)
    checklist_estatus = models.ForeignKey(EstatusUsuario , on_delete=models.SET_NULL, null=True)
    frecuencia = models.ForeignKey(Frecuencia , on_delete=models.SET_NULL, null=True)
    id_asignado = models.IntegerField()
    instalacion =  models.ForeignKey(Instalacion , on_delete=models.SET_NULL, null=True)
    checklist = models.CharField(max_length=50)
    checklist_codigo = models.CharField(max_length=30)
    checklist_creacion = models.CharField(max_length=10)
    checklist_cada = models.IntegerField()
    checklist_modificado = models.CharField(max_length=10)
    tipo_ot =  models.ForeignKey(Orden_Trabajo_Tipo , on_delete=models.SET_NULL, null=True)
    tipo_programa =  models.ForeignKey(Tipo_Programa , on_delete=models.SET_NULL, null=True)
    checklist_alcance = models.IntegerField()
    checklist_trabajadores = models.IntegerField()
    checklist_realizar_activo = models.IntegerField()
    tiempo_estimado = models.CharField(max_length=10)

    def __str__(self):
        return super().__str__()

class Checklist_Equipo(models.Model):
    id_checklist_equipo = models.AutoField(primary_key=True)
    checklist = models.ForeignKey(Checklist, on_delete=models.SET_NULL, null=True)
    equipo =  models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
    estatus_equipo = models.ForeignKey(Equipo_Estatus , on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return super().__str__()

class Orden_Trabajo_Ruta_Set_Point(models.Model):
    id_orden_trabajo_ruta_set_point = models.AutoField(primary_key=True)
    orden_trabajo_ruta = models.ForeignKey(Orden_Trabajo_Ruta, on_delete=models.SET_NULL, null=True)
    operador =  models.ForeignKey(Ruta_Set_Point_Operador, on_delete=models.SET_NULL, null=True)
    punto_a_base = models.IntegerField() 
    lectura = models.IntegerField() 
    punto_b_base = models.IntegerField() 
    modifico = models.IntegerField() 

    def __str__(self):
        return super().__str__()

class Checklist_Aspecto(models.Model):
    id_checklist_aspecto = models.AutoField(primary_key=True)
    checklist_aspecto = models.CharField(max_length=1000)
    checklist_equipo =  models.ForeignKey(Checklist_Equipo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Checklist_Instruccion(models.Model):
    id_checklist_instruccion = models.AutoField(primary_key=True)
    checklist_instruccion = models.CharField(max_length=1000)
    checklist_aspecto =  models.ForeignKey(Checklist_Aspecto, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Checklist_Aspecto_Copiado(models.Model):
    id_checklist_aspecto_copiado = models.AutoField(primary_key=True)
    equipo_base = models.ForeignKey(Equipo ,related_name='+', on_delete=models.SET_NULL, null=True)
    equipo_copia = models.ForeignKey(Equipo , related_name='+', on_delete=models.SET_NULL, null=True)
    usuario =  models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    hora = models.TimeField()
    notas = models.CharField(max_length=1000)

    def __str__(self):
        return super().__str__()

class Chk(models.Model):
    id_chk = models.AutoField(primary_key=True)
    id_checklist = models.ForeignKey(Checklist, on_delete=models.SET_NULL, null=True)
    chk_codigo =  models.CharField(max_length=10)
    checklist =  models.CharField(max_length=50)
    chk_fecha_creacion = models.DateField()
    chk_hora_creacion = models.TimeField()
    chk_estatus = models.ForeignKey(EstatusUsuario, on_delete=models.SET_NULL, null=True)
    chk_fecha_modificado = models.DateField()
    chk_hora_modificado = models.TimeField()
    chk_modificado_por = models.ForeignKey(Usuario , related_name='+', on_delete=models.SET_NULL, null=True)
    id_asignado = models.IntegerField()
    instalacion = models.ForeignKey(Instalacion, on_delete=models.SET_NULL, null=True)
    tipo_ot = models.ForeignKey(Orden_Trabajo_Tipo, on_delete=models.SET_NULL, null=True)
    tipo_programa = models.ForeignKey(Tipo_Programa, on_delete=models.SET_NULL, null=True)
    num_trabajadores = models.IntegerField()
    realizar_Activo = models.IntegerField()
    tiempo_estimado = models.IntegerField()

    def __str__(self):
        return super().__str__()

class Chk_Equipo(models.Model):
    id_chk_equipo = models.AutoField(primary_key=True)
    chk = models.ForeignKey(Chk, on_delete=models.SET_NULL, null=True)
    checklist_equipo =  models.ForeignKey(Checklist_Equipo, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return super().__str__()

class Chk_Aspecto(models.Model):
    id_chk_aspecto = models.AutoField(primary_key=True)
    chk_equipo = models.ForeignKey(Chk_Equipo, on_delete=models.SET_NULL, null=True)
    checklist_aspecto =  models.ForeignKey(Checklist_Aspecto, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return super().__str__()

class Chk_Instruccion(models.Model):
    id_chk_instruccion = models.AutoField(primary_key=True)
    chk_aspecto = models.ForeignKey(Chk_Aspecto, on_delete=models.SET_NULL, null=True)
    chk_instruccion = models.CharField(max_length=1000)
    chk_opcion = models.IntegerField()
    chk_comentarios = models.CharField(max_length=1000)
    chk_modificacion = models.IntegerField()
    chk_modifico = models.IntegerField()

    def __str__(self):
        return super().__str__()

class Orden_Trabajo_Checklist(models.Model):
    id_orden_trabajo_checklist = models.AutoField(primary_key=True)
    ot = models.ForeignKey(OT, on_delete=models.SET_NULL, null=True)
    chk = models.ForeignKey(Chk, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Dashboard_Ajuste(models.Model):
    id_dashboard_ajuste = models.AutoField(primary_key=True)
    dispo_1 = models.IntegerField()
    dispo_2 = models.IntegerField()
    dispo_3 = models.IntegerField()
    proa_1 = models.IntegerField()
    proa_2 = models.IntegerField()
    proa_3 = models.IntegerField()
    cump_1 = models.IntegerField()
    cump_2 = models.IntegerField()
    cump_3 = models.IntegerField()

    def __str__(self):
        return super().__str__()

class Dashboard_Mtbf(models.Model):
    id_dashboard_mtbf = models.AutoField(primary_key=True)
    id_mes = models.IntegerField()
    anio = models.IntegerField()
    ajuste = models.ForeignKey(Dashboard_Ajuste, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return super().__str__()

class Accion_Correctiva(models.Model):
    id_accion_correctiva = models.AutoField(primary_key=True)
    ot = models.ForeignKey(OT, on_delete=models.SET_NULL, null=True)
    comentarios = models.CharField(max_length=1000)
    
    def __str__(self):
        return super().__str__()

class Act_Equipo(models.Model):
    id_act_equipo = models.AutoField(primary_key=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
    descr_act = models.CharField(max_length=200)
    
    def __str__(self):
        return super().__str__()

class Causa_Raiz(models.Model):
    id_causa_raiz = models.AutoField(primary_key=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
    descripcion_causa_raiz = models.CharField(max_length=200)
    
    def __str__(self):
        return super().__str__()

class Cuenta_Cc(models.Model):
    id_cuenta_cc = models.AutoField(primary_key=True)
    centro_costos = models.ForeignKey(CentroCosto, on_delete=models.SET_NULL, null=True)
    cuenta_cc = models.CharField(max_length=20)
    descripcion_cuenta_cc = models.CharField(max_length=50)
    
    def __str__(self):
        return super().__str__()

class Empaque_Tipo(models.Model):
    id_empaque_tipo = models.AutoField(primary_key=True)
    empaque_tipo_es = models.CharField(max_length=50)
    empaque_tipo_en = models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()

class Empaque_Categoria(models.Model):
    id_empaque_categoria = models.AutoField(primary_key=True)
    empaque_categoria = models.CharField(max_length=120)
    empaque_categoria_estatus = models.ForeignKey(EstatusUsuario, on_delete=models.SET_NULL, null=True)
    empaque_categoria_notas = models.CharField(max_length=500)

    def __str__(self):
        return super().__str__()

class Empaque(models.Model):
    id_empaque = models.AutoField(primary_key=True)
    empaque = models.CharField(max_length=100)
    descripcion_empaque = models.CharField(max_length=1000)
    codigo_empaque = models.CharField(max_length=50)
    estatus_empaque= models.ForeignKey(EstatusUsuario, on_delete=models.SET_NULL, null=True)
    prioridad_empaque= models.ForeignKey(Orden_Trabajo_Prioridad, on_delete=models.SET_NULL, null=True)
    foto_empaque = models.CharField(max_length=200)
    empaque_categoria = models.ForeignKey(Empaque_Categoria, on_delete=models.SET_NULL, null=True)
    empaque_tipo = models.ForeignKey(Empaque_Tipo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Empaque_Stock_Entrada(models.Model):
    id_empaque_stock_entrada = models.AutoField(primary_key=True)
    empaque = models.ForeignKey(Empaque, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    fecha_orden = models.DateField()
    fecha_recibido = models.DateField()
    orden_compra =  models.CharField(max_length=50)
    cantidad_recibida = models.CharField(max_length=10)
    precio_unitario = models.CharField(max_length=10)
    embargado_a = models.IntegerField()
    user_entrada = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    cantidad_disponible = models.CharField(max_length=10)
    moneda = models.IntegerField()
    dolares = models.CharField(max_length=10)

    def __str__(self):
        return super().__str__()

class Empaque_Stock(models.Model):
    id_empaque_stock = models.AutoField(primary_key=True)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.SET_NULL, null=True)
    empaque = models.ForeignKey(Empaque, on_delete=models.SET_NULL, null=True)
    cantidad_actual = models.IntegerField()
    punto_reorden = models.IntegerField()
    pasillo =  models.CharField(max_length=50)
    columna = models.CharField(max_length=50)
    contenedor = models.CharField(max_length=50)
    user_stock = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    img_empaque = models.CharField(max_length=200)
    maxima = models.IntegerField()

    def __str__(self):
        return super().__str__()

class Empaque_Stock_Detalle(models.Model):
    id_empaque_stock_detalle = models.AutoField(primary_key=True)
    empaque = models.ForeignKey(Empaque, on_delete=models.SET_NULL, null=True)
    cuenta =  models.CharField(max_length=20)
    centro_costo = models.ForeignKey(CentroCosto, on_delete=models.SET_NULL, null=True)
    modelo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=50)
    notas_detalles = models.CharField(max_length=1000)
    unidad = models.ForeignKey(Unidad, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Empaque_Stock_Ajuste(models.Model):
    id_empaque_stock_ajuste = models.AutoField(primary_key=True)
    empaque_stock_entrada = models.ForeignKey(Empaque_Stock_Entrada, on_delete=models.SET_NULL, null=True)
    usuario_ajuste = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    fecha_ajuste = models.CharField(max_length=16)
    orden_compra_1 =   models.CharField(max_length=50)
    orden_compra_2 =   models.CharField(max_length=50)
    proveedor_1 = models.ForeignKey(Proveedor , related_name='+', on_delete=models.SET_NULL, null=True)
    proveedor_2 = models.ForeignKey(Proveedor , related_name='+', on_delete=models.SET_NULL, null=True)
    cantidad_disponible_1 = models.CharField(max_length=12)
    cantidad_disponible_2 = models.CharField(max_length=12)
    precio_unitario_1 = models.CharField(max_length=12)
    precio_unitario_2 = models.CharField(max_length=12)
    moneda_1 = models.IntegerField()
    moneda_2 = models.IntegerField()
    dolares_1 = models.CharField(max_length=12)
    dolares_2 = models.CharField(max_length=12)

    def __str__(self):
        return super().__str__()

class Empaque_Stock_Orden_Compra(models.Model):
    id_empaque_stock_orden_compra = models.AutoField(primary_key=True)
    empaque = models.ForeignKey(Empaque, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    fecha_orden = models.DateField()
    fecha_recibido = models.DateField()
    orden_compra =  models.CharField(max_length=50)
    cantidad_recibida = models.CharField(max_length=10)
    precio_unitario = models.CharField(max_length=10)
    embargado_a = models.IntegerField()
    user_entrada = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    cantidad_disponible = models.CharField(max_length=10)
    moneda = models.IntegerField()
    dolares = models.CharField(max_length=10)
    estatus = models.ForeignKey(EstatusUsuario, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return super().__str__()

class Empaque_Stock_Salida(models.Model):
    id_empaque_stock_salida = models.AutoField(primary_key=True)
    empaque = models.ForeignKey(Empaque, on_delete=models.SET_NULL, null=True)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.SET_NULL, null=True)
    fecha_salida = models.DateField()
    notas =  models.CharField(max_length=1000)
    cantidad_salida = models.IntegerField()
    precio_unitario = models.CharField(max_length=12)
    user_salida = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return super().__str__()

class Empaque_Vale(models.Model):
    id_empaque_vale = models.AutoField(primary_key=True)
    nombre_empaque =  models.CharField(max_length=20)    
    empaque = models.ForeignKey(Empaque, on_delete=models.SET_NULL, null=True)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.SET_NULL, null=True)
    solicitante = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    cantidad_solicitada = models.CharField(max_length=12)
    cantidad_surtida = models.CharField(max_length=12)
    parte_estatus = models.ForeignKey(Parte_Estatus, on_delete=models.SET_NULL, null=True)
    fecha_surtido = models.DateField()
    fecha_solicitado = models.DateField()
    
    def __str__(self):
        return super().__str__()

class Orden_Archivo(models.Model):
    id_orden_archivo = models.AutoField(primary_key=True)
    nombre_archivo =  models.CharField(max_length=50)    
    archivo = models.CharField(max_length=70)
    fecha = models.DateField()    
    comentarios = models.CharField(max_length=255)
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Orden_Inventario(models.Model):
    id_orden_inventario = models.AutoField(primary_key=True)
    nombre_archivo =  models.CharField(max_length=50)    
    archivo = models.CharField(max_length=70)
    fecha = models.DateField()    
    comentarios = models.CharField(max_length=255)
    inventario = models.ForeignKey(Inventario, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return super().__str__()

class Mes(models.Model):
    id_mes = models.AutoField(primary_key=True)
    mes_es =  models.CharField(max_length=20)    
    mes_en = models.CharField(max_length=20)
    mes_c_es =  models.CharField(max_length=3)    
    mes_c_en = models.CharField(max_length=3)
   

    def __str__(self):
        return super().__str__()

class Mantenimiento(models.Model): 
    id_mantenimiento = models.AutoField(primary_key=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
    instalacion = models.ForeignKey(Instalacion, on_delete=models.SET_NULL, null=True)
    mes = models.ForeignKey(Mes, on_delete=models.SET_NULL, null=True)
    total = models.CharField(max_length=12)

    def __str__(self):
        return super().__str__()

class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    menu_mx =  models.CharField(max_length=70)    
    menu_us = models.CharField(max_length=70)
    id = models.CharField(max_length=50)
    url = models.CharField(max_length=500)

    def __str__(self):
        return super().__str__()

class Parte(models.Model):
    id_parte = models.AutoField(primary_key=True)
    ot =  models.ForeignKey(OT, on_delete=models.SET_NULL, null=True)
    creador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    parte = models.CharField(max_length=50)
    cantidad_sugerida = models.CharField(max_length=12)
    cantidad_real = models.CharField(max_length=12)
    costo_individual = models.CharField(max_length=12)
    fecha_parte = models.DateField()    

    def __str__(self):
        return super().__str__()

class Prob_Equipo(models.Model):
    id_prob_equipo = models.AutoField(primary_key=True)
    equipo =  models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
    codigo_prob_equipo = models.CharField(max_length=11)
    descripcion_prob_equipo = models.CharField(max_length=200)

    def __str__(self):
        return super().__str__()

class Requisicion_Estatus(models.Model):
    id_requisicion_estatus = models.AutoField(primary_key=True)
    requisicion_estatus_es = models.CharField(max_length=20)
    requisicion_estatus_en = models.CharField(max_length=20)

    def __str__(self):
        return super().__str__()

class Requisicion(models.Model):
    id_requisicion = models.AutoField(primary_key=True)
    requisitor =  models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    requisicion_estatus = models.ForeignKey(Requisicion_Estatus, on_delete=models.SET_NULL, null=True)
    departamento_solicitante = models.CharField(max_length=50)
    maquina_usarse = models.CharField(max_length=50)
    centro_costos = models.CharField(max_length=50)
    requisicion = models.CharField(max_length=50)
    requisicion_descripcion = models.CharField(max_length=500)    
    proveedor_principal = models.CharField(max_length=50)
    proveedor_alterno = models.CharField(max_length=50)
    numero_parte_proveedor = models.CharField(max_length=50)
    costo = models.CharField(max_length=12)
    tiempo_entrega = models.CharField(max_length=50)
    maximo = models.IntegerField()
    punto_reorden = models.IntegerField()
    fecha_creacion = models.DateField()
    responde = models.IntegerField()
    fecha_respuesta = models.CharField(max_length=10)

    def __str__(self):
        return super().__str__()

class Satisfaccion(models.Model):
    id_satisfaccion = models.AutoField(primary_key=True)
    ot =  models.ForeignKey(OT, on_delete=models.SET_NULL, null=True)
    requisitor = models.ForeignKey(Usuario , related_name='+', on_delete=models.SET_NULL, null=True)
    folio = models.CharField(max_length=20)
    fecha_completado = models.CharField(max_length=16)
    fecha_satisfaccion = models.CharField(max_length=16)
    user_completo = models.ForeignKey(Usuario , related_name='+', on_delete=models.SET_NULL, null=True)
    satisfaccion = models.IntegerField()
    comentarios = models.CharField(max_length=2000)

    def __str__(self):
        return super().__str__()

class Submenu(models.Model):
    id_submenu = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    submenu_mx =  models.CharField(max_length=70)    
    submenu_us = models.CharField(max_length=70)
    url = models.CharField(max_length=500)

    def __str__(self):
        return super().__str__()

class Suscripcion(models.Model):
    id_suscripcion = models.AutoField(primary_key=True)
    nivel =  models.CharField(max_length=20)    
    usuarios  = models.IntegerField()

    def __str__(self):
        return super().__str__()

class Token(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    hash =  models.CharField(max_length=2000)    

    def __str__(self):
        return super().__str__()

class Usuario_A(models.Model):
    id_usuario_a = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)  
    usuario  = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)  
    fecha = models.DateField()
    hora = models.TimeField()
    alertas = models.IntegerField()
    nota_2 = models.CharField(max_length=45)   
    nota_3 = models.CharField(max_length=45)    
    nota_4 = models.CharField(max_length=45)    
    nota_5 = models.CharField(max_length=45)    
    nota_6 = models.CharField(max_length=45)    
    nota_7 = models.CharField(max_length=45)     

    def __str__(self):
        return super().__str__()

class Criticidad(models.Model):
    id_criticidad = models.AutoField(primary_key=True)
    criticidad_es = models.CharField(max_length=50)  
    criticidad_en  = models.CharField(max_length=50)      

    def __str__(self):
        return super().__str__()

class Estado_Material(models.Model):
    id_estado_material = models.AutoField(primary_key=True)
    estado_material_es = models.CharField(max_length=50)  
    estado_material_en  = models.CharField(max_length=50)      

    def __str__(self):
        return super().__str__()

class Estado_Paquete(models.Model):
    id_estado_paquete = models.AutoField(primary_key=True)
    estado_paquete_es = models.CharField(max_length=50)  
    estado_paquete_en  = models.CharField(max_length=50)      

    def __str__(self):
        return super().__str__()

class Estado_Sello(models.Model):
    id_estado_sello = models.AutoField(primary_key=True)
    estado_sello_es = models.CharField(max_length=50)  
    estado_sello_en  = models.CharField(max_length=50)      

    def __str__(self):
        return super().__str__()

class Giro(models.Model):
    id_giro = models.AutoField(primary_key=True)
    giro = models.CharField(max_length=50)  
    codigo_giro  = models.CharField(max_length=50)      

    def __str__(self):
        return super().__str__()

class Nivel_Mro(models.Model):
    id_nivel_mro = models.AutoField(primary_key=True)
    nivel_es = models.CharField(max_length=50)  
    nivel_en  = models.CharField(max_length=50)      

    def __str__(self):
        return super().__str__()

class Nivel_Gastos(models.Model):
    id_nivel_gastos = models.AutoField(primary_key=True)
    gastos_es = models.CharField(max_length=50)  
    gastos_en  = models.CharField(max_length=50)      

    def __str__(self):
        return super().__str__()

class Orden_De_Compra_Estado(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=45)  
    clave  = models.CharField(max_length=45)      

    def __str__(self):
        return super().__str__()

class Orden_De_Compra_Accion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_accion = models.CharField(max_length=45)  
    clave_accion  = models.CharField(max_length=45) 
    estado =    models.ForeignKey(Orden_De_Compra_Estado, on_delete=models.SET_NULL, null=True)    

    def __str__(self):
        return super().__str__()

class Orden_De_Compra_Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    proveedor = models.CharField(max_length=60)  
    calle  = models.CharField(max_length=45) 
    colonia  = models.CharField(max_length=45) 
    cp  = models.CharField(max_length=45) 
    municipio  = models.CharField(max_length=45) 
    estado  = models.CharField(max_length=45) 
    pais  = models.CharField(max_length=45) 
    razon_social  = models.CharField(max_length=70) 
    rfc  = models.CharField(max_length=20) 
    telefono  = models.CharField(max_length=20) 
    contacto  = models.CharField(max_length=20) 
    email  = models.CharField(max_length=45) 
    pagina_web  = models.CharField(max_length=45) 
    foto_proveedor  = models.CharField(max_length=200) 
    estatus_proveedor =  models.ForeignKey(EstatusUsuario, on_delete=models.SET_NULL, null=True)   
    numero_proveedor  = models.CharField(max_length=45) 
    moneda = models.IntegerField()

    def __str__(self):
        return super().__str__()

class Orden_De_Compra(models.Model):
    id = models.AutoField(primary_key=True)
    id_visible_orden_de_compra = models.CharField(max_length=45)  
    accion = models.IntegerField()
    usuario_elabora =  models.ForeignKey(Usuario, related_name='+', on_delete=models.SET_NULL, null=True)   
    fecha_emitido  = models.CharField(max_length=45) 
    hora_emitido  = models.CharField(max_length=45) 
    fecha_deadline  = models.CharField(max_length=45) 
    hora_deadline  = models.CharField(max_length=45) 
    proveedor = models.ForeignKey(Orden_De_Compra_Proveedor, on_delete=models.SET_NULL, null=True) 
    producto_servicio = models.IntegerField()
    sub_total = models.IntegerField()
    procentaje_iva = models.IntegerField()
    iva = models.IntegerField()
    gran_total = models.IntegerField()
    explicativo = models.CharField(max_length=150) 
    fecha_salida_por_oc  = models.CharField(max_length=45) 
    hora_salida_por_oc  = models.CharField(max_length=45) 
    fecha_ingreso_por_oc  = models.CharField(max_length=45) 
    hora_ingreso_por_oc  = models.CharField(max_length=45) 
    tipo_cambio = models.IntegerField()
    comprador_asignado = models.IntegerField()
    criticidad = models.IntegerField()
    linea_caida = models.IntegerField()
    solicitante = models.ForeignKey(Usuario, related_name='+', on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return super().__str__()

class Orden_De_Compra_Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)  
    cantidad = models.IntegerField()
    cantidad_recibida = models.IntegerField()
    unidad =  models.ForeignKey(Unidad, on_delete=models.SET_NULL, null=True)   
    precio  = models.IntegerField() 
    oc_moneda = models.IntegerField()
    total = models.IntegerField()
    compra =  models.ForeignKey(Orden_De_Compra, on_delete=models.SET_NULL, null=True)   
    
    def __str__(self):
        return super().__str__()

class Orden_De_Compra_Cotizacion_Producto(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=45)  
    precio = models.IntegerField()
    moneda = models.IntegerField()
    precio_divisa =  models.IntegerField()
    total  = models.IntegerField() 
    fk_oc_cotizacion = models.IntegerField()
    
    def __str__(self):
        return super().__str__()

class Orden_De_Compra_Archivo(models.Model):
    id_orden_compra_archivo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)  
    archivo = models.CharField(max_length=50) 
    orden_compra = models.ForeignKey(Orden_De_Compra, on_delete=models.SET_NULL, null=True)   
    fecha = models.CharField(max_length=20) 
    usuario  = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)   
    producto_oc = models.ForeignKey(Orden_De_Compra_Producto, on_delete=models.SET_NULL, null=True)   
    
    def __str__(self):
        return super().__str__()

class Orden_De_Compra_Archivo_Proveedor(models.Model):
    id_orden_compra_archivo_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)  
    archivo = models.CharField(max_length=50) 
    orden_compra = models.ForeignKey(Orden_De_Compra, on_delete=models.SET_NULL, null=True)   
    fecha = models.CharField(max_length=20) 
    usuario  = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)   
    proveedor_oc = models.ForeignKey(Orden_De_Compra_Proveedor, on_delete=models.SET_NULL, null=True)   
    
    def __str__(self):
        return super().__str__()

class Orden_De_Compra_Cotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_cotizacion  = models.CharField(max_length=45) 
    hora_cotizacion  = models.CharField(max_length=45) 
    productos = models.IntegerField()
    tipo_de_pago = models.IntegerField()
    porcentaje_descuento = models.IntegerField()
    descuento = models.IntegerField()
    porcentaje_iva = models.IntegerField()
    iva = models.IntegerField()
    sub_total = models.IntegerField()
    total = models.IntegerField()
    observaciones = models.CharField(max_length=255)
    oc = models.ForeignKey(Orden_De_Compra, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(Orden_De_Compra_Proveedor, on_delete=models.SET_NULL, null=True)   
    accion = models.IntegerField()
    deadline_prov  = models.CharField(max_length=50)
    motivo_elim  = models.CharField(max_length=255)  

    def __str__(self):
        return super().__str__()

class Orden_De_Compra_Archivo_Costo(models.Model):
    id = models.AutoField(primary_key=True)
    importe = models.CharField(max_length=50)  
    realizado_por = models.CharField(max_length=50) 
    fecha_realizado = models.CharField(max_length=45) 
    hora_realizado = models.CharField(max_length=45) 
    oc  = models.ForeignKey(Orden_De_Compra, on_delete=models.SET_NULL, null=True)   
    oc_cot = models.ForeignKey(Orden_De_Compra_Cotizacion, on_delete=models.SET_NULL, null=True)   
    
    def __str__(self):
        return super().__str__()

class Orden_De_Compra_Email_Visto(models.Model):
    orden_de_compra_email_visto = models.AutoField(primary_key=True)
    oc  = models.ForeignKey(Orden_De_Compra, on_delete=models.SET_NULL, null=True)   
    prov = models.ForeignKey(Orden_De_Compra_Proveedor, on_delete=models.SET_NULL, null=True)   
    estado = models.IntegerField()
    
    def __str__(self):
        return super().__str__()

class Orden_De_Compra_Historial(models.Model):
    id = models.AutoField(primary_key=True)
    usuario  = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)   
    estado = models.ForeignKey(Orden_De_Compra_Estado, on_delete=models.SET_NULL, null=True)   
    oc = models.ForeignKey(Orden_De_Compra, on_delete=models.SET_NULL, null=True)   
    accion = models.ForeignKey(Orden_De_Compra_Accion, on_delete=models.SET_NULL, null=True) 
    fecha = models.CharField(max_length=45)
    hora = models.CharField(max_length=45)
    timestamp = models.CharField(max_length=45)

    def __str__(self):
        return super().__str__()

class Orden_De_Compra_Mensaje(models.Model):
    id = models.AutoField(primary_key=True)
    oc = models.ForeignKey(Orden_De_Compra, on_delete=models.SET_NULL, null=True)   
    oc_prov = models.ForeignKey(Orden_De_Compra_Proveedor, on_delete=models.SET_NULL, null=True) 
    mensaje = models.CharField(max_length=255)
    timestamp = models.CharField(max_length=45)
    
    def __str__(self):
        return super().__str__()

class Orden_De_Compra_Presupuesto(models.Model):
    id = models.AutoField(primary_key=True)
    id_fiscal = models.CharField(max_length=45)
    usuario_autoriza_presupuesto = models.ForeignKey(Usuario ,related_name='+', on_delete=models.SET_NULL, null=True)   
    usuario_solicita_presupuesto = models.ForeignKey(Usuario , related_name='+', on_delete=models.SET_NULL, null=True) 
    fecha_presupuesto = models.CharField(max_length=45)
    plazo_presupuesto = models.CharField(max_length=45)
    importe = models.CharField(max_length=45)
    
    def __str__(self):
        return super().__str__()