document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('searchForm');
    const loadingOverlay = document.getElementById('loadingOverlay');

    if (!form || !loadingOverlay) {
        return;
    }

    form.addEventListener('submit', function () {
        loadingOverlay.hidden = false;
    });
});