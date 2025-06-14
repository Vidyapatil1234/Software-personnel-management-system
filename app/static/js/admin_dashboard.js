/* admin_dashboard.js */
document.addEventListener('DOMContentLoaded', function() {
    // Add any interactive JavaScript functionality here
    // Example: Add hover effects or dynamic content loading

    const featureLinks = document.querySelectorAll('.dashboard-features .feature-list li a');

    featureLinks.forEach(link => {
        link.addEventListener('mouseover', function() {
            this.style.textDecoration = 'underline';
        });

        link.addEventListener('mouseout', function() {
            this.style.textDecoration = 'none';
        });
    });
});