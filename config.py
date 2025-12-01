# Configuración de MongoDB y la Aplicación

# Configuración de Conexión a MongoDB
# MONGODB_URI = "mongodb://localhost:27017/"  # Para MongoDB local
MONGODB_URI = "mongodb+srv://alex:1234@cluster0.k6zxwgc.mongodb.net/?appName=Cluster0"  # Para MongoDB Atlas

DATABASE_NAME = "tienda_tecnologica"
COLLECTION_NAME = "productos"

# Configuración de la Aplicación Streamlit
APP_TITLE = "Tienda Tecnológica - Sistema de Gestión"
APP_ICON = "🛍️"

# Configuración de Interfaz
ITEMS_PER_PAGE = 10
THEME = "light"

# Categorías de Productos
CATEGORIAS = [
    "Laptops",
    "Smartphones",
    "Tablets",
    "Accesorios",
    "Componentes"
]

# Rangos de Precio
PRECIO_MIN = 0
PRECIO_MAX = 5000

# Configuración de Validación
NOMBRE_MIN_LENGTH = 3
NOMBRE_MAX_LENGTH = 100
DESCRIPCION_MAX_LENGTH = 500
PRECIO_MIN_VALOR = 0.01
STOCK_MIN_VALOR = 0

# Mensajes de la Aplicación
MENSAJES = {
    "bienvenida": "Bienvenido al Sistema de Gestión de Tienda Tecnológica",
    "producto_agregado": "✅ Producto agregado exitosamente",
    "producto_actualizado": "✅ Producto actualizado exitosamente",
    "producto_eliminado": "✅ Producto eliminado exitosamente",
    "error_conexion": "❌ Error al conectar con la base de datos",
    "error_validacion": "❌ Error en la validación de datos",
    "no_resultados": "No se encontraron productos con los criterios especificados"
}
