/* app. css /Variables y breakpoints para responsive */
:root {
    --azul: #232deb;
    --rojo: #ff0101;
    --gris-claro: #f5f5f5;
    --gris-medio: #ebebeb;
    --gris-oscuro: #323232;
    --texto: #333;
    --texto-claro: #666;
    
    /* Breakpoints */
    --mobile: 768px;
    --medium: 992px;
    --tablet: 1024px;
    --desktop: 1200px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Fira Sans', sans-serif;
    line-height: 1.6;
    color: var(--texto);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    padding-top: 140px; /* Adjusted for fixed header and search */
    background-color: var(--azul);
}

/* Utilidades */
.cont {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.cbi {
    clear: both;
}

.ohidden {
    overflow-x: hidden;
}

const barrio = document.getElementById("campobusq").value.toLowerCase();

/* Banner de construcción */
.construction-banner {
    display: block; /* Mostrar por defecto en desktop */
    text-align: center;
    background: yellow;
    padding: 8px;
    position: relative;
    z-index: 500;
    font-size: 0.9rem;
    line-height: 1.2;
}

/* Ocultar banner de construcción en dispositivos móviles */
@media (max-width: 768px) {
    .construction-banner {
        display: none !important;
    }
}

.blinking {
    animation: blinkingOpacity 1.2s infinite;
    font-size: clamp(1rem, 3vw, 1.2rem);
}




.propiedad {
  background: #fff;
  border: 1px solid #ddd;
  padding: 15px;
  margin-bottom: 20px;
  border-radius: 6px;
}


@keyframes blinkingOpacity {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
}

/* Header */
#cab {
    background: var(--azul);
    color: white;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1001;
    height: 70px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

#cab.cabfix {
    box-shadow: 0 2px 15px rgba(0,0,0,0.2);
}

#cab .cont {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 9px 20px; /* Further reduced padding */
}

#cab .logo {
    display: flex;
    align-items: center;
    gap: 15px;
    text-decoration: none;
    color: white;
}

#cab .logo img {
    width: 57px; /* Further reduced size */
    height: auto;
}

#cab .logo-text {
    font-size: 1.0rem; /* Further reduced size */
    font-weight: 600;
    letter-spacing: 0.5px;
}

.menugen {
    display: flex;
    align-items: center;
    gap: 20px;
}

.menucab {
    display: flex;
    list-style: none;
    gap: 15px;
}

.menucab li a {
    color: white;
    text-decoration: none;
    font-weight: 500;
    padding: 10px 15px;
    transition: all 0.3s ease;
}

.menucab li a:hover {
    opacity: 0.8;
}

.redescab {
    display: flex;
    list-style: none;
    gap: 10px;
}

.redescab li a {
    color: white;
    font-size: 1.2rem;
    padding: 8px;
}

.menudesp {
    background: white;
    color: var(--rojo);
    border: none;
    font-size: 1.3rem;
    padding: 10px 12px;
    cursor: pointer;
    display: none;
}

/* Elementos que solo se muestran en desktop */
.desktop-only {
    display: block;
}

.mobile-info {
    display: none;
}

.mobile-call-btn,
.mobile-valuation-btn {
    display: block;
    width: 100%;
    padding: 12px 16px;
    margin-bottom: 10px;
    text-align: center;
    text-decoration: none;
    border-radius: 6px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.mobile-call-btn {
    background: var(--rojo);
    color: white;
}

.mobile-call-btn:hover {
    background: #e00101;
    transform: translateY(-2px);
}

.mobile-valuation-btn {
    background: var(--azul);
    color: white;
}

.mobile-valuation-btn:hover {
    background: #1a23c7;
    transform: translateY(-2px);
}

/* Menú principal - Oculto por defecto en móviles */
.menucab {
    display: flex;
    list-style: none;
    gap: 15px;
}

.menucab li a {
    color: white;
    text-decoration: none;
    font-weight: 500;
    padding: 10px 15px;
    transition: all 0.3s ease;
}

.menucab li a:hover {
    opacity: 0.8;
}

/* Menú hamburguesa - Visible solo en móviles */
.menudesp {
    background: white;
    color: var(--rojo);
    border: none;
    font-size: 1.3rem;
    padding: 10px 12px;
    cursor: pointer;
    display: none; /* Oculto por defecto */
}

/* Menú móvil desplegable */
#menuslide {
    position: fixed;
    top: 60px; /* Ajustado para header móvil */
    right: -100%;
    width: 85%;
    max-width: 280px;
    height: calc(100vh - 60px);
    background: white;
    z-index: 1100;
    transition: right 0.3s ease;
    padding: 20px;
    overflow-y: auto;
    box-shadow: -5px 0 15px rgba(0,0,0,0.1);
}

#menuslide.menuabierto {
    right: 0;
}

.cerrarmenu {
    position: absolute;
    top: 20px;
    right: 20px;
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: var(--rojo);
}

/* SLIDER PRINCIPAL - MEJORADO CON MEJOR MANEJO DE ERRORES */
#sliderini {
    position: relative;
    margin-top: 0;
    padding: 0;
    width: 100%;
    height: 500px;
    overflow: hidden;
    background-color: var(--gris-medio);
}

.slini {
    position: relative;
    height: 100% !important;
    width: 100%;
    background-color: var(--gris-medio);
}

.slini .slick-track,
.slini .slick-list {
    height: 100% !important;
}

.slini .slick-slide {
    height: 500px !important;
}

.slide {
    position: relative;
    height: 100% !important;
    width: 100%;
    background-color: var(--gris-medio);
    display: flex !important;
    align-items: center;
    justify-content: center;
}

