from ..serializers import MenuSerializer  
from ..models import Menu


class ControllerMenu:
    def crearmenu(request):
        datosmenu = request.data
        try:
            menuNuevo = Menu.objects.create(
                menu_mx =  datosmenu['menu_mx'],
                menu_us = datosmenu['menu_us'],
                id = datosmenu['id'],
                url = datosmenu['url']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_menu': menuNuevo.menu_mx}
       
    def listarmenu(id_menu=None):
        if id_menu:
            try:
                queryset = Menu.objects.get(id_menu=id_menu)
            except Menu.DoesNotExist:
                return ({'result': 'No se encontró el menú deseado'})
            serializer = MenuSerializer(queryset)
            return serializer.data
        else:
            queryset = Menu.objects.all()
            serializer = MenuSerializer(queryset, many=True)
            return serializer.data
