from ..serializers import Clase_Equipo, ClaseEquipoSerializer
from ..models import Equipo_Categoria, Clase_Equipo


class ControllerClaseEquipo:

    def crearclaseequipo(request):
        datosClaseEquipo = request.data
        try:
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = datosClaseEquipo['equipo_categoria'])
            claseEquipoNuevo = Clase_Equipo.objects.create(
            clase_equipo_en = datosClaseEquipo['clase_equipo_en'],
            clase_equipo_es = datosClaseEquipo['clase_equipo_es'],
            codigo_clase = datosClaseEquipo['codigo_clase'],
            equipo_categoria = equipo_categoria,
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'clase_equipo': claseEquipoNuevo.clase_equipo_en}

    def listarclaseequipo(id_clase_equipo=None):
        if id_clase_equipo:
            try:
                queryset = Clase_Equipo.objects.get(id_clase_equipo=id_clase_equipo)
            except Clase_Equipo.DoesNotExist:
                return ({'result': 'No se encontró la clase de equipo deseada'})
            serializer = ClaseEquipoSerializer(queryset)
            return serializer.data
        else:
            queryset = Clase_Equipo.objects.all()
            serializer = ClaseEquipoSerializer(queryset, many=True)
            return serializer.data

    def generarclaseequipo(self):

        CE = Equipo_Categoria.objects.create(
            clase_equipo_en = "Combustion Engines",
            clase_equipo_es = "Máquinas de Combustión",
            codigo_clase = "CE",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 1),
        )
        CE.save()

        CO= Equipo_Categoria.objects.create(
            clase_equipo_en = "Compressors",
            clase_equipo_es = "Compresores",
            codigo_clase = "CO",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 1),
        )
        CO.save()

        EG= Equipo_Categoria.objects.create(
            clase_equipo_en = "Electric Generators",
            clase_equipo_es = "Generadores Eléctricos",
            codigo_clase = "EG",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 1),
        )
        EG.save()

        EM = Equipo_Categoria.objects.create(
            clase_equipo_en = "Electric Motors",
            clase_equipo_es = "Motores Eléctricos",
            codigo_clase = "EM",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 1),
        )
        EM.save()

        GT = Equipo_Categoria.objects.create(
            clase_equipo_en = "Gas Turbines",
            clase_equipo_es = "Turbinas de Gas",
            codigo_clase = "GT",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 1),
        )
        GT.save()

        PU = Equipo_Categoria.objects.create(
            clase_equipo_en = "Pumps",
            clase_equipo_es = "Bombas",
            codigo_clase = "PU",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 1),
        )
        PU.save()

        ST = Equipo_Categoria.objects.create(
            clase_equipo_en = "Steam Turbines",
            clase_equipo_es = "Turbinas de Vapor",
            codigo_clase = "ST",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 1),
        )
        ST.save()

        TE = Equipo_Categoria.objects.create(
            clase_equipo_en = "Turboexpanders",
            clase_equipo_es = "Turboexpansores",
            codigo_clase = "TE",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 1),
        )
        TE.save()

        BF = Equipo_Categoria.objects.create(
            clase_equipo_en = "Blowers and fans",
            clase_equipo_es = "Sopladores y Ventiladores",
            codigo_clase = "BF",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 1),
        )
        BF.save()

        EX = Equipo_Categoria.objects.create(
            clase_equipo_en = "Liquid Expanders",
            clase_equipo_es = "Expansor de Líquidos",
            codigo_clase = "EX",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 1),
        )
        EX.save()

        MX = Equipo_Categoria.objects.create(
            clase_equipo_en = "Mixers",
            clase_equipo_es = "Mezcladoras",
            codigo_clase = "MX",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 1),
        )
        MX.save()

        CR = Equipo_Categoria.objects.create(
            clase_equipo_en = "Cranes",
            clase_equipo_es = "Grúas",
            codigo_clase = "CR",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 2),
        )
        CR.save()

        HE= Equipo_Categoria.objects.create(
            clase_equipo_en = "Heat Exchangers",
            clase_equipo_es = "Intercambiadores de Calor",
            codigo_clase = "HE",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 2),
        )
        HE.save()

        HB = Equipo_Categoria.objects.create(
            clase_equipo_en = "Heaters and Boilers",
            clase_equipo_es = "Calderas y Calentadores",
            codigo_clase = "HB",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 2),
        )
        HB.save()

        VE = Equipo_Categoria.objects.create(
            clase_equipo_en = "Vessels",
            clase_equipo_es = "Contenedores",
            codigo_clase = "VE",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 2),
        )
        VE.save()

        PI = Equipo_Categoria.objects.create(
            clase_equipo_en = "General",
            clase_equipo_es = "General",
            codigo_clase = "PI",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 2),
        )
        PI.save()

        WI = Equipo_Categoria.objects.create(
            clase_equipo_en = "Winches",
            clase_equipo_es = "Malacates",
            codigo_clase = "WI",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 2),
        )
        WI.save()

        ST = Equipo_Categoria.objects.create(
            clase_equipo_en = "Storage Tanks",
            clase_equipo_es = "Tanques de Almacenamiento",
            codigo_clase = "ST",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 2),
        )
        ST.save()

        FS = Equipo_Categoria.objects.create(
            clase_equipo_en = "Filters and Strainers",
            clase_equipo_es = "Filtros y Coladores",
            codigo_clase = "FS",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 2),
        )
        FS.save()

        PS= Equipo_Categoria.objects.create(
            clase_equipo_en = "Power Supply",
            clase_equipo_es = "Fuente de EnergÍa",
            codigo_clase = "PS",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 3),
        )
        PS.save()

        TR = Equipo_Categoria.objects.create(
            clase_equipo_en = "Power transformers",
            clase_equipo_es = "Transformadores",
            codigo_clase = "TR",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 3),
        )
        TR.save()

        TD = Equipo_Categoria.objects.create(
            clase_equipo_en = "Distribution Boards",
            clase_equipo_es = "Tableros de Distribución",
            codigo_clase = "TD",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 3),
        ) 
        TD.save()

        FC = Equipo_Categoria.objects.create(
            clase_equipo_en = "Frequency Converters",
            clase_equipo_es = "Convertidores de Frecuencia",
            codigo_clase = "FC",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 3),
        )
        FC.save()

        CB = Equipo_Categoria.objects.create(
            clase_equipo_en = "Power Cables",
            clase_equipo_es = "Cables de Energí­a",
            codigo_clase = "CB",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 3),
        )
        CB.save()

        CPB = Equipo_Categoria.objects.create(
            clase_equipo_en = "Capacitors Bank",
            clase_equipo_es = "Banco de Capacitores",
            codigo_clase = "CPB",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 3),
        )
        CPB.save()

        FD = Equipo_Categoria.objects.create(
            clase_equipo_en = "Fire and gas detectors",
            clase_equipo_es = "Detectores de gas y fuego",
            codigo_clase = "FS",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 4),
        )
        FD.save()

        VV = Equipo_Categoria.objects.create(
            clase_equipo_en = "Valves",
            clase_equipo_es = "Válvulas",
            codigo_clase = "VV",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 4),
        )
        VV.save()

        FF = Equipo_Categoria.objects.create(
            clase_equipo_en = "Fire-fighting Equipment",
            clase_equipo_es = "Equipo Contra Incendio",
            codigo_clase = "FF",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 4),
        )
        FF.save()

        NZ = Equipo_Categoria.objects.create(
            clase_equipo_en = "Nozzles",
            clase_equipo_es = "Boquillas",
            codigo_clase = "NZ",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 4),
        )
        NZ.save()

        CU= Equipo_Categoria.objects.create(
            clase_equipo_en = "Control Unit",
            clase_equipo_es = "Unidad de Control",
            codigo_clase = "CU",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 4),
        ) 
        CU.save()

        VV = Equipo_Categoria.objects.create(
            clase_equipo_en = "Valves",
            clase_equipo_es = "Válvulas",
            codigo_clase = "VV",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 2),
        )
        VV.save()

        EVV = Equipo_Categoria.objects.create(
            clase_equipo_en = "Electrovalves",
            clase_equipo_es = "Electoválvulas",
            codigo_clase = "EVV",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 12),
        )
        EVV.save()

        VV = Equipo_Categoria.objects.create(
            clase_equipo_en = "Valves",
            clase_equipo_es = "Válvulas",
            codigo_clase = "VV",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 13),
        )
        VV.save()

        CY = Equipo_Categoria.objects.create(
            clase_equipo_en = "Cylenders",
            clase_equipo_es = "Cilindros",
            codigo_clase = "CY",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 12),
        )
        CY.save()

        EVV= Equipo_Categoria.objects.create(
            clase_equipo_en = "Electrovalves",
            clase_equipo_es = "Electoválvulas",
            codigo_clase = "EVV",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 13),
        )
        EVV.save()

        VV = Equipo_Categoria.objects.create(
            clase_equipo_en = "Valves",
            clase_equipo_es = "Válvulas",
            codigo_clase = "VV",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 13),
        )
        VV.save()

        CY = Equipo_Categoria.objects.create(
            clase_equipo_en = "Cylenders",
            clase_equipo_es = "Cilindros",
            codigo_clase = "CY",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 13),
        )
        CY.save()

        HY = Equipo_Categoria.objects.create(
            clase_equipo_en = "Hydraulic Power Units",
            clase_equipo_es = "Unidad Hidráulica",
            codigo_clase = "HY",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 10),
        )
        HY.save()

        AS = Equipo_Categoria.objects.create(
            clase_equipo_en = "Air-Supply Equipment",
            clase_equipo_es = "Suministro de Aire",
            codigo_clase = "AS",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 10),
        )
        AS.save()

        NI = Equipo_Categoria.objects.create(
            clase_equipo_en = "Nitrogen-Supply Equipment",
            clase_equipo_es = "Suministro de Nitrógeno",
            codigo_clase = "NI",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 10),
        )
        NI.save()

        BO = Equipo_Categoria.objects.create(
            clase_equipo_en = "Boiler",
            clase_equipo_es = "Caldera",
            codigo_clase = "BO",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 10),
        )
        BO.save()

        CT = Equipo_Categoria.objects.create(
            clase_equipo_en = "Cooling Tower",
            clase_equipo_es = "Torre de Enfriamiento",
            codigo_clase = "CT",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 10),
        )
        CT.save()

        CH = Equipo_Categoria.objects.create(
            clase_equipo_en = "Chiller",
            clase_equipo_es = "Enfriador",
            codigo_clase = "CH",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 10),
        )
        CH.save()

        HVAC = Equipo_Categoria.objects.create(
            clase_equipo_en = "HVACs",
            clase_equipo_es = "Manejadoras de Aire",
            codigo_clase = "HVAC",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 10),
        )
        HVAC.save()

        SE = Equipo_Categoria.objects.create(
            clase_equipo_en = "Electric Substation",
            clase_equipo_es = "Subestacion Eléctrica",
            codigo_clase = "SE",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 10),
        )
        SE.save()

        WA= Equipo_Categoria.objects.create(
            clase_equipo_en = "Water Treatment",
            clase_equipo_es = "Tratamiento de Agua",
            codigo_clase = "WA",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 10),
        )
        WA.save()
               
        GN = Equipo_Categoria.objects.create(
            clase_equipo_en = "General",
            clase_equipo_es = "General",
            codigo_clase = "GN",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 5),
        )
        GN.save()

        GN = Equipo_Categoria.objects.create(
            clase_equipo_en = "General",
            clase_equipo_es = "General",
            codigo_clase = "GN",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 6),
        )
        GN.save()

        GN = Equipo_Categoria.objects.create(
            clase_equipo_en = "General",
            clase_equipo_es = "General",
            codigo_clase = "GN",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 7),
        )
        GN.save()

        GN = Equipo_Categoria.objects.create(
            clase_equipo_en = "General",
            clase_equipo_es = "General",
            codigo_clase = "GN",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 8),
        )
        GN.save()

        GN= Equipo_Categoria.objects.create(
            clase_equipo_en = "General",
            clase_equipo_es = "General",
            codigo_clase = "GN",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 9),
        )
        GN.save()

        GN = Equipo_Categoria.objects.create(
            clase_equipo_en = "General",
            clase_equipo_es = "General",
            codigo_clase = "GN",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 14),
        )
        GN.save()

        IM = Equipo_Categoria.objects.create(
            clase_equipo_en = "Printer",
            clase_equipo_es = "Impresora",
            codigo_clase = "IM",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 15),
        )
        IM.save()

        PC = Equipo_Categoria.objects.create(
            clase_equipo_en = "PC",
            clase_equipo_es = "PC",
            codigo_clase = "PC",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 15),
        )
        PC.save()

        LT = Equipo_Categoria.objects.create(
            clase_equipo_en = "Laptop",
            clase_equipo_es = "Laptop",
            codigo_clase = "LT",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 15),
        ) 
        LT.save()

        DP = Equipo_Categoria.objects.create(
            clase_equipo_en = "Display",
            clase_equipo_es = "Monitor",
            codigo_clase = "DP",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 15),
        )
        DP.save()

        TV = Equipo_Categoria.objects.create(
            clase_equipo_en = "TV",
            clase_equipo_es = "TV",
            codigo_clase = "TV",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 15),
        )
        TV.save()

        PY = Equipo_Categoria.objects.create(
            clase_equipo_en = "Projector",
            clase_equipo_es = "Projector",
            codigo_clase = "PY",
            equipo_categoria = Equipo_Categoria.objects.get(id_equipo_categoria = 15),
        )
        PY.save()

        
        