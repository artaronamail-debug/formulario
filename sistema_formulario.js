/**
 * 🚀 SISTEMA DE FORMULARIOS - JAVASCRIPT AVANZADO
 * =================================================
 * 
 * Sistema completo de gestión de formularios con:
 * ✅ Almacenamiento en servidor y localStorage
 * ✅ Integración WhatsApp automática
 * ✅ Validación en tiempo real
 * ✅ Modo offline completo
 * ✅ Exportación de datos
 * ✅ Analytics básicos
 */

// Configuración global del sistema
const FormSystemConfig = {
    // URLs del servidor
    serverEndpoints: {
        save: 'http://localhost:5000/api/guardar-contacto',
        getConsultas: 'http://localhost:5000/api/obtener-consultas',
        resumen: 'http://localhost:5000/api/resumen',
        health: 'http://localhost:5000/health'
    },
    
    // Configuración de almacenamiento
    storage: {
        localKey: 'formulario_consultas_respaldo',
        backupInterval: 60000, // 1 minuto
        maxLocalRecords: 1000
    },
    
    // WhatsApp
    whatsapp: {
        number: '+5491125368595',
        enabled: true
    },
    
    // Validación
    validation: {
        requiredFields: ['nombre', 'email', 'mensaje'],
        emailRegex: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        phoneRegex: /^[\+]?[0-9\s\-\(\)]{8,}$/
    }
};

class FormStorageManager {
    /**
     * 💾 Gestor de almacenamiento con múltiples métodos
     */
    constructor() {
        this.localData = this._loadFromLocalStorage();
        this.syncQueue = [];
        this.isOnline = navigator.onLine;
        
        // Event listeners para cambios de conectividad
        window.addEventListener('online', () => {
            this.isOnline = true;
            this._syncPendingData();
        });
        
        window.addEventListener('offline', () => {
            this.isOnline = false;
        });
        
        // Auto-sync cada minuto
        setInterval(() => this._syncPendingData(), FormSystemConfig.storage.backupInterval);
    }
    
    /**
     * 💾 Guardar datos del formulario
     */
    async guardarDatos(datos) {
        const timestamp = new Date().toISOString();
        const registroCompleto = {
            ...datos,
            timestamp,
            pagina: window.location.href,
            userAgent: navigator.userAgent,
            online: this.isOnline
        };
        
        // 1. Guardar inmediatamente en localStorage
        this._saveToLocalStorage(registroCompleto);
        
        // 2. Intentar enviar al servidor
        if (this.isOnline) {
            try {
                const resultado = await this._enviarAlServidor(registroCompleto);
                console.log('✅ Datos guardados en servidor:', resultado);
                return { ...resultado, localGuardado: true, servidorGuardado: true };
            } catch (error) {
                console.warn('⚠️ Error en servidor, usando localStorage:', error);
                this._agregarAColaSync(registroCompleto);
                return { localGuardado: true, servidorGuardado: false, error: error.message };
            }
        } else {
            // Modo offline
            this._agregarAColaSync(registroCompleto);
            return { localGuardado: true, servidorGuardado: false, modo: 'offline' };
        }
    }
    
    /**
     * 📊 Obtener estadísticas
     */
    obtenerEstadisticas() {
        const datos = this._loadFromLocalStorage();
        const total = datos.length;
        const hoy = datos.filter(item => {
            const fechaItem = new Date(item.timestamp).toDateString();
            const fechaHoy = new Date().toDateString();
            return fechaItem === fechaHoy;
        }).length;
        
        const intereses = {};
        const presupuestos = {};
        
        datos.forEach(item => {
            // Contar intereses
            if (item.interes) {
                intereses[item.interes] = (intereses[item.interes] || 0) + 1;
            }
            // Contar presupuestos
            if (item.presupuesto) {
                presupuestos[item.presupuesto] = (presupuestos[item.presupuesto] || 0) + 1;
            }
        });
        
        return {
            total,
            hoy,
            intereses,
            presupuestos,
            ultimoRegistro: datos.length > 0 ? datos[datos.length - 1].timestamp : null
        };
    }
    
    /**
     * 📤 Exportar datos
     */
    exportarDatos(formato = 'csv') {
        const datos = this._loadFromLocalStorage();
        
        if (formato === 'csv') {
            return this._exportarCSV(datos);
        } else if (formato === 'json') {
            return this._exportarJSON(datos);
        }
    }
    
    // Métodos privados
    _saveToLocalStorage(datos) {
        let datosExistentes = this._loadFromLocalStorage();
        datosExistentes.push(datos);
        
        // Limitar número de registros
        if (datosExistentes.length > FormSystemConfig.storage.maxLocalRecords) {
            datosExistentes = datosExistentes.slice(-FormSystemConfig.storage.maxLocalRecords);
        }
        
        localStorage.setItem(FormSystemConfig.storage.localKey, JSON.stringify(datosExistentes));
        this.localData = datosExistentes;
    }
    