.image-wrapper {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: var(--gris-medio);
    position: relative;
}

.slider-img {
    max-width: 100%;
    max-height: 100%;
    width: auto;
    height: auto;
    object-fit: contain;
    display: block;
}



/* Estilos para cuando la imagen falla */
.slider-img[data-error="true"] {
    opacity: 1 !important;
    background: linear-gradient(135deg, var(--azul), var(--rojo));
    min-width: 100%;
    min-height: 100%;
    display: flex !important;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1.2rem;
    font-weight: bold;
    text-align: center;
    padding: 20px;
}

.slider-img.loaded ~ .image-wrapper::before {
    display: none;
}




.slider-img.loaded ~ .image-wrapper::before,
.image-wrapper:has(.slider-img.loaded)::before {
    display: none;
}

/* Navegación personalizada del slider */
.slider-nav {
    position: absolute;
    bottom: 15px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 8px;
    z-index: 50;
}

.slider-nav button {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    border: 2px solid white;
    background: transparent;
    cursor: pointer;
    transition: all 0.3s ease;
}

.slider-nav button.active,
.slider-nav button:hover {
    background: white;
}

/* Buscador */
.buscadorcab {
    position: fixed;
    top: 70px; /* Positioned below the header */
    left: 0;
    z-index: 1000;
    background: rgba(255,255,255,0.95);
    padding: 10px 0;
    box-shadow: 0 3px 15px rgba(0,0,0,0.1);
    width: 100%;
    backdrop-filter: blur(5px);
}

.buscadorcab .cont {
    display: grid;
    grid-template-columns: auto auto 1fr auto auto;
    gap: 12px;
    align-items: center;
}

.ope {
    display: flex;
    border-radius: 50px;
    overflow: hidden;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.ope span {
    padding: 10px 12px;
    background: var(--azul);
    color: white;
    cursor: pointer;
    text-align: center;
    transition: all 0.3s ease;
    flex: 1;
    min-width: 70px;
    font-size: 0.85rem;
    line-height: 1.2;
}

.ope span:hover {
    background: #1a23c7;
}

.ope span.activo {
    background: var(--rojo);
}

.buscarsug {
    position: relative;
}

.suggestionsBox {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    border: 1px solid #ddd;
    border-radius: 0 0 5px 5px;
    max-height: 200px;
    overflow-y: auto;
    display: none;
    z-index: 1000;
}

.suggestionList li {
    padding: 10px;
    cursor: pointer;
    border-bottom: 1px solid #eee;
}

.suggestionList li:hover {
    background: #f5f5f5;
}

.colini {
    min-width: 140px;
}

.colini input,
.colini select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 50px;
    font-size: 0.9rem;
}

.colini input:focus,
.colini select:focus {
    outline: none;
    border-color: var(--azul);
    box-shadow: 0 0 5px rgba(35, 45, 235, 0.3);
}

.buscadorcab button[type="submit"] {
    background: var(--rojo);
    color: white;
    border: none;
    padding: 10px 16px;
    border-radius: 50px;
    cursor: pointer;
    font-size: 1.1rem;
    transition: all 0.3s ease;
}

.buscadorcab button[type="submit"]:hover {
    background: #e00101;
    transform: scale(1.05);
}

/* Secciones principales */
section {
    padding: 50px 0;
    overflow: hidden;
}

.tit {
    text-align: center;
    margin-bottom: 35px;
}

.tit h2 {
    color: var(--rojo);
    font-size: 2.2rem;
    margin-bottom: 12px;
}

.tit p {
    font-size: 1.1rem;
    color: var(--texto-claro);
}

/* Secciones destacadas */
#destacadasini {
    background: white;
    padding: 50px 0;
}

#destacadasini .tit h2 {
    color: var(--rojo);
    font-size: 2.2rem;
    margin-bottom: 12px;
}

#destacadasini .tit p {
    font-size: 1.1rem;
    color: var(--texto-claro);
    margin-bottom: 35px;
}

/* Emprendimientos */
#Lotes {
    background: var(--gris-claro);
    padding: 50px 0;
}

#Lotes .coltit h3 {
    color: var(--rojo);
    font-size: 2rem;
    margin-bottom: 12px;
    text-align: center;
}

#Lotes .coltit p {
    font-size: 1rem;
    color: var(--texto-claro);
    text-align: center;
    margin-bottom: 35px;
}

.emprendimientos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
    margin-bottom: 35px;
}

.btn-container {
    text-align: center;
    margin-top: 25px;
}

.btn-container .btn {
    margin: 0 8px;
}

/* Banner de empleo */
.empleo-banner {
    background: linear-gradient(135deg, var(--azul), var(--rojo));
    padding: 35px 0;
    text-align: center;
}

.empleo-btn {
    background: white;
    color: var(--azul);
    font-size: 1.1rem;
    font-weight: 700;
    padding: 12px 25px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-radius: 6px;
    transition: all 0.3s ease;
}

.empleo-btn:hover {
    background: var(--gris-claro);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
}

/* === Propiedades destacadas === */

.propiedades-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
  margin-top: 35px;
}

.col .logopie img {
  max-width: 100px;
  height: auto;
  margin-right: 10px;
}

.col:first-child {
  flex: 0 0 100px; /* 👈 fuerza que la columna del logo no crezca más allá de 100px */
  display: flex;
  align-items: center;
  justify-content: flex-start;
}


.formulario-legal {
  display: flex;
  flex-wrap: nowrap; /* 👈 evita que los elementos se apilen */
  gap: 30px;
  width: 100%;
  max-width: 1400px;
  margin: 40px auto;
  padding: 20px;
  box-sizing: border-box;
}

