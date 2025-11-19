# -*- coding: utf-8 -*-
"""
🚀 SISTEMA DE ALMACENAMIENTO EXCEL - BACKEND COMPLETO
================================================================

Este servidor Python recibe los datos del formulario y los almacena automáticamente
en Excel y CSV. Incluye modo offline, respaldos automáticos y manejo de errores.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import json
import os
from datetime import datetime
import csv
import logging
import threading
import time
import glob
from pathlib import Path

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data/sistema-formularios.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

class ExcelStorageManager:
    """
    📊 Gestor completo de almacenamiento en Excel
    Maneja múltiples archivos, respaldos y exportación automática
    """
    
    def __init__(self, base_path='data'):
        self.base_path = Path(base_path)
        self.excel_path = self.base_path / 'excel' / 'consultas.xlsx'
        self.csv_path = self.base_path / 'excel' / 'consultas.csv'
        self.backup_path = self.base_path / 'backups'
        
        # Crear directorios si no existen
        self._crear_estructura_directorios()
        
        # Configuración de columnas
        self.columnas = [
            'Fecha', 'Hora', 'Timestamp', 'Nombre', 'Email', 'Teléfono', 
            'Interés', 'Presupuesto', 'Mensaje', 'Página', 'IP', 'User_Agent',
            'Estado', 'Notas'
        ]
        
        # Inicializar archivos
        self._inicializar_archivos()
        
        logging.info(f"✅ Sistema de almacenamiento inicializado en: {self.base_path}")
    
    def _crear_estructura_directorios(self):
        """Crear estructura de directorios necesaria"""
        directorios = [
            self.base_path / 'excel',
            self.base_path / 'backups',
            self.base_path / 'temp'
        ]
        
        for directorio in directorios:
            directorio.mkdir(parents=True, exist_ok=True)
    
    def _inicializar_archivos(self):
        """Inicializar archivos Excel y CSV con encabezados"""
        # Crear DataFrame con encabezados
        df_vacio = pd.DataFrame(columns=self.columnas)
        
        # Guardar en Excel si no existe
        if not self.excel_path.exists():
            with pd.ExcelWriter(self.excel_path, engine='openpyxl') as writer:
                df_vacio.to_excel(writer, sheet_name='Consultas', index=False)
                df_vacio.to_excel(writer, sheet_name='Backup', index=False)
        
        # Crear CSV con encabezados
        if not self.csv_path.exists():
            with open(self.csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(self.columnas)
    
    def añadir_consulta(self, datos_formulario):
        """
        📝 Añadir nueva consulta al sistema de almacenamiento
        """
        try:
            # Preparar datos completos
            timestamp = datetime.now()
            fecha_hora = timestamp.strftime('%d/%m/%Y %H:%M:%S')
            
            consulta_completa = {
                'Fecha': timestamp.strftime('%d/%m/%Y'),
                'Hora': timestamp.strftime('%H:%M:%S'),
                'Timestamp': timestamp.isoformat(),
                'Nombre': datos_formulario.get('nombre', ''),
                'Email': datos_formulario.get('email', ''),
                'Teléfono': datos_formulario.get('telefono', ''),
                'Interés': datos_formulario.get('interes', ''),
                'Presupuesto': datos_formulario.get('presupuesto', ''),
                'Mensaje': datos_formulario.get('mensaje', ''),
                'Página': datos_formulario.get('pagina', 'Desconocida'),
                'IP': request.remote_addr if request else 'N/A',
                'User_Agent': request.headers.get('User-Agent', 'N/A') if request else 'N/A',
                'Estado': 'Nueva',
                'Notas': ''
            }
            
            # Guardar en Excel (sheet principal)
            self._guardar_en_excel(consulta_completa)
            
            # Guardar en CSV
            self._guardar_en_csv(consulta_completa)
            
            # Crear backup automático
            self._crear_backup_automatico()
            
            logging.info(f"✅ Consulta guardada: {consulta_completa['Nombre']} - {consulta_completa['Email']}")
            
            return {
                'success': True,
                'message': 'Consulta guardada correctamente',
                'timestamp': consulta_completa['Timestamp'],
                'file': str(self.excel_path)
            }
            
        except Exception as e:
            logging.error(f"❌ Error guardando consulta: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Error al guardar consulta'
            }
    
    def _guardar_en_excel(self, consulta):
        """💾 Guardar en archivo Excel con formato"""
        try:
            # Leer Excel existente
            df = pd.read_excel(self.excel_path, sheet_name='Consultas')
            
            # Añadir nueva fila
            df_nuevo = pd.DataFrame([consulta])
            df_completo = pd.concat([df, df_nuevo], ignore_index=True)
            
            # Guardar con formato
            with pd.ExcelWriter(self.excel_path, engine='openpyxl') as writer:
                # Sheet principal con formato
                df_completo.to_excel(writer, sheet_name='Consultas', index=False)
                
                # Sheet de backup
                df_completo.to_excel(writer, sheet_name='Backup', index=False)
                
                # Sheet de estadísticas
                stats = self._generar_estadisticas()
                stats.to_excel(writer, sheet_name='Estadísticas', index=False)
                
                # Formatear columnas
                workbook = writer.book
                worksheet = writer.sheets['Consultas']
                
                # Formatear columnas de texto
                for column in worksheet.columns:
                    max_length = 0
                    column_letter = column[0].column_letter
                    for cell in column:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    adjusted_width = min(max_length + 2, 50)
                    worksheet.column_dimensions[column_letter].width = adjusted_width
            
            logging.info("✅ Guardado en Excel completado")
            
        except Exception as e:
            logging.error(f"❌ Error guardando en Excel: {str(e)}")
            raise
    
    def _guardar_en_csv(self, consulta):
        """📄 Guardar en archivo CSV"""
        try:
            with open(self.csv_path, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.columnas)
                writer.writerow(consulta)
            
            logging.info("✅ Guardado en CSV completado")
            
        except Exception as e:
            logging.error(f"❌ Error guardando en CSV: {str(e)}")
            raise
    
    def _crear_backup_automatico(self):
        """🗂️ Crear backup automático cada 50 consultas"""
        try:
            # Contar consultas actuales
            df = pd.read_excel(self.excel_path, sheet_name='Consultas')
            total_consultas = len(df)
            
            if total_consultas > 0 and total_consultas % 50 == 0:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                backup_file = self.backup_path / f'backup_consultas_{timestamp}.xlsx'
                
                # Copiar archivo completo
                import shutil
                shutil.copy2(self.excel_path, backup_file)
                
                logging.info(f"🗂️ Backup creado: {backup_file}")
                
        except Exception as e:
            logging.error(f"❌ Error creando backup: {str(e)}")
    
    def _generar_estadisticas(self):
        """📊 Generar estadísticas de las consultas"""
        try:
            df = pd.read_excel(self.excel_path, sheet_name='Consultas')
            
            stats = {
                'Total Consultas': len(df),
                'Consultas Hoy': len(df[df['Fecha'] == datetime.now().strftime('%d/%m/%Y')]),
                'Interés Más Común': df['Interés'].value_counts().head(1).to_dict() if not df.empty else {},
                'Presupuesto Más Común': df['Presupuesto'].value_counts().head(1).to_dict() if not df.empty else {},
                'Última Consulta': df['Fecha'].max() if not df.empty else 'N/A',
                'Consultas Esta Semana': len(df[df['Fecha'] >= (datetime.now() - pd.Timedelta(days=7)).strftime('%d/%m/%Y')]) if not df.empty else 0
            }
            
            return pd.DataFrame(list(stats.items()), columns=['Métrica', 'Valor'])
            
        except Exception as e:
            logging.error(f"❌ Error generando estadísticas: {str(e)}")
            return pd.DataFrame({'Métrica': ['Error'], 'Valor': [str(e)]})
    
    def obtener_consultas(self, limite=100):
        """📋 Obtener últimas consultas"""
        try:
            df = pd.read_excel(self.excel_path, sheet_name='Consultas')
            return df.tail(limite).to_dict('records')
        except Exception as e:
            logging.error(f"❌ Error obteniendo consultas: {str(e)}")
            return []
    
    def exportar_resumen(self):
        """📊 Exportar resumen de estadísticas"""
        try:
            df = pd.read_excel(self.excel_path, sheet_name='Consultas')
            if df.empty:
                return "No hay datos para exportar"
            
            resumen = f"""
