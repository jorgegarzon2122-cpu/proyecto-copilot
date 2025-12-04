// Funcionalidad básica del blog
document.addEventListener('DOMContentLoaded', function() {
    // Navegar a un post
    function navigateToPost(postId) {
        window.location.href = `posts/${postId}.html`;
    }

    // Volver al índice
    function backToHome() {
        window.location.href = '../index.html';
    }

    // Agregar event listeners a botones de lectura
    const readMoreButtons = document.querySelectorAll('.read-more-btn');
    readMoreButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const postId = this.getAttribute('data-post');
            navigateToPost(postId);
        });
    });

    // Back button functionality
    const backButton = document.querySelector('.back-btn');
    if (backButton) {
        backButton.addEventListener('click', function(e) {
            e.preventDefault();
            backToHome();
        });
    }

    // Resaltar código
    const codeBlocks = document.querySelectorAll('pre code');
    codeBlocks.forEach(block => {
        block.parentElement.style.position = 'relative';
    });
});