.formulario-iframe {
  flex: 0 0 70%; /* 👈 ocupa el 70% del ancho */
  min-width: 700px;
  height: 823px;
  border: none;
}


.nota-legal {
  flex: 0 1 45%; /* 👈 antes era 30% o 35% */
  min-width: 500px;
  padding: 20px;
  font-size: 14px;
  line-height: 1.6;
  background-color: #f5f5f5;
  border-radius: 8px;
  color: #333;
}


.col:first-child {
  flex: 0 0 80px;
  max-width: 80px;
}


.formulario-iframe {
  flex: 1 1 600px;
  height: 823px;
  border: none;
}


.propiedad-item img,
.property-image {
  height: 420px;
  width: 100%;
  object-fit: cover;
  display: block;
  border-radius: 8px;
}

.image-description {
  padding: 15px;
  font-size: 16px;
  text-align: center;
  color: #333;
}
/* 
  Grid de propiedades modular.
  - `display: grid` activa el layout de grilla.
  - `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))` crea columnas flexibles.
    - `auto-fit`: ajusta automáticamente el número de columnas para llenar el espacio.
    - `minmax(280px, 1fr)`: cada columna tendrá un ancho mínimo de 280px y crecerá para ocupar el espacio disponible.
  - `gap`: define el espacio entre los items de la grilla, evitando solapamientos.
*/
/* .propiedades-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 25px;
    margin-top: 35px;
} */


.propiedad-card {
    background: white;
    border-radius: 6px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.propiedad-img {
    width: 100%;
    height: 220px;
    object-fit: cover;
}

.propiedad-info {
    padding: 18px;
}

.propiedad-info h3 {
    font-size: 1.1rem;
    margin-bottom: 8px;
}


.precio {
  color: var(--rojo);
  font-weight: 600;
  font-size: 1.2rem;
  margin-top: 8px;
  margin-bottom: 20px; /* opcional para separación inferior */
  padding: 15px 20px;   /* opcional para que el fondo blanco se note */
  background-color: #fff; /* ✅ fondo blanco */
  border-radius: 8px;      /* opcional para estética consistente */
  box-shadow: 0 2px 10px rgba(0,0,0,0.1); /* opcional para profundidad visual */
}

/* Botones */
.btn {
    display: inline-block;
    background: var(--azul);
    color: white;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
    font-weight: 500;
    transition: all 0.3s;
    border: none;
    cursor: pointer;
}

.btn:hover {
    background: var(--rojo);
    transform: translateY(-2px);
}

.btn-whatsapp {
    background: #25D366;
    width: 55px;
    height: 55px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 3px 12px rgba(0,0,0,0.2);
    transition: transform 0.3s;
}

.btn-whatsapp:hover {
    transform: scale(1.1);
}

.whatsapp-fixed {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1001; /* Alto para que sea siempre accesible */
}

/* Ajustes específicos para móviles */
@media (max-width: 768px) {
    .whatsapp-fixed {
        bottom: 15px;
        right: 15px;
        z-index: 1001; /* Mantener alto z-index en móviles */
    }
}

/* Footer */
#pie {
    background: var(--gris-claro);
    padding: 40px 0 25px;
}

#pie .cont {
    display: grid;
    grid-template-columns: 280px 1fr 240px;
    gap: 35px;
    align-items: start;
}

#pie .col:first-child {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.logopie {
    display: inline-block;
    margin-bottom: 18px;
}

.logopie img {
  max-width: 80px;
  height: auto;
}

.col {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
}


.subcol {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.subcol > ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* o 1fr si querés una sola columna */
  gap: 25px; /* ajustá según lo que prefieras */
}

.subcol > ul > li {
    margin-bottom: 20px;
}

#pie h4 {
    color: var(--rojo);
    margin-bottom: 10px;
    font-size: 1rem;
    font-weight: 600;
}

#pie h4 a {
    color: var(--rojo);
    text-decoration: none;
}

#pie h4 a:hover {
    color: var(--azul);
}

#pie ul ul {
    list-style: none;
    margin: 6px 0 0 0;
    padding: 0;
}

#pie ul ul li {
    margin-bottom: 5px;
}

#pie a {
    color: var(--texto);
    text-decoration: none;
    transition: color 0.3s ease;
    font-size: 0.9rem;
}

#pie a:hover {
    color: var(--rojo);
}

#pie .col:last-child {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    text-align: right;
}

.llamar {
    margin-bottom: 20px;
}

.llamar strong a {
    color: var(--rojo);
    font-size: 1.2rem;
    text-decoration: none;
    font-weight: 700;
}

.llamar strong a:hover {
    color: var(--azul);
}

.redes {
    width: 100%;
}

.redes strong {
    display: block;
    margin-bottom: 12px;
}

.redes strong a {
    color: var(--azul);
    text-decoration: none;
    font-size: 1rem;
}

.redespie {
    display: flex;
    justify-content: flex-end;
    gap: 12px;
    margin-top: 12px;
}

.redespie li {
    list-style: none;
}

.redespie a {
    font-size: 1.3rem;
    color: var(--azul);
    transition: all 0.3s ease;
    padding: 6px;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: rgba(35, 45, 235, 0.1);
}

.redespie a:hover {
    color: white;
    background: var(--rojo);
}

/* Copyright */
#copy {
    background: var(--rojo);
    color: white;
    text-align: center;
    padding: 35px 0;
}

#copy .cont {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 25px;
}