📊 RESUMEN DE CONSULTAS - {datetime.now().strftime('%d/%m/%Y %H:%M')}

📈 ESTADÍSTICAS GENERALES:
• Total de consultas: {len(df)}
• Consultas hoy: {len(df[df['Fecha'] == datetime.now().strftime('%d/%m/%Y')])}
• Última consulta: {df['Fecha'].max()}

🎯 INTERESES MÁS CONSULTADOS:
{df['Interés'].value_counts().head(5).to_string() if not df.empty else 'No hay datos'}

💰 PRESUPUESTOS MÁS CONSULTADOS:
{df['Presupuesto'].value_counts().head(5).to_string() if not df.empty else 'No hay datos'}

📁 ARCHIVOS:
• Excel: {self.excel_path}
• CSV: {self.csv_path}
• Backups: {self.backup_path}
            """
            
            return resumen
            
        except Exception as e:
            return f"Error generando resumen: {str(e)}"

# Crear aplicación Flask
app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde cualquier origen

# Inicializar gestor de almacenamiento
storage_manager = ExcelStorageManager()

@app.route('/')
def home():
    """🏠 Página principal del sistema"""
    return jsonify({
        'message': '🚀 Sistema de Formularios con Almacenamiento Excel',
        'version': '1.0.0',
        'status': 'active',
        'endpoints': {
            '/api/guardar-contacto': 'POST - Guardar consulta de contacto',
            '/api/obtener-consultas': 'GET - Obtener últimas consultas',
            '/api/resumen': 'GET - Obtener resumen estadístico',
            '/health': 'GET - Estado del sistema'
        }
    })

@app.route('/health')
def health_check():
    """🏥 Verificar estado del sistema"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'storage_path': str(storage_manager.excel_path),
        'files_exist': {
            'excel': storage_manager.excel_path.exists(),
            'csv': storage_manager.csv_path.exists()
        }
    })

