/* ===========================
   FUNCIONALIDAD DE NAVEGACIÓN
   =========================== */

document.addEventListener('DOMContentLoaded', function() {
    initializeNavigation();
    initializeTableOfContents();
    initializeSmoothScroll();
    initializeLazyLoad();
});

// Navegación activa
function initializeNavigation() {
    const navLinks = document.querySelectorAll('nav a');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            navLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Detectar scroll y activar nav automáticamente
    window.addEventListener('scroll', function() {
        const sections = document.querySelectorAll('section[id]');
        
        sections.forEach(section => {
            const rect = section.getBoundingClientRect();
            if (rect.top <= 150 && rect.bottom >= 150) {
                const id = section.getAttribute('id');
                navLinks.forEach(link => link.classList.remove('active'));
                const activeLink = document.querySelector(`nav a[href="#${id}"]`);
                if (activeLink) activeLink.classList.add('active');
            }
        });
    });
}

// Tabla de contenidos
function initializeTableOfContents() {
    const toc = document.getElementById('toc');
    if (!toc) return;

    const sections = document.querySelectorAll('section[id]');
    const tocList = document.createElement('ul');

    sections.forEach(section => {
        const h2 = section.querySelector('h2');
        if (h2) {
            const li = document.createElement('li');
            const a = document.createElement('a');
            a.href = '#' + section.id;
            a.textContent = h2.textContent;
            li.appendChild(a);
            tocList.appendChild(li);
        }
    });

    toc.appendChild(tocList);
}

// Scroll suave
function initializeSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
}

// Lazy loading de imágenes
function initializeLazyLoad() {
    const images = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            });
        });

        images.forEach(img => imageObserver.observe(img));
    }
}

// Función para copiar código
function copyToClipboard(element) {
    const text = element.textContent;
    navigator.clipboard.writeText(text).then(() => {
        const originalText = element.textContent;
        element.textContent = '✓ Copiado!';
        setTimeout(() => {
            element.textContent = originalText;
        }, 2000);
    });
}

// Expandir/Contraer secciones
function toggleSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.classList.toggle('hidden');
    }
}