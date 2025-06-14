async function changeLanguage() {
    const lang = document.getElementById('language').value;
    const response = await fetch(`/static/translations/${lang}.json`);
    const translations = await response.json();
    document.querySelectorAll('[data-translate]').forEach(element => {
        const key = element.getAttribute('data-translate');
        element.textContent = translations[key] || key;
    });
}

document.addEventListener('DOMContentLoaded', () => {
    changeLanguage();
});