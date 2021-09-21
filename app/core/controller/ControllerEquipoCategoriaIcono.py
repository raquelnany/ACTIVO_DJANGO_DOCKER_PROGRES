from ..serializers import EquipoCategoriaIconoSerializaer
from ..models import Equipo_Categoria_Icono,Equipo_Categoria, Modelo_Icono


class ControllerEquipoCategoriaIcono:
    def crearequipocategoriaicono(request):
        datosEquipoCategoriaIcono = request.data
        try:
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=datosEquipoCategoriaIcono['equipo_categoria'])
            modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=datosEquipoCategoriaIcono['modelo_icono'])
            equipoCategoriaIconoNuevo = Equipo_Categoria_Icono.objects.create(
                equipo_categoria= equipo_categoria,
                modelo_icono = modelo_icono,
            )
        except Exception:
             return {"estatus":"Error"}

        equipoCategoriaIconoNuevo.save()
        return {"estatus":"Ok", 'equipo_categoria_icono:': equipoCategoriaIconoNuevo.id_equipo_categoria_icono}

    def listarequipocategoriaicono(id_equipo_categoria_icono=None):
        if id_equipo_categoria_icono:
            try:
                queryset = Equipo_Categoria_Icono.objects.get(id_equipo_categoria_icono=id_equipo_categoria_icono)
            except Equipo_Categoria_Icono.DoesNotExist:
                return ({'result': 'No se encontró el equipo categoria icono'})
            serializer = EquipoCategoriaIconoSerializaer(queryset)
            return serializer.data
        else:
            queryset = Equipo_Categoria_Icono.objects.all()
            serializer = EquipoCategoriaIconoSerializaer(queryset, many=True)
            return serializer.data

    def generarequipocategoriaIcono(self):
        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=3),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=9)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=3),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=9)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=3),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=3),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=19)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=3),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=20)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=3),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=21)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=1),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=1)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=1),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=3)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=1),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=5)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=1),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=1),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=13)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=1),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=17)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=2),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=2)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=2),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=4)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=2),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=6)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=2),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=7)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=2),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=2),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=22)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=2),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=14)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=2),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=23)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=2),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=18)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=4),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=5),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=6),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=7),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=8),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=9),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=10),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=11),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=12),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=13),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=14),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()

        EQI=Equipo_Categoria_Icono.objects.create(
           equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria=15),
           modelo_icono = Modelo_Icono.objects.get(id_modelo_icono=10)
        )
        EQI.save()