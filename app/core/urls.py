from django.urls import path
from . import views

urlpatterns = [
    path('v1/user/create/', views.CreateUserView.as_view(), name='create'),
    path('v1/user/token/', views.CreateTokenView.as_view(), name='token'),

    path('v1/ltn_lng/', views.UsuarioLatLngView.as_view()),
    
    path('v1/proveedores/', views.Proveedorview.as_view()),
    path('v1/proveedores/<int:id_proveedor>', views.Proveedorview.as_view()),
    path('v1/contacto_proveedores/', views.Contacto_Proveedorview.as_view()),
    path('v1/contacto_proveedores/<int:id_contacto_proveedor>', views.Contacto_Proveedorview.as_view()),
    path('v1/centrosdecostos/', views.CentroCostosview.as_view()),
    path('v1/centrosdecostos/<int:id_centro_costo>', views.CentroCostosview.as_view()),
    path('v1/departamentos/', views.Departamentoview.as_view()),
    path('v1/departamentos/<int:id_departamento>',
         views.Departamentoview.as_view()),
    path('v1/turnos/', views.Turnoview.as_view()),
    path('v1/turnos/<int:id_turno>', views.Turnoview.as_view()),
    path('v1/tipos_rol/', views.Tipo_Rolview.as_view()),
    path('v1/tipos_rol/<int:id_tipo_rol>', views.Tipo_Rolview.as_view()),
    path('v1/scopes/', views.Scopeview.as_view()),
    path('v1/scopes/<int:id_scope>', views.Scopeview.as_view()),
    path('v1/estatus/', views.Estatusview.as_view()),
    path('v1/estatus/<int:id_estatus>', views.Estatusview.as_view()),
    path('v1/idiomas/', views.Idiomaview.as_view()),
    path('v1/idiomas/<int:id_idioma>', views.Idiomaview.as_view()),
    path('v1/roles/', views.Rolview.as_view()),
    path('v1/roles/<int:id_rol>', views.Rolview.as_view()),
    path('v1/departamentos_turnos/', views.Departamento_Turnoview.as_view()),
    path('v1/departamentos_turnos/<int:id_departamento_turno>',
         views.Departamento_Turnoview.as_view()),
    path('v1/puestos/', views.Puestoview.as_view()),
    path('v1/puestos/<int:id_puesto>', views.Puestoview.as_view()),
    path('v1/usuarios/', views.Usuarioview.as_view()),
    path('v1/usuarios/<int:id_usuario>', views.Usuarioview.as_view()),
    path('v1/usuarios/<slug:p_nombre>', views.PerfilUsuarioview.as_view()),
    path('v1/historial_turnos/', views.Historial_TurnoView.as_view()),
    path('v1/historial_turnos/<int:id_historial_turno>',
         views.Historial_TurnoView.as_view()),
    path('v1/jornadas/', views.Jornadaview.as_view()),
    path('v1/jornadas/<int:id_jornada>',
         views.Jornadaview.as_view()),
    path('v1/jornadas_horas/', views.JornadaHorasview.as_view()),
    path('v1/jornadas_horas/<int:id_jornada_horas>',
         views.JornadaHorasview.as_view()),
    path('v1/unidades/', views.Unidadview.as_view()),
    path('v1/unidades/<int:id_unidad>', views.Unidadview.as_view()),
    path('v1/setup/', views.Setup.as_view()),
    path('v1/inventario_categorias/', views.Inventario_Categoriaview.as_view()),
    path('v1/inventario_categorias/<int:id_inventario_categoria>', views.Inventario_Categoriaview.as_view()),
    path('v1/clientes/', views.Clienteview.as_view()),
    path('v1/clientes/<int:id_cliente>', views.Clienteview.as_view()),
    path('v1/equipo_categoria_estatus/', views.EquipoCategoriaEstatusview.as_view()),
    path('v1/equipo_categoria_estatus/<int:id_equipo_categoria_estatus>', views.EquipoCategoriaEstatusview.as_view()),
    path('v1/equipos_categorias/', views.EquipoCategoriaview.as_view()),
    path('v1/equipos_categorias/<int:id_equipo_categoria>', views.EquipoCategoriaview.as_view()),
    path('v1/clases_equipos/', views.ClaseEquipoview.as_view()),
    path('v1/clases_equipos/<int:id_clase_equipo>', views.ClaseEquipoview.as_view()),
    path('v1/modelos_iconos/', views.ModeloIconoview.as_view()),
    path('v1/modelos_iconos/<int:id_modelo_icono>', views.ModeloIconoview.as_view()),
    path('v1/equipos_categorias_iconos/', views.EquipoCategoriaIconoview.as_view()),
    path('v1/equipos_categorias_iconos/<int:id_equipo_categoria>', views.EquipoCategoriaIconoview.as_view()), 
    path('v1/modelos/', views.Modeloview.as_view()),
    path('v1/modelos/<int:id_modelo>', views.Modeloview.as_view()),    
    path('v1/instalacio_iconos/', views.InstalacionIconoview.as_view()),
    path('v1/instalacio_iconos/<int:id_instalacion_icono>', views.InstalacionIconoview.as_view()),   
    path('v1/instalaciones/', views.InstalacionView.as_view()),
    path('v1/instalaciones/<int:id_instalacion>', views.InstalacionView.as_view()),  
    path('v1/equipos_estatus/', views.EquipoEstatusView.as_view()),
    path('v1/equipos_estatus/<int:id_equipo_estatus>', views.EquipoEstatusView.as_view()),  
    path('v1/equipos/', views.Equipoview.as_view()),
    path('v1/equipos/<int:id_equipos>', views.Equipoview.as_view()),  
    path('v1/herramientas_movimientos/', views.HerramientaMovimientoview.as_view()),
    path('v1/herramientas_movimientos/<int:id_herramienta_movimiento>', views.HerramientaMovimientoview.as_view()),
    path('v1/herramientas/', views.Herramientaview.as_view()),
    path('v1/herramientas/<int:id_herramienta>', views.Herramientaview.as_view()),  
    path('v1/herramientas_historial/', views.HerramientaHistorialview.as_view()),
    path('v1/herramientas_historial/<int:id_herramienta_historial>', views.HerramientaHistorialview.as_view()),  
    path('v1/inventario_tipos/', views.InventarioTipoview.as_view()),
    path('v1/inventario_tipos/<int:id_inventario_tipo>', views.InventarioTipoview.as_view()), 
    path('v1/stocks/', views.Stockview.as_view()),
    path('v1/stocks/<int:id_stock>', views.Stockview.as_view()), 
    path('v1/stock_detalles/', views.StockDetalleview.as_view()),
    path('v1/stock_detalles/<int:id_stock_detalle>', views.StockDetalleview.as_view()), 
    path('v1/stock_entradas/', views.StockEntradaview.as_view()),
    path('v1/stock_entradas/<int:id_stock_entrada>', views.StockEntradaview.as_view()), 
    path('v1/stock_ajustes/', views.StockAjusteview.as_view()),
    path('v1/stock_ajustes/<int:id_stock_ajuste>', views.StockAjusteview.as_view()), 
    path('v1/parte_estatus/', views.ParteEstatusview.as_view()),
    path('v1/parte_estatus/<int:id_parte_estatus>', views.ParteEstatusview.as_view()), 
    path('v1/inventario_ajustes/', views.InventarioAjusteview.as_view()),
    path('v1/inventario_ajustes/<int:id_inventario_ajuste>', views.InventarioAjusteview.as_view()),
    path('v1/parte_detalles/', views.ParteDetalleview.as_view()),
    path('v1/parte_detalles/<int:id_parte_detalle>', views.ParteDetalleview.as_view()),  
    path('v1/devoluciones/', views.Devolucionview.as_view()),
    path('v1/devoluciones/<int:id_devolucion>', views.Devolucionview.as_view()), 
    path('v1/almacenes/', views.Almacenview.as_view()),
    path('v1/almacenes/<int:id_almacen>', views.Almacenview.as_view()), 
    path('v1/orden_trabajo_tipos/', views.OrdenTrabajoTipoview.as_view()),
    path('v1/orden_trabajo_tipos/<int:id_orden_trabajo_tipo>', views.OrdenTrabajoTipoview.as_view()), 
    path('v1/inventario_vales/', views.InventarioValeview.as_view()),
    path('v1/inventario_vales/<int:id_inventario_vale>', views.InventarioValeview.as_view()), 
    path('v1/partes_detalle_surtido/', views.ParteDetalleSurtidoview.as_view()),
    path('v1/partes_detalle_surtido/<int:id_parte_detalle_surtido>', views.ParteDetalleSurtidoview.as_view()),
    path('v1/orden_trabajo_estatus/', views.OrdenTrabajoEstatusview.as_view()),
    path('v1/orden_trabajo_estatus/<int:id_orden_trabajo_estatus>', views.OrdenTrabajoEstatusview.as_view()), 
    path('v1/orden_subestatus/', views.OrdenSubestatusview.as_view()),
    path('v1/orden_subestatus/<int:id_orden_subestatus>', views.OrdenSubestatusview.as_view()),
    path('v1/ots/', views.OTview.as_view()),
    path('v1/ots/<int:id_ot>', views.OTview.as_view()),
    path('v1/act_ot_tipos/', views.ActOtTipoview.as_view()),
    path('v1/act_ot_tipos/<int:id_act_ot_tipo>', views.ActOtTipoview.as_view()),
    path('v1/act_ot_codigos/', views.ActOtCodigoview.as_view()),
    path('v1/act_ot_codigo/<int:id_act_ot_codigo>', views.ActOtCodigoview.as_view()),
    path('v1/eventos/', views.Eventoview.as_view()),
    path('v1/eventos/<int:id_evento>', views.Eventoview.as_view()),
    path('v1/orden_archivos/', views.OrdenArchivosview.as_view()),
    path('v1/orden_archivos/<int:id_orden_archivos>', views.OrdenArchivosview.as_view()),
    path('v1/orden_trabajo_parte/', views.OrdenTrabajoParteview.as_view()),
    path('v1/orden_trabajo_parte/<int:id_orden_trabajo_parte>', views.OrdenTrabajoParteview.as_view()),
    path('v1/tarea_orden_trabajo/', views.OrdenTrabajoParteview.as_view()),
    path('v1/tarea_orden_trabajo/<int:id_tarea_orden_trabajo>', views.OrdenTrabajoParteview.as_view()),
    path('v1/tipos_cambio/', views.TipoCambioview.as_view()),
    path('v1/tipos_cambio/<int:id_tipocambio>', views.TipoCambioview.as_view()),
    path('v1/orden_trabajo_completas/', views.OrdenTrabajoCompletaview.as_view()),
    path('v1/orden_trabajo_completas/<int:id_orden_trabajo_completa>', views.OrdenTrabajoCompletaview.as_view()),
    path('v1/rca/', views.RcaView.as_view()),
    path('v1/rca/<int:id_rca>', views.RcaView.as_view()),
    path('v1/rca_accion_preventiva/', views.RcaAccionPreventivaView.as_view()),
    path('v1/rca_accion_preventiva/<int:id_rca_accion_preventiva>', views.RcaAccionPreventivaView.as_view()),
    path('v1/rca_preventive_status/', views.RcaPreventiveStatusview.as_view()),
    path('v1/rca_preventive_status/<int:id_rca_preventive_status>', views.RcaPreventiveStatusview.as_view()),
    path('v1/rca_status/', views.RcaStatusView.as_view()),
    path('v1/rca_status/<int:id_rca_status>', views.RcaStatusView.as_view()),
    path('v1/rca_tipo_accion/', views.RcaTipoAccionview.as_view()),
    path('v1/rca_tipo_accion/<int:id_rca_tipo_accion>', views.RcaTipoAccionview.as_view()),
    path('v1/actividades_mantenimiento/', views.ActividadMantenimientoview.as_view()),
    path('v1/actividades_mantenimiento/<int:id_actividad_mantenimiento>', views.ActividadMantenimientoview.as_view()),
    path('v1/modo_deteccion/', views.ModoDeteccionview.as_view()),
    path('v1/modo_deteccion/<int:id_modo_deteccion>', views.ModoDeteccionview.as_view()),
    path('v1/usuario_revisar/', views.UsuarioRevisarview.as_view()),
    path('v1/usuario_revisar/<int:id_usuario_revisar>', views.UsuarioRevisarview.as_view()),
    path('v1/orden_trabajo_revisada/', views.OrdenTrabajoRevisadaview.as_view()),
    path('v1/orden_trabajo_revisada/<int:id_orden_trabajo_revisada>', views.OrdenTrabajoRevisadaview.as_view()),
    path('v1/ruta_estatus/', views.RutaEstatusview.as_view()),
    path('v1/ruta_estatus/<int:id_ruta_estatus>', views.RutaEstatusview.as_view()),
    path('v1/ruta/', views.Rutaview.as_view()),
    path('v1/ruta/<int:id_ruta>', views.Rutaview.as_view()),
    path('v1/ruta_equipo/', views.RutaEquipoview.as_view()),
    path('v1/ruta_equipo/<int:id_ruta_equipo>', views.RutaEquipoview.as_view()),
    path('v1/ruta_condicion/', views.RutaCondicionview.as_view()),
    path('v1/ruta_condicion/<int:id_ruta_condicion>', views.RutaCondicionview.as_view()),
    path('v1/ruta_condicion_unidad/', views.RutaCondicionUnidadview.as_view()),
    path('v1/ruta_condicion_unidad/<int:id_ruta_condicion_unidad>', views.RutaCondicionUnidadview.as_view()),
    path('v1/ruta_equipo_componente/', views.RutaEquipoComponenteview.as_view()),
    path('v1/ruta_equipo_componente/<int:id_ruta_equipo_componente>', views.RutaEquipoComponenteview.as_view()),
    path('v1/ruta_set_point_operador/', views.RutaSetPointOperadorview.as_view()),
    path('v1/ruta_set_point_operador/<int:id_ruta_set_point_operador>', views.RutaSetPointOperadorview.as_view()),
    path('v1/ruta_set_point/', views.RutaSetPointview.as_view()),
    path('v1/ruta_set_point/<int:id_ruta_set_point>', views.RutaSetPointview.as_view()),

]
