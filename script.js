// Script mejorado  manejo robusto de errores y optimizaciones móviles
document.addEventListener('DOMContentLoaded', function() {
    console.log('=== INICIANDO DANTE PROPIEDADES ===');
    
    // Inicializar funciones en orden de importancia
    initMenu();
    initSlider();
    initSearch();
    initWhatsApp();
    initTouchOptimizations(); // Nueva función para optimizaciones táctiles
});

function initMenu() {
    const menuBtn = document.querySelector('.menudesp');
    const closeBtn = document.querySelector('.cerrarmenu');
    const menuSlide = document.getElementById('menuslide');
    
    if (menuBtn && closeBtn && menuSlide) {
        // Mejorar usabilidad táctil
        menuBtn.addEventListener('click', (e) => {
            e.preventDefault();
            menuSlide.classList.add('menuabierto');
            document.body.style.overflow = 'hidden'; // Prevenir scroll del body
            console.log('Menú abierto');
        });
        
        closeBtn.addEventListener('click', (e) => {
            e.preventDefault();
            menuSlide.classList.remove('menuabierto');
            document.body.style.overflow = ''; // Restaurar scroll
            console.log('Menú cerrado');
        });
        
        // Cerrar menú al tocar fuera
        menuSlide.addEventListener('click', (e) => {
            if (e.target === menuSlide) {
                menuSlide.classList.remove('menuabierto');
                document.body.style.overflow = '';
            }
        });
    }
}

function initSlider() {
    if (typeof $ !== 'undefined' && $('.slini').length) {
        console.log('Inicializando slider...');
        
        // Configuración optimizada para móviles
        $('.slini').slick({
            dots: false,
            arrows: false,
            infinite: true,
            speed: 500,
            fade: true,
            autoplay: true,
            autoplaySpeed: 4000,
            cssEase: 'linear',
            adaptiveHeight: false,
            mobileFirst: true,
            responsive: [
                {
                    breakpoint: 768,
                    settings: {
                        adaptiveHeight: true
                    }
                }
            ]
        });

        // Navegación táctil mejorada
        const navButtons = document.querySelectorAll('.slider-nav button');
        navButtons.forEach(button => {
            button.addEventListener('touchstart', function(e) {
                e.preventDefault();
                const slideIndex = parseInt(this.dataset.slide);
                $('.slini').slick('slickGoTo', slideIndex);
            });
            
            button.addEventListener('click', function() {
                const slideIndex = parseInt(this.dataset.slide);
                $('.slini').slick('slickGoTo', slideIndex);
            });
        });

        $('.slini').on('afterChange', function(event, slick, currentSlide) {
            navButtons.forEach(btn => btn.classList.remove('active'));
            const activeBtn = document.querySelector(`[data-slide="${currentSlide}"]`);
            if (activeBtn) activeBtn.classList.add('active');
        });
        
        console.log('Slider inicializado correctamente');
    }
}

function initSearch() {
    const searchForm = document.querySelector('.buscadorcab');
    const opeSpans = document.querySelectorAll('.buscadorcab .ope span');
    const inputOpe = document.querySelector('input[name="ope"]');
    
    // Modal elements
    const modal = document.getElementById('results-modal');
    const closeModalBtn = document.getElementById('modal-close-btn');

    // Handle operation type selection con mejoras táctiles
    opeSpans.forEach(opcion => {
        opcion.addEventListener('touchstart', function(e) {
            e.preventDefault();
            selectOperation(this);
        });
        
        opcion.addEventListener('click', function() {
            selectOperation(this);
        });
    });
    
    function selectOperation(element) {
        opeSpans.forEach(o => o.classList.remove('activo'));
        element.classList.add('activo');
        if (inputOpe) inputOpe.value = element.dataset.val;
    }

    // Handle form submission
    if (searchForm) {
        searchForm.addEventListener('submit', async function(event) {
            event.preventDefault();

            // Mostrar indicador de carga en móviles
            const submitBtn = searchForm.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            submitBtn.disabled = true;

            const formData = new FormData(searchForm);
            const params = new URLSearchParams();
            for (const pair of formData.entries()) {
                if (pair[1]) {
                    params.append(pair[0], pair[1]);
                }
            }
            const activeOpe = document.querySelector('.buscadorcab .ope span.activo');
            if (activeOpe && activeOpe.dataset.val) {
                params.set('ope', activeOpe.dataset.val);
            } else {
                params.delete('ope');
            }

            const locInput = document.getElementById('campobusq');
            if (locInput && locInput.value) {
                params.set('loc', locInput.value);
            } else {
                params.delete('loc');
            }

            const queryString = params.toString();
            const backendUrl = `https://danterealestate-github-io.onrender.com/api/properties/search?${queryString}`;

            try {
                const response = await fetch(backendUrl);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const properties = await response.json();
                console.log('Raw properties response:', JSON.stringify(properties));
                displayResultsInModal(properties);

            } catch (error) {
                console.error('Error fetching properties:', error);
                const modalResultsGrid = document.getElementById('modal-results-grid');
                if (modalResultsGrid) {
                    modalResultsGrid.innerHTML = '<p>Error al cargar propiedades. Intente de nuevo más tarde.</p>';
                    modal.classList.add('active');
                }
            } finally {
                // Restaurar botón
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }
        });
    }

    // Close modal con mejoras móviles
    if (modal && closeModalBtn) {
        closeModalBtn.addEventListener('click', () => {
            closeModal();
        });
        
        // Cerrar modal al tocar fuera en móviles
        modal.addEventListener('touchstart', (event) => {
            if (event.target === modal) {
                closeModal();
            }
        });
        
        modal.addEventListener('click', (event) => {
            if (event.target === modal) {
                closeModal();
            }
        });
        
        // Prevenir cierre accidental al desplazarse
        const modalContent = modal.querySelector('.modal-content');
        modalContent.addEventListener('touchstart', (e) => {
            e.stopPropagation();
        });
    }
    
    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = ''; // Restaurar scroll
    }
}

