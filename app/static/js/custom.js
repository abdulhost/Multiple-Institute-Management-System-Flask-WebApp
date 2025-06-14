// Fade-in animation on scroll
document.addEventListener('DOMContentLoaded', () => {
    const elements = document.querySelectorAll('.fade-in');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    elements.forEach(element => {
        observer.observe(element);
    });
});

document.addEventListener('DOMContentLoaded', () => {
    // Sidebar navigation
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.demo-section');

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const sectionId = link.getAttribute('data-section');
            
            // Update active states
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');

            // Toggle sections with animation
            sections.forEach(section => {
                if (section.id === sectionId) {
                    section.classList.remove('d-none');
                    section.style.opacity = '0';
                    setTimeout(() => {
                        section.style.transition = 'opacity 0.5s ease-in';
                        section.style.opacity = '1';
                    }, 50);
                } else {
                    section.style.transition = 'opacity 0.3s ease-out';
                    section.style.opacity = '0';
                    setTimeout(() => section.classList.add('d-none'), 300);
                }
            });
        });
    });

    // Search functionality
    const searchInput = document.querySelector('#search-input');
    if (searchInput) {
        searchInput.addEventListener('input', () => {
            const query = searchInput.value.toLowerCase();
            const currentSection = document.querySelector('.demo-section:not(.d-none)').id;
            window.dispatchEvent(new CustomEvent('searchData', { detail: { query, section: currentSection } }));
        });
    }

    // Filter functionality
    const filters = document.querySelectorAll('#institute-filter, #class-filter, #attendance-filter, #homework-filter');
    filters.forEach(filter => {
        filter.addEventListener('change', () => {
            const section = filter.closest('.demo-section').id;
            const value = filter.value;
            window.dispatchEvent(new CustomEvent('filterData', { detail: { section, value } }));
        });
    });

    // Modal handling
    document.addEventListener('showDetails', (e) => {
        const { title, content } = e.detail;
        document.getElementById('modalTitle').textContent = title;
        document.getElementById('modalBody').innerHTML = content;
        const modal = new bootstrap.Modal(document.getElementById('detailsModal'));
        modal.show();
    });
});