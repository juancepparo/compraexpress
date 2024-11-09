from tkinter import *
from tkinter import messagebox
import random
import sqlite3
from tkinter import ttk
import os
from datetime import datetime
conexion = sqlite3.connect("Base de Datos/compra_express.db")
color_login = "gray24"
color_fondo = "gray25"
color_frames = "gray23"
color_botones = "LightSteelBlue4"
fuente_principal = "Arial_Black, 16"
fuente_botones = "Arial, 14"
carrito = []

def ventana(ancho,alto,maximizada,titulo):
	ventana = Tk()
	ventana.geometry(f"{ancho}x{alto}")
	ventana.state(maximizada)
	ventana.title("Compra Express - Sistema de Ventas")
	ventana.iconbitmap("logo_icono.ico")
	imagen_logo = PhotoImage(file = "Iconos e imagenes/logo.png")
	img_ver_pedidos = PhotoImage(file = "Iconos e imagenes/pedidos.png")
	img_vender = PhotoImage(file = "Iconos e imagenes/bolsa_papel.png")
	img_clientes = PhotoImage(file = "Iconos e imagenes/clientes.png")
	img_inventario = PhotoImage(file = "Iconos e imagenes/inventario.png")
	img_proveedores = PhotoImage(file = "Iconos e imagenes/industria.png")
	img_reportes = PhotoImage(file = "Iconos e imagenes/reportes.png")
	img_ajustes = PhotoImage(file = "Iconos e imagenes/ajustes.png")
	img_volver = PhotoImage(file = "Iconos e imagenes/volver3.png")
	img_ver_proveedor = PhotoImage(file = "Iconos e imagenes/carpeta.png")
	img_añadir_prod = PhotoImage(file = "Iconos e imagenes/suma.png")
	img_editar_prod = PhotoImage(file = "Iconos e imagenes/lapiz.png")
	img_eliminar = PhotoImage(file = "Iconos e imagenes/eliminar.png")
	img_añadir_carro = PhotoImage(file = "Iconos e imagenes/flecha.png")
	img_tilde = PhotoImage(file = "Iconos e imagenes/tilde.png")
	img_ticket = PhotoImage(file = "Iconos e imagenes/ticket.png")
	img_preparacion = PhotoImage(file = "Iconos e imagenes/preparacion.png")
	img_cerrado = PhotoImage(file = "Iconos e imagenes/cerrado.png")
	img_borrador = PhotoImage(file = "Iconos e imagenes/borrador.png")
	img_revisar = PhotoImage(file = "Iconos e imagenes/revisar.png")

	frame_login = Frame(ventana, bg=color_login)
	frame_principal = Frame(ventana, bg=color_fondo)
	frame_izquierdo = Frame(frame_principal, bg = color_frames)
	frame_central = Frame(frame_principal, bg = color_frames)
	frame_derecho = Frame(frame_principal, bg = color_frames)
	frame_inferior = Frame(frame_principal, bg = color_frames)
	label_logo = Label(frame_principal, image = imagen_logo, relief = "flat")
	label_usuario = Label(frame_login, text = "Ingrese Usuario", font = fuente_principal, fg = "white", bg = color_login)
	label_contraseña = Label(frame_login, text = "Ingrese Contraseña", font = fuente_principal, fg = "white", bg = color_login)
	entry_usuario = Entry(frame_login, font = fuente_principal)
	entry_contraseña = Entry(frame_login, font = fuente_principal)
	frame_principal.pack(expand = 1, fill = BOTH, side = "left")
	frame_login.pack(expand = 1, fill = BOTH, side = "right")
	label_logo.pack (pady = 70)
	label_usuario.pack(pady = 10)
	entry_usuario.pack(pady = 10)	
	label_contraseña.pack(pady = 10)
	entry_contraseña.pack(pady = 10)

	def misestilos():
		global estilos
		estilos = ttk.Style()
		estilos.theme_use("alt")
		estilos.configure("oscuro.Treeview",
						   background = "dark slate gray", 
						   foreground = "white",
						   fieldbackground = "dark slate gray",
						   font = ("calibri", 14)
						    )
		
		return estilos
	
	def acceder(): 
		#usuario = entry_usuario.get()
		#contraseña = entry_contraseña.get()
		#entry_usuario.delete(0, END)
		entry_contraseña.delete(0, END)
		#if(usuario != "admin" or contraseña != "1234"):
		#	#messagebox.showwarning("Error", "Usuario o contraseña incorrectos")
		#else:
			#messagebox.showinfo("Compra Express", "Acceso correcto")
		pantalla_principal()
	boton_acceder = Button(frame_login, font = "Arial, 12", text = "Acceder", relief = "flat", bg = "white", command = acceder)
	boton_acceder.pack(pady = 10)

	def pantalla_principal():
		
		def realizar_venta():
			olvidar_pantalla_principal()
			mensaje_busqueda_pedidos = Label(cinta_superior, bg= color_botones, text = "Menú Ventas", font = fuente_principal, fg = "white")
			label_buscar = Label(frame_principal, text = "Elija Código, Categoria o Nombre", font = fuente_botones, bg = color_fondo, fg = "white")
			cajon_buscar_productos = Entry(frame_principal, font = fuente_principal, bg = "gray66")
			mensaje_seleccione = Label(frame_inferior, text = "Click Tabla: Seleccionar Producto", font = fuente_principal, bg = color_frames, fg = "white")
			frame_centro = Frame(frame_principal, bg = color_fondo)
			label_cantidad = Label(frame_centro, text = "Cantidad", font = "Calibri, 10", bg = color_fondo, fg = "white")
			entry_cantidad = ttk.Entry(frame_centro, font = "Calibri, 10")
			frame_principal.pack(fill = BOTH, expand = 1)
			cinta_superior.pack(fill = X)
			mensaje_busqueda_pedidos.pack()
			label_buscar.pack()
			cajon_buscar_productos.pack(ipadx = 200, pady = 10, anchor = N)
			frame_inferior.pack(side = BOTTOM, ipadx = 610, ipady = 20)
			mensaje_seleccione.pack(side = LEFT, padx = 10, anchor = N)
			frame_izquierdo.pack(side = LEFT, fill = BOTH, expand = 1, padx = (10,10), pady = (0, 10))
			frame_centro.pack(side = LEFT, fill = Y, expand = 1, padx = (10,10), pady = (0, 10))
			frame_derecho.pack(side = LEFT, fill = Y, padx = (0, 10), pady = (0,10), ipadx = 250, ipady = 200)
			label_cantidad.pack()
			entry_cantidad.pack()
			
			###FUNCION VOLVER ATRAS###
			def volver():
				olvidar_realizar_venta()
				pantalla_principal()
			boton_volver = Button(frame_inferior, bg = color_botones, text = "Volver", font = fuente_botones, command = volver, image = img_volver, compound = RIGHT)
			boton_volver.pack(side = BOTTOM, anchor = E)
			
			def emitir_ticket():
				pass
			boton_ticket = Button(frame_inferior, text = "Emitir Ticket", font = fuente_botones, bg = color_botones, image = img_ticket, compound = RIGHT)
			boton_ticket.pack(side = RIGHT, padx = 10, anchor = N)

			###FUNCION VENDER###
			def vender():
				total_venta = 0
				total_iva = 0
				total_costo_carr = 0
				total_ganancia_carr = 0

				if(len(carrito)<1):
					messagebox.showerror("Error", "Primero debe cargar productos")
					return
				tabla = conexion.cursor()
				for articulo in carrito:
					id_en_carrito = articulo[0]
					id_select = (articulo[0],)
					cant_carrito = articulo[2]
					nombre_prod_carrito = articulo[3]
					stock_carrito = articulo[5]
					stock_nuevo = (articulo[5] - articulo [2])
					total_venta = total_venta + float(articulo[4])
					precio_sin_iva_carr = float(articulo[4]) / 1.21
					precio_sin_iva_red = round(precio_sin_iva_carr,2)
					iva_carr = precio_sin_iva_carr * 0.21
					iva_redondeado = round(iva_carr,2)
					precio_con_iva_carr = articulo[4]
					total_iva_carr = total_iva + iva_redondeado
					datos_carrito = (stock_nuevo, id_en_carrito)
					tabla.execute("UPDATE productos SET stock = ? WHERE id_producto = ?", datos_carrito)
					conexion.commit()

					tabla.execute("SELECT costo FROM productos WHERE id_producto = ?", id_select)
					datos = tabla.fetchall()
					costo_carr = datos[0][0]
					total_costo_carr = (total_costo_carr + costo_carr)
					ganancia_carr = (precio_sin_iva_red - costo_carr)
					total_ganancia_carr = (total_ganancia_carr + ganancia_carr)
					print(total_costo_carr, total_ganancia_carr)
											
				fecha = datetime.now()
				fecha_actual = fecha.strftime('%d/%m/%Y, %H:%M:%S')
				guardar_venta = (fecha_actual, total_venta, total_iva_carr, total_costo_carr, total_ganancia_carr)
				tabla.execute("INSERT INTO reportes(fecha_hora, total_ticket, total_iva, total_costo, ganancia) VALUES(?,?,?,?,?)", guardar_venta)
				conexion.commit()
				tabla.close()	
				messagebox.showinfo("Ventas", "Venta realizada")
				for fila in tabla_carrito.get_children():
					tabla_carrito.delete(fila)
				for fila in tabla_productos.get_children():
					tabla_productos.delete(fila)
				carrito.clear()
				entry_cantidad.delete(0, END)
				cargar_articulos()
								
			boton_vender = Button(frame_inferior, text = "      Vender     ", font = fuente_botones, bg = color_botones, command = vender, image = img_tilde, compound = RIGHT)
			boton_vender.pack(side = RIGHT, padx = 10, anchor = N)

			###TABLA PRODUCTOS###
			tabla_productos = ttk.Treeview(frame_izquierdo, style = "oscuro.Treeview")
			tabla_productos.pack(side = TOP, fill = BOTH, expand = 1)
			tabla_productos["columns"] = ("Categoria","Detalle", "Precio", "Stock")
			tabla_productos.heading("#0", text = "Codigo")
			tabla_productos.heading("Categoria", text = "Categoria")
			tabla_productos.heading("Detalle", text = "Detalle")
			tabla_productos.heading("Precio", text = "Precio")
			tabla_productos.heading("Stock", text = "Stock")
			tabla_productos.column("#0", width = 50)
			tabla_productos.column("Categoria", width = 100)
			tabla_productos.column("Detalle", width = 220)
			tabla_productos.column("Precio", width = 85)
			tabla_productos.column("Stock", width = 45)
			
			###TABLA CARRITO###
			tabla_carrito = ttk.Treeview(frame_derecho, style = "oscuro.Treeview")
			tabla_carrito.pack(side = TOP, fill = BOTH, expand = 1)
			tabla_carrito["columns"] = ("Categoria","Cantidad","Detalle", "Precio")
			tabla_carrito.heading("#0", text = "Codigo")
			tabla_carrito.heading("Categoria", text = "Categoria")
			tabla_carrito.heading("Cantidad", text = "Cantidad")
			tabla_carrito.heading("Detalle", text = "Detalle")
			tabla_carrito.heading("Precio", text = "Precio")
			tabla_carrito.column("#0", width = 1)
			tabla_carrito.column("Categoria", width = 5)
			tabla_carrito.column("Cantidad", width = 1)
			tabla_carrito.column("Detalle", width = 140)
			tabla_carrito.column("Precio", width = 10)
						
			###Selecciona articulos de la tabla productos y la inserta en el carrito###
			
			###VALIDACIONES###
			def seleccionar_articulo():
				index = tabla_productos.selection()
				fila = tabla_productos.item(index)
				if (len(index) == 0):
					messagebox.showwarning("Aviso", "Debe seleccionar un artículo")
					return		
				if (entry_cantidad.get() == ""):
					messagebox.showwarning("Aviso", "Debe ingresar una cantidad")
					return
				###VERIFICA QUE LA CANTIDAD NO SUPERE AL STOCK###
				cod_art = (fila["text"],)
				tabla = conexion.cursor()
				tabla.execute("SELECT stock FROM productos WHERE id_producto = ?", cod_art)
				datos = tabla.fetchall()
				tabla.close()
				stock = datos[0][0]
				if (stock < int(entry_cantidad.get())):
					messagebox.showwarning("Error", "La cantidad no puede ser mayor al stock")
					entry_cantidad.delete(0, END)
					return
				###TOMA DE DATOS DE LA FILA SELECCIONADA###
				codigo = fila["text"]
				categoria = fila["values"][0]
				cantidad = int(entry_cantidad.get())
				detalle = fila["values"][1]
				precio = fila["values"][2]
				precio_float = float(precio)
				sub_total = (cantidad * precio_float)

				###CARGA DE DATOS EN TABLA CARRITO###
				tabla_carrito.insert("", END, text = codigo, values = (categoria, cantidad, detalle, sub_total))
				entry_cantidad.delete(0, END)
				
				###CARGA ARTICULOS SELECCIONADOS CARRITO (BACK)###
				articulo = [codigo, categoria, cantidad, detalle, sub_total, stock]
				carrito.append(articulo)
											
			##tabla_productos.bind("<<TreeviewSelect>>", seleccionar_articulo)### Este evento no se usará, se reemplazó por el botón añadir. Si se quita el botón colocar def seleccionar_articulo(evento):### 
			boton_añadir = Button(frame_centro, text = "Añadir al Carro", font = "Calibri, 12", bg = color_botones, image = img_añadir_carro, compound = RIGHT, command = seleccionar_articulo )
			boton_añadir.pack(pady = 20)
			###side = LEFT, , anchor = N
			
			###CARGA INICIAL ARTICULOS TABLA PRODUCTOS DESDE BD###
			def cargar_articulos():
				tabla = conexion.cursor()
				tabla.execute("SELECT* FROM productos")
				datos = tabla.fetchall()
				for fila in tabla_productos.get_children():
					tabla_productos.delete(fila)
				for dato in datos:
					id_categoria = (dato[1],)
					tabla.execute("SELECT nombre_categoria FROM categorias WHERE id = ?", id_categoria)
					datos_categoria = tabla.fetchall()
					tabla_productos.insert("", END, text = dato[0], values = (datos_categoria[0], dato[2], dato[4], dato[5]))
				tabla.close()
			cargar_articulos()

			###Buscar productos entry búsqueda###
			def buscar_productos(evento):
				buscar = ("%"+cajon_buscar_productos.get()+"%","%"+cajon_buscar_productos.get()+"%","%"+cajon_buscar_productos.get()+"%")
				tabla = conexion.cursor()
				tabla.execute("SELECT * FROM productos WHERE id_producto LIKE ? OR nombre_producto LIKE ? OR categoria LIKE (SELECT id FROM categorias WHERE nombre_categoria LIKE?)", buscar)
				datos_articulos = tabla.fetchall()
				
				###Borrar Treeview###
				for fila in tabla_productos.get_children():
					tabla_productos.delete(fila)
				
				###Reescriir Treeview###
				for dato in datos_articulos:
					id_categoria = (dato[1],)
					tabla.execute("SELECT nombre_categoria FROM categorias WHERE id = ?", id_categoria)
					datos_categoria = tabla.fetchall()
					tabla_productos.insert("", END, text = dato[0], values = (datos_categoria[0], dato[2], dato[4], dato[5]))
				tabla.close()
			cajon_buscar_productos.bind("<KeyRelease>", buscar_productos)

			###FUNCION QUITAR DEL CARRITO###
			def quitar_del_carrito():
				index = tabla_carrito.selection()
				if (len(index) > 0):
					tabla_carrito.delete(index)
				else:
					messagebox.showerror("Error", "Previo debe ingresar algún producto")
					return
			boton_quitar = Button(frame_inferior, text = "Quitar del Carro", font = fuente_botones, bg = color_botones, image = img_eliminar, compound = RIGHT, command = quitar_del_carrito)
			boton_quitar.pack(side = RIGHT, padx = 10, anchor = N)

			def olvidar_realizar_venta():
				frame_principal.forget()
				cinta_superior.forget()
				mensaje_busqueda_pedidos.forget()
				label_buscar.forget()
				cajon_buscar_productos.forget()
				frame_inferior.forget()
				frame_izquierdo.forget()
				frame_centro.forget()
				frame_derecho.forget()
				boton_añadir.forget()
				boton_quitar.forget()
				boton_vender.forget()
				boton_ticket.forget()
				boton_volver.forget()
				tabla_productos.forget()
				tabla_carrito.forget()
				mensaje_seleccione.forget()
				carrito.clear()
				entry_cantidad.forget()
				label_cantidad.forget()

		def ver_pedidos():
			olvidar_pantalla_principal()
			cajon_buscar_pedidos = Entry(frame_principal, font = fuente_principal, bg = "gray66")
			label_buscar = Label(frame_principal, text = "Elija Código, Cliente o Estado", font = fuente_botones, bg = color_fondo, fg = "white")
			mensaje_busqueda_productos = Label(cinta_superior, bg= color_botones, text = "Búsqueda de Pedidos", font = fuente_principal, fg = "white")
			frame_izquierdo2 = Frame(frame_principal, bg = color_frames)
			mensaje_seleccione = Label (frame_inferior, text = "Click: Seleccionar", font = fuente_principal, bg = color_frames, fg = "white")
			frame_principal.pack(fill = BOTH, expand = 1)
			cinta_superior.pack(fill = X, anchor = N)
			mensaje_busqueda_productos.pack()
			label_buscar.pack()
			cajon_buscar_pedidos.pack(ipadx = 200, pady = 10, anchor = N)
			frame_inferior.pack(side = BOTTOM, ipadx = 610, ipady = 20)
			frame_izquierdo2.pack(side = LEFT, fill = BOTH, expand = 1, padx = (10,10), pady = (0, 10))
			frame_derecho.pack(side = LEFT, fill = Y, padx = (0, 10), pady = (0,10), ipadx = 250, ipady = 200)
			mensaje_seleccione.pack(side = LEFT, padx = 10, anchor = N)
			tabla_lista_pedidos = ttk.Treeview(frame_izquierdo2, style = "oscuro.Treeview")
			tabla_lista_pedidos.pack(side = TOP, fill = BOTH, expand = 1)
			tabla_lista_pedidos["columns"] = ("Cliente","Estado")
			tabla_lista_pedidos.heading("#0", text = "Número")
			tabla_lista_pedidos.heading("Cliente", text = "Cliente")
			tabla_lista_pedidos.heading("Estado", text = "Estado")
			tabla_lista_pedidos.column("#0", width = 50)
			tabla_lista_pedidos.column("Cliente", width = 200)
			tabla_lista_pedidos.column("Estado", width = 80)
			tabla_detalle_pedidos = ttk.Treeview(frame_derecho, style = "oscuro.Treeview")
			tabla_detalle_pedidos.pack(side = TOP, fill = BOTH, expand = 1)
			tabla_detalle_pedidos["columns"] = ("Detalle", "Precio")
			tabla_detalle_pedidos.heading("#0", text = "Cantidad")
			tabla_detalle_pedidos.heading("Detalle", text = "Detalle")
			tabla_detalle_pedidos.heading("Precio", text = "Precio")
			tabla_detalle_pedidos.column("#0", width = 1)
			tabla_detalle_pedidos.column("Detalle", width = 200)
			tabla_detalle_pedidos.column("Precio", width = 10)
			
			def volver():
				olvidar_ver_pedidos()
				pantalla_principal()
			boton_volver = Button(frame_inferior, bg = color_botones, text = "Volver", font = fuente_botones, command = volver, image = img_volver, compound = RIGHT)
			boton_volver.pack(side = BOTTOM, anchor = E)

			###FUNCION BUSCAR EN SQL SELECCION DE TABLA###
			def buscar_seleccion():
				index = tabla_lista_pedidos.selection()
				fila = tabla_lista_pedidos.item(index)
				codigo = (fila["text"],)
				tabla = conexion.cursor()
				tabla.execute("SELECT * FROM pedidos WHERE id = ?", codigo)
				datos = tabla.fetchall()
				tabla.close()
				return(datos)

			###BOTON PREPARACION PEDIDO###	
			def preparacion():
				datos = buscar_seleccion()
				tabla = conexion.cursor()
				if(len(datos)<1):
					return
				if ((datos[0][2]) == 2):
					messagebox.showerror("Error", "Ya se encuentra en preparación")
					return
				elif((datos[0][2]) == 4):
					messagebox.showerror("Error", "No se puede modificar un pedido enviado")
					return
				nuevo_estado = ("2", datos[0][0],)
				tabla.execute("UPDATE pedidos SET estado = ? WHERE id = ?", nuevo_estado)
				conexion.commit()
				tabla.close()
				messagebox.showinfo("En preparación", "Estado actualizado")
				cargar_articulos()
			boton_preparacion = Button(frame_inferior, text = "Marcar en Preparacion", font = fuente_botones, bg = color_botones, command = preparacion, image = img_preparacion, compound = RIGHT)
			boton_preparacion.pack(side = LEFT, padx = 10, anchor = N)

			###BOTON CERRAR PEDIDO###
			def cerrar():
				datos = buscar_seleccion()
				tabla = conexion.cursor()
				if(len(datos)<1):
					return
				if ((datos[0][2]) == 3):
					messagebox.showerror("Error", "Ya se encuentra cerrado")
					return
				elif((datos[0][2]) == 4):
					messagebox.showerror("Error", "No se puede modificar un pedido enviado")
					return
				nuevo_estado = ("3", datos[0][0],)
				tabla.execute("UPDATE pedidos SET estado = ? WHERE id = ?", nuevo_estado)
				conexion.commit()
				tabla.close()
				messagebox.showinfo("Cerrado", "Estado actualizado")
				cargar_articulos()
			boton_cerrar_pedido = Button(frame_inferior, text = "Cerrar Pedido", font = fuente_botones, bg = color_botones, command = cerrar, image = img_cerrado, compound = RIGHT)
			boton_cerrar_pedido.pack(side = LEFT, padx = 10, anchor = N)
			
			###BOTON VENDER Y ENVIAR###
			def vender():
				datos = buscar_seleccion()
				tabla = conexion.cursor()
				if(len(datos)<1):
					return
				if ((datos[0][2]) == 4):
					messagebox.showerror("Error", "No puede enviar nuevamente el pedido")
					return
				nuevo_estado = ("4", datos[0][0],)
				tabla.execute("UPDATE pedidos SET estado = ? WHERE id = ?", nuevo_estado)
				conexion.commit()
				tabla.close()
				messagebox.showinfo("Venta", "Venta realizada y pedido en despacho")
				cargar_articulos()
			boton_vender = Button(frame_inferior, text = "Vender y Enviar", font = fuente_botones, bg = color_botones, command = vender, image = img_tilde, compound = RIGHT)
			boton_vender.pack(side = LEFT, padx = 10, anchor = N)

			def emitir_ticket():
				pass
			boton_ticket = Button(frame_inferior, text = "Emitir Ticket", font = fuente_botones, bg = color_botones, image = img_ticket, compound = RIGHT)
			boton_ticket.pack(side = LEFT, padx = 10, anchor = N)
			
			##Cargar Pedidos Tabla##
			def cargar_articulos():
				tabla = conexion.cursor()
				tabla.execute("SELECT* FROM pedidos")
				datos = tabla.fetchall()
				for fila in tabla_lista_pedidos.get_children():
					tabla_lista_pedidos.delete(fila)
				for dato in datos:
					id_pedido = (dato[1],)
					id_estado = (dato[2],)
					tabla.execute("SELECT nombre FROM clientes WHERE id = ?", id_pedido)
					datos_cliente = tabla.fetchall()
					tabla.execute("SELECT tipo_estado FROM estados WHERE id = ?", id_estado)
					datos_estado = tabla.fetchall()
					tabla_lista_pedidos.insert("", END, text = dato[0], values = (datos_cliente[0][0], datos_estado[0][0]))
				tabla.close()
			cargar_articulos()

			###CARGAR DETALLE DE PEDIDO EN TABLA DERECHA###
			def seleccionar_pedido(evento):
				datos = buscar_seleccion()
				tabla = conexion.cursor()
				if(len(datos)<1):
					return
				id_pedido = (datos[0][0],)
				tabla.execute("SELECT* FROM detalle_pedido WHERE id_detalle_pedido = ?", id_pedido)
				detalle_pedidos = tabla.fetchall()
				for fila in tabla_detalle_pedidos.get_children():
					tabla_detalle_pedidos.delete(fila)
				for dato in detalle_pedidos:
					nombre_producto = (dato[2],)
					tabla.execute("SELECT nombre_producto, precio_venta FROM productos WHERE id_producto = ?", nombre_producto)
					prod_encontrado = tabla.fetchall()
					precio = ((dato[1])*(prod_encontrado[0][1]))
					tabla_detalle_pedidos.insert("", END, text = dato[1], values = (prod_encontrado[0][0], precio))
				tabla.close()
			tabla_lista_pedidos.bind("<<TreeviewSelect>>", seleccionar_pedido)
			
			###Buscar productos entry búsqueda###
			def buscar_pedidos(evento):
				buscar = ("%"+cajon_buscar_pedidos.get()+"%","%"+cajon_buscar_pedidos.get()+"%","%"+cajon_buscar_pedidos.get()+"%")
				tabla = conexion.cursor()
				tabla.execute("SELECT * FROM pedidos WHERE id LIKE ? OR estado LIKE (SELECT id FROM estados WHERE tipo_estado LIKE ?) OR cliente LIKE (SELECT id FROM clientes WHERE nombre LIKE ?)", buscar)
				datos_pedido = tabla.fetchall()
				
				###Borrar Treeview###
				for fila in tabla_lista_pedidos.get_children():
					tabla_lista_pedidos.delete(fila)
				
				###Reescriir Treeview izquierdo###
				for dato in datos_pedido:
					id_cliente = (dato[1],)
					id_estado = (dato[2],)
					tabla.execute("SELECT nombre FROM clientes WHERE id = ?", id_cliente)
					datos_cliente = tabla.fetchall()
					tabla.execute("SELECT tipo_estado FROM estados WHERE id = ?", id_estado)
					datos_estado = tabla.fetchall()
					tabla_lista_pedidos.insert("", END, text = dato[0], values = (datos_cliente[0][0], datos_estado[0][0]))
				tabla.close()
			cajon_buscar_pedidos.bind("<KeyRelease>", buscar_pedidos)

			def olvidar_ver_pedidos():
				cinta_superior.forget()
				mensaje_busqueda_productos.forget()
				frame_principal.forget()
				boton_volver.forget()
				frame_inferior.forget()
				frame_izquierdo2.forget()
				frame_derecho.forget()
				cajon_buscar_pedidos.forget()
				tabla_lista_pedidos.forget()
				tabla_detalle_pedidos.forget()
				boton_preparacion.forget()
				boton_cerrar_pedido.forget()
				boton_vender.forget()
				mensaje_seleccione.forget()
				boton_volver.forget()
				label_buscar.forget()
				boton_ticket.forget()
			
		def mis_clientes():
			olvidar_pantalla_principal()
			mensaje_busqueda_clientes = Label(cinta_superior, bg= color_botones, text = "Búsqueda de clientes", font = fuente_principal, fg = "white")
			label_buscar = Label(frame_principal, text = "Elija Código o Nombre", font = fuente_botones, bg = color_fondo, fg = "white")
			cajon_buscar_clientes = Entry(frame_principal, font = fuente_principal, bg = "gray66")
			frame_principal.pack(fill = BOTH, expand = 1)
			cinta_superior.pack(fill = X, anchor = N)
			mensaje_seleccione = Label (frame_inferior, text = "Click: Seleccionar", font = fuente_principal, bg = color_frames, fg = "white")
			mensaje_busqueda_clientes.pack()
			label_buscar.pack()
			cajon_buscar_clientes.pack(ipadx = 200, pady = 10, anchor = N)
			frame_central.pack(fill = BOTH, expand = 1, pady = 20)
			frame_inferior.pack(side = BOTTOM, ipadx = 610, ipady = 30)
			mensaje_seleccione.pack(side = LEFT, padx = 10, anchor = N)
			tabla_clientes = ttk.Treeview(frame_central, style = "oscuro.Treeview")
			tabla_clientes.pack(side = TOP, fill = BOTH, expand = 1)
			tabla_clientes["columns"] = ("Nombre","Domicilio","Teléfono","E-Mail")
			tabla_clientes.heading("#0", text = "Número")
			tabla_clientes.heading("Nombre", text = "Nombre")
			tabla_clientes.heading("Domicilio", text = "Domicilio")
			tabla_clientes.heading("Teléfono", text = "Teléfono")
			tabla_clientes.heading("E-Mail", text = "E-Mail")
			tabla_clientes.column("#0", width = 10)
			tabla_clientes.column("Nombre", width = 150)
			tabla_clientes.column("Domicilio", width = 350)
			tabla_clientes.column("Teléfono", width = 80)
			tabla_clientes.column("E-Mail", width = 150)

			###CARGA CLIENTES DESDE BD###
			def cargar_clientes():
				tabla = conexion.cursor()
				tabla.execute("SELECT* FROM clientes")
				datos = tabla.fetchall()
				for fila in tabla_clientes.get_children():
					tabla_clientes.delete(fila)
				for dato in datos:
					tabla_clientes.insert("", END, text = dato[0], values = (dato[1], dato[2], dato[3],dato[4]))
				tabla.close()
			cargar_clientes()

			def añadir_cliente():
				pass
			boton_añadir_cliente = Button(frame_inferior, bg = color_botones, text = "  Añadir Cliente  ", font = fuente_botones, command = añadir_cliente, image = img_añadir_prod, compound = RIGHT)
			boton_añadir_cliente.pack(side = LEFT, padx = 10, anchor = N)

			def editar_cliente():
				pass
			boton_editar_cliente = Button(frame_inferior, bg = color_botones, text = " Editar Cliente ", font = fuente_botones, command = editar_cliente, image = img_editar_prod, compound = RIGHT)
			boton_editar_cliente.pack(side = LEFT, padx = 10, anchor = N)

			def eliminar_cliente():
				pass
			boton_eliminar_cliente = Button(frame_inferior, bg = color_botones, text = "Eliminar Cliente", font = fuente_botones, command = eliminar_cliente, image = img_eliminar, compound = RIGHT)
			boton_eliminar_cliente.pack(side = LEFT, padx = 10, anchor = N)

			def volver():
				olvidar_mis_clientes()
				pantalla_principal()
			boton_volver = Button(frame_inferior, bg = color_botones, text = "Volver", font = fuente_botones, command = volver, image = img_volver, compound = RIGHT)
			boton_volver.pack(side = BOTTOM, anchor = E)

			def olvidar_mis_clientes():
				cinta_superior.forget()
				mensaje_busqueda_clientes.forget()
				frame_principal.forget()
				boton_volver.forget()
				label_buscar.forget()
				cajon_buscar_clientes.forget()
				frame_inferior.forget()
				frame_central.forget()
				mensaje_seleccione.forget()
				boton_añadir_cliente.forget()
				boton_editar_cliente.forget()
				boton_eliminar_cliente.forget()
				tabla_clientes.forget()

		def inventario():
			olvidar_pantalla_principal()
			mensaje_busqueda_productos = Label(cinta_superior, bg= color_botones, text = "Búsqueda de productos", font = fuente_principal, fg = "white")
			label_buscar = Label(frame_principal, text = "Elija Código, Categoria o Nombre", font = fuente_botones, bg = color_fondo, fg = "white")
			cajon_buscar_productos = Entry(frame_principal, font = fuente_principal, bg = "gray66")
			mensaje_seleccione = Label (frame_inferior, text = "Click Tabla: Seleccionar Producto", font = fuente_principal, bg = color_frames, fg = "white")
			label_codigo = Label(frame_derecho, text = "Codigo", font = fuente_principal, bg = color_frames, fg = "white")
			label_categoria = Label(frame_derecho, text = "Categoria", font = fuente_principal, bg = color_frames, fg = "white")
			label_producto = Label(frame_derecho, text = "Producto", font = fuente_principal, bg = color_frames, fg = "white")
			label_costo = Label(frame_derecho, text = "Costo", font = fuente_principal, bg = color_frames, fg = "white")
			label_precio_venta = Label(frame_derecho, text = "Precio de Venta", font = fuente_principal, bg = color_frames, fg = "white")
			label_stock = Label(frame_derecho, text = "Stock", font = fuente_principal, bg = color_frames, fg = "white")
			entry_codigo = Entry(frame_derecho, font = fuente_principal)
			entry_categoria = Entry(frame_derecho, font = fuente_principal)
			entry_producto = Entry(frame_derecho, font = fuente_principal)
			entry_costo = Entry(frame_derecho, font = fuente_principal)
			entry_precio_venta = Entry(frame_derecho, font = fuente_principal)
			entry_stock = Entry(frame_derecho, font = fuente_principal)
			tabla_inventario = ttk.Treeview(frame_izquierdo, style = "oscuro.Treeview")
			tabla_inventario["columns"] = ("Categoria", "Producto", "Costo", "Precio Venta", "Stock")
			tabla_inventario.heading("#0", text = "Código")
			tabla_inventario.heading("Categoria", text = "Categoria")
			tabla_inventario.heading("Producto", text = "Producto")
			tabla_inventario.heading("Costo", text = "Costo")
			tabla_inventario.heading("Precio Venta", text = "Precio Venta")
			tabla_inventario.heading("Stock", text = "Stock")
			tabla_inventario.column("#0", width = 10)
			tabla_inventario.column("Categoria", width = 60)
			tabla_inventario.column("Producto", width = 250)
			tabla_inventario.column("Costo", width = 35)
			tabla_inventario.column("Precio Venta", width = 35)
			tabla_inventario.column("Stock", width = 10)
			cinta_superior.pack(fill = X, anchor = N)
			mensaje_busqueda_productos.pack()
			label_buscar.pack()
			frame_principal.pack(fill = BOTH, expand = 1)
			cajon_buscar_productos.pack(ipadx = 200, pady = 10, anchor = N)
			frame_inferior.pack(side = BOTTOM, ipadx = 610, ipady = 20)
			frame_izquierdo.pack(side = LEFT, fill = BOTH, expand = 1, padx = (10,10), pady = (0, 10))
			frame_derecho.pack(side = LEFT, fill = Y, padx = (0, 10), pady = (0,10), ipadx = 150, ipady = 200)
			tabla_inventario.pack(side = TOP, fill = BOTH, expand = 1)
			mensaje_seleccione.pack(side = LEFT, padx = 10, anchor = N)
			label_codigo.pack()
			entry_codigo.pack(ipadx = 20)
			label_categoria.pack()
			entry_categoria.pack(ipadx = 20)
			label_producto.pack()
			entry_producto.pack(ipadx = 20)
			label_costo.pack()
			entry_costo.pack(ipadx = 20)
			label_precio_venta.pack()
			entry_precio_venta.pack(ipadx = 20)
			label_stock.pack()
			entry_stock.pack(ipadx = 20)
			entry_codigo.config(state = "readonly")

			def volver():
				olvidar_inventario()
				pantalla_principal()
			boton_volver = Button(frame_inferior, bg = color_botones, text = "Volver", font = fuente_botones, command = volver, image = img_volver, compound = RIGHT)
			boton_volver.pack(side = BOTTOM, anchor = E)
			
			###VERIFICA LA EXISTENCIA DE LA CATEGORIA, SINO LA CREA###
			def verificar_categoria():
				tabla = conexion.cursor()
				categoria = (entry_categoria.get(),)
				tabla.execute("SELECT id FROM categorias WHERE nombre_categoria = ?", categoria)
				resultado_categoria = tabla.fetchall()
				if(len(resultado_categoria)<1):
					tabla.execute("INSERT INTO categorias(nombre_categoria) VALUES (?)", categoria)
				tabla.execute("SELECT id FROM categorias WHERE nombre_categoria = ?", categoria)
				categorias_actuales = tabla.fetchall()
				return(categorias_actuales)
			
			def guardar_articulo():
				if(entry_categoria.get() == "" or entry_producto.get() == "" or entry_costo.get() == "" or entry_precio_venta.get() == "" or entry_stock.get() == ""):
					messagebox.showerror("Guardar", "Debe rellenar todos los campos")
					return
				categorias_actuales = verificar_categoria()
				datos = (categorias_actuales[0][0], entry_producto.get(), entry_costo.get(), entry_precio_venta.get(), entry_stock.get())
				tabla = conexion.cursor()
				tabla.execute("INSERT INTO productos (categoria, nombre_producto, costo, precio_venta, stock) VALUES (?,?,?,?,?)", datos)
				conexion.commit()
				tabla.close()
				messagebox.showinfo("Guardar", "Artículo guardado exitosamente")
				borrar_entrys()
				cargar_articulos()
			
			def modificar_articulo():
				if(entry_categoria.get() == "" or entry_producto.get() == "" or entry_costo.get() == "" or entry_precio_venta.get() == "" or entry_stock.get() == ""):
					messagebox.showerror("Modificar Artículo", "Debe seleccionar un artículo")
					return
				confirmar = messagebox.askyesno("Modificar Artículo", "¿Desea modificar el articulo seleccionado?")
				if(confirmar == False):
					return
				entry_codigo.config(state = "normal")
				categorias_actuales = verificar_categoria()
				datos = (categorias_actuales[0][0], entry_producto.get(), entry_costo.get(), entry_precio_venta.get(), entry_stock.get(), entry_codigo.get())
				tabla = conexion.cursor()
				tabla.execute("UPDATE productos SET categoria = ?, nombre_producto = ?, costo = ?, precio_venta = ?, stock = ? WHERE id_producto = ?", datos)
				conexion.commit()
				tabla.close()
				messagebox.showinfo("Actualizar", "Artículo modificado con éxito")
				borrar_entrys()
				cargar_articulos()

			def eliminar_articulo():
				if(entry_categoria.get() == "" or entry_producto.get() == "" or entry_costo.get() == "" or entry_precio_venta.get() == "" or entry_stock.get() == ""):
					messagebox.showerror("Eliminar", "Debe seleccionar un artículo")
					return
				confirmar = messagebox.askyesno("Eliminar Artículo", "¿Desea eliminar el articulo seleccionado?")
				if(confirmar == False):
					return
				entry_codigo.config(state = "normal")
				datos = (entry_codigo.get(),)
				tabla = conexion.cursor()
				tabla.execute("DELETE FROM productos WHERE id_producto = ?", datos)
				conexion.commit()
				tabla.close()
				messagebox.showinfo("Eliminar", "Artículo eliminado con éxito")
				borrar_entrys()
				cargar_articulos()

			def limpiar():
				borrar_entrys()

			boton_limpiar = Button(frame_derecho, text = "Limpiar",font = fuente_botones,bg = color_botones, command = limpiar)
			boton_limpiar.pack(pady = 10)
			boton_añadir_producto = Button(frame_inferior, text = "Añadir Producto",font = fuente_botones,bg = color_botones, command = guardar_articulo, image = img_añadir_prod, compound = RIGHT)
			boton_editar_producto = Button(frame_inferior, text = "Editar Producto", font = fuente_botones, bg = color_botones, command = modificar_articulo, image = img_editar_prod, compound = RIGHT)
			boton_eliminar_producto = Button(frame_inferior, text = "Eliminar Producto", font = fuente_botones, bg = color_botones, command = eliminar_articulo, image = img_eliminar, compound = RIGHT)
			boton_eliminar_producto.pack(side = RIGHT, padx = 10, anchor = N)
			boton_editar_producto.pack(side = RIGHT, padx = 10, anchor = N)
			boton_añadir_producto.pack(side = RIGHT, padx = 10, anchor = N)

			def ver_proveedor():
				olvidar_inventario()
				proveedores()
			boton_ver_proveedor = Button(frame_inferior, text = "Ver Proveedores", font = fuente_botones, bg = color_botones, image = img_ver_proveedor, compound = RIGHT, command = ver_proveedor)
			boton_ver_proveedor.pack(side = RIGHT, padx = 10, anchor = N)

			##Cargar Articulos Tabla##
			def cargar_articulos():
				tabla = conexion.cursor()
				tabla.execute("SELECT* FROM productos")
				datos = tabla.fetchall()
				for fila in tabla_inventario.get_children():
					tabla_inventario.delete(fila)
				for dato in datos:
					id_categoria = (dato[1],)
					tabla.execute("SELECT nombre_categoria FROM categorias WHERE id = ?", id_categoria)
					datos_categoria = tabla.fetchall()
					tabla_inventario.insert("", END, text = dato[0], values = (datos_categoria[0][0], dato[2], dato[3], dato[4], dato[5]))
				tabla.close()
			cargar_articulos()
			
			###Buscar productos entry búsqueda###
			def buscar_productos(evento):
				buscar = ("%"+cajon_buscar_productos.get()+"%","%"+cajon_buscar_productos.get()+"%","%"+cajon_buscar_productos.get()+"%")
				tabla = conexion.cursor()
				tabla.execute("SELECT * FROM productos WHERE id_producto LIKE ? OR nombre_producto LIKE ? OR categoria LIKE (SELECT id FROM categorias WHERE nombre_categoria LIKE?)", buscar)
				datos_articulos = tabla.fetchall()
				
				###Borrar Treeview###
				for fila in tabla_inventario.get_children():
					tabla_inventario.delete(fila)
				
				###Reescriir Treeview###
				for dato in datos_articulos:
					id_categoria = (dato[1],)
					tabla.execute("SELECT nombre_categoria FROM categorias WHERE id = ?", id_categoria)
					datos_categoria = tabla.fetchall()
					tabla_inventario.insert("", END, text = dato[0], values = (datos_categoria[0], dato[2], dato[3], dato[4], dato[5]))
				tabla.close()
			cajon_buscar_productos.bind("<KeyRelease>", buscar_productos)

			###Selecciona articulo tabla y pega en entrys derecha###
			def seleccionar_articulo(evento):
				index = tabla_inventario.selection()
				fila = tabla_inventario.item(index)
				codigo = (fila["text"],)
				tabla = conexion.cursor()
				tabla.execute("SELECT * FROM productos WHERE id_producto = ?", codigo)
				datos = tabla.fetchall()
				if(len(datos)<1):
					return
				id_categoria = (datos[0][1],)
				tabla.execute("SELECT nombre_categoria FROM categorias WHERE id = ?", id_categoria)
				datos_categoria = tabla.fetchall()
				tabla.close()
				borrar_entrys()
				entry_codigo.config(state = "normal")
				entry_codigo.insert(END, datos [0][0])
				entry_categoria.insert(END, datos_categoria[0][0])
				entry_producto.insert(END, datos[0][2])
				entry_costo.insert(END, datos[0][3])
				entry_precio_venta.insert(END, datos[0][4])
				entry_stock.insert(END, datos[0][5])
				entry_codigo.config(state = "readonly")
	
			### Borrar Entrys###
			def borrar_entrys():
				entry_codigo.config(state = "normal")
				entry_codigo.delete(0, END)
				entry_categoria.delete(0, END)
				entry_producto.delete(0, END)
				entry_costo.delete(0, END)
				entry_precio_venta.delete(0, END)
				entry_stock.delete(0, END)
				entry_codigo.config(state = "readonly")								
			tabla_inventario.bind("<<TreeviewSelect>>", seleccionar_articulo)

			def olvidar_inventario():
				cinta_superior.forget()
				mensaje_busqueda_productos.forget()
				label_buscar.forget()
				frame_principal.forget()
				cajon_buscar_productos.forget()
				frame_inferior.forget()
				tabla_inventario.forget()
				boton_volver.forget()
				mensaje_seleccione.forget()
				boton_añadir_producto.forget()
				boton_editar_producto.forget()
				boton_eliminar_producto.forget()
				boton_ver_proveedor.forget()
				frame_izquierdo.forget()
				frame_derecho.forget()
				label_codigo.forget()
				entry_codigo.forget()
				label_categoria.forget()
				entry_categoria.forget()
				label_producto.forget()
				entry_producto.forget()
				label_costo.forget()
				entry_costo.forget()
				label_precio_venta.forget()
				entry_precio_venta.forget()
				label_stock.forget()
				entry_stock.forget()
				boton_limpiar.forget()

		def proveedores():
			olvidar_pantalla_principal()
			mensaje_busqueda_proveedores = Label(cinta_superior, bg= color_botones, text = "Búsqueda de Proveedores", font = fuente_principal, fg = "white")
			label_buscar = Label(frame_principal, text = "Elija Código o Nombre", font = fuente_botones, bg = color_fondo, fg = "white")
			cajon_buscar_proveedores = Entry(frame_principal, font = fuente_principal, bg = "gray66")
			frame_principal.pack(fill = BOTH, expand = 1)
			cinta_superior.pack(fill = X, anchor = N)
			mensaje_seleccione = Label (frame_inferior, text = "Click: Seleccionar", font = fuente_principal, bg = color_frames, fg = "white")
			mensaje_busqueda_proveedores.pack()
			label_buscar.pack()
			cajon_buscar_proveedores.pack(ipadx = 200, pady = 10, anchor = N)
			frame_central.pack(fill = BOTH, expand = 1, pady = 20)
			frame_inferior.pack(side = BOTTOM, ipadx = 610, ipady = 30)
			mensaje_seleccione.pack(side = LEFT, padx = 10, anchor = N)
			tabla_proveedores = ttk.Treeview(frame_central, style = "oscuro.Treeview")
			tabla_proveedores.pack(side = TOP, fill = BOTH, expand = 1)
			tabla_proveedores["columns"] = ("Razón Social","Domicilio","Teléfono","E-Mail")
			tabla_proveedores.heading("#0", text = "Número")
			tabla_proveedores.heading("Razón Social", text = "Razón Social")
			tabla_proveedores.heading("Domicilio", text = "Domicilio")
			tabla_proveedores.heading("Teléfono", text = "Teléfono")
			tabla_proveedores.heading("E-Mail", text = "E-Mail")
			tabla_proveedores.column("#0", width = 10)
			tabla_proveedores.column("Razón Social", width = 150)
			tabla_proveedores.column("Domicilio", width = 350)
			tabla_proveedores.column("Teléfono", width = 80)
			tabla_proveedores.column("E-Mail", width = 150)

			###CARGA PROVEEDORES DESDE BD###
			def cargar_proveedores():
				tabla = conexion.cursor()
				tabla.execute("SELECT* FROM proveedores")
				datos = tabla.fetchall()
				for fila in tabla_proveedores.get_children():
					tabla_proveedores.delete(fila)
				for dato in datos:
					tabla_proveedores.insert("", END, text = dato[0], values = (dato[1], dato[2], dato[3],dato[4]))
				tabla.close()
			cargar_proveedores()

			def añadir_proveedor():
				pass
			boton_añadir_proveedor = Button(frame_inferior, bg = color_botones, text = "  Añadir Proveedor  ", font = fuente_botones, command = añadir_proveedor, image = img_añadir_prod, compound = RIGHT)
			boton_añadir_proveedor.pack(side = LEFT, padx = 10, anchor = N)

			def editar_proveedor():
				pass
			boton_editar_proveedor = Button(frame_inferior, bg = color_botones, text = " Editar Proveedor ", font = fuente_botones, command = editar_proveedor, image = img_editar_prod, compound = RIGHT)
			boton_editar_proveedor.pack(side = LEFT, padx = 10, anchor = N)

			def eliminar_proveedor():
				pass
			boton_eliminar_proveedor = Button(frame_inferior, bg = color_botones, text = "Eliminar Proveedor", font = fuente_botones, command = eliminar_proveedor, image = img_eliminar, compound = RIGHT)
			boton_eliminar_proveedor.pack(side = LEFT, padx = 10, anchor = N)

			def volver():
				olvidar_proveedores()
				pantalla_principal()
			boton_volver = Button(frame_inferior, bg = color_botones, text = "Volver", font = fuente_botones, command = volver, image = img_volver, compound = RIGHT)
			boton_volver.pack(side = BOTTOM, anchor = E)

			def olvidar_proveedores():
				cinta_superior.forget()
				mensaje_busqueda_proveedores.forget()
				frame_principal.forget()
				boton_volver.forget()
				label_buscar.forget()
				cajon_buscar_proveedores.forget()
				frame_inferior.forget()
				frame_central.forget()
				mensaje_seleccione.forget()
				boton_añadir_proveedor.forget()
				boton_editar_proveedor.forget()
				boton_eliminar_proveedor.forget()
				tabla_proveedores.forget()

		def reportes():
			olvidar_pantalla_principal()
			mensaje_busqueda_fechas = Label(cinta_superior, bg= color_botones, text = "Módulo Reportes", font = fuente_principal, fg = "white")
			label_buscar = Label(frame_principal, text = "Búsqueda por fecha (formato dd-mm-aaaa)", font = fuente_botones, bg = color_fondo, fg = "white")
			cajon_buscar_reportes = Entry(frame_principal, font = fuente_principal, bg = "gray66")
			frame_principal.pack(fill = BOTH, expand = 1)
			cinta_superior.pack(fill = X, anchor = N)
			mensaje_seleccione = Label (frame_inferior, text = "Click: Seleccionar", font = fuente_principal, bg = color_frames, fg = "white")
			mensaje_busqueda_fechas.pack()
			label_buscar.pack()
			cajon_buscar_reportes.pack(ipadx = 200, pady = 10, anchor = N)
			frame_central.pack(ipadx = 165, ipady = 90, pady = 20)
			frame_inferior.pack(side = BOTTOM, ipadx = 610, ipady = 30)
			mensaje_seleccione.pack(side = LEFT, padx = 10, anchor = N)
			tabla_reportes = ttk.Treeview(frame_central, style = "oscuro.Treeview")
			tabla_reportes.pack(side = TOP, fill = BOTH, expand = 1)
			tabla_reportes["columns"] = ("Fecha y Hora","Total Ticket", "Total IVA","Costo Total","Ganancia")
			tabla_reportes.heading("#0", text = "Número")
			tabla_reportes.heading("Fecha y Hora", text = "Fecha y Hora")
			tabla_reportes.heading("Total Ticket", text = "Total Ticket")
			tabla_reportes.heading("Total IVA", text = "Total IVA")
			tabla_reportes.heading("Costo Total", text = "Costo Total")
			tabla_reportes.heading("Ganancia", text = "Ganancia")
			tabla_reportes.column("#0", width = 10)
			tabla_reportes.column("Fecha y Hora", width = 170)
			tabla_reportes.column("Total Ticket", width = 45)
			tabla_reportes.column("Total IVA", width = 45)
			tabla_reportes.column("Costo Total", width = 45)
			tabla_reportes.column("Ganancia", width = 45)
			
			###CARGA REPORTES DESDE BD###
			def cargar_reportes():
				tabla = conexion.cursor()
				tabla.execute("SELECT* FROM reportes")
				datos = tabla.fetchall()
				for fila in tabla_reportes.get_children():
					tabla_reportes.delete(fila)
				for dato in datos:
					tabla_reportes.insert("", END, text = dato[0], values = (dato[1], dato[2], dato[3], dato[4], dato[5]))
				tabla.close()
			cargar_reportes()

			def ver_ticket():
				pass
			boton_ver_ticket = Button(frame_inferior, bg = color_botones, text = "     Ver Ticket     ", font = fuente_botones, command = ver_ticket, image = img_revisar, compound = RIGHT)
			boton_ver_ticket.pack(side = LEFT, padx = (145,0), anchor = N)

			def imprimir_reporte():
				pass
			boton_imprimir_reporte = Button(frame_inferior, bg = color_botones, text = "Imprimir Reporte", font = fuente_botones, command = imprimir_reporte, image = img_ticket, compound = RIGHT)
			boton_imprimir_reporte.pack(side = LEFT, padx = (20,0), anchor = N)

			def limpiar_pant():
				pass
			boton_limpiar_pant = Button(frame_inferior, bg = color_botones, text = "Limpiar Pantalla", font = fuente_botones, command = limpiar_pant, image = img_borrador, compound = RIGHT)
			boton_limpiar_pant.pack(side = LEFT, padx = (20,0), anchor = N)

			def volver():
				olvidar_reportes()
				pantalla_principal()
			boton_volver = Button(frame_inferior, bg = color_botones, text = "Volver", font = fuente_botones, command = volver, image = img_volver, compound = RIGHT)
			boton_volver.pack(side = BOTTOM, anchor = E)

			def olvidar_reportes():
				cinta_superior.forget()
				mensaje_busqueda_fechas.forget()
				frame_principal.forget()
				boton_volver.forget()
				label_buscar.forget()
				cajon_buscar_reportes.forget()
				frame_inferior.forget()
				frame_central.forget()
				mensaje_seleccione.forget()
				boton_ver_ticket.forget()
				boton_imprimir_reporte.forget()
				boton_limpiar_pant.forget()
				tabla_reportes.forget()

		def ajustes():
			olvidar_pantalla_principal()
			mensaje_ajustes = Label(cinta_superior, bg= color_botones, text = "Seleccione su configuración preferida:", font = fuente_principal, fg = "white")
			cinta_superior.pack(fill = X, anchor = N)
			mensaje_ajustes.pack()
			frame_principal.pack(fill = BOTH, expand = 1)

			def volver():
				olvidar_ajustes()
				pantalla_principal()
			boton_volver = Button(frame_principal, bg = color_botones, text = "Volver", font = fuente_botones, command = volver, image = img_volver, compound = RIGHT)
			boton_volver.pack(side = BOTTOM, anchor = E)

			def olvidar_ajustes():
				cinta_superior.forget()
				mensaje_ajustes.forget()
				frame_principal.forget()
				boton_volver.forget()
		
		olvidar_ventana_acceder()

		fondo_a = Frame(frame_principal, bg = color_fondo)
		fondo_b = Frame(frame_principal, bg = color_fondo)
		fondo_c = Frame(frame_principal, bg = color_fondo)
		cinta_superior = Frame(frame_principal, bg = color_botones)
		mensaje_bienvenido = Label(cinta_superior, bg= color_botones, text = "Bienvenido, seleccione una opción:", font = fuente_principal, fg = "white")
		
		boton1 = Button(fondo_a, bg = color_botones, text = "  Realizar Venta ", command = realizar_venta, image = img_vender, compound = TOP, font = fuente_botones)
		boton2 = Button(fondo_a, bg = color_botones, text = "  Ver Pedidos  ", command = ver_pedidos, image = img_ver_pedidos, compound = TOP, font = fuente_botones)
		boton3 = Button(fondo_a, bg = color_botones, text = " Mis Clientes  ", command = mis_clientes, image = img_clientes, compound = TOP, font = fuente_botones)
		boton4 = Button(fondo_b, bg = color_botones, text = "      Inventario     ", command = inventario, image = img_inventario, compound= TOP, font = fuente_botones)
		boton5 = Button(fondo_b, bg = color_botones, text = "  Proveedores ", command = proveedores, image = img_proveedores, compound = TOP, font = fuente_botones)
		boton6 = Button(fondo_b, bg = color_botones, text = "  Reportes  ", command = reportes, image = img_reportes, compound = TOP, font = fuente_botones)
		boton_ajustes = Button(fondo_c, bg = color_botones, text = "Ajustes   ", command = ajustes, image = img_ajustes, compound = RIGHT, font = fuente_botones)

		frame_principal.pack(fill = BOTH, expand = 1)
		cinta_superior.pack(fill = X, anchor = N)
		mensaje_bienvenido.pack(anchor = N)
		fondo_a.pack(fill = BOTH, expand = 1)
		fondo_b.pack(fill = BOTH, expand = 1)
		fondo_c.pack(side = BOTTOM, fill = X, expand = 1)
		boton1.pack(side = LEFT, anchor = N, pady = 60, padx = 140)
		boton2.pack(side = LEFT, anchor = N, pady = 60, padx = 140)
		boton3.pack(side = LEFT, anchor = N, pady = 60, padx = 140)
		boton4.pack(side = LEFT, anchor = N, pady = 60, padx = 140)
		boton5.pack(side = LEFT, anchor = N, pady = 60, padx = 140)
		boton6.pack(side = LEFT, anchor = N, pady = 60, padx = 138)
		boton_ajustes.pack(side = RIGHT, anchor = E)

		def olvidar_pantalla_principal():
			cinta_superior.forget()
			mensaje_bienvenido.forget()
			fondo_a.forget()
			fondo_b.forget()
			fondo_c.forget()
			boton1.forget()
			boton2.forget()
			boton3.forget()
			boton4.forget()
			boton5.forget()
			boton6.forget()
			boton_ajustes.forget()

	def olvidar_ventana_acceder():
		frame_principal.forget()
		frame_login.forget()
		label_logo.forget()
		label_usuario.forget()
		entry_usuario.forget()
		label_contraseña.forget()
		entry_contraseña.forget()
		boton_acceder.forget()

	misestilos()
	ventana.mainloop()
if __name__ == '__main__':
	ventana(800,600,"zoomed","Compra Express")