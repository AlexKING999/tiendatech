# Caso Práctico: Tienda Tecnológica con MongoDB y Streamlit

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema de gestión de tienda tecnológica utilizando **MongoDB** como base de datos y **Streamlit** como interfaz de usuario. El sistema permite visualizar, buscar, filtrar y gestionar productos tecnológicos de forma sencilla e intuitiva.

## 🏗️ Arquitectura del Sistema

### Base de Datos MongoDB

La base de datos `tienda_tecnologica` contiene una colección principal `productos` con la siguiente estructura:

```json
{
  "_id": ObjectId,
  "nombre": "String",
  "categoria": "String",
  "precio": Number,
  "stock": Number,
  "descripcion": "String",
  "especificaciones": {
    "procesador": "String",
    "ram": "String",
    "almacenamiento": "String",
    "pantalla": "String"
  },
  "marca": "String",
  "rating": Number,
  "fecha_agregado": Date
}
```

### Categorías de Productos

El sistema gestiona las siguientes categorías de productos tecnológicos:

- **Laptops:** Computadoras portátiles de diferentes marcas
- **Smartphones:** Teléfonos inteligentes con especificaciones variadas
- **Tablets:** Dispositivos portátiles de pantalla táctil
- **Accesorios:** Periféricos y accesorios tecnológicos
- **Componentes:** Partes individuales para computadoras

## 🚀 Instalación y Configuración

### Requisitos Previos

- Python 3.8 o superior
- MongoDB instalado y ejecutándose localmente (o acceso a MongoDB Atlas)
- pip (gestor de paquetes de Python)

### Paso 1: Instalar Dependencias

```bash
pip install pymongo streamlit pandas
```

### Paso 2: Configurar MongoDB

Si usas MongoDB localmente, asegúrate de que esté ejecutándose:

```bash
# En Windows
mongod

# En macOS/Linux
brew services start mongodb-community
```

Para usar **MongoDB Atlas** (nube), reemplaza la cadena de conexión en el código.

### Paso 3: Ejecutar el Script de Inicialización

```bash
python init_database.py
```

Este script crea la base de datos, la colección y carga datos de ejemplo.

### Paso 4: Ejecutar la Aplicación Streamlit

```bash
streamlit run app.py
```

La aplicación se abrirá en `http://localhost:8501`

## 📊 Funcionalidades de la Aplicación

### 1. Visualización de Productos

Muestra todos los productos disponibles en la tienda en un formato de tabla interactiva con información completa.

### 2. Filtrado por Categoría

Permite filtrar productos por categoría (Laptops, Smartphones, Tablets, Accesorios, Componentes).

### 3. Búsqueda por Nombre

Busca productos por nombre o parte del nombre en tiempo real.

### 4. Filtrado por Rango de Precio

Filtra productos dentro de un rango de precio específico.

### 5. Estadísticas de la Tienda

Muestra métricas clave como:
- Total de productos
- Promedio de precios
- Producto más caro
- Producto más barato
- Stock total disponible

### 6. Agregar Nuevo Producto

Formulario para agregar nuevos productos a la tienda con validación de datos.

### 7. Actualizar Producto

Permite modificar la información de productos existentes.

### 8. Eliminar Producto

Opción para eliminar productos de la tienda.

## 📝 Estructura de Archivos

```
tienda_tech_mongodb/
├── README.md                 # Este archivo
├── app.py                    # Aplicación Streamlit principal
├── init_database.py          # Script para inicializar la base de datos
├── config.py                 # Configuración de conexión a MongoDB
└── requirements.txt          # Dependencias del proyecto
```

## 💻 Código Principal

### config.py - Configuración de Conexión

```python
# Configuración de MongoDB
MONGODB_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "tienda_tecnologica"
COLLECTION_NAME = "productos"
```

### init_database.py - Inicialización de Datos

Este script crea la base de datos con productos de ejemplo listos para usar.

### app.py - Aplicación Streamlit

La aplicación principal que proporciona la interfaz de usuario para gestionar la tienda.

## 🔍 Ejemplos de Consultas MongoDB

### Obtener todos los productos

```python
productos = db.productos.find()
```

### Buscar por categoría

```python
laptops = db.productos.find({"categoria": "Laptops"})
```

### Filtrar por rango de precio

```python
productos_baratos = db.productos.find({"precio": {"$gte": 500, "$lte": 1500}})
```

### Buscar por nombre

```python
resultado = db.productos.find({"nombre": {"$regex": "MacBook", "$options": "i"}})
```

### Obtener productos con stock disponible

```python
con_stock = db.productos.find({"stock": {"$gt": 0}})
```

### Ordenar por precio

```python
ordenados = db.productos.find().sort("precio", 1)  # 1 = ascendente, -1 = descendente
```

## 🎯 Casos de Uso Prácticos

### Caso 1: Buscar Laptops en Rango de Precio

El gerente de la tienda necesita encontrar todas las laptops entre $1000 y $2000 para una promoción especial.

```python
laptops_promocion = db.productos.find({
    "categoria": "Laptops",
    "precio": {"$gte": 1000, "$lte": 2000}
})
```

### Caso 2: Actualizar Stock Después de una Venta

Después de vender un producto, se debe actualizar el stock.

```python
db.productos.update_one(
    {"_id": ObjectId("...")},
    {"$inc": {"stock": -1}}
)
```

### Caso 3: Agregar Nuevo Producto

Cuando llega un nuevo producto a la tienda, se registra en la base de datos.

```python
nuevo_producto = {
    "nombre": "iPhone 15 Pro",
    "categoria": "Smartphones",
    "precio": 999,
    "stock": 15,
    "descripcion": "Último modelo de Apple",
    "marca": "Apple",
    "rating": 4.8,
    "fecha_agregado": datetime.now()
}
db.productos.insert_one(nuevo_producto)
```

## 🔐 Consideraciones de Seguridad

Para un entorno de producción, se recomienda:

1. **Usar MongoDB Atlas** con autenticación segura
2. **Implementar validación de entrada** en todos los formularios
3. **Usar variables de entorno** para credenciales sensibles
4. **Implementar control de acceso** basado en roles
5. **Encriptar datos sensibles** en tránsito y en reposo

## 📈 Posibles Mejoras Futuras

- Implementar autenticación de usuarios
- Agregar carrito de compras
- Sistema de órdenes y facturas
- Análisis de ventas y reportes
- Integración con pasarelas de pago
- Sistema de recomendaciones basado en IA
- Sincronización con inventario en tiempo real

## 🤝 Contribuciones

Este proyecto es educativo y está diseñado para demostrar la integración de MongoDB con Streamlit. Se anima a modificar y extender el código según sea necesario.

## 📞 Soporte

Para preguntas o problemas, consulta la documentación oficial:

- [MongoDB Documentation](https://docs.mongodb.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [PyMongo Documentation](https://pymongo.readthedocs.io/)

---

**Proyecto Académico - TECAZUAY**
**Materia:** Marco de Referencia de la Big Data
**Docente:** Veronica Chimbo
**Estudiante:** Alexander Mosquera
