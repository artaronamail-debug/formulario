Guía Completa: Sistema de Automatización Excel para Dante Propiedades
🎯 Objetivo
Automatizar el almacenamiento de datos del formulario de contacto en un archivo Excel sin intervención manual.

📋 Archivos Necesarios (Ya disponibles)
formulario.html - Formulario actualizado
servidor_excel.py - Servidor Flask mejorado
test_sistema.py - Script de pruebas
index.html y notas-legales.html - Páginas del sitio
🚀 Pasos de Instalación y Prueba
Paso 1: Instalar Dependencias
Abre tu terminal y ejecuta en el orden exacto:

bash
# Windows
pip install flask pandas openpyxl flask-cors requests

# Mac/Linux
pip3 install flask pandas openpyxl flask-cors requests
Si tienes problemas con permisos:

bash
# Windows
python -m pip install flask pandas openpyxl flask-cors requests

# Mac/Linux
python3 -m pip install flask pandas openpyxl flask-cors requests
Paso 2: Iniciar el Servidor
Desde la carpeta donde tienes todos los archivos:

bash
python servidor_excel.py
Verás algo como esto:

🏢 Dante Propiedades - Servidor de Contactos
==================================================
📁 Archivo Excel: contactos_dante_propiedades.xlsx
📋 Archivo Log: registro_contactos.log
🚀 Iniciando servidor...
📄 Archivo Excel inicializado
🌐 Servidor corriendo en: http://localhost:5000
📄 Páginas web disponibles:
   http://localhost:5000/ - Página principal
   http://localhost:5000/formulario - Formulario de contacto
   http://localhost:5000/notas-legales - Términos legales
   http://localhost:5000/contactos_dante_propiedades.xlsx - Descargar Excel

📡 APIs disponibles:
   POST /api/guardar-contacto - Guardar nuevo contacto
   GET  /api/estadisticas - Ver estadísticas
   GET  /health - Estado del servidor
   GET  /api/descargar-excel - Descargar archivo Excel
==================================================
Paso 3: Probar el Sistema Automáticamente
Abre otra terminal (mantén la primera corriendo) y ejecuta:

bash
python test_sistema.py
Resultado esperado:

🏢 Dante Propiedades - Prueba del Sistema Completo
============================================================
🕐 Hora de prueba: 2025-11-09 02:31:21

✅ Servidor funcionando correctamente

🧪 Enviando datos de prueba...
✅ Datos guardados exitosamente
   Nombre: Test Automatizado
   Email: test@ejemplo.com
   Fecha: 2025-11-09 02:31:21

📊 Estadísticas del sistema:
   Total contactos: 1
   Contactos hoy: 1
   Archivo: contactos_dante_propiedades.xlsx
   Último contacto: 2025-11-09 02:31:21

🌐 Verificando páginas web...
   ✅ Página principal: /
   ✅ Formulario: /formulario
   ✅ Formulario (.html): /formulario.html
   ✅ Notas legales: /notas-legales
   ✅ Notas legales (.html): /notas-legales.html

🎯 Instrucciones para uso manual:
1. Abre tu navegador en: http://localhost:5000/formulario
2. Llena el formulario con datos reales
3. Revisa el archivo: contactos_dante_propiedades.xlsx
4. Descarga el Excel desde: http://localhost:5000/contactos_dante_propiedades.xlsx

✅ ¡Sistema de automatización Excel funcionando!
Paso 4: Prueba Manual del Formulario
1.
Abre tu navegador
2.
Ve a: http://localhost:5000/formulario
3.
Llena el formulario con datos reales:
Nombre: "Juan Pérez"
Email: "juan@email.com"
Teléfono: "11-1234-5678"
Selecciona propiedad de interés
Mensaje: "Estoy interesado en una propiedad de 2 ambientes"
4.
Haz clic en "Enviar Mensaje"
Resultado esperado:

✅ Mensaje de éxito
✅ Botón "Contactar por WhatsApp" con el nuevo número: +54 11 2536-8595
✅ Datos guardados automáticamente en Excel
Paso 5: Verificar el Archivo Excel
1.
Busca en tu carpeta - aparece el archivo: contactos_dante_propiedades.xlsx
2.
Ábrelo con Excel o Google Sheets
3.
Verifica los datos - deberías ver:
Columnas: Fecha, Nombre, Email, Teléfono, Interés, Presupuesto, Mensaje, Página_Origen, IP_Cliente, User_Agent
Tus datos de prueba
Paso 6: Descargar el Excel (Opcional)
Para descargar desde el navegador:

Ve a: http://localhost:5000/contactos_dante_propiedades.xlsx
Se descarga automáticamente
🔧 Comandos Útiles
Ver estadísticas en tiempo real:
bash
curl http://localhost:5000/api/estadisticas
Verificar estado del servidor:
bash
curl http://localhost:5000/health
Ver logs del sistema:
bash
# Windows
type registro_contactos.log

# Mac/Linux
cat registro_contactos.log
🛠️ Solución de Problemas
Error: "No module named 'flask'"
Solución: Instala las dependencias correctamente

bash
pip install flask pandas openpyxl flask-cors requests
Error: "Address already in use"
Solución: El puerto 5000 está ocupado

Cierra otros programas que usen el puerto 5000
O cambia el puerto en servidor_excel.py (línea 192):
python
app.run(debug=True, host='0.0.0.0', port=5001)  # Cambia a 5001
El formulario no guarda datos
Verificaciones:

1.
✅ ¿El servidor está corriendo?
2.
✅ ¿Hay errores en la consola del navegador (F12)?
3.
✅ ¿El archivo Excel se está creando?
Error al abrir el Excel
Solución: Cierra el archivo Excel antes de enviar nuevos datos, o usa Google Sheets.

📊 Funcionalidades del Sistema
✅ Automatización Completa
Datos se guardan automáticamente en Excel
No requiere intervención manual
Sistema de fallback (CSV) si el servidor falla
✅ WhatsApp Integrado
Número actualizado: +54 11 2536-8595
Formato automático de mensaje
✅ Monitoreo y Estadísticas
Endpoint /api/estadisticas para ver datos
Archivo de logs para auditoria
Descarga directa del Excel
✅ Resiliente
Manejo de errores
Múltiples formatos de respaldo
Validación de datos
🎉 ¡Sistema Listo para Producción!
El sistema está completamente funcional y listo para uso real. Los datos se almacenarán automáticamente en contactos_dante_propiedades.xlsx cada vez que alguien complete el formulario.

Para detener el servidor: Presiona Ctrl + C en la terminal del servidor.