    _loadFromLocalStorage() {
        try {
            const data = localStorage.getItem(FormSystemConfig.storage.localKey);
            return data ? JSON.parse(data) : [];
        } catch (error) {
            console.error('Error cargando datos locales:', error);
            return [];
        }
    }
    
    async _enviarAlServidor(datos) {
        const response = await fetch(FormSystemConfig.serverEndpoints.save, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(datos)
        });
        
        if (!response.ok) {
            throw new Error(`Error del servidor: ${response.status}`);
        }
        
        return await response.json();
    }
    
    _agregarAColaSync(datos) {
        this.syncQueue.push(datos);
        console.log(`📋 Datos agregados a cola de sincronización. Total en cola: ${this.syncQueue.length}`);
    }
    
    async _syncPendingData() {
        if (this.syncQueue.length === 0 || !this.isOnline) {
            return;
        }
        
        console.log(`🔄 Sincronizando ${this.syncQueue.length} registros pendientes...`);
        
        const colaActual = [...this.syncQueue];
        this.syncQueue = [];
        
        for (const datos of colaActual) {
            try {
                await this._enviarAlServidor(datos);
                console.log('✅ Sincronización exitosa');
            } catch (error) {
                console.error('❌ Error en sincronización:', error);
                // Re-agregar a la cola si falla
                this.syncQueue.push(datos);
            }
        }
    }
    
    _exportarCSV(datos) {
        if (datos.length === 0) return 'No hay datos para exportar';
        
        const headers = Object.keys(datos[0]);
        const csvContent = [
            headers.join(','),
            ...datos.map(row => 
                headers.map(header => {
                    const value = row[header] || '';
                    // Escapar comillas y envolver en comillas si contiene comas
                    const escaped = value.toString().replace(/"/g, '""');
                    return escaped.includes(',') ? `"${escaped}"` : escaped;
                }).join(',')
            )
        ].join('\n');
        
        return csvContent;
    }
    
    _exportarJSON(datos) {
        return JSON.stringify(datos, null, 2);
    }
}

class FormValidator {
    /**
     * ✅ Validador de formularios en tiempo real
     */
    constructor() {
        this.rules = {
            nombre: {
                required: true,
                minLength: 2,
                maxLength: 100
            },
            email: {
                required: true,
                pattern: FormSystemConfig.validation.emailRegex
            },
            telefono: {
                required: false,
                pattern: FormSystemConfig.validation.phoneRegex
            },
            mensaje: {
                required: true,
                minLength: 10,
                maxLength: 1000
            }
        };
    }
    
    validarFormulario(formData) {
        const errores = {};
        
        Object.keys(this.rules).forEach(campo => {
            const regla = this.rules[campo];
            const valor = formData[campo];
            
            if (regla.required && (!valor || valor.trim() === '')) {
                errores[campo] = `El campo ${campo} es obligatorio`;
                return;
            }
            
            if (valor && regla.minLength && valor.length < regla.minLength) {
                errores[campo] = `Mínimo ${regla.minLength} caracteres`;
                return;
            }
            
            if (valor && regla.maxLength && valor.length > regla.maxLength) {
                errores[campo] = `Máximo ${regla.maxLength} caracteres`;
                return;
            }
            
            if (valor && regla.pattern && !regla.pattern.test(valor)) {
                errores[campo] = 'Formato inválido';
                return;
            }
        });
        
        return {
            esValido: Object.keys(errores).length === 0,
            errores
        };
    }
    
    mostrarErrores(errores, formId) {
        // Limpiar errores anteriores
        document.querySelectorAll(`#${formId} .error-message`).forEach(el => el.remove());
        document.querySelectorAll(`#${formId} .field-error`).forEach(el => el.classList.remove('field-error'));
        
        // Mostrar nuevos errores
        Object.keys(errores).forEach(campo => {
            const field = document.getElementById(campo);
            if (field) {
                field.classList.add('field-error');
                
                const errorDiv = document.createElement('div');
                errorDiv.className = 'error-message';
                errorDiv.textContent = errores[campo];
                errorDiv.style.cssText = 'color: #dc3545; font-size: 0.875em; margin-top: 5px;';
                
                field.parentNode.appendChild(errorDiv);
            }
        });
    }
}

