from ..serializers import SubmenuSerializer  
from ..models import Submenu, Menu


class ControllerSubmenu:
    def crearsubmenu(request):
        datossubMenu = request.data
        try:
            menu = Menu.objects.get(id_menu=datossubMenu['menu'])
            
            submenuNuevo = Submenu.objects.create(
                menu = menu,
                submenu_mx = datossubMenu['submenu_mx'], 
                submenu_us = datossubMenu['submenu_us'],
                url = datossubMenu['url']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_submenu': submenuNuevo.submenu_mx}
       
    def listarsubmenu(id_submenu=None):
        if id_submenu:
            try:
                queryset = Submenu.objects.get(id_submenu=id_submenu)
            except Submenu.DoesNotExist:
                return ({'result': 'No se encontró el submenu deseado'})
            serializer = SubmenuSerializer(queryset)
            return serializer.data
        else:
            queryset = Submenu.objects.all()
            serializer = SubmenuSerializer(queryset, many=True)
            return serializer.data