@app.route('/api/guardar-contacto', methods=['POST'])
def guardar_contacto():
    """💾 Guardar nueva consulta de contacto"""
    try:
        # Verificar que se envió JSON
        if not request.is_json:
            return jsonify({
                'success': False,
                'error': 'Se requiere contenido JSON'
            }), 400
        
        datos = request.get_json()
        
        # Validaciones básicas
        campos_requeridos = ['nombre', 'email', 'mensaje']
        for campo in campos_requeridos:
            if not datos.get(campo, '').strip():
                return jsonify({
                    'success': False,
                    'error': f'Campo requerido faltante: {campo}'
                }), 400
        
        # Validar email
        email = datos.get('email', '')
        if '@' not in email:
            return jsonify({
                'success': False,
                'error': 'Email inválido'
            }), 400
        
        # Añadir información de contexto
        datos['pagina'] = request.headers.get('Referer', 'Directo')
        
        # Guardar en almacenamiento
        resultado = storage_manager.añadir_consulta(datos)
        
        if resultado['success']:
            return jsonify(resultado), 200
        else:
            return jsonify(resultado), 500
            
    except Exception as e:
        logging.error(f"❌ Error en guardar-contacto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Error interno del servidor'
        }), 500

@app.route('/api/obtener-consultas', methods=['GET'])
def obtener_consultas():
    """📋 Obtener últimas consultas"""
    try:
        limite = request.args.get('limite', 100, type=int)
        consultas = storage_manager.obtener_consultas(limite)
        
        return jsonify({
            'success': True,
            'consultas': consultas,
            'total': len(consultas)
        })
        
    except Exception as e:
        logging.error(f"❌ Error en obtener-consultas: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/resumen', methods=['GET'])
def obtener_resumen():
    """📊 Obtener resumen estadístico"""
    try:
        resumen = storage_manager.exportar_resumen()
        return jsonify({
            'success': True,
            'resumen': resumen,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logging.error(f"❌ Error en resumen: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/exportar-excel', methods=['GET'])
def exportar_excel():
    """📊 Exportar archivo Excel"""
    try:
        if not storage_manager.excel_path.exists():
            return jsonify({
                'success': False,
                'error': 'No hay datos para exportar'
            }), 404
        
        # Leer archivo y devolver como descarga
        return app.send_file(
            storage_manager.excel_path,
            as_attachment=True,
            download_name=f'consultas_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
        )
        
    except Exception as e:
        logging.error(f"❌ Error exportando Excel: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("🚀 Iniciando Sistema de Formularios con Almacenamiento Excel")
    print(f"📁 Archivos de datos en: {storage_manager.base_path}")
    print(f"📊 Excel: {storage_manager.excel_path}")
    print(f"📄 CSV: {storage_manager.csv_path}")
    print("🌐 Servidor disponible en: http://localhost:5000")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)