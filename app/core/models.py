import binascii
import os
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
    herramienta_costo = models.DecimalField(10,2)

    def __str__(self):
        return super().__str__()

class Herramienta_Historial(models.Model):
    id_herramienta_historial = models.AutoField(primary_key=True)
    herramienta= models.ForeignKey(Herramienta, on_delete=models.SET_NULL, null=True)
    herramienta_movimiento = models.ForeignKey(Herramienta_Movimiento, on_delete=models.SET_NULL, null=True)
    fecha_movimiento = models.DateField()
    notas_herramienta = models.CharField(max_length=1000)
    solicitante = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
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