#copy p {
    flex: 1;
    margin: 0;
    font-size: 0.85rem;
    line-height: 1.6;
}

.prov {
    text-align: center;
    flex-shrink: 0;
}

.prov a {
    color: white;
    text-decoration: none;
}

.prov img {
    margin-bottom: 8px;
    border-radius: 50%;
}

/* Loader */
.loader {
    display: inline-block;
    position: relative;
    width: 70px;
    height: 70px;
}

.loader div {
    position: absolute;
    border: 3px solid var(--rojo);
    opacity: 1;
    border-radius: 50%;
    animation: loader 1s cubic-bezier(0,0.2,0.8,1) infinite;
}

.loader div:nth-child(2) {
    animation-delay: -0.5s;
}

@keyframes loader {
    0% {
        top: 32px;
        left: 32px;
        width: 0;
        height: 0;
        opacity: 1;
    }
    100% {
        top: 0;
        left: 0;
        width: 64px;
        height: 64px;
        opacity: 0;
    }
}

.cargando {
    text-align: center;
    padding: 50px 0;
}

.centrado {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
}

.cargando span {
    font-size: 1rem;
    color: var(--texto-claro);
}

/* RESPONSIVE DESIGN - OPTIMIZADO */

/* Slick Carousel optimizado */
.slick-slider {
    position: relative;
    display: block;
    box-sizing: border-box;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}

.slick-list {
    position: relative;
    display: block;
    overflow: hidden;
    margin: 0;
    padding: 0;
}

.slick-track {
    position: relative;
    top: 0;
    left: 0;
    display: block;
}

.slick-slide {
    display: none;
    float: left;
    height: 100%;
    min-height: 1px;
}

.slick-initialized .slick-slide {
    display: block;
}

/* === Propiedades destacadas === */
.propiedad-item {
  display: flex;
  flex-direction: column;
  background-color: #f9f9f9; /* o "white" si preferís fondo blanco puro */
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.propiedad-info-principal {
  display: flex;
  flex-direction: column; /* si querés disposición vertical */
  align-items: center;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  overflow: hidden; /* evita que el contenido se desborde visualmente */
}


.property-image {
    max-width: 100%;
    height: 420px;
    object-fit: cover;
    display: block;
    border-radius: 8px;
}

.image-description {
    padding: 10px;
    text-align: center;
    font-size: 0.9rem;
    color: var(--texto);
    background-color: var(--gris-claro);
    margin-top: 5px;
    border-radius: 0 0 6px 6px;
    flex-grow: 1; /* Permite que la descripción se estire para igualar la altura de otros items en la misma fila */
}

/* Estilos para la descripcion del inmueble */
.descripcion {
  background-image: url('fondo.jpg'); /* reemplazar cuando tengas la imagen */
  background-size: cover;
  background-position: center;
  padding: 40px;
  color: #333;
  background-color: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(2px);
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  max-width: 900px;
  margin: 40px auto;
  font-family: 'Segoe UI', sans-serif;
}

.descripcion h2 {
  color: #004080;
  font-size: 28px;
  margin-bottom: 20px;
  text-align: left;
  display: flex;
  align-items: center;
}

.descripcion p {
  font-size: 16px;
  line-height: 1.6;
  margin-bottom: 15px;
}

.descripcion strong {
  color: #000;
  font-weight: 600;
}

.descripcion em {
  color: #555;
  font-style: italic;
}

.boton-contacto {
  display: inline-block;
  margin-top: 20px;
  padding: 12px 24px;
  background-color: #25D366;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  font-weight: bold;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.boton-contacto:hover {
  background-color: #1ebe5d;
}


.caracteristicas {
  display: flex;
  gap: 30px;
  background-color: #fff; /* Fondo blanco */
  padding: 20px;           /* Espaciado interno para que el contenido no toque los bordes */
  border-radius: 8px;      /* Opcional: bordes redondeados para mantener consistencia visual */
  box-shadow: 0 2px 10px rgba(0,0,0,0.1); /* Opcional: sombra suave como en otras secciones */
}

body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 20px;
  background: #f2f2f2;
}

.buscadorcab {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 30px;
}

.cont {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  align-items: center;
}

.ope span {
  cursor: pointer;
  padding: 10px 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
}

.ope .activo {
  background-color: #0077cc;
  color: white;
}

.sel select,
.buscarsug input,
.cod {
  padding: 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
  min-width: 180px;
}

button {
  padding: 10px 15px;
  background-color: #0077cc;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

#resultados {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.propiedad {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}


.propiedad:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}



#resultados {
  margin-top: 2rem;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

/* Estilos para el Modal de Resultados */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10000; /* Asegura que esté por encima de todo */
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease, visibility 0.3s ease;
}

.modal-overlay.active {
    opacity: 1;
    visibility: visible;
}

.modal-content {
    background-color: white;
    padding: 30px;
    border-radius: 8px;
    max-width: 90%;
    max-height: 90%;
    overflow-y: auto;
    position: relative;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    transform: translateY(-20px);
    transition: transform 0.3s ease;
}

.modal-overlay.active .modal-content {
    transform: translateY(0);
}

.modal-close {
    position: absolute;
    top: 15px;
    right: 15px;
    font-size: 28px;
    cursor: pointer;
    background: none;
    border: none;
    color: var(--gris-oscuro);
    transition: color 0.2s ease;
}

.modal-close:hover {
    color: var(--rojo);
}

.modal-content h2 {
    color: var(--azul);
    margin-bottom: 20px;
    text-align: center;
    font-size: 2rem;
}

/* Ajustes para la grilla de propiedades dentro del modal */
#modal-results-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 25px;
    padding-top: 10px;
}

/* Estilos para los items de propiedad dentro del modal, si son diferentes */
#modal-results-grid .propiedad-item {
    background-color: #f9f9f9;
    border: 1px solid #eee;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease;
}

#modal-results-grid .propiedad-item:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

#modal-results-grid .propiedad-item img {
    width: 100%;
    height: 200px; /* Altura fija para las imágenes en el modal */
    object-fit: cover;
    display: block;
}

#modal-results-grid .propiedad-item .image-description {
    padding: 15px;
    text-align: left;
    font-size: 0.95rem;
    color: var(--texto);
}

#modal-results-grid .propiedad-item h3 {
    font-size: 1.1rem;
    margin-bottom: 5px;
    color: var(--azul);
}

#modal-results-grid .propiedad-item p {
    margin-bottom: 3px;
    color: var(--texto-claro);
}

/* ========== CORRECCIONES PARA DISPOSITIVOS MÓVILES ========== */

/* Ajustes específicos para móviles (celulares) */
@media (max-width: 768px) {
    body {
        padding-top: 60px; /* Reducido para móviles */
    }
    
    /* Ocultar elementos desktop y mostrar móviles */
    .desktop-only {
        display: none !important;
    }
    
    .mobile-info {
        display: block !important;
    }
    
    .construction-banner.desktop-only {
        display: none !important;
    }
    
    .menucab {
        display: none !important;
    }
    
    /* Header más compacto en móviles */
    #cab {
        height: 60px;
        z-index: 1001;
    }
    
    #cab .cont {
        padding: 6px 10px;
    }
    
    #cab .logo img {
        width: 45px;
    }
    
    #cab .logo-text {
        font-size: 0.9rem;
        max-width: 120px;
    }
    
    /* Buscador completamente adaptado para móviles - SOLUCIÓN PRINCIPAL */
    .buscadorcab {
        top: 60px;
        padding: 8px 0;
        background: rgba(255,255,255,0.98);
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        z-index: 1000;
    }
    
    .buscadorcab .cont {
        display: flex;
        flex-direction: column;
        gap: 8px;
        padding: 0 10px;
    }
    
    /* Operación buttons - SOLUCIÓN PARA "TASACION" vs "ALQUILER TEMPORAL" */
    .ope {
        display: flex;
        justify-content: center;
        width: 100%;
        margin: 0;
    }
    
    .ope span {
        flex: 1;
        min-width: 0;
        padding: 6px 4px;
        font-size: 0.7rem;
        line-height: 1.1;
        text-align: center;
        white-space: normal; /* Permitir salto de línea en móviles */
        overflow: visible;
        text-overflow: clip;
    }
    
    /* Ajuste específico para "Alquiler temporal" en móviles muy pequeños */
    .ope span[data-val="T"] {
        font-size: 0.65rem;
        line-height: 1.0;
    }
    
    /* Campos de búsqueda - SOLUCIÓN PARA "LLAMÀ" vs "ALQUILER" */
    .sel, .buscarsug, .cod {
        width: 100%;
        order: unset;
    }
    
    .colini input,
    .colini select {
        width: 100%;
        padding: 8px;
        font-size: 14px; /* Previene zoom en iOS */
        border-radius: 4px;
        border: 1px solid #ddd;
    }
    
    .buscadorcab button[type="submit"] {
        width: 100%;
        padding: 10px;
        font-size: 14px;
        margin-top: 2px;
        border-radius: 4px;
    }
    
    /* Ocultar código en móviles para dar más espacio */
    .cod {
        display: none;
    }
    
    /* Ocultar completamente el banner de construcción en móviles */
    .construction-banner {
        display: none !important;
    }
    
    /* Menú más compacto en móviles */
    .menucab {
        display: none; /* Usar menú hamburguesa en móviles */
    }
    
    .menudesp {
        display: block !important;
    }
    
    /* Slider optimizado para móviles */
    #sliderini {
        height: 200px;
        margin-top: 0;
    }
    
    .slini .slick-slide {
        height: 200px !important;
    }
    
    .slide, .image-wrapper {
        height: 200px !important;
    }
    
    .slider-img {
        max-height: 200px;
        object-fit: cover;
    }
    
    /* Propiedades en una sola columna en móviles */
    .propiedades-grid {
        grid-template-columns: 1fr;
        gap: 15px;
    }
    
    .propiedad-item img,
    .property-image {
        height: 180px;
    }
    
    /* Footer simplificado en móviles */
    #pie .cont {
        grid-template-columns: 1fr;
        gap: 20px;
        text-align: center;
    }
    
    /* WhatsApp más accesible en móviles */
    .whatsapp-fixed {
        bottom: 15px;
        right: 15px;
        z-index: 1001; /* Alto para que sea siempre accesible */
    }
    
    .btn-whatsapp {
        width: 50px;
        height: 50px;
    }
    
    /* Mostrar menú hamburguesa y ocultar menú normal en móviles */
    .menucab {
        display: none !important;
    }
    
    .menudesp {
        display: block !important;
    }
    
    /* Ajustes para el menú deslizable en móviles */
    #menuslide {
        top: 60px;
        height: calc(100vh - 60px);
        width: 85%;
        max-width: 280px;
        box-shadow: -5px 0 15px rgba(0,0,0,0.1);
    }
}

/* Ajustes para pantallas muy pequeñas */
@media (max-width: 480px) {
    body {
        padding-top: 55px;
    }
    
    #cab {
        height: 55px;
    }
    
    #cab .logo-text {
        font-size: 0.8rem;
        max-width: 100px;
    }
    
    /* Menú hamburguesa para pantallas muy pequeñas */
    #menuslide {
        top: 55px;
        height: calc(100vh - 55px);
    }
    
    /* Operación buttons más compactas en pantallas pequeñas */
    .ope span {
        padding: 5px 3px;
        font-size: 0.65rem;
        line-height: 1.0;
    }
    
    /* Ajuste específico para "Alquiler temporal" en pantallas muy pequeñas */
    .ope span[data-val="T"] {
        font-size: 0.6rem;
        line-height: 0.9;
    }
    
    .buscadorcab {
        top: 55px;
    }
    
    /* Propiedades aún más pequeñas */
    .propiedad-item img,
    .property-image {
        height: 150px;
    }
}

/* Ajustes generales para móviles */
@media (max-width: 768px) {
    body {
        padding-top: 70px;
    }
    
    /* Header optimizado para móviles */
    #cab {
        height: 70px;
    }
    
    #cab .cont {
        padding: 8px 15px;
    }
    
    #cab .logo img {
        width: 50px;
    }
    
    #cab .logo-text {
        font-size: 1rem;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 150px;
    }
    
    /* Slider optimizado para móviles */
    #sliderini {
        height: 220px;
        margin-top: 0;
    }
    
    .slini .slick-slide {
        height: 220px !important;
    }
    
    .slide, .image-wrapper {
        height: 220px !important;
    }
    
    .slider-img {
        max-height: 220px;
        object-fit: cover;
    }
    
    /* Buscador completamente responsivo */
    .buscadorcab {
        position: relative;
        top: 0;
        padding: 10px 0;
        background: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .buscadorcab .cont {
        display: flex;
        flex-direction: column;
        gap: 10px;
        padding: 0 15px;
    }
    
    .ope {
        order: 1;
        display: flex;
        justify-content: center;
        width: 100%;
    }
    
    .ope span {
        flex: 1;
        min-width: 0;
        padding: 8px 5px;
        font-size: 0.75rem;
        line-height: 1.2;
    }
    
    .sel {
        order: 2;
        width: 100%;
    }
    
    .buscarsug {
        order: 3;
        width: 100%;
    }
    
    .cod {
        order: 4;
        width: 100%;
    }
    
    .buscadorcab button[type="submit"] {
        order: 5;
        width: 100%;
        margin-top: 5px;
    }
    
    .colini input,
    .colini select {
        width: 100%;
        padding: 12px;
        font-size: 16px; /* Previene zoom en iOS */
    }
    
    /* Propiedades destacadas */
    .propiedades-grid {
        grid-template-columns: 1fr;
        gap: 15px;
    }
    
    .propiedad-item img,
    .property-image {
        height: 200px;
    }
    
    /* Footer optimizado para móviles */
    #pie .cont {
        grid-template-columns: 1fr;
        gap: 25px;
        text-align: left;
    }
    
    .formulario-legal {
        flex-direction: column;
        padding: 15px;
    }
    
    .formulario-iframe,
    .nota-legal {
        flex: 1 1 100%;
        min-width: auto;
        width: 100%;
    }
    
    .formulario-iframe {
        height: 600px;
    }
    
    .nota-legal {
        font-size: 0.85rem;
        padding: 15px;
    }
    
    /* Modal optimizado para móviles */
    .modal-content {
        width: 95%;
        max-height: 85vh;
        padding: 20px 15px;
        margin: 10px;
    }
    
    .modal-content h2 {
        font-size: 1.5rem;
        margin-bottom: 15px;
    }
    
    #modal-results-grid {
        grid-template-columns: 1fr;
        gap: 15px;
    }
    
    #modal-results-grid .propiedad-item img {
        height: 180px;
    }
    
    /* Ajustes para el menú móvil */
    #menuslide {
        top: 70px;
        width: 85%;
        max-width: 300px;
    }
    
    /* WhatsApp flotante */
    .whatsapp-fixed {
        bottom: 15px;
        right: 15px;
    }
    
    .btn-whatsapp {
        width: 50px;
        height: 50px;
    }
    
    /* Copyright optimizado */
    #copy .cont {
        flex-direction: column;
        text-align: center;
        gap: 15px;
    }
    
    #copy p {
        font-size: 0.75rem;
        line-height: 1.4;
    }
}

/* Ajustes adicionales para pantallas muy pequeñas */
@media (max-width: 480px) {
    #sliderini {
        height: 180px;
    }
    
    .slini .slick-slide {
        height: 180px !important;
    }
    
    .slide, .image-wrapper {
        height: 180px !important;
    }
    
    .slider-img {
        max-height: 180px;
    }
    
    .tit h2 {
        font-size: 1.5rem;
    }
    
    .propiedad-item img,
    .property-image {
        height: 160px;
    }
    
    .formulario-iframe {
        height: 500px;
    }
}

/* Mejoras de usabilidad táctil */
@media (max-width: 768px) {
    .btn, 
    .ope span,
    .menudesp,
    .cerrarmenu,
    .suggestionList li {
        min-height: 44px; /* Tamaño mínimo recomendado para elementos táctiles */
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .menucab li a {
        padding: 12px 15px;
    }
}

/* ====================================
   SISTEMA AVANZADO DE GESTIÓN DE PROPIEDADES
   ==================================== */

/* --- Buscador Avanzado --- */
.search-group {
    display: flex;
    flex-direction: column;
    min-width: 140px;
}

.search-group label {
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--azul);
    margin-bottom: 4px;
}