class WhatsAppIntegration {
    /**
     * 📱 Integración con WhatsApp
     */
    static generarMensaje(datos) {
        const timestamp = new Date().toLocaleString('es-AR');
        
        return `*NUEVA CONSULTA - SISTEMA DE FORMULARIOS*

👤 *Nombre:* ${datos.nombre}
📧 *Email:* ${datos.email}
📱 *Teléfono:* ${datos.telefono || 'No especificado'}
🎯 *Interés:* ${datos.interes || 'No especificado'}
💰 *Presupuesto:* ${datos.presupuesto || 'No especificado'}

💬 *Mensaje:*
${datos.mensaje}

---
📅 Enviado: ${timestamp}
🌐 Desde: ${window.location.origin}`;
    }
    
    static abrirWhatsApp(datos) {
        if (!FormSystemConfig.whatsapp.enabled) return;
        
        const mensaje = this.generarMensaje(datos);
        const url = `https://wa.me/${FormSystemConfig.whatsapp.number.replace(/[^\d]/g, '')}?text=${encodeURIComponent(mensaje)}`;
        
        // Abrir en nueva ventana
        window.open(url, '_blank');
        
        console.log('📱 WhatsApp abierto con mensaje generado');
    }
}

class FormAnalytics {
    /**
     * 📊 Analytics básicos del formulario
     */
    constructor() {
        this.eventos = [];
        this.inicioSesion = Date.now();
    }
    
    registrarEvento(tipo, datos = {}) {
        const evento = {
            tipo,
            timestamp: Date.now(),
            datos,
            duracion: Date.now() - this.inicioSesion
        };
        
        this.eventos.push(evento);
        
        // Enviar a Google Analytics si está disponible
        if (typeof gtag !== 'undefined') {
            gtag('event', tipo, {
                custom_parameter_1: datos.interes || 'no-especificado',
                custom_parameter_2: datos.presupuesto || 'no-especificado'
            });
        }
    }
    
    obtenerResumen() {
        const eventosPorTipo = {};
        this.eventos.forEach(evento => {
            eventosPorTipo[evento.tipo] = (eventosPorTipo[evento.tipo] || 0) + 1;
        });
        
        return {
            totalEventos: this.eventos.length,
            duracionTotal: Date.now() - this.inicioSesion,
            eventosPorTipo,
            ultimoEvento: this.eventos[this.eventos.length - 1] || null
        };
    }
}

// Clase principal del sistema
class FormSystem {
    /**
     * 🚀 Sistema principal de formularios
     */
    constructor(config = {}) {
        this.config = { ...FormSystemConfig, ...config };
        this.storage = new FormStorageManager();
        this.validator = new FormValidator();
        this.analytics = new FormAnalytics();
        this.formularioActivo = null;
        
        this._inicializarEventListeners();
    }
    
    /**
     * 🔧 Inicializar el sistema
     */
    inicializar(formId, opciones = {}) {
        this.formularioActivo = document.getElementById(formId);
        if (!this.formularioActivo) {
            throw new Error(`Formulario con ID '${formId}' no encontrado`);
        }
        
        // Configurar validaciones en tiempo real
        this._configurarValidacionTiempoReal();
        
        // Configurar envío del formulario
        this._configurarEnvioFormulario(opciones);
        
        // Registrar evento de inicialización
        this.analytics.registrarEvento('formulario_inicializado', { formId });
        
        console.log('✅ Sistema de formularios inicializado');
    }
    
    /**
     * 📨 Enviar formulario manualmente
     */
    async enviarFormulario(formId, datos = null) {
        try {
            const formData = datos || this._obtenerDatosFormulario(formId);
            
            // Validar datos
            const validacion = this.validator.validarFormulario(formData);
            if (!validacion.esValido) {
                this.validator.mostrarErrores(validacion.errores, formId);
                throw new Error('Errores de validación');
            }
            
            // Mostrar estado de carga
            this._mostrarEstadoCarga(formId, 'Enviando...');
            
            // Registrar evento
            this.analytics.registrarEvento('formulario_enviado', formData);
            
            // Guardar datos
            const resultado = await this.storage.guardarDatos(formData);
            
            // Abrir WhatsApp
            WhatsAppIntegration.abrirWhatsApp(formData);
            
            // Mostrar éxito
            this._mostrarExito(formId, resultado);
            
            return resultado;
            
        } catch (error) {
            console.error('❌ Error enviando formulario:', error);
            this._mostrarError(formId, error.message);
            throw error;
        } finally {
            this._ocultarEstadoCarga(formId);
        }
    }
    
    // Métodos privados
    _inicializarEventListeners() {
        // Detectar cambios de conectividad
        window.addEventListener('online', () => {
            console.log('🌐 Conexión restaurada');
        });
        
        window.addEventListener('offline', () => {
            console.log('📴 Modo offline activado');
        });
    }
    
