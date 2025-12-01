"""
Aplicación Streamlit para Gestión de Tienda Tecnológica con MongoDB
Sistema integrado de visualización, búsqueda y gestión de productos
"""

import streamlit as st
import pandas as pd
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
import config

# Configuración de la página
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon=config.APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
        .main-header {
            color: #1f77b4;
            text-align: center;
            padding: 20px;
            border-bottom: 3px solid #1f77b4;
        }
        .metric-card {
            background-color: #f0f2f6;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .success-message {
            background-color: #d4edda;
            color: #155724;
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .error-message {
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Función para conectar a MongoDB
@st.cache_resource
def conectar_mongodb():
    """Establece conexión con MongoDB"""
    try:
        client = MongoClient(config.MONGODB_URI)
        db = client[config.DATABASE_NAME]
        return db
    except Exception as e:
        st.error(f"❌ Error de conexión: {str(e)}")
        return None

# Función para obtener todos los productos
def obtener_productos(db, filtros=None):
    """Obtiene productos de la base de datos con filtros opcionales"""
    try:
        coleccion = db[config.COLLECTION_NAME]
        if filtros:
            productos = list(coleccion.find(filtros))
        else:
            productos = list(coleccion.find())
        return productos
    except Exception as e:
        st.error(f"Error al obtener productos: {str(e)}")
        return []

# Función para agregar producto
def agregar_producto(db, producto):
    """Agrega un nuevo producto a la base de datos"""
    try:
        coleccion = db[config.COLLECTION_NAME]
        producto["fecha_agregado"] = datetime.now()
        resultado = coleccion.insert_one(producto)
        return True, resultado.inserted_id
    except Exception as e:
        return False, str(e)

# Función para actualizar producto
def actualizar_producto(db, producto_id, datos_actualizados):
    """Actualiza un producto existente"""
    try:
        coleccion = db[config.COLLECTION_NAME]
        resultado = coleccion.update_one(
            {"_id": ObjectId(producto_id)},
            {"$set": datos_actualizados}
        )
        return resultado.modified_count > 0
    except Exception as e:
        st.error(f"Error al actualizar: {str(e)}")
        return False

# Función para eliminar producto
def eliminar_producto(db, producto_id):
    """Elimina un producto de la base de datos"""
    try:
        coleccion = db[config.COLLECTION_NAME]
        resultado = coleccion.delete_one({"_id": ObjectId(producto_id)})
        return resultado.deleted_count > 0
    except Exception as e:
        st.error(f"Error al eliminar: {str(e)}")
        return False

# Función para convertir productos a DataFrame
def productos_a_dataframe(productos):
    """Convierte lista de productos a DataFrame para visualización"""
    if not productos:
        return pd.DataFrame()
    
    datos = []
    for prod in productos:
        datos.append({
            "ID": str(prod["_id"])[:8] + "...",
            "Nombre": prod["nombre"],
            "Categoría": prod["categoria"],
            "Marca": prod["marca"],
            "Precio": f"${prod['precio']:.2f}",
            "Stock": prod["stock"],
            "Rating": f"⭐ {prod['rating']}/5"
        })
    
    return pd.DataFrame(datos)

# ==================== INTERFAZ PRINCIPAL ====================

# Encabezado
st.markdown('<div class="main-header"><h1>🛍️ Tienda Tecnológica - Sistema de Gestión</h1></div>', 
            unsafe_allow_html=True)

# Conectar a la base de datos
db = conectar_mongodb()

if db is None:
    st.error("❌ No se pudo conectar a MongoDB. Asegúrate de que esté ejecutándose.")
    st.stop()

# Barra lateral con opciones
st.sidebar.title("📋 Menú Principal")
opcion = st.sidebar.radio(
    "Selecciona una opción:",
    ["📊 Dashboard", "🔍 Buscar Productos", "➕ Agregar Producto", 
     "✏️ Actualizar Producto", "🗑️ Eliminar Producto"]
)

# ==================== OPCIÓN 1: DASHBOARD ====================
if opcion == "📊 Dashboard":
    st.header("📊 Dashboard de la Tienda")
    
    # Obtener todos los productos
    productos = obtener_productos(db)
    
    if productos:
        # Métricas principales
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total de Productos", len(productos))
        
        with col2:
            precios = [p["precio"] for p in productos]
            st.metric("Precio Promedio", f"${sum(precios)/len(precios):.2f}")
        
        with col3:
            stock_total = sum([p["stock"] for p in productos])
            st.metric("Stock Total", stock_total)
        
        with col4:
            rating_promedio = sum([p["rating"] for p in productos]) / len(productos)
            st.metric("Rating Promedio", f"⭐ {rating_promedio:.1f}/5")
        
        # Separador
        st.divider()
        
        # Productos por categoría
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📂 Productos por Categoría")
            categorias = {}
            for prod in productos:
                cat = prod["categoria"]
                categorias[cat] = categorias.get(cat, 0) + 1
            
            df_categorias = pd.DataFrame(
                list(categorias.items()),
                columns=["Categoría", "Cantidad"]
            )
            st.bar_chart(df_categorias.set_index("Categoría"))
        
        with col2:
            st.subheader("💰 Productos por Rango de Precio")
            rangos = {
                "$0-500": 0,
                "$500-1000": 0,
                "$1000-2000": 0,
                "$2000+": 0
            }
            
            for prod in productos:
                precio = prod["precio"]
                if precio < 500:
                    rangos["$0-500"] += 1
                elif precio < 1000:
                    rangos["$500-1000"] += 1
                elif precio < 2000:
                    rangos["$1000-2000"] += 1
                else:
                    rangos["$2000+"] += 1
            
            df_rangos = pd.DataFrame(
                list(rangos.items()),
                columns=["Rango", "Cantidad"]
            )
            st.bar_chart(df_rangos.set_index("Rango"))
        
        # Separador
        st.divider()
        
        # Top 5 productos más caros
        st.subheader("💎 Top 5 Productos Más Caros")
        top_caros = sorted(productos, key=lambda x: x["precio"], reverse=True)[:5]
        df_caros = pd.DataFrame([
            {
                "Nombre": p["nombre"],
                "Marca": p["marca"],
                "Precio": f"${p['precio']:.2f}",
                "Stock": p["stock"]
            }
            for p in top_caros
        ])
        st.table(df_caros)
        
        # Top 5 productos mejor calificados
        st.subheader("⭐ Top 5 Productos Mejor Calificados")
        top_rating = sorted(productos, key=lambda x: x["rating"], reverse=True)[:5]
        df_rating = pd.DataFrame([
            {
                "Nombre": p["nombre"],
                "Marca": p["marca"],
                "Rating": f"⭐ {p['rating']}/5",
                "Precio": f"${p['precio']:.2f}"
            }
            for p in top_rating
        ])
        st.table(df_rating)
    
    else:
        st.warning("No hay productos en la tienda. Agrega algunos para comenzar.")

# ==================== OPCIÓN 2: BUSCAR PRODUCTOS ====================
elif opcion == "🔍 Buscar Productos":
    st.header("🔍 Buscar Productos")
    
    # Filtros
    col1, col2, col3 = st.columns(3)
    
    with col1:
        categoria_filtro = st.selectbox(
            "Filtrar por Categoría:",
            ["Todas"] + config.CATEGORIAS
        )
    
    with col2:
        nombre_filtro = st.text_input("Buscar por Nombre:")
    
    with col3:
        marca_filtro = st.text_input("Buscar por Marca:")
    
    # Filtro de rango de precio
    col1, col2 = st.columns(2)
    
    with col1:
        precio_min = st.number_input("Precio Mínimo:", min_value=0, value=0)
    
    with col2:
        precio_max = st.number_input("Precio Máximo:", min_value=0, value=5000)
    
    # Construir filtro
    filtro = {}
    
    if categoria_filtro != "Todas":
        filtro["categoria"] = categoria_filtro
    
    if nombre_filtro:
        filtro["nombre"] = {"$regex": nombre_filtro, "$options": "i"}
    
    if marca_filtro:
        filtro["marca"] = {"$regex": marca_filtro, "$options": "i"}
    
    if precio_min > 0 or precio_max < 5000:
        filtro["precio"] = {"$gte": precio_min, "$lte": precio_max}
    
    # Obtener productos filtrados
    productos_filtrados = obtener_productos(db, filtro)
    
    # Mostrar resultados
    st.subheader(f"📦 Resultados: {len(productos_filtrados)} producto(s) encontrado(s)")
    
    if productos_filtrados:
        df = productos_a_dataframe(productos_filtrados)
        st.dataframe(df, use_container_width=True)
        
        # Mostrar detalles de un producto seleccionado
        st.subheader("📋 Detalles del Producto")
        producto_seleccionado = st.selectbox(
            "Selecciona un producto para ver detalles:",
            [p["nombre"] for p in productos_filtrados],
            key="producto_detalle"
        )
        
        if producto_seleccionado:
            prod = next(p for p in productos_filtrados if p["nombre"] == producto_seleccionado)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Nombre:** {prod['nombre']}")
                st.write(f"**Marca:** {prod['marca']}")
                st.write(f"**Categoría:** {prod['categoria']}")
                st.write(f"**Precio:** ${prod['precio']:.2f}")
                st.write(f"**Stock:** {prod['stock']} unidades")
            
            with col2:
                st.write(f"**Rating:** ⭐ {prod['rating']}/5")
                st.write(f"**Descripción:** {prod['descripcion']}")
            
            # Especificaciones
            st.subheader("🔧 Especificaciones")
            for key, value in prod.get("especificaciones", {}).items():
                st.write(f"• **{key.capitalize()}:** {value}")
    
    else:
        st.info(config.MENSAJES["no_resultados"])

# ==================== OPCIÓN 3: AGREGAR PRODUCTO ====================
elif opcion == "➕ Agregar Producto":
    st.header("➕ Agregar Nuevo Producto")
    
    with st.form("form_agregar_producto"):
        col1, col2 = st.columns(2)
        
        with col1:
            nombre = st.text_input("Nombre del Producto *")
            marca = st.text_input("Marca *")
            categoria = st.selectbox("Categoría *", config.CATEGORIAS)
            precio = st.number_input("Precio ($) *", min_value=0.01, step=0.01)
        
        with col2:
            stock = st.number_input("Stock *", min_value=0, step=1)
            rating = st.slider("Rating", min_value=0.0, max_value=5.0, step=0.1)
            descripcion = st.text_area("Descripción *", max_chars=500)
        
        # Especificaciones
        st.subheader("🔧 Especificaciones")
        especificaciones = {}
        
        col1, col2 = st.columns(2)
        
        with col1:
            spec1_key = st.text_input("Especificación 1 (clave)")
            spec1_value = st.text_input("Especificación 1 (valor)")
            if spec1_key and spec1_value:
                especificaciones[spec1_key] = spec1_value
        
        with col2:
            spec2_key = st.text_input("Especificación 2 (clave)")
            spec2_value = st.text_input("Especificación 2 (valor)")
            if spec2_key and spec2_value:
                especificaciones[spec2_key] = spec2_value
        
        # Botón de envío
        submitted = st.form_submit_button("✅ Agregar Producto", use_container_width=True)
        
        if submitted:
            # Validación
            if not nombre or not marca or not descripcion:
                st.error("❌ Por favor completa todos los campos requeridos (*)")
            elif len(nombre) < config.NOMBRE_MIN_LENGTH:
                st.error(f"❌ El nombre debe tener al menos {config.NOMBRE_MIN_LENGTH} caracteres")
            else:
                # Crear documento del producto
                nuevo_producto = {
                    "nombre": nombre,
                    "marca": marca,
                    "categoria": categoria,
                    "precio": precio,
                    "stock": stock,
                    "descripcion": descripcion,
                    "rating": rating,
                    "especificaciones": especificaciones
                }
                
                # Agregar a la base de datos
                exito, resultado = agregar_producto(db, nuevo_producto)
                
                if exito:
                    st.success(config.MENSAJES["producto_agregado"])
                    st.balloons()
                else:
                    st.error(f"❌ Error: {resultado}")

# ==================== OPCIÓN 4: ACTUALIZAR PRODUCTO ====================
elif opcion == "✏️ Actualizar Producto":
    st.header("✏️ Actualizar Producto")
    
    # Obtener lista de productos
    productos = obtener_productos(db)
    
    if productos:
        producto_seleccionado = st.selectbox(
            "Selecciona un producto para actualizar:",
            [p["nombre"] for p in productos],
            key="producto_actualizar"
        )
        
        prod = next(p for p in productos if p["nombre"] == producto_seleccionado)
        
        with st.form("form_actualizar_producto"):
            col1, col2 = st.columns(2)
            
            with col1:
                nuevo_nombre = st.text_input("Nombre", value=prod["nombre"])
                nueva_marca = st.text_input("Marca", value=prod["marca"])
                nueva_categoria = st.selectbox("Categoría", config.CATEGORIAS, 
                                              index=config.CATEGORIAS.index(prod["categoria"]))
                nuevo_precio = st.number_input("Precio ($)", value=prod["precio"], min_value=0.01, step=0.01)
            
            with col2:
                nuevo_stock = st.number_input("Stock", value=prod["stock"], min_value=0, step=1)
                nuevo_rating = st.slider("Rating", value=prod["rating"], min_value=0.0, max_value=5.0, step=0.1)
                nueva_descripcion = st.text_area("Descripción", value=prod["descripcion"], max_chars=500)
            
            submitted = st.form_submit_button("✅ Actualizar Producto", use_container_width=True)
            
            if submitted:
                datos_actualizados = {
                    "nombre": nuevo_nombre,
                    "marca": nueva_marca,
                    "categoria": nueva_categoria,
                    "precio": nuevo_precio,
                    "stock": nuevo_stock,
                    "rating": nuevo_rating,
                    "descripcion": nueva_descripcion
                }
                
                if actualizar_producto(db, str(prod["_id"]), datos_actualizados):
                    st.success(config.MENSAJES["producto_actualizado"])
                    st.rerun()
                else:
                    st.error("❌ Error al actualizar el producto")
    else:
        st.warning("No hay productos para actualizar")

# ==================== OPCIÓN 5: ELIMINAR PRODUCTO ====================
elif opcion == "🗑️ Eliminar Producto":
    st.header("🗑️ Eliminar Producto")
    
    # Obtener lista de productos
    productos = obtener_productos(db)
    
    if productos:
        producto_seleccionado = st.selectbox(
            "Selecciona un producto para eliminar:",
            [p["nombre"] for p in productos],
            key="producto_eliminar"
        )
        
        prod = next(p for p in productos if p["nombre"] == producto_seleccionado)
        
        # Mostrar información del producto
        st.warning(f"⚠️ Estás a punto de eliminar: **{prod['nombre']}**")
        st.write(f"Precio: ${prod['precio']:.2f}")
        st.write(f"Stock: {prod['stock']} unidades")
        
        # Confirmación
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🗑️ Confirmar Eliminación", use_container_width=True, type="primary"):
                if eliminar_producto(db, str(prod["_id"])):
                    st.success(config.MENSAJES["producto_eliminado"])
                    st.rerun()
                else:
                    st.error("❌ Error al eliminar el producto")
        
        with col2:
            if st.button("❌ Cancelar", use_container_width=True):
                st.info("Eliminación cancelada")
    else:
        st.warning("No hay productos para eliminar")

# ==================== PIE DE PÁGINA ====================
st.divider()
st.markdown("""
    <div style="text-align: center; color: #666; font-size: 12px; margin-top: 30px;">
        <p>🛍️ Tienda Tecnológica - Sistema de Gestión | MongoDB + Streamlit</p>
        <p>Proyecto Académico - TECAZUAY | Materia: Marco de Referencia de la Big Data</p>
        <p>Docente: Veronica Chimbo | Estudiante: Alexander Mosquera</p>
    </div>
""", unsafe_allow_html=True)
