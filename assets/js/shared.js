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

    // ── Mobile Nav Docs Link & Auto-Open behavior ──
    const mobileDocsLink = document.querySelector('.mobile-docs-link');
    if (mobileDocsLink) {
        mobileDocsLink.addEventListener('click', function (e) {
            const sidebar = document.querySelector('.sidebar');
            const backdrop = document.getElementById('sidebar-backdrop');
            if (sidebar && backdrop) {
                // If we are already on a docs page, prevent actual navigation and just pop up the bottom sheet
                e.preventDefault();
                if (hamburger && mobileNav) {
                    hamburger.classList.remove('active');
                    mobileNav.classList.remove('active');
                }
                sidebar.classList.add('active');
                backdrop.classList.add('active');
            }
        });
    }

    // Auto-open docs menu if URL has open-menu parameter
    if (window.location.search.indexOf('open-menu=1') !== -1) {
        const sidebar = document.querySelector('.sidebar');
        const backdrop = document.getElementById('sidebar-backdrop');
        if (sidebar && backdrop) {
            // Delay slightly to allow main page layout to settle and give visual feedback
            setTimeout(function () {
                sidebar.classList.add('active');
                backdrop.classList.add('active');
            }, 100);
            
            // Clean URL query param from address bar without reloading
            try {
                const cleanUrl = window.location.protocol + "//" + window.location.host + window.location.pathname;
                window.history.replaceState({ path: cleanUrl }, '', cleanUrl);
            } catch (e) {
                console.warn('Could not clean history state', e);
            }
        }
    }

    // ── Mobile Docs Sidebar (Draggable FAB) ──
    const docToggle = document.getElementById('mobile-sidebar-toggle');
    const sidebar = document.querySelector('.sidebar');
    const sidebarClose = document.getElementById('sidebar-close');
    const backdrop = document.getElementById('sidebar-backdrop');

    if (docToggle && sidebar && backdrop) {
        var isDragging = false;
        var wasDragged = false;
        var startX = 0, startY = 0;
        var offsetX = 0, offsetY = 0;
        var dragThreshold = 8;

        docToggle.addEventListener('touchstart', function (e) {
            var touch = e.touches[0];
            startX = touch.clientX;
            startY = touch.clientY;
            var rect = docToggle.getBoundingClientRect();
            offsetX = touch.clientX - rect.left;
            offsetY = touch.clientY - rect.top;
            isDragging = false;
            wasDragged = false;
        }, { passive: true });

        docToggle.addEventListener('touchmove', function (e) {
            var touch = e.touches[0];
            var dx = touch.clientX - startX;
            var dy = touch.clientY - startY;

            if (!isDragging && (Math.abs(dx) > dragThreshold || Math.abs(dy) > dragThreshold)) {
                isDragging = true;
                wasDragged = true;
                docToggle.classList.add('dragging');
            }

            if (isDragging) {
                e.preventDefault();
                var newX = touch.clientX - offsetX;
                var newY = touch.clientY - offsetY;
                // Keep within viewport
                var maxX = window.innerWidth - docToggle.offsetWidth;
                var maxY = window.innerHeight - docToggle.offsetHeight;
                newX = Math.max(0, Math.min(newX, maxX));
                newY = Math.max(0, Math.min(newY, maxY));

                docToggle.style.left = newX + 'px';
                docToggle.style.top = newY + 'px';
                docToggle.style.right = 'auto';
                docToggle.style.bottom = 'auto';
            }
        }, { passive: false });

        docToggle.addEventListener('touchend', function () {
            if (isDragging) {
                // Snap to nearest left or right edge
                var rect = docToggle.getBoundingClientRect();
                var centerX = rect.left + rect.width / 2;
                var screenMid = window.innerWidth / 2;

                docToggle.style.transition = 'left 0.25s ease, right 0.25s ease';
                if (centerX < screenMid) {
                    docToggle.style.left = '16px';
                    docToggle.style.right = 'auto';
                } else {
                    docToggle.style.left = 'auto';
                    docToggle.style.right = '16px';
                }
                setTimeout(function () {
                    docToggle.style.transition = '';
                }, 300);
            }
            isDragging = false;
            docToggle.classList.remove('dragging');
        }, { passive: true });

        // Only open sidebar on tap (not drag)
        docToggle.addEventListener('click', function () {
            if (!wasDragged) {
                sidebar.classList.add('active');
                backdrop.classList.add('active');
            }
            wasDragged = false;
        });

        if (sidebarClose) {
            sidebarClose.addEventListener('click', function () {
                sidebar.classList.remove('active');
                backdrop.classList.remove('active');
            });
        }
        backdrop.addEventListener('click', function () {
            sidebar.classList.remove('active');
            backdrop.classList.remove('active');
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