    _configurarValidacionTiempoReal() {
        if (!this.formularioActivo) return;
        
        const campos = this.formularioActivo.querySelectorAll('input, textarea, select');
        campos.forEach(campo => {
            campo.addEventListener('blur', () => {
                this._validarCampo(campo);
            });
            
            campo.addEventListener('input', () => {
                this._limpiarErrorCampo(campo);
            });
        });
    }
    
    _configurarEnvioFormulario(opciones) {
        this.formularioActivo.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            if (opciones.onSubmit) {
                await opciones.onSubmit();
            } else {
                await this.enviarFormulario(this.formularioActivo.id);
            }
        });
    }
    
    _obtenerDatosFormulario(formId) {
        const form = document.getElementById(formId);
        const formData = new FormData(form);
        const datos = {};
        
        for (let [key, value] of formData.entries()) {
            datos[key] = value;
        }
        
        return datos;
    }
    
    _validarCampo(campo) {
        const nombre = campo.name || campo.id;
        const valor = campo.value;
        const reglas = this.validator.rules[nombre];
        
        if (!reglas) return;
        
        let error = null;
        
        if (reglas.required && (!valor || valor.trim() === '')) {
            error = `El campo ${nombre} es obligatorio`;
        } else if (valor && reglas.pattern && !reglas.pattern.test(valor)) {
            error = 'Formato inválido';
        }
        
        if (error) {
            this._mostrarErrorCampo(campo, error);
        } else {
            this._limpiarErrorCampo(campo);
        }
    }
    
    _mostrarErrorCampo(campo, mensaje) {
        campo.classList.add('field-error');
        
        let errorDiv = campo.parentNode.querySelector('.error-message');
        if (!errorDiv) {
            errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.style.cssText = 'color: #dc3545; font-size: 0.875em; margin-top: 5px;';
            campo.parentNode.appendChild(errorDiv);
        }
        errorDiv.textContent = mensaje;
    }
    
    _limpiarErrorCampo(campo) {
        campo.classList.remove('field-error');
        const errorDiv = campo.parentNode.querySelector('.error-message');
        if (errorDiv) {
            errorDiv.remove();
        }
    }
    
    _mostrarEstadoCarga(formId, mensaje) {
        const form = document.getElementById(formId);
        const submitBtn = form.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.textContent = mensaje;
        }
    }
    
    _ocultarEstadoCarga(formId) {
        const form = document.getElementById(formId);
        const submitBtn = form.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Enviar';
        }
    }
    
    _mostrarExito(formId, resultado) {
        const form = document.getElementById(formId);
        const mensaje = form.querySelector('.success-message') || this._crearMensajeExito(formId);
        
        let texto = '¡Formulario enviado correctamente!';
        if (resultado.servidorGuardado === false) {
            texto += ' (Modo offline - datos guardados localmente)';
        }
        
        mensaje.textContent = texto;
        mensaje.style.display = 'block';
        
        setTimeout(() => {
            mensaje.style.display = 'none';
            form.reset();
        }, 5000);
    }
    
    _mostrarError(formId, error) {
        const form = document.getElementById(formId);
        const mensaje = form.querySelector('.error-message') || this._crearMensajeError(formId);
        
        mensaje.textContent = `Error: ${error}`;
        mensaje.style.display = 'block';
        
        setTimeout(() => {
            mensaje.style.display = 'none';
        }, 5000);
    }
    
    _crearMensajeExito(formId) {
        const form = document.getElementById(formId);
        const mensaje = document.createElement('div');
        mensaje.className = 'success-message';
        mensaje.style.cssText = 'background: #d4edda; color: #155724; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: none;';
        form.insertBefore(mensaje, form.firstChild);
        return mensaje;
    }
    
    _crearMensajeError(formId) {
        const form = document.getElementById(formId);
        const mensaje = document.createElement('div');
        mensaje.className = 'error-message';
        mensaje.style.cssText = 'background: #f8d7da; color: #721c24; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: none;';
        form.insertBefore(mensaje, form.firstChild);
        return mensaje;
    }
}

// Inicialización automática si se incluye el script
if (typeof window !== 'undefined') {
    // Hacer disponible globalmente
    window.FormSystem = FormSystem;
    window.FormStorageManager = FormStorageManager;
    window.FormValidator = FormValidator;
    window.WhatsAppIntegration = WhatsAppIntegration;
    
    // Auto-inicializar si hay un formulario con data-auto-init
    document.addEventListener('DOMContentLoaded', function() {
        const formsToInit = document.querySelectorAll('[data-auto-init]');
        formsToInit.forEach(form => {
            const formSystem = new FormSystem();
            formSystem.inicializar(form.id);
        });
    });
}

// Exportar para módulos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        FormSystem,
        FormStorageManager,
        FormValidator,
        WhatsAppIntegration,
        FormAnalytics
    };
}