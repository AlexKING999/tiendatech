"""
Script de Inicialización de Base de Datos MongoDB
Crea la base de datos, colecciones e inserta datos de ejemplo
"""

from pymongo import MongoClient
from datetime import datetime
from config import MONGODB_URI, DATABASE_NAME, COLLECTION_NAME

def inicializar_base_datos():
    """Inicializa la base de datos con datos de ejemplo"""
    
    try:
        # Conectar a MongoDB
        client = MongoClient(MONGODB_URI)
        db = client[DATABASE_NAME]
        coleccion = db[COLLECTION_NAME]
        
        # Limpiar colección existente (opcional)
        coleccion.delete_many({})
        
        # Datos de ejemplo de productos tecnológicos
        productos_ejemplo = [
            {
                "nombre": "MacBook Pro 16\"",
                "categoria": "Laptops",
                "precio": 2499.99,
                "stock": 8,
                "descripcion": "Laptop profesional de Apple con procesador M3 Max",
                "especificaciones": {
                    "procesador": "Apple M3 Max",
                    "ram": "36GB",
                    "almacenamiento": "1TB SSD",
                    "pantalla": "16 pulgadas Liquid Retina XDR"
                },
                "marca": "Apple",
                "rating": 4.9,
                "fecha_agregado": datetime.now()
            },
            {
                "nombre": "Dell XPS 13",
                "categoria": "Laptops",
                "precio": 1299.99,
                "stock": 12,
                "descripcion": "Ultrabook compacto y potente de Dell",
                "especificaciones": {
                    "procesador": "Intel Core i7-13700H",
                    "ram": "16GB DDR5",
                    "almacenamiento": "512GB SSD NVMe",
                    "pantalla": "13.4 pulgadas OLED"
                },
                "marca": "Dell",
                "rating": 4.7,
                "fecha_agregado": datetime.now()
            },
            {
                "nombre": "Lenovo ThinkPad X1",
                "categoria": "Laptops",
                "precio": 1199.99,
                "stock": 15,
                "descripcion": "Laptop empresarial confiable de Lenovo",
                "especificaciones": {
                    "procesador": "Intel Core i5-1335U",
                    "ram": "16GB",
                    "almacenamiento": "512GB SSD",
                    "pantalla": "14 pulgadas FHD"
                },
                "marca": "Lenovo",
                "rating": 4.6,
                "fecha_agregado": datetime.now()
            },
            {
                "nombre": "iPhone 15 Pro Max",
                "categoria": "Smartphones",
                "precio": 1199.99,
                "stock": 20,
                "descripcion": "Smartphone premium de Apple con cámara avanzada",
                "especificaciones": {
                    "procesador": "Apple A17 Pro",
                    "ram": "8GB",
                    "almacenamiento": "256GB",
                    "pantalla": "6.7 pulgadas Super Retina XDR"
                },
                "marca": "Apple",
                "rating": 4.8,
                "fecha_agregado": datetime.now()
            },
            {
                "nombre": "Samsung Galaxy S24 Ultra",
                "categoria": "Smartphones",
                "precio": 1299.99,
                "stock": 18,
                "descripcion": "Flagship de Samsung con pantalla AMOLED y cámara 200MP",
                "especificaciones": {
                    "procesador": "Snapdragon 8 Gen 3",
                    "ram": "12GB",
                    "almacenamiento": "512GB",
                    "pantalla": "6.8 pulgadas AMOLED 120Hz"
                },
                "marca": "Samsung",
                "rating": 4.7,
                "fecha_agregado": datetime.now()
            },
            {
                "nombre": "Google Pixel 8 Pro",
                "categoria": "Smartphones",
                "precio": 999.99,
                "stock": 14,
                "descripcion": "Smartphone con IA integrada y excelente cámara",
                "especificaciones": {
                    "procesador": "Google Tensor G3",
                    "ram": "12GB",
                    "almacenamiento": "256GB",
                    "pantalla": "6.7 pulgadas OLED 120Hz"
                },
                "marca": "Google",
                "rating": 4.6,
                "fecha_agregado": datetime.now()
            },
            {
                "nombre": "iPad Pro 12.9\"",
                "categoria": "Tablets",
                "precio": 1099.99,
                "stock": 10,
                "descripcion": "Tablet profesional de Apple con M2",
                "especificaciones": {
                    "procesador": "Apple M2",
                    "ram": "8GB",
                    "almacenamiento": "256GB",
                    "pantalla": "12.9 pulgadas Liquid Retina XDR"
                },
                "marca": "Apple",
                "rating": 4.8,
                "fecha_agregado": datetime.now()
            },
            {
                "nombre": "Samsung Galaxy Tab S9 Ultra",
                "categoria": "Tablets",
                "precio": 1199.99,
                "stock": 8,
                "descripcion": "Tablet premium de Samsung con pantalla AMOLED",
                "especificaciones": {
                    "procesador": "Snapdragon 8 Gen 2",
                    "ram": "12GB",
                    "almacenamiento": "512GB",
                    "pantalla": "14.6 pulgadas AMOLED"
                },
                "marca": "Samsung",
                "rating": 4.7,
                "fecha_agregado": datetime.now()
            },
            {
                "nombre": "AirPods Pro Max",
                "categoria": "Accesorios",
                "precio": 549.99,
                "stock": 25,
                "descripcion": "Auriculares premium con cancelación de ruido",
                "especificaciones": {
                    "procesador": "Apple H1",
                    "tipo": "Over-ear",
                    "bateria": "20 horas",
                    "caracteristicas": "Cancelación de ruido, Audio espacial"
                },
                "marca": "Apple",
                "rating": 4.7,
                "fecha_agregado": datetime.now()
            },
            {
                "nombre": "Sony WH-1000XM5",
                "categoria": "Accesorios",
                "precio": 399.99,
                "stock": 30,
                "descripcion": "Auriculares inalámbricos con mejor cancelación de ruido",
                "especificaciones": {
                    "procesador": "Sony HD Noise Cancelling",
                    "tipo": "Over-ear",
                    "bateria": "30 horas",
                    "caracteristicas": "Cancelación de ruido, Bluetooth 5.3"
                },
                "marca": "Sony",
                "rating": 4.8,
                "fecha_agregado": datetime.now()
            },
            {
                "nombre": "Procesador Intel Core i9-13900K",
                "categoria": "Componentes",
                "precio": 589.99,
                "stock": 5,
                "descripcion": "Procesador de alto rendimiento para gaming y workstations",
                "especificaciones": {
                    "nucleos": "24 cores (8P+16E)",
                    "velocidad": "5.8 GHz",
                    "socket": "LGA1700",
                    "tdp": "125W"
                },
                "marca": "Intel",
                "rating": 4.6,
                "fecha_agregado": datetime.now()
            },
            {
                "nombre": "Tarjeta Gráfica RTX 4090",
                "categoria": "Componentes",
                "precio": 1599.99,
                "stock": 3,
                "descripcion": "GPU de gama alta para gaming y rendering",
                "especificaciones": {
                    "memoria": "24GB GDDR6X",
                    "arquitectura": "Ada",
                    "velocidad": "2.52 GHz",
                    "potencia": "450W"
                },
                "marca": "NVIDIA",
                "rating": 4.9,
                "fecha_agregado": datetime.now()
            },
            {
                "nombre": "Memoria RAM DDR5 32GB",
                "categoria": "Componentes",
                "precio": 149.99,
                "stock": 40,
                "descripcion": "Memoria RAM de alta velocidad DDR5",
                "especificaciones": {
                    "capacidad": "32GB",
                    "velocidad": "6000 MHz",
                    "latencia": "30-36 ns",
                    "voltaje": "1.25V"
                },
                "marca": "Corsair",
                "rating": 4.5,
                "fecha_agregado": datetime.now()
            }
        ]
        
        # Insertar datos
        resultado = coleccion.insert_many(productos_ejemplo)
        
        print(f"✅ Base de datos inicializada exitosamente")
        print(f"📊 Se insertaron {len(resultado.inserted_ids)} productos")
        print(f"🗄️  Base de datos: {DATABASE_NAME}")
        print(f"📦 Colección: {COLLECTION_NAME}")
        
        # Crear índices para optimizar búsquedas
        coleccion.create_index("nombre")
        coleccion.create_index("categoria")
        coleccion.create_index("precio")
        coleccion.create_index("marca")
        
        print("📑 Índices creados para optimizar búsquedas")
        
        # Mostrar estadísticas
        total_productos = coleccion.count_documents({})
        print(f"\n📈 Estadísticas Iniciales:")
        print(f"   Total de productos: {total_productos}")
        
        # Estadísticas por categoría
        categorias = coleccion.distinct("categoria")
        print(f"\n📂 Productos por Categoría:")
        for categoria in categorias:
            cantidad = coleccion.count_documents({"categoria": categoria})
            print(f"   {categoria}: {cantidad} productos")
        
        client.close()
        
    except Exception as e:
        print(f"❌ Error al inicializar la base de datos: {str(e)}")
        print("Asegúrate de que MongoDB esté ejecutándose en localhost:27017")

if __name__ == "__main__":
    inicializar_base_datos()
