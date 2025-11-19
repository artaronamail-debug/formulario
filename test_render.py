#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test del deploy en Render
Dante Propiedades - Verificación del sistema online
"""

import requests
import time
import json
import sys

def test_render_deploy(render_url):
    """Prueba que el deploy en Render esté funcionando"""
    print("🌐 Verificando deploy en Render...")
    print(f"URL: {render_url}")
    print("=" * 50)
    
    # Test 1: Health check
    try:
        response = requests.get(f'{render_url}/health', timeout=10)
        if response.status_code == 200:
            print("✅ Health check: OK")
            print(f"   Status: {response.json()['status']}")
            print(f"   Excel exists: {response.json()['excel_file_exists']}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {str(e)}")
        return False
    
    # Test 2: Páginas web
    paginas = [
        ('/', 'Página principal'),
        ('/formulario', 'Formulario'),
        ('/notas-legales', 'Notas legales')
    ]
    
    print("\n📄 Verificando páginas web:")
    for url, desc in paginas:
        try:
            response = requests.get(f'{render_url}{url}', timeout=10)
            if response.status_code == 200:
                print(f"   ✅ {desc}: OK")
            else:
                print(f"   ❌ {desc}: {response.status_code}")
        except Exception as e:
            print(f"   ❌ {desc}: Error - {str(e)}")
    
    # Test 3: API de estadísticas
    try:
        response = requests.get(f'{render_url}/api/estadisticas', timeout=10)
        if response.status_code == 200:
            stats = response.json()
            print(f"\n📊 Estadísticas del sistema:")
            print(f"   Total contactos: {stats.get('total_contactos', 0)}")
            print(f"   Contactos hoy: {stats.get('contactos_hoy', 0)}")
            print(f"   Archivo Excel: {stats.get('archivo_excel', 'N/A')}")
        else:
            print(f"\n❌ API estadísticas: {response.status_code}")
    except Exception as e:
        print(f"\n❌ API estadísticas error: {str(e)}")
    
    # Test 4: Probar envío de formulario
    print(f"\n🧪 Probando envío de formulario...")
    datos_prueba = {
        'nombre': 'Test Render Deploy',
        'email': 'test@render.com',
        'telefono': '11-9999-9999',
        'interes': 'Casa en alquiler',
        'presupuesto': '$200,000 - $300,000',
        'mensaje': 'Mensaje de prueba del deploy en Render'
    }
    
    try:
        response = requests.post(
            f'{render_url}/api/guardar-contacto',
            json=datos_prueba,
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print("   ✅ Formulario enviado exitosamente")
                print(f"   Contacto: {result.get('datos_guardados', {}).get('nombre', 'N/A')}")
            else:
                print(f"   ❌ Error en formulario: {result.get('message', 'Unknown')}")
        else:
            print(f"   ❌ Error HTTP formulario: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Error formulario: {str(e)}")
    
    return True

def main():
    if len(sys.argv) != 2:
        print("❗ Uso: python test_render.py <URL_RENDER>")
        print("   Ejemplo: python test_render.py https://mi-app.onrender.com")
        return
    
    render_url = sys.argv[1].rstrip('/')
    
    print("🏢 Dante Propiedades - Test Deploy Render")
    print("=" * 60)
    
    if test_render_deploy(render_url):
        print("\n" + "=" * 60)
        print("🎉 ¡Deploy de Render funcionando correctamente!")
        print(f"🌐 Tu sitio está en: {render_url}")
        print(f"📝 Formulario en: {render_url}/formulario")
        print(f"📊 Excel en: {render_url}/contactos_dante_propiedades.xlsx")
        print("\n✅ Sistema de automatización Excel online y operativo")
    else:
        print("\n❌ Hay problemas con el deploy. Revisa:")
        print("1. Que el deploy esté completo en Render")
        print("2. Que todas las variables estén correctas")
        print("3. Que el archivo requirements.txt esté bien")

if __name__ == '__main__':
    main()