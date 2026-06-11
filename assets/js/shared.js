/* ═══════════════════════════════════════════
   OmniIDE Shared JavaScript
   Version: 1.0.0
   ═══════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', function () {
    // ── Navigation scroll behavior ──
    const nav = document.querySelector('.site-nav');
    if (nav) {
        window.addEventListener('scroll', function () {
            nav.classList.toggle('scrolled', window.scrollY > 50);
        });
    }

    // ── Mobile hamburger menu ──
    const hamburger = document.querySelector('.nav-hamburger');
    const mobileNav = document.querySelector('.mobile-nav');
    if (hamburger && mobileNav) {
        hamburger.addEventListener('click', function () {
            hamburger.classList.toggle('active');
            mobileNav.classList.toggle('active');
        });
        mobileNav.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                hamburger.classList.remove('active');
                mobileNav.classList.remove('active');
            });
        });
    }

    // ── FAQ Accordion ──
    document.querySelectorAll('.faq-question').forEach(function (btn) {
        btn.addEventListener('click', function () {
            var item = this.closest('.faq-item');
            var wasOpen = item.classList.contains('open');
            // Close all items in the same FAQ section
            item.parentNode.querySelectorAll('.faq-item').forEach(function (i) {
                i.classList.remove('open');
            });
            if (!wasOpen) item.classList.add('open');
        });
    });

    // ── Sidebar search (docs) ──
    var sidebarSearch = document.getElementById('sidebar-search');
    if (sidebarSearch) {
        sidebarSearch.addEventListener('input', function () {
            var query = this.value.toLowerCase().trim();
            document.querySelectorAll('.sidebar-link').forEach(function (link) {
                var text = link.textContent.toLowerCase();
                link.style.display = text.indexOf(query) !== -1 ? '' : 'none';
            });
            document.querySelectorAll('.sidebar-section').forEach(function (sec) {
                var visible = sec.querySelectorAll('.sidebar-link:not([style*="display: none"])').length;
                sec.style.display = visible > 0 || query === '' ? '' : 'none';
            });
        });
    }

    // ── Smooth scroll for anchor links ──
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
        a.addEventListener('click', function (e) {
            var target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                window.scrollTo({ top: target.offsetTop - 80, behavior: 'smooth' });
            }
        });
    });

    // ── Active sidebar link highlighting ──
    var currentPath = window.location.pathname;
    document.querySelectorAll('.sidebar-link').forEach(function (link) {
        if (link.getAttribute('href') === currentPath || 
            link.getAttribute('href') === currentPath.replace(/\/$/, '') ||
            link.getAttribute('href') + '/' === currentPath) {
            link.classList.add('active');
        }
    });
});
