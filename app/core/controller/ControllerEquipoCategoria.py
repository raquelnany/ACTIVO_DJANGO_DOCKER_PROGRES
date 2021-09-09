from ..serializers import EquipoCategoriaSerializer
from ..models import Equipo_Categoria, Equipo_Categoria_Estatus


class ControllerEquipoCategoria:

    def crearequipocategoria(request):
        datosEquipoCategoria = request.data
        EquipoCategoriaNuevo = Equipo_Categoria()
        try:
           estatus = Equipo_Categoria_Estatus.objects.get(id_equipo_categoria_estatus=datosEquipoCategoria['estatus'])
           EquipoCategoriaNuevo = Equipo_Categoria.objects.create(
            equipo_categoria_en = datosEquipoCategoria['equipo_categoria_en'],
            equipo_categoria_es = datosEquipoCategoria['equipo_categoria_es'],
            equipo_categoria_clave_en = datosEquipoCategoria['equipo_categoria_clave_en'],
            equipo_categoria_clave_es = datosEquipoCategoria['equipo_categoria_clave_es'],
            estatus = estatus,
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'equipo_categoria': EquipoCategoriaNuevo.equipo_categoria_es}

    def listarequipocategoria(id_equipo_categoria=None):
        if id_equipo_categoria:
            try:
                queryset = Equipo_Categoria.objects.get(id_equipo_categoria=id_equipo_categoria)
            except Equipo_Categoria_Estatus.DoesNotExist:
                return ({'result': 'No se encontró la categoria de equipo deseadas'})
            serializer = EquipoCategoriaSerializer(queryset)
            return serializer.data
        else:
            queryset = Equipo_Categoria.objects.all()
            serializer = EquipoCategoriaSerializer(queryset, many=True)
            return serializer.data

    def generarequipocategoria(self):
        estatusInactivo = Equipo_Categoria_Estatus.objects.get(id_equipo_categoria_estatus=1)
        estatusActivo = Equipo_Categoria_Estatus.objects.get(id_equipo_categoria_estatus=2)

        RTT=Equipo_Categoria.objects.create(
           equipo_categoria_en='Rotating',
           equipo_categoria_es='Rotativas',
           equipo_categoria_clave_en='RTT',
           equipo_categoria_clave_es='RTT',
           estatus = estatusActivo
        )
        RTT.save()

        MCH=Equipo_Categoria.objects.create(
           equipo_categoria_en='Mechanical',
           equipo_categoria_es='Mecanicas',
           equipo_categoria_clave_en='MCH',
           equipo_categoria_clave_es='MCN',
           estatus = estatusActivo
        )
        MCH.save()

        ELC=Equipo_Categoria.objects.create(
           equipo_categoria_en='Electrical',
           equipo_categoria_es='Electricas',
           equipo_categoria_clave_en='ELC',
           equipo_categoria_clave_es='ELC',
           estatus = estatusActivo
        )
        ELC.save()       

        SFC=Equipo_Categoria.objects.create(
           equipo_categoria_en='Safety and Control',
           equipo_categoria_es='Seguridad y Control',
           equipo_categoria_clave_en='SFC',
           equipo_categoria_clave_es='SGC',
           estatus = estatusActivo
        )
        SFC.save()

        SBP=Equipo_Categoria.objects.create(
           equipo_categoria_en='Subsea Production',
           equipo_categoria_es='Producción Submarina',
           equipo_categoria_clave_en='SBP',
           equipo_categoria_clave_es='PRS',
           estatus = estatusActivo
        )
        SBP.save()

        DLL=Equipo_Categoria.objects.create(
           equipo_categoria_en='Drilling',
           equipo_categoria_es='Perforación',
           equipo_categoria_clave_en='DLL',
           equipo_categoria_clave_es='PRF',
           estatus = estatusActivo
        )
        DLL.save()

        WLC=Equipo_Categoria.objects.create(
           equipo_categoria_en='Well Completion (Downhole)',
           equipo_categoria_es='Equipo de Completación',
           equipo_categoria_clave_en='WLC',
           equipo_categoria_clave_es='',
           estatus = estatusActivo
        )
        WLC.save()

        WLI=Equipo_Categoria.objects.create(
           equipo_categoria_en='Well Intervention',
           equipo_categoria_es='Intervención de Pozo',
           equipo_categoria_clave_en='WLI',
           equipo_categoria_clave_es='',
           estatus = estatusActivo
        )
        WLI.save()

        MRN=Equipo_Categoria.objects.create(
           equipo_categoria_en='Marine',
           equipo_categoria_es='Marina',
           equipo_categoria_clave_en='MRN',
           equipo_categoria_clave_es='MRN',
           estatus = estatusActivo
        )
        MRN.save()

        UTL=Equipo_Categoria.objects.create(
           equipo_categoria_en='Utilities',
           equipo_categoria_es='Utilidades',
           equipo_categoria_clave_en='UTL',
           equipo_categoria_clave_es='UTL',
           estatus = estatusActivo
        )
        UTL.save()

        PN=Equipo_Categoria.objects.create(
           equipo_categoria_en='Pneumatic',
           equipo_categoria_es='Neumatica',
           equipo_categoria_clave_en='PN',
           equipo_categoria_clave_es='PN',
           estatus = estatusInactivo
        )
        PN.save()

        HD=Equipo_Categoria.objects.create(
           equipo_categoria_en='Hidraulic',
           equipo_categoria_es='Hidraulica',
           equipo_categoria_clave_en='HD',
           equipo_categoria_clave_es='HD',
           estatus = estatusInactivo
        )
        HD.save()

        PL=Equipo_Categoria.objects.create(
           equipo_categoria_en='Assembly Line',
           equipo_categoria_es='Linea de Ensamble',
           equipo_categoria_clave_en='PL',
           equipo_categoria_clave_es='LP',
           estatus = estatusInactivo
        )
        PL.save()

        ST=Equipo_Categoria.objects.create(
           equipo_categoria_en='Systems',
           equipo_categoria_es='Sistemas',
           equipo_categoria_clave_en='ST',
           equipo_categoria_clave_es='ST',
           estatus = estatusActivo
        )
        ST.save()
        