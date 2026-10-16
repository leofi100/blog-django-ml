// Función para cambiar el tema
function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme');
    const icon = document.getElementById('theme-icon');
    const text = document.getElementById('theme-text');
    
    if (currentTheme === 'dark') {
        // Cambiar a modo claro
        html.setAttribute('data-theme', 'light');
        icon.textContent = '🌙';
        text.textContent = 'Oscuro';
        localStorage.setItem('theme', 'light');
    } else {
        // Cambiar a modo oscuro
        html.setAttribute('data-theme', 'dark');
        icon.textContent = '☀️';
        text.textContent = 'Claro';
        localStorage.setItem('theme', 'dark');
    }
}

// Cargar el tema guardado al iniciar
document.addEventListener('DOMContentLoaded', function() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    const icon = document.getElementById('theme-icon');
    const text = document.getElementById('theme-text');
    
    if (savedTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        icon.textContent = '☀️';
        text.textContent = 'Claro';
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        icon.textContent = '🌙';
        text.textContent = 'Oscuro';
    }
});