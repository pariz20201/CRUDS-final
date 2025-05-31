import flet as ft
import mysql.connector
from mysql.connector import Error
from datetime import datetime


current_sale_items_list = []
sale_items_display_column = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
total_sale_amount_text = ft.Text("Total: $0.00", size=16, weight="bold")

dropdown_articulos_venta = ft.Dropdown(label="Artículo", hint_text="Seleccione un artículo", expand=True)
txt_cantidad_articulo_venta = ft.TextField(label="Cantidad", keyboard_type=ft.KeyboardType.NUMBER, value="1", width=100)
txt_codigo_barras_venta = ft.TextField(label="Código de Barras", width=200, on_submit=lambda e: add_item_to_sale(e, from_barcode=True))
dropdown_clientes_generales_venta = ft.Dropdown(label="Cliente General ID", hint_text="Seleccione ID cliente general")
dropdown_metodos_pago_venta = ft.Dropdown(label="Método de Pago", hint_text="Seleccione método")
dropdown_cajas_venta = ft.Dropdown(label="Caja", hint_text="Seleccione caja")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pariz2020",
            database="bat-store2"
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        pass
    return None



def cerrar_dialogo(page: ft.Page):
    if page.dialog:
        page.dialog.open = False
        page.update()

def ver_usuarios(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM articulo")
    registros = cursor.fetchall()
    result = "\n".join([str(row) for row in registros])
    cursor.close()
    return result

def insertar_usuario(conexion, nombre, precio, reorden, codigo_barras):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO articulo (codigo_barras, nombre, precio, reorden) VALUES (%s, %s, %s, %s)", 
                   (codigo_barras, nombre, precio, reorden))
    conexion.commit()
    cursor.close()
    return "Artículo insertado correctamente"

def actualizar_usuario(conexion, nombre_nuevo, codigo_barras):
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE articulo SET nombre = %s WHERE codigo_barras = %s", (nombre_nuevo, codigo_barras))
        conexion.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        if affected_rows > 0:
            return "Artículo actualizado correctamente"
        else:
            return "Artículo no encontrado o sin cambios."
    except Error as e:
        return f"Error al actualizar artículo: {e}"

def eliminar_usuario(conexion, codigo_barras):
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM articulo WHERE codigo_barras = %s", (codigo_barras,))
        conexion.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        if affected_rows > 0:
            return "Artículo eliminado correctamente"
        else:
            return "Artículo no encontrado para eliminar."
    except Error as e:
        return f"Error al eliminar artículo: {e}"

def ver_proveedores(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM proveedor")
    registros = cursor.fetchall()
    result = "\n".join([str(row) for row in registros])
    cursor.close()
    return result

def insertar_proveedor(conexion, idProveedor, nombre, telefono, direccion):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO proveedor (idProveedor, nombre, telefono, direccion) VALUES (%s, %s, %s, %s)", 
                   (idProveedor, nombre, telefono, direccion))
    conexion.commit()
    cursor.close()
    return "Proveedor insertado correctamente"

def actualizar_proveedor(conexion, nombre_nuevo, telefono):
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE proveedor SET nombre = %s WHERE telefono = %s", (nombre_nuevo, telefono))
        conexion.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        if affected_rows > 0: return "Proveedor actualizado correctamente"
        else: return "Proveedor no encontrado o sin cambios."
    except Error as e:
        return f"Error al actualizar proveedor: {e}"

def eliminar_proveedor(conexion, idProveedor):
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM proveedor WHERE idProveedor = %s", (idProveedor,))
        conexion.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        if affected_rows > 0: return "Proveedor eliminado correctamente"
        else: return "Proveedor no encontrado para eliminar."
    except Error as e:
        return f"Error al eliminar proveedor: {e}"

def ver_cliente(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM cliente")
    registros = cursor.fetchall()
    result = "\n".join([str(row) for row in registros])
    cursor.close()
    return result

def insertar_cliente(conexion, idCliente, nombre):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO cliente (idCliente, nombre) VALUES (%s, %s)", (idCliente, nombre))
    conexion.commit()
    cursor.close()
    return "Clienet insertado correctamente"

def actualizar_cliente(conexion, nuevo_nombre, idCliente):
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE cliente SET Nombre = %s WHERE idCliente = %s", (nuevo_nombre, idCliente))
        conexion.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        if affected_rows > 0: return "Cliente actualizado correctamente"
        else: return "Cliente no encontrado o sin cambios."
    except Error as e:
        return f"Error al actualizar cliente: {e}"

def eliminar_cliente(conexion, idCliente):
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM cliente WHERE idCliente = %s", (idCliente,))
        conexion.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        if affected_rows > 0: return "Cliente eliminado correctamente"
        else: return "Cliente no encontrado para eliminar."
    except Error as e:
        return f"Error al eliminar cliente: {e}"

def ver_empleados(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM empleado")
    registros = cursor.fetchall()
    result = "\n".join([str(row) for row in registros])
    cursor.close()
    return result

def insertar_empleado(conexion, idEmpleado, nombre, numero, puesto):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO empleado (idEmpleado, nombre, numero, puesto) VALUES (%s, %s, %s, %s)", 
                   (idEmpleado, nombre, numero, puesto))
    conexion.commit()
    cursor.close()
    return "Empleado insertado correctamente"

def actualizar_empleado(conexion, idEmpleado, nuevo_nombre):
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE empleado SET nombre = %s WHERE idEmpleado = %s", (nuevo_nombre, idEmpleado))
        conexion.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        if affected_rows > 0: return "Empleado actualizado correctamente"
        else: return "Empleado no encontrado o sin cambios."
    except Error as e:
        return f"Error al actualizar empleado: {e}"

def eliminar_empleado(conexion, idEmpleado):
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM empleado WHERE idEmpleado = %s", (idEmpleado,))
        conexion.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        if affected_rows > 0: return "Empleado eliminado correctamente"
        else: return "Empleado no encontrado para eliminar."
    except Error as e:
        return f"Error al eliminar empleado: {e}"

def get_articulos_para_venta(conexion):
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT codigo_barras, Nombre, Precio FROM Articulo")
    articulos = cursor.fetchall()
    cursor.close()
    return articulos

def get_clientes_generales_para_venta(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT idCliente FROM `cliente_general`")
    clientes = cursor.fetchall()
    cursor.close()
    return clientes

def get_metodos_pago_para_venta(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM metodo_de_pago")
    metodos = cursor.fetchall()
    cursor.close()
    return metodos


def get_cajas_para_venta(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT idcaja, Empleado_idEmpleado FROM caja")
    cajas = cursor.fetchall()
    cursor.close()
    return cajas

def registrar_nueva_venta_db(conexion, fecha, total, cliente_general_id, metodo_pago_id, caja_id):
    cursor = conexion.cursor()
    sql = "INSERT INTO Venta (fecha, total, `cliente general_idCliente`, `Metodo de pago_idMetodo de pago`, caja_idcaja) VALUES (%s, %s, %s, %s, %s)"
    val = (fecha, total, cliente_general_id, metodo_pago_id, caja_id)
    cursor.execute(sql, val)
    conexion.commit()
    venta_id = cursor.lastrowid
    cursor.close()
    return venta_id

def registrar_detalle_venta_db(conexion, venta_id, articulo_codigo_barras, cantidad, precio_unitario):
    cursor = conexion.cursor()
    sql = "INSERT INTO `detalle_venta` (Venta_idVenta, Articulo_codigo_barras, cantidad, precio_unitario) VALUES (%s, %s, %s, %s)"
    val = (venta_id, articulo_codigo_barras, cantidad, precio_unitario)
    conexion.commit()
    cursor.close()

# --- Nueva función para obtener o crear cliente general diario ---
def get_or_create_daily_general_client(db_conn):
    fecha_actual_str = datetime.now().strftime('%Y-%m-%d')
    cliente_general_id = None
    cursor = None
    try:
        cursor = db_conn.cursor()
        
        # 1. Intentar encontrar el cliente general para la fecha actual
        cursor.execute("SELECT idCliente FROM `cliente_general` WHERE nombre = %s", (f"Cliente General {fecha_actual_str}",))
        result = cursor.fetchone()

        if result:
            cliente_general_id = result[0]
        else:
            # 2. Si no existe, crearlo
            cursor.execute("INSERT INTO `cliente_general` (nombre) VALUES (%s)", (f"Cliente General {fecha_actual_str}",))
            db_conn.commit()
            cliente_general_id = cursor.lastrowid # Obtener el ID del cliente recién insertado
            
    except Error as db_err:
        print(f"[TERMINAL] Error en la base de datos al obtener/crear cliente general diario: {db_err}")
    except Exception as ex:
        print(f"[TERMINAL] Excepción al obtener/crear cliente general diario: {ex}")
    finally:
        if cursor:
            cursor.close()
    return cliente_general_id


def main(page: ft.Page):
    page.title = "Sistema BAT-STORE"
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    contenedor_acciones_articulos = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    contenedor_acciones_proveedores = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    contenedor_acciones_clientes = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    contenedor_acciones_empleados = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    contenedor_acciones_ventas = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)

    def mostrar_mensaje(mensaje):
        page.open( ft.AlertDialog(title=ft.Text("Resultado"), content=ft.Text(mensaje)))
        page.dialog.open = True
        page.update()


    def acciones_articulos(e, action):
        conexion = conectar()
        contenedor_acciones_articulos.controls.clear()

        if action == "ver":
            result = ver_usuarios(conexion)
            mostrar_mensaje(result)
            db_conn_ver = None
            try:
                db_conn_ver = conectar()
                if db_conn_ver is None:
                    return
                result = ver_usuarios(db_conn_ver)
                mostrar_mensaje(result)
            except Exception as ex_v:
                pass
            finally:
                if db_conn_ver and db_conn_ver.is_connected():
                    db_conn_ver.close()
        
        elif action == "insertar":
            nombre = ft.TextField(label="Nombre del artículo", width=300)
            precio = ft.TextField(label="Precio", keyboard_type=ft.KeyboardType.NUMBER, width=300)
            reorden = ft.TextField(label="Punto de Reorden", width=300)
            codigo = ft.TextField(label="Código de barras (13 chars)", width=300, max_length=13)

            def insertar_click(e_insert):
                conexion = None
                try:
                    conexion = conectar()
                    if conexion is None:
                        return
                    r = insertar_usuario(conexion, nombre.value, float(precio.value), reorden.value, codigo.value)
                    if "correctamente" in r.lower(): contenedor_acciones_articulos.controls.clear(); page.update()
                except Exception as ex_op:
                    pass
                finally:
                    if conexion and conexion.is_connected():
                        conexion.close()
            contenedor_acciones_articulos.controls.extend([nombre, precio, reorden, codigo, ft.ElevatedButton("Insertar Artículo", on_click=insertar_click, icon=ft.Icons.ADD)])

        elif action == "actualizar":
            nuevo_nombre = ft.TextField(label="Nuevo nombre", width=300)
            codigo = ft.TextField(label="Código de barras del artículo a actualizar", width=300)
            def actualizar_click(e_update):
                conexion = None
                try:
                    conexion = conectar()
                    if conexion is None:
                        return
                    r = actualizar_usuario(conexion, nuevo_nombre.value, codigo.value)
                    if "correctamente" in r.lower(): contenedor_acciones_articulos.controls.clear(); page.update()
                except Exception as ex_op:
                    pass
                finally:
                    if conexion and conexion.is_connected():
                        conexion.close()
            contenedor_acciones_articulos.controls.extend([codigo, nuevo_nombre, ft.ElevatedButton("Actualizar Artículo", on_click=actualizar_click, icon=ft.Icons.EDIT)])

        elif action == "eliminar":
            codigo = ft.TextField(label="Código de barras del artículo a eliminar", width=300)
            def eliminar_click(e_delete):
                conexion = None
                try:
                    conexion = conectar()
                    if conexion is None:
                        return
                    r = eliminar_usuario(conexion, codigo.value)
                    if "correctamente" in r.lower(): contenedor_acciones_articulos.controls.clear(); page.update()
                except Exception as ex_op:
                    pass
                finally:
                    if conexion and conexion.is_connected():
                        conexion.close()
            contenedor_acciones_articulos.controls.extend([codigo, ft.ElevatedButton("Eliminar Artículo", on_click=eliminar_click, icon=ft.Icons.DELETE, bgcolor=ft.Colors.RED_ACCENT, color=ft.Colors.WHITE)])
        page.update()

    def acciones_proveedores(e, action):
        contenedor_acciones_proveedores.controls.clear()
        if action == "ver":
            db_conn_ver = None
            try:
                db_conn_ver = conectar()
                if db_conn_ver is None:
                    return
                result = ver_proveedores(db_conn_ver)
                mostrar_mensaje(result)
            finally:
                if db_conn_ver and db_conn_ver.is_connected(): db_conn_ver.close()
        elif action == "insertar":
            idprov = ft.TextField(label="ID Proveedor", width=300)
            nombre = ft.TextField(label="Nombre", width=300)
            telefono = ft.TextField(label="Teléfono (10 dígitos)", width=300, max_length=10)
            direccion = ft.TextField(label="Dirección", width=300)
            def insertar_click(e_insert):
                conexion = None
                try:
                    conexion = conectar()
                    if conexion is None: mostrar_mensaje(page, "Error de conexión.", success=False); return
                    r = insertar_proveedor(conexion, idprov.value, nombre.value, telefono.value, direccion.value)
                    if "correctamente" in r.lower(): contenedor_acciones_proveedores.controls.clear(); page.update()
                finally:
                    if conexion and conexion.is_connected(): conexion.close()
            contenedor_acciones_proveedores.controls.extend([idprov, nombre, telefono, direccion, ft.ElevatedButton("Insertar Proveedor", on_click=insertar_click, icon=ft.Icons.ADD)])
        elif action == "actualizar":
            nuevo_nombre = ft.TextField(label="Nuevo nombre", width=300)
            telefono = ft.TextField(label="Teléfono del proveedor a actualizar", width=300)
            def actualizar_click(e_update):
                conexion = None
                try:
                    conexion = conectar()
                    if conexion is None: mostrar_mensaje(page, "Error de conexión.", success=False); return
                    r = actualizar_proveedor(conexion, nuevo_nombre.value, telefono.value)
                    mostrar_mensaje(page, r, success="correctamente" in r.lower() or "sin cambios" in r.lower())
                    if "correctamente" in r.lower(): contenedor_acciones_proveedores.controls.clear(); page.update()
                finally:
                    if conexion and conexion.is_connected(): conexion.close()
            contenedor_acciones_proveedores.controls.extend([telefono, nuevo_nombre, ft.ElevatedButton("Actualizar Proveedor", on_click=actualizar_click, icon=ft.Icons.EDIT)])
        elif action == "eliminar":
            idprov = ft.TextField(label="ID Proveedor a eliminar", width=300)
            def eliminar_click(e_delete):
                conexion = None
                try:
                    conexion = conectar()
                    if conexion is None: mostrar_mensaje(page, "Error de conexión.", success=False); return
                    r = eliminar_proveedor(conexion, idprov.value)
                    mostrar_mensaje(page, r, success="correctamente" in r.lower())
                    if "correctamente" in r.lower(): contenedor_acciones_proveedores.controls.clear(); page.update()
                finally:
                    if conexion and conexion.is_connected(): conexion.close()
            contenedor_acciones_proveedores.controls.extend([idprov, ft.ElevatedButton("Eliminar Proveedor", on_click=eliminar_click, icon=ft.Icons.DELETE, bgcolor=ft.Colors.RED_ACCENT, color=ft.Colors.WHITE)])
        page.update()

    def acciones_clientes(e, action):
        contenedor_acciones_clientes.controls.clear()
        if action == "ver":
            db_conn_ver = None
            try:
                db_conn_ver = conectar()
                if db_conn_ver is None: mostrar_mensaje(page, "Error de conexión.", success=False); return
                result = ver_cliente(db_conn_ver)
                mostrar_mensaje(result)
            finally:
                if db_conn_ver and db_conn_ver.is_connected(): db_conn_ver.close()
        elif action == "insertar":
            idcliente = ft.TextField(label="IdCliente", width=300)
            nombre = ft.TextField(label="Nombre", width=300)
            telefono_cliente = ft.TextField(label="Teléfono (10 dígitos)", width=300, max_length=10)
            def insertar_click(e_insert):
                conexion = None
                try:
                    conexion = conectar()
                    if conexion is None: mostrar_mensaje(page, "Error de conexión.", success=False); return
                    r = insertar_cliente(conexion, idcliente.value, nombre.value)
                    mostrar_mensaje(page, r, success="correctamente" in r.lower())
                    if "correctamente" in r.lower(): contenedor_acciones_clientes.controls.clear(); page.update()
                finally:
                    if conexion and conexion.is_connected(): conexion.close()
            contenedor_acciones_clientes.controls.extend([idcliente, nombre, telefono_cliente, ft.ElevatedButton("Insertar Cliente", on_click=insertar_click, icon=ft.Icons.PERSON_ADD)])
        elif action == "actualizar":
            idcliente = ft.TextField(label="IdCliente a actualizar", width=300)
            nuevo_nombre = ft.TextField(label="Nuevo nombre", width=300)
            def actualizar_click(e_update):
                conexion = None
                try:
                    conexion = conectar()
                    if conexion is None: mostrar_mensaje(page, "Error de conexión.", success=False); return
                    r = actualizar_cliente(conexion, nuevo_nombre.value, idcliente.value)
                    mostrar_mensaje(page, r, success="correctamente" in r.lower() or "sin cambios" in r.lower())
                    if "correctamente" in r.lower(): contenedor_acciones_clientes.controls.clear(); page.update()
                finally:
                    if conexion and conexion.is_connected(): conexion.close()
            contenedor_acciones_clientes.controls.extend([idcliente, nuevo_nombre, ft.ElevatedButton("Actualizar Cliente", on_click=actualizar_click, icon=ft.Icons.EDIT)])
        elif action == "eliminar":
            idcliente = ft.TextField(label="IdCliente a eliminar", width=300)
            def eliminar_click(e_delete):
                conexion = None
                try:
                    conexion = conectar()
                    if conexion is None: mostrar_mensaje(page, "Error de conexión.", success=False); return
                    r = eliminar_cliente(conexion, idcliente.value)
                    mostrar_mensaje(page, r, success="correctamente" in r.lower())
                    if "correctamente" in r.lower(): contenedor_acciones_clientes.controls.clear(); page.update()
                finally:
                    if conexion and conexion.is_connected(): conexion.close()
            contenedor_acciones_clientes.controls.extend([idcliente, ft.ElevatedButton("Eliminar Cliente", on_click=eliminar_click, icon=ft.Icons.PERSON_REMOVE, bgcolor=ft.Colors.RED_ACCENT, color=ft.Colors.WHITE)])
        page.update()

    def acciones_empleados(e, action):
        contenedor_acciones_empleados.controls.clear()
        if action == "ver":
            db_conn_ver = None
            try:
                db_conn_ver = conectar()
                if db_conn_ver is None: mostrar_mensaje(page, "Error de conexión.", success=False); return
                result = ver_empleados(db_conn_ver)
                mostrar_mensaje(result)
            finally:
                if db_conn_ver and db_conn_ver.is_connected(): db_conn_ver.close()
        elif action == "insertar":
            idEmp = ft.TextField(label="ID Empleado", width=300)
            nombre = ft.TextField(label="Nombre", width=300)
            numero = ft.TextField(label="Número", width=300)
            puesto = ft.TextField(label="Puesto", width=300)
            def insertar_click(e_insert):
                conexion = None
                try:
                    conexion = conectar()
                    if conexion is None: mostrar_mensaje(page, "Error de conexión.", success=False); return
                    r = insertar_empleado(conexion, idEmp.value, nombre.value, numero.value, puesto.value)
                    mostrar_mensaje(page, r, success="correctamente" in r.lower())
                    if "correctamente" in r.lower(): contenedor_acciones_empleados.controls.clear(); page.update()
                finally:
                    if conexion and conexion.is_connected(): conexion.close()
            contenedor_acciones_empleados.controls.extend([idEmp, nombre, numero, puesto, ft.ElevatedButton("Insertar Empleado", on_click=insertar_click, icon=ft.Icons.ADD)])
        elif action == "actualizar":
            idEmp = ft.TextField(label="ID Empleado a Actualizar", width=300)
            nuevo_nombre = ft.TextField(label="Nuevo nombre", width=300)
            def actualizar_click(e_update):
                conexion = None
                try:
                    conexion = conectar()
                    if conexion is None: mostrar_mensaje(page, "Error de conexión.", success=False); return
                    r = actualizar_empleado(conexion, idEmp.value, nuevo_nombre.value)
                    mostrar_mensaje(page, r, success="correctamente" in r.lower() or "sin cambios" in r.lower())
                    if "correctamente" in r.lower(): contenedor_acciones_empleados.controls.clear(); page.update()
                finally:
                    if conexion and conexion.is_connected(): conexion.close()
            contenedor_acciones_empleados.controls.extend([idEmp, nuevo_nombre, ft.ElevatedButton("Actualizar Empleado", on_click=actualizar_click, icon=ft.Icons.EDIT)])
        elif action == "eliminar":
            idEmp = ft.TextField(label="ID Empleado a Eliminar", width=300)
            def eliminar_click(e_delete):
                conexion = None
                try:
                    conexion = conectar()
                    if conexion is None: mostrar_mensaje(page, "Error de conexión.", success=False); return
                    r = eliminar_empleado(conexion, idEmp.value)
                    mostrar_mensaje(page, r, success="correctamente" in r.lower())
                    if "correctamente" in r.lower(): contenedor_acciones_empleados.controls.clear(); page.update()
                finally:
                    if conexion and conexion.is_connected(): conexion.close()
            contenedor_acciones_empleados.controls.extend([idEmp, ft.ElevatedButton("Eliminar Empleado", on_click=eliminar_click, icon=ft.Icons.DELETE, bgcolor=ft.Colors.RED_ACCENT, color=ft.Colors.WHITE)])
        page.update()

    def update_sale_display_and_total():
        global total_sale_amount_text, sale_items_display_column, current_sale_items_list
        sale_items_display_column.controls.clear()
        current_total = 0.0
        for item_idx, item in enumerate(current_sale_items_list):
            sale_items_display_column.controls.append(
                ft.Row([
                    ft.Text(f"{item['nombre']} (x{item['cantidad']})", expand=True),
                    ft.Text(f"${item['subtotal']:.2f}")
                ])
            )
            current_total += item['subtotal']
        total_sale_amount_text.value = f"Total: ${current_total:.2f}"
        page.update()


    def add_item_to_sale(e, from_barcode=False):
        global current_sale_items_list, dropdown_articulos_venta, txt_cantidad_articulo_venta, txt_codigo_barras_venta
        
        selected_articulo_codigo = ""
        if from_barcode: # Si la llamada viene del on_submit del campo de código de barras
            selected_articulo_codigo = txt_codigo_barras_venta.value.strip()
        
        # Si el campo de código de barras está vacío o la llamada no vino del on_submit, intenta con el dropdown
        if not selected_articulo_codigo:
            selected_articulo_codigo = dropdown_articulos_venta.value
        
        if not selected_articulo_codigo:
            mostrar_mensaje("Por favor, seleccione un artículo o ingrese un código de barras.")
            return

        cantidad_str = txt_cantidad_articulo_venta.value

        try:
            cantidad = int(cantidad_str)
            if cantidad <= 0:
                mostrar_mensaje("La cantidad debe ser un número positivo.")
                return
        except ValueError:
            mostrar_mensaje("La cantidad debe ser un número válido.")
            return
        
        nombre_articulo = None
        precio_unitario = None

        selected_option = next((opt for opt in dropdown_articulos_venta.options if opt.key == selected_articulo_codigo), None)
        if selected_option and hasattr(selected_option, 'data') and 'precio' in selected_option.data and 'nombre' in selected_option.data:
            precio_unitario = selected_option.data['precio']
            nombre_articulo = selected_option.data['nombre']
        else: 
            db_conn_fallback = None
            try:
                db_conn_fallback = conectar()
                if db_conn_fallback:
                    cursor_temp = db_conn_fallback.cursor(dictionary=True)
                    cursor_temp.execute("SELECT Nombre, Precio FROM Articulo WHERE codigo_barras = %s", (selected_articulo_codigo,))
                    articulo_db = cursor_temp.fetchone()
                    cursor_temp.close()
                    if articulo_db:
                        nombre_articulo = articulo_db['Nombre']
                        precio_unitario = float(articulo_db['Precio'])
                    else:
                        mostrar_mensaje(f"Artículo con código '{selected_articulo_codigo}' no encontrado.")
                        return
                else:
                    mostrar_mensaje("Error de conexión a la base de datos para obtener el artículo.")
                    return
            except Exception as ex_db:
                mostrar_mensaje(f"Error al buscar artículo en BD: {ex_db}")
                return
            finally:
                if db_conn_fallback and db_conn_fallback.is_connected():
                    db_conn_fallback.close()
        
        if nombre_articulo is None or precio_unitario is None:
            mostrar_mensaje(f"No se pudo obtener la información completa del artículo '{selected_articulo_codigo}'.")
            return

        existing_item = next((item for item in current_sale_items_list if item['codigo_barras'] == selected_articulo_codigo), None)
        if existing_item:
            existing_item['cantidad'] += cantidad
            existing_item['subtotal'] = existing_item['cantidad'] * existing_item['precio_unitario']
        else:
            current_sale_items_list.append({
                'codigo_barras': selected_articulo_codigo,
                'nombre': nombre_articulo,
                'cantidad': cantidad,
                'precio_unitario': precio_unitario,
                'subtotal': cantidad * precio_unitario
            })
        
        update_sale_display_and_total()
        txt_cantidad_articulo_venta.value = "1"
        txt_codigo_barras_venta.value = "" # Limpia el campo de código de barras
        txt_codigo_barras_venta.focus() # Vuelve el foco al campo para el siguiente escaneo/ingreso
        page.update()

    def finalize_sale(e):
        global current_sale_items_list, total_sale_amount_text
        global dropdown_clientes_generales_venta, dropdown_metodos_pago_venta, dropdown_cajas_venta

        if not current_sale_items_list:
            mostrar_mensaje("No hay artículos en la venta para finalizar.")
            return

        cliente_id = dropdown_clientes_generales_venta.value
        metodo_pago_id = dropdown_metodos_pago_venta.value
        caja_id = dropdown_cajas_venta.value

        if not cliente_id or not metodo_pago_id or not caja_id:
            mostrar_mensaje("Faltan datos para finalizar la venta (Cliente, Método de Pago o Caja).")
            return

        db_conn_sale = None
        try:
            db_conn_sale = conectar()
            if not db_conn_sale:
                mostrar_mensaje("Error de conexión a la base de datos al finalizar venta.")
                return

            current_total_numeric = float(total_sale_amount_text.value.split("$")[1])
            fecha_actual = datetime.now().strftime('%Y-%m-%d')

            venta_id = registrar_nueva_venta_db(db_conn_sale, fecha_actual, current_total_numeric, cliente_id, metodo_pago_id, caja_id)

            if not venta_id:
                return 
            
            for item in current_sale_items_list:
                registrar_detalle_venta_db(db_conn_sale, venta_id, item['codigo_barras'], item['cantidad'], item['precio_unitario'])
            
            current_sale_items_list.clear()
            update_sale_display_and_total()

        except Error as db_err:
            mostrar_mensaje(f"Error en la base de datos durante la finalización de la venta: {db_err}")
        except Exception as ex:
            mostrar_mensaje(f"Ocurrió una excepción general durante la finalización de la venta: {ex}")
        finally:
            if db_conn_sale and db_conn_sale.is_connected():
                db_conn_sale.close()
        page.update()

    def populate_venta_dropdowns():
        global dropdown_articulos_venta, dropdown_clientes_generales_venta, dropdown_metodos_pago_venta, dropdown_cajas_venta
        db_conn_populate = None
        try:
            db_conn_populate = conectar()
            if not db_conn_populate:
                return

            articulos_data = get_articulos_para_venta(db_conn_populate)
            dropdown_articulos_venta.options = [
                ft.dropdown.Option(
                    key=art['codigo_barras'], 
                    text=f"{art['Nombre']} - ${art['Precio']:.2f}",
                    data={'precio': float(art['Precio']), 'nombre': art['Nombre']}
                ) for art in articulos_data
            ]

            clientes_g_data = get_clientes_generales_para_venta(db_conn_populate)
            dropdown_clientes_generales_venta.options = [ft.dropdown.Option(key=str(cg[0]), text=f"ID Cliente Gen: {cg[0]}") for cg in clientes_g_data]
            if not clientes_g_data: dropdown_clientes_generales_venta.hint_text = "No hay clientes generales."

            metodos_p_data = get_metodos_pago_para_venta(db_conn_populate)
            dropdown_metodos_pago_venta.options = [ft.dropdown.Option(key=str(mp[0]), text=mp[1]) for mp in metodos_p_data]
            if not metodos_p_data: dropdown_metodos_pago_venta.hint_text = "No hay métodos de pago."

            cajas_data = get_cajas_para_venta(db_conn_populate)
            dropdown_cajas_venta.options = [ft.dropdown.Option(key=str(c[0]), text=f"Caja ID: {c[0]} (Emp: {c[1]})") for c in cajas_data]
            if not cajas_data: dropdown_cajas_venta.hint_text = "No hay cajas."

            # --- Lógica para auto-asignar cliente general diario ---
            daily_client_id = get_or_create_daily_general_client(db_conn_populate)
            if daily_client_id:
                # Asegúrate de que la opción del cliente diario esté en el dropdown si aún no lo está
                if not any(opt.key == str(daily_client_id) for opt in dropdown_clientes_generales_venta.options):
                    dropdown_clientes_generales_venta.options.append(ft.dropdown.Option(key=str(daily_client_id), text=f"Cliente General {datetime.now().strftime('%Y-%m-%d')}"))
                dropdown_clientes_generales_venta.value = str(daily_client_id) # Preseleccionar
            else:
                mostrar_mensaje("No se pudo obtener o crear el cliente general diario. Por favor, seleccione uno manualmente.")


        except Exception as e_pop:
            pass
        finally:
            if db_conn_populate and db_conn_populate.is_connected():
                db_conn_populate.close()
        page.update()

    # --- Tab Definitions ---
    def tab_articulos_content():
        return ft.Column([
            ft.Text("Gestión de Artículos", size=24, weight="bold"),
            ft.Row([
                ft.ElevatedButton("Ver Artículos", icon=ft.Icons.LIST_ALT, on_click=lambda e: acciones_articulos(e, "ver")),
                ft.ElevatedButton("Insertar Artículo", icon=ft.Icons.ADD, on_click=lambda e: acciones_articulos(e, "insertar")),
                ft.ElevatedButton("Actualizar Artículo", icon=ft.Icons.EDIT, on_click=lambda e: acciones_articulos(e, "actualizar")),
                ft.ElevatedButton("Eliminar Artículo", icon=ft.Icons.DELETE, on_click=lambda e: acciones_articulos(e, "eliminar"), bgcolor=ft.Colors.RED_200),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Divider(),
            contenedor_acciones_articulos
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)

    def tab_proveedores_content():
        return ft.Column([
            ft.Text("Gestión de Proveedores", size=24, weight="bold"),
            ft.Row([
                ft.ElevatedButton("Ver Proveedores", icon=ft.Icons.LIST_ALT, on_click=lambda e: acciones_proveedores(e, "ver")),
                ft.ElevatedButton("Insertar Proveedor", icon=ft.Icons.ADD, on_click=lambda e: acciones_proveedores(e, "insertar")),
                ft.ElevatedButton("Actualizar Proveedor", icon=ft.Icons.EDIT, on_click=lambda e: acciones_proveedores(e, "actualizar")),
                ft.ElevatedButton("Eliminar Proveedor", icon=ft.Icons.DELETE, on_click=lambda e: acciones_proveedores(e, "eliminar"), bgcolor=ft.Colors.RED_200),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Divider(),
            contenedor_acciones_proveedores
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)

    def tab_clientes_content():
        return ft.Column([
            ft.Text("Gestión de Clientes", size=24, weight="bold"),
            ft.Row([
                ft.ElevatedButton("Ver Clientes", icon=ft.Icons.PEOPLE_ALT, on_click=lambda e: acciones_clientes(e, "ver")),
                ft.ElevatedButton("Insertar Cliente", icon=ft.Icons.PERSON_ADD, on_click=lambda e: acciones_clientes(e, "insertar")),
                ft.ElevatedButton("Actualizar Cliente", icon=ft.Icons.EDIT, on_click=lambda e: acciones_clientes(e, "actualizar")),
                ft.ElevatedButton("Eliminar Cliente", icon=ft.Icons.PERSON_REMOVE, on_click=lambda e: acciones_clientes(e, "eliminar"), bgcolor=ft.Colors.RED_200),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Divider(),
            contenedor_acciones_clientes
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)

    def tab_empleados_content():
        return ft.Column([
            ft.Text("Gestión de Empleados", size=24, weight="bold"),
            ft.Row([
                ft.ElevatedButton("Ver Empleados", icon=ft.Icons.BADGE, on_click=lambda e: acciones_empleados(e, "ver")),
                ft.ElevatedButton("Insertar Empleado", icon=ft.Icons.ADD, on_click=lambda e: acciones_empleados(e, "insertar")),
                ft.ElevatedButton("Actualizar Empleado", icon=ft.Icons.EDIT, on_click=lambda e: acciones_empleados(e, "actualizar")),
                ft.ElevatedButton("Eliminar Empleado", icon=ft.Icons.DELETE, on_click=lambda e: acciones_empleados(e, "eliminar"), bgcolor=ft.Colors.RED_200),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Divider(),
            contenedor_acciones_empleados
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)

    def tab_ventas_content():
        global sale_items_display_column, total_sale_amount_text
        global dropdown_articulos_venta, txt_cantidad_articulo_venta, txt_codigo_barras_venta
        global dropdown_clientes_generales_venta, dropdown_metodos_pago_venta, dropdown_cajas_venta
        
        populate_venta_dropdowns() 

        return ft.Column([
            ft.Text("Registrar Nueva Venta", size=24, weight="bold"),
            ft.Row([dropdown_clientes_generales_venta, dropdown_metodos_pago_venta, dropdown_cajas_venta], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(),
            ft.Text("Añadir Artículos a la Venta:", size=18, weight="bold"),
            ft.Column([ # Agrupamos los campos de entrada de artículo en una columna
                ft.Row([
                    dropdown_articulos_venta,
                    txt_cantidad_articulo_venta,
                    ft.IconButton(icon=ft.Icons.ADD_SHOPPING_CART, on_click=add_item_to_sale, tooltip="Añadir Artículo (desde lista)")
                ], alignment=ft.MainAxisAlignment.START, spacing=10),
                ft.Row([
                    txt_codigo_barras_venta,
                    ft.ElevatedButton("Añadir por Código", on_click=lambda e: add_item_to_sale(e, from_barcode=True), icon=ft.Icons.BARCODE_READER)
                ], alignment=ft.MainAxisAlignment.START, spacing=10),
            ]),
            ft.Container(
                content=sale_items_display_column,
                border=ft.border.all(1, ft.Colors.OUTLINE),
                border_radius=5,
                padding=10,
                height=200,
                expand=False
            ),
            ft.Row([total_sale_amount_text], alignment=ft.MainAxisAlignment.END),
            ft.ElevatedButton("Finalizar y Registrar Venta", icon=ft.Icons.POINT_OF_SALE, on_click=finalize_sale, width=300, height=50, style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_ACCENT_700, color=ft.Colors.WHITE)),
            contenedor_acciones_ventas
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15, expand=True)

    # --- Initialize Tabs ---
    def on_tab_change(e):
        # Si la pestaña de Ventas (índice 4) es seleccionada, repopular dropdowns
        if tabs_control.selected_index == 4: 
            populate_venta_dropdowns()

    tabs_control = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Artículos", icon=ft.Icons.INVENTORY_2, content=tab_articulos_content()),
            ft.Tab(text="Proveedores", icon=ft.Icons.LOCAL_SHIPPING, content=tab_proveedores_content()),
            ft.Tab(text="Clientes", icon=ft.Icons.PEOPLE, content=tab_clientes_content()),
            ft.Tab(text="Empleados", icon=ft.Icons.BADGE, content=tab_empleados_content()),
            ft.Tab(text="Ventas", icon=ft.Icons.POINT_OF_SALE, content=tab_ventas_content()),
        ],
        expand=True,
        on_change=on_tab_change
    )

    page.add(ft.Container(tabs_control, expand=True, padding=10))
    page.update()

ft.app(target=main)