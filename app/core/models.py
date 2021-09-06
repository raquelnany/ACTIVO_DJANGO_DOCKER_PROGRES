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