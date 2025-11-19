Especificación de Estructura JSON para Propiedades
📋 Estructura General
El archivo properties.json debe contener un array de objetos, donde cada objeto representa una propiedad inmobiliaria.

json
[
  {
    "id_temporal": "P001",
    "titulo": "Título de la propiedad",
    // ... más campos
  },
  {
    "id_temporal": "P002", 
    "titulo": "Otra propiedad",
    // ... más campos
  }
]
🔧 Campos Requeridos
Identificación y Título
id_temporal (String) - ID único de la propiedad
titulo (String) - Título descriptivo del anuncio
Ubicación
barrio (String) - Nombre del barrio
direccion (String) - Dirección completa con número
Características Básicas
tipo (String) - Tipo de propiedad: "Departamento", "Casa", "Oficina", "Local", "Ph", "Terreno"
operacion (String) - Tipo de operación: "Venta" o "Alquiler"
precio (Number) - Precio numérico (sin símbolos de moneda)
moneda_precio (String) - Moneda del precio: "USD" o "ARS"
Detalles de la Propiedad
ambientes (Number) - Número de ambientes/habitaciones
metros_cuadrados (Number) - Superficie en metros cuadrados
piso (Number|String) - Número de piso o "PB" (planta baja)
antiguedad (Number) - Años de antigüedad de la propiedad
Características Técnicas
estado (String) - Estado: "Excelente", "Muy bueno", "Bueno", "Regular"
orientacion (String) - Orientación: "Norte", "Sur", "Este", "Oeste", "Noreste", etc.
expensas (Number) - Monto de expensas mensuales
moneda_expensas (String) - Moneda de las expensas: "USD" o "ARS"
🔄 Campos Opcionales
Amenities y Características
amenities (Array[String]) - Lista de amenities: "Gimnasio", "SUM", "Pileta", "Seguridad 24hs", "Laundry", "Parrilla", etc.
caracteristicas (Array[String]) - Características adicionales: "Luminoso", "Amoblado", "Vista abierta", etc.
Características Especiales (Boolean)
cochera (Boolean) - Si tiene cochera
balcon (Boolean) - Si tiene balcón
pileta (Boolean) - Si tiene pileta (propia o del edificio)
acepta_mascotas (Boolean) - Si acepta mascotas
aire_acondicionado (Boolean) - Si tiene aire acondicionado
Información Adicional
descripcion (String) - Descripción detallada de la propiedad
fecha_publicacion (String) - Fecha en formato YYYY-MM-DD
info_adicional (String) - Información extra o notas especiales
fotos (Array[String]) - Array de URLs de imágenes de la propiedad
📝 Ejemplo Completo
json
{
  "id_temporal": "P001",
  "titulo": "Moderno Departamento en Microcentro",
  "barrio": "Microcentro",
  "precio": 45000,
  "moneda_precio": "USD",
  "ambientes": 3,
  "metros_cuadrados": 75,
  "operacion": "Venta",
  "tipo": "Departamento",
  "descripcion": "Excelente departamento en ubicación privilegiada del Microcentro...",
  "direccion": "Av. Corrientes 1234, Piso 5",
  "antiguedad": 15,
  "estado": "Excelente",
  "orientacion": "Noreste",
  "piso": 5,
  "expensas": 150,
  "moneda_expensas": "ARS",
  "amenities": ["Gimnasio", "SUM", "Seguridad 24hs", "Laundry"],
  "cochera": true,
  "balcon": true,
  "pileta": false,
  "acepta_mascotas": true,
  "aire_acondicionado": true,
  "caracteristicas": ["Luminoso", "Piso parquet", "Vista abierta", "Apto profesional"],
  "fecha_publicacion": "2024-10-15",
  "info_adicional": "Apto créditos. No apto Perrissinotto",
  "fotos": [
    "https://example.com/fotos/P001-1.jpg",
    "https://example.com/fotos/P001-2.jpg",
    "https://example.com/fotos/P001-3.jpg"
  ]
}
🎯 Valos Típicos
Tipos de Propiedad
"Departamento", "Casa", "Oficina", "Local", "Ph", "Terreno", "Cocheras", "Depósito"
Operaciones
"Venta", "Alquiler", "Alquiler temporario"
Estados
"Excelente", "Muy bueno", "Bueno", "Regular", "A reciclar"
Orientaciones
"Norte", "Sur", "Este", "Oeste", "Noreste", "Noroeste", "Sureste", "Suroeste"
Amenities Comunes
"Gimnasio", "SUM", "Pileta", "Seguridad 24hs", "Laundry", "Parrilla", "Quincho", 
"Jardín", "Terraza", "Balcón", "Estacionamiento", "Recepción", "Estacionamiento"
⚠️ Notas Importantes
1.
Moneda: Siempre especifica la moneda (USD o ARS) para precio y expensas
2.
Fechas: Usa formato YYYY-MM-DD para fechas
3.
Números: No uses comas ni símbolos de moneda, solo números
4.
Booleanos: Usa true o false (no "si", "no", etc.)
5.
Arrays: Para campos múltiples usa arrays de strings
6.
URLs: Las URLs de fotos deben ser completas (https://...)
7.
Caracteres especiales: Evita caracteres especiales en JSON
🔄 Compatibilidad
El sistema está diseñado para trabajar con esta estructura de datos. Si falta un campo opcional, simplemente no se mostrará en la interfaz. Los campos requeridos siempre deben estar presentes para el funcionamiento correcto.

📁 Archivo de Ejemplo
Consulta el archivo properties.json incluido para ver ejemplos reales con la estructura completa.