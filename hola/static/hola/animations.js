// ===== EFECTO CONFETTI AL CREAR ARTÍCULO =====
function createConfetti() {
    const colors = ['#667eea', '#764ba2', '#11998e', '#38ef7d', '#f39c12', '#e74c3c'];
    const confettiCount = 100;
    
    for (let i = 0; i < confettiCount; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.left = Math.random() * 100 + '%';
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.animationDelay = Math.random() * 2 + 's';
        confetti.style.animationDuration = (Math.random() * 2 + 2) + 's';
        document.body.appendChild(confetti);
        
        // Remover después de la animación
        setTimeout(() => confetti.remove(), 4000);
    }
}

// Detectar si venimos de crear un artículo
if (window.location.search.includes('created=true')) {
    createConfetti();
}

// ===== EFECTO 3D TILT EN TARJETAS =====
const cards = document.querySelectorAll('.articulo');

cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = (y - centerY) / 10;
        const rotateY = (centerX - x) / 10;
        
        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-5px)`;
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
    });
});

// ===== EFECTO DE ESCRITURA EN EL TÍTULO =====
const h1 = document.querySelector('h1');
if (h1) {
    const text = h1.textContent;
    h1.textContent = '';
    let i = 0;
    
    function typeWriter() {
        if (i < text.length) {
            h1.textContent += text.charAt(i);
            i++;
            setTimeout(typeWriter, 80);
        }
    }
    
    typeWriter();
}

// ===== EFECTO DE PARTÍCULAS EN EL FONDO =====
function createParticle() {
    const particle = document.createElement('div');
    particle.className = 'particle';
    particle.style.left = Math.random() * 100 + '%';
    particle.style.animationDuration = (Math.random() * 3 + 3) + 's';
    document.body.appendChild(particle);
    
    setTimeout(() => particle.remove(), 6000);
}

// Crear partículas cada 500ms
setInterval(createParticle, 500);