function displayResultsInModal(properties) {
    const modal = document.getElementById('results-modal');
    const modalResultsGrid = document.getElementById('modal-results-grid');

    if (!modal || !modalResultsGrid) {
        console.error('Modal elements not found');
        return;
    }

    modalResultsGrid.innerHTML = '';

    console.log('Properties received:', properties);

    if (properties.length === 0) {
        modalResultsGrid.innerHTML = '<p>No se encontraron propiedades que coincidan con su búsqueda.</p>';
    } else {
        properties.forEach(prop => {
            console.log('Processing property:', prop);
            const imageUrl = 'llave.png';
            const titleText = prop.titulo || 'Propiedad sin título';
            const priceText = prop.precio ? `USD ${prop.precio.toLocaleString('es-AR')}` : 'Consultar precio';
            const locationText = prop.barrio || '';
            const typeOpText = `${prop.tipo || ''} en ${prop.operacion || ''}`;
            const codeText = prop.id_temporal ? `Código: ${prop.id_temporal}` : '';

            const propertyElement = document.createElement('div');
            propertyElement.className = 'propiedad-item';
            propertyElement.innerHTML = `
                <a href="details.html?id=${prop.id_temporal}" target="_blank">
                    <img src="${imageUrl}" alt="${titleText}" loading="lazy" style="width:100%">
                </a>
                <div class="image-description">
                    <h3>${titleText}</h3>
                    <p>${locationText}</p>
                    <p>${typeOpText}</p>
                    <p class="precio">${priceText}</p>
                    <p>${codeText}</p>
                </div>
            `;
            modalResultsGrid.appendChild(propertyElement);
        });
    }

    modal.classList.add('active');
    document.body.style.overflow = 'hidden'; // Prevenir scroll del body
}

function initWhatsApp() {
    const whatsappLink = document.getElementById('whatsappLink');
    if (whatsappLink) {
        whatsappLink.href = 'https://wa.me/5491125368595';
        
        // Mejorar usabilidad táctil
        whatsappLink.addEventListener('touchstart', function(e) {
            e.preventDefault();
            window.open(this.href, '_blank');
        });
    }
}

// Nueva función para optimizaciones táctiles
function initTouchOptimizations() {
    // Prevenir zoom de doble tap en elementos interactivos
    document.addEventListener('touchstart', function(e) {
        if (e.touches.length > 1) {
            e.preventDefault();
        }
    }, { passive: false });
    
    // Mejorar respuesta táctil en botones
    const buttons = document.querySelectorAll('button, .btn, .ope span');
    buttons.forEach(button => {
        button.addEventListener('touchstart', function() {
            this.style.transform = 'scale(0.95)';
        });
        
        button.addEventListener('touchend', function() {
            this.style.transform = '';
        });
    });
}

// Header sticky
window.addEventListener('scroll', function() {
    const header = document.getElementById('cab');
    if (header) {
        header.classList.toggle('cabfix', window.scrollY > 100);
    }
});

// Debug: Mostrar información de carga
window.addEventListener('load', function() {
    console.log('=== PÁGINA COMPLETAMENTE CARGADA ===');
    console.log('Todas las imágenes deberían estar cargadas');
});