.form-select, .form-input {
    padding: 8px 12px;
    border: 2px solid #e1e5e9;
    border-radius: 6px;
    font-size: 0.9rem;
    transition: all 0.3s ease;
    background: white;
}

.form-select:focus, .form-input:focus {
    outline: none;
    border-color: var(--rojo);
    box-shadow: 0 0 0 3px rgba(220, 20, 60, 0.1);
}

.search-btn {
    background: var(--rojo);
    color: white;
    border: none;
    padding: 12px 20px;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 8px;
    align-self: flex-end;
    margin-top: 20px;
}

.search-btn:hover {
    background: #b91c1c;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(220, 20, 60, 0.3);
}

/* Filtros rápidos */
.quick-filters {
    margin-top: 15px;
    padding-top: 15px;
    border-top: 1px solid #e5e7eb;
}

.filter-tabs {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

.filter-tab {
    padding: 6px 12px;
    border: 1px solid #d1d5db;
    border-radius: 20px;
    background: white;
    color: #374151;
    font-size: 0.85rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

.filter-tab:hover, .filter-tab.active {
    background: var(--azul);
    color: white;
    border-color: var(--azul);
}

/* --- Controles de Resultados --- */
.results-controls {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding: 15px 0;
    border-bottom: 2px solid #f3f4f6;
}

.results-info h3 {
    color: var(--azul);
    margin-bottom: 5px;
    font-size: 1.3rem;
}

.results-info p {
    color: #6b7280;
    font-size: 0.9rem;
}

.view-controls {
    display: flex;
    gap: 5px;
}

.view-btn {
    padding: 8px 12px;
    border: 1px solid #d1d5db;
    background: white;
    color: #6b7280;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.view-btn:hover, .view-btn.active {
    background: var(--azul);
    color: white;
    border-color: var(--azul);
}

/* --- Estados de Carga y Vacío --- */
.loading, .no-results, .error-state {
    text-align: center;
    padding: 60px 20px;
    min-height: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.spinner {
    width: 40px;
    height: 40px;
    border: 4px solid #f3f4f6;
    border-top: 4px solid var(--rojo);
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin: 0 auto 20px;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.loading p {
    color: #6b7280;
    font-size: 1.1rem;
}

.no-results-content, .error-content {
    max-width: 500px;
}

.no-results-content i, .error-content i {
    font-size: 4rem;
    color: #d1d5db;
    margin-bottom: 20px;
}

.no-results-content h3, .error-content h3 {
    color: #374151;
    font-size: 1.5rem;
    margin-bottom: 10px;
}

.no-results-content p, .error-content p {
    color: #6b7280;
    font-size: 1rem;
    margin-bottom: 25px;
}

.no-results-actions {
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
}

.btn-primary, .btn-secondary {
    padding: 10px 20px;
    border-radius: 6px;
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
    border: none;
}

.btn-primary {
    background: var(--rojo);
    color: white;
}

.btn-primary:hover {
    background: #b91c1c;
    transform: translateY(-1px);
}

.btn-secondary {
    background: white;
    color: #374151;
    border: 1px solid #d1d5db;
}

.btn-secondary:hover {
    background: #f9fafb;
    border-color: #9ca3af;
}

/* --- Modal de Propiedades --- */
.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 10000;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
}

.modal.hidden {
    display: none;
}

.modal-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(4px);
}

.modal-content {
    position: relative;
    background: white;
    border-radius: 12px;
    max-width: 900px;
    width: 100%;
    max-height: 90vh;
    overflow: hidden;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
    animation: modalSlideIn 0.3s ease;
}

@keyframes modalSlideIn {
    from {
        opacity: 0;
        transform: scale(0.9) translateY(-20px);
    }
    to {
        opacity: 1;
        transform: scale(1) translateY(0);
    }
}

.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 25px;
    border-bottom: 1px solid #e5e7eb;
    background: #f9fafb;
}

.modal-header h2 {
    color: var(--azul);
    font-size: 1.3rem;
    margin: 0;
}

.modal-close {
    background: none;
    border: none;
    font-size: 1.2rem;
    color: #6b7280;
    cursor: pointer;
    padding: 5px;
    border-radius: 4px;
    transition: all 0.3s ease;
}

.modal-close:hover {
    background: #e5e7eb;
    color: #374151;
}

.modal-body {
    max-height: calc(90vh - 80px);
    overflow-y: auto;
    padding: 25px;
}

/* --- Tarjetas de Propiedades Mejoradas --- */
.property-card {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
    cursor: pointer;
}

.property-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.property-card-image {
    position: relative;
    height: 200px;
    overflow: hidden;
}

.property-card-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
}

.property-card:hover .property-card-image img {
    transform: scale(1.05);
}

.property-card-badge {
    position: absolute;
    top: 10px;
    left: 10px;
    background: var(--rojo);
    color: white;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
}

.property-card-content {
    padding: 20px;
}

.property-card-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--azul);
    margin-bottom: 8px;
    line-height: 1.3;
}

.property-card-price {
    font-size: 1.4rem;
    font-weight: 800;
    color: var(--rojo);
    margin-bottom: 12px;
}

.property-card-details {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 15px;
}

.property-card-detail {
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 0.9rem;
    color: #6b7280;
}

.property-card-detail i {
    color: var(--azul);
    width: 16px;
}

.property-card-amenities {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
    margin-bottom: 15px;
}

.property-amenity {
    background: #f3f4f6;
    color: #374151;
    padding: 3px 8px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 500;
}

.property-card-actions {
    display: flex;
    gap: 10px;
}

.property-card-btn {
    flex: 1;
    padding: 8px 12px;
    border: 1px solid var(--azul);
    background: white;
    color: var(--azul);
    border-radius: 6px;
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    text-align: center;
    text-decoration: none;
}

.property-card-btn.primary {
    background: var(--azul);
    color: white;
}

.property-card-btn:hover {
    background: var(--azul);
    color: white;
}

.property-card-btn.primary:hover {
    background: #1e40af;
}

/* --- Vista de Lista --- */
.property-list-item {
    display: flex;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 15px;
    transition: all 0.3s ease;
    cursor: pointer;
}

.property-list-item:hover {
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.property-list-image {
    width: 200px;
    height: 150px;
    flex-shrink: 0;
    overflow: hidden;
}

.property-list-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.property-list-content {
    flex: 1;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.property-list-header {
    display: flex;
    justify-content: space-between;
    align-items: start;
    margin-bottom: 10px;
}

.property-list-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--azul);
    margin: 0;
}

.property-list-price {
    font-size: 1.3rem;
    font-weight: 800;
    color: var(--rojo);
    margin: 0;
}

.property-list-details {
    display: flex;
    gap: 20px;
    margin-bottom: 10px;
    flex-wrap: wrap;
}

.property-list-amenities {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 15px;
}

/* --- Vista de Modal Detallada --- */
.property-detail {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
}

.property-detail-gallery {
    position: relative;
}

.property-detail-images {
    display: flex;
    gap: 10px;
    overflow-x: auto;
    margin-bottom: 15px;
}

.property-detail-image {
    width: 200px;
    height: 150px;
    object-fit: cover;
    border-radius: 8px;
    cursor: pointer;
    transition: transform 0.3s ease;
}

.property-detail-image:hover {
    transform: scale(1.05);
}

.property-detail-info {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.property-detail-header {
    border-bottom: 1px solid #e5e7eb;
    padding-bottom: 20px;
}

.property-detail-title {
    font-size: 1.8rem;
    font-weight: 800;
    color: var(--azul);
    margin-bottom: 10px;
}

.property-detail-price {
    font-size: 2rem;
    font-weight: 900;
    color: var(--rojo);
    margin-bottom: 15px;
}

.property-detail-specs {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    margin-bottom: 20px;
}

.property-spec-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px;
    background: #f9fafb;
    border-radius: 6px;
}

.property-spec-item i {
    color: var(--azul);
    font-size: 1.1rem;
    width: 20px;
    text-align: center;
}

.property-spec-item span {
    font-weight: 600;
    color: #374151;
}

.property-detail-description {
    background: #f9fafb;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
}

.property-detail-description h4 {
    color: var(--azul);
    margin-bottom: 10px;
    font-size: 1.1rem;
}

.property-detail-description p {
    color: #6b7280;
    line-height: 1.6;
}

.property-detail-amenities-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin-bottom: 20px;
}

.property-amenity-item {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px;
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 6px;
}

.property-amenity-item i {
    color: var(--rojo);
    width: 16px;
    text-align: center;
}

.property-detail-actions {
    display: flex;
    gap: 15px;
    justify-content: center;
    padding-top: 20px;
    border-top: 1px solid #e5e7eb;
}

.property-detail-action {
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 8px;
    border: none;
}

.property-detail-action.primary {
    background: var(--rojo);
    color: white;
}

.property-detail-action.secondary {
    background: white;
    color: var(--azul);
    border: 2px solid var(--azul);
}

.property-detail-action:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* --- Responsive Design --- */
@media (max-width: 768px) {
    /* Buscador móvil */
    .buscadorcab .cont {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }
    
    .search-group {
        min-width: auto;
    }
    
    .filter-tabs {
        justify-content: center;
    }
    
    .search-btn {
        margin-top: 0;
        align-self: stretch;
    }
    
    /* Controles de resultados móvil */
    .results-controls {
        flex-direction: column;
        gap: 15px;
        align-items: stretch;
    }
    
    .view-controls {
        justify-content: center;
    }
    
    /* Tarjetas móviles */
    .property-card-details {
        grid-template-columns: 1fr;
        gap: 5px;
    }
    
    .property-card-amenities {
        justify-content: center;
    }
    
    .property-card-actions {
        flex-direction: column;
    }
    
    /* Vista de lista móvil */
    .property-list-item {
        flex-direction: column;
    }
    
    .property-list-image {
        width: 100%;
        height: 200px;
    }
    
    .property-list-content {
        padding: 15px;
    }
    
    .property-list-details {
        gap: 10px;
    }
    
    /* Modal móvil */
    .modal-content {
        margin: 10px;
        max-height: calc(100vh - 20px);
    }
    
    .modal-body {
        padding: 20px;
    }
    
    .property-detail {
        grid-template-columns: 1fr;
        gap: 20px;
    }
    
    .property-detail-specs {
        grid-template-columns: 1fr;
    }
    
    .property-detail-amenities-grid {
        grid-template-columns: 1fr;
    }
    
    .property-detail-actions {
        flex-direction: column;
    }
}

@media (max-width: 480px) {
    .property-detail-images {
        flex-direction: column;
    }
    
    .property-detail-image {
        width: 100%;
        height: 150px;
    }
    
    .no-results-actions {
        flex-direction: column;
        align-items: center;
    }
    
    .btn-primary, .btn-secondary {
        width: 100%;
        max-width: 200px;
    }
}

/* Estados de visibilidad */
.hidden {
    display: none !important;
}

.visible {
    display: block !important;
}

/* Prevenir zoom en inputs en iOS */
@media (max-width: 768px) {
    input, select, textarea {
        font-size: 16px !important;
    }
}
