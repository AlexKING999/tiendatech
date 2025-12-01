# Guía de Instalación y Uso - Tienda Tecnológica MongoDB

## 🚀 Inicio Rápido

### Requisitos del Sistema

- **Python:** 3.8 o superior
- **MongoDB:** Versión 4.4 o superior (local o MongoDB Atlas)
- **Sistema Operativo:** Windows, macOS o Linux
- **Espacio en Disco:** Mínimo 500MB

### Instalación en 5 Pasos

#### Paso 1: Clonar o Descargar el Proyecto

```bash
# Crear carpeta del proyecto
mkdir tienda_tech_mongodb
cd tienda_tech_mongodb

# Copiar los archivos del proyecto en esta carpeta
```

#### Paso 2: Crear Entorno Virtual (Recomendado)

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

#### Paso 4: Configurar MongoDB

**Opción A: MongoDB Local**

```bash
# Windows - Descargar desde: https://www.mongodb.com/try/download/community
# macOS - Usar Homebrew
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community

# Linux - Seguir guía oficial
# https://docs.mongodb.com/manual/installation/
```

**Opción B: MongoDB Atlas (Recomendado)**

1. Ir a [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Crear cuenta gratuita
3. Crear un cluster
4. Obtener cadena de conexión
5. Reemplazar en `config.py`:

```python
MONGODB_URI = "mongodb+srv://usuario:contraseña@cluster.mongodb.net/"
```

#### Paso 5: Inicializar Base de Datos

```bash
python init_database.py
```

Deberías ver:

```
✅ Base de datos inicializada exitosamente
📊 Se insertaron 12 productos
🗄️  Base de datos: tienda_tecnologica
📦 Colección: productos
📑 Índices creados para optimizar búsquedas

📈 Estadísticas Iniciales:
   Total de productos: 12

📂 Productos por Categoría:
   Laptops: 3 productos
   Smartphones: 3 productos
   Tablets: 2 productos
   Accesorios: 2 productos
   Componentes: 2 productos
```

#### Paso 6: Ejecutar la Aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en `http://localhost:8501`

## 📱 Uso de la Aplicación

### Dashboard (📊)

**Descripción:** Panel de control con estadísticas generales de la tienda.

**Funcionalidades:**
- Visualización de métricas clave (total de productos, precio promedio, stock total, rating promedio)
- Gráfico de productos por categoría
- Gráfico de productos por rango de precio
- Top 5 productos más caros
- Top 5 productos mejor calificados

**Cómo usar:**
1. Selecciona "📊 Dashboard" en el menú lateral
2. Visualiza las estadísticas automáticamente
3. Usa los gráficos para análisis rápido

### Buscar Productos (🔍)

**Descripción:** Busca y filtra productos con múltiples criterios.

**Filtros disponibles:**
- Categoría (Laptops, Smartphones, Tablets, Accesorios, Componentes)
- Nombre del producto
- Marca
- Rango de precio (mínimo y máximo)

**Cómo usar:**
1. Selecciona "🔍 Buscar Productos" en el menú
2. Aplica los filtros deseados
3. Visualiza resultados en tabla
4. Haz clic en un producto para ver detalles completos
5. Consulta especificaciones técnicas

**Ejemplo de búsqueda:**
- Categoría: Laptops
- Rango de precio: $1000 - $2000
- Resultado: Muestra laptops en ese rango

### Agregar Producto (➕)

**Descripción:** Agrega nuevos productos a la tienda.

**Campos requeridos:**
- Nombre del producto (mínimo 3 caracteres)
- Marca
- Categoría
- Precio
- Stock
- Descripción
- Rating (0-5 estrellas)

**Especificaciones opcionales:**
- Hasta 2 especificaciones técnicas personalizadas

**Cómo usar:**
1. Selecciona "➕ Agregar Producto"
2. Completa todos los campos requeridos
3. Agrega especificaciones si es necesario
4. Haz clic en "✅ Agregar Producto"
5. Verás confirmación de éxito

**Ejemplo de producto:**
```
Nombre: Samsung Galaxy A54
Marca: Samsung
Categoría: Smartphones
Precio: $449.99
Stock: 25
Descripción: Smartphone de gama media con excelente cámara
Rating: 4.5
Especificaciones:
  - Procesador: Exynos 1280
  - Pantalla: 6.4" AMOLED
```

### Actualizar Producto (✏️)

**Descripción:** Modifica información de productos existentes.

**Campos modificables:**
- Nombre
- Marca
- Categoría
- Precio
- Stock
- Rating
- Descripción

**Cómo usar:**
1. Selecciona "✏️ Actualizar Producto"
2. Elige el producto a modificar
3. Edita los campos necesarios
4. Haz clic en "✅ Actualizar Producto"
5. Verás confirmación de cambios

**Caso de uso común:**
- Actualizar stock después de una venta
- Cambiar precio por promoción
- Modificar descripción o especificaciones

### Eliminar Producto (🗑️)

**Descripción:** Elimina productos de la tienda.

**Precauciones:**
- Muestra confirmación antes de eliminar
- Muestra detalles del producto a eliminar
- Opción para cancelar la operación

**Cómo usar:**
1. Selecciona "🗑️ Eliminar Producto"
2. Elige el producto a eliminar
3. Revisa la información mostrada
4. Haz clic en "🗑️ Confirmar Eliminación"
5. El producto se elimina inmediatamente

## 🔧 Configuración Avanzada

### Modificar Categorías

En `config.py`, edita:

```python
CATEGORIAS = [
    "Laptops",
    "Smartphones",
    "Tablets",
    "Accesorios",
    "Componentes",
    "Monitores",  # Agregar nueva categoría
    "Periféricos"  # Agregar nueva categoría
]
```

### Cambiar Rango de Precios

En `config.py`:

```python
PRECIO_MIN = 0
PRECIO_MAX = 10000  # Aumentar límite máximo
```

### Personalizar Mensajes

En `config.py`:

```python
MENSAJES = {
    "bienvenida": "Tu mensaje personalizado",
    # ... más mensajes
}
```

### Usar MongoDB Atlas

En `config.py`:

```python
MONGODB_URI = "mongodb+srv://usuario:contraseña@cluster0.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "tienda_tecnologica"
```

## 🐛 Solución de Problemas

### Error: "Connection refused"

**Problema:** No se puede conectar a MongoDB

**Solución:**
```bash
# Verificar que MongoDB esté ejecutándose
# Windows: Abrir Services y buscar MongoDB
# macOS: brew services list
# Linux: sudo systemctl status mongod

# Si no está ejecutándose:
# macOS: brew services start mongodb-community
# Linux: sudo systemctl start mongod
```

### Error: "ModuleNotFoundError: No module named 'pymongo'"

**Problema:** Dependencias no instaladas

**Solución:**
```bash
pip install -r requirements.txt
```

### Error: "Database already exists"

**Problema:** Base de datos ya inicializada

**Solución:**
```bash
# Ejecutar init_database.py nuevamente (borra datos anteriores)
python init_database.py

# O conectar a MongoDB y eliminar manualmente:
# db.tienda_tecnologica.drop()
```

### Aplicación Streamlit lenta

**Problema:** Rendimiento bajo

**Soluciones:**
1. Crear índices en MongoDB: `db.productos.create_index("nombre")`
2. Limitar número de productos mostrados
3. Usar filtros más específicos
4. Verificar conexión a MongoDB

### Error de validación al agregar producto

**Problema:** Campos rechazados

**Verificar:**
- Nombre tiene al menos 3 caracteres
- Precio es mayor a 0
- Stock es un número entero
- Descripción no está vacía
- Descripción tiene menos de 500 caracteres

## 📊 Consultas Útiles en MongoDB

### Obtener todos los productos

```python
db.productos.find()
```

### Contar productos

```python
db.productos.count_documents({})
```

### Obtener precio promedio

```python
db.productos.aggregate([
    {"$group": {"_id": None, "promedio": {"$avg": "$precio"}}}
])
```

### Productos sin stock

```python
db.productos.find({"stock": 0})
```

### Ordenar por precio descendente

```python
db.productos.find().sort("precio", -1)
```

### Buscar por expresión regular

```python
db.productos.find({"nombre": {"$regex": "iPhone", "$options": "i"}})
```

## 📈 Mejoras Futuras Sugeridas

1. **Autenticación de usuarios** - Agregar login
2. **Carrito de compras** - Sistema de pedidos
3. **Historial de cambios** - Auditoría de modificaciones
4. **Reportes PDF** - Exportar datos
5. **Gráficos avanzados** - Análisis de ventas
6. **API REST** - Integración con otras aplicaciones
7. **Notificaciones** - Alertas de stock bajo
8. **Multi-idioma** - Soporte para varios idiomas

## 📞 Soporte y Recursos

- **MongoDB Docs:** https://docs.mongodb.com/
- **Streamlit Docs:** https://docs.streamlit.io/
- **PyMongo Docs:** https://pymongo.readthedocs.io/
- **Stack Overflow:** https://stackoverflow.com/questions/tagged/mongodb

## ✅ Checklist de Instalación

- [ ] Python 3.8+ instalado
- [ ] MongoDB instalado o cuenta Atlas creada
- [ ] Repositorio clonado/descargado
- [ ] Entorno virtual creado y activado
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] MongoDB ejecutándose
- [ ] Base de datos inicializada (`python init_database.py`)
- [ ] Aplicación ejecutándose (`streamlit run app.py`)
- [ ] Navegador abierto en `http://localhost:8501`

---

**¡Listo! Ya puedes usar el sistema de Tienda Tecnológica con MongoDB y Streamlit.**

Para preguntas o problemas, consulta la documentación oficial o los recursos listados arriba.

**Proyecto Académico - TECAZUAY**
**Materia:** Marco de Referencia de la Big Data
**Docente:** Veronica Chimbo
**Estudiante:** Alexander Mosquera
