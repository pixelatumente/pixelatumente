// Menú móvil — toggle con hamburguesa
(function () {
  const menuToggle = document.getElementById('menu-toggle');
  const mobileNav = document.getElementById('mobile-nav');

  if (!menuToggle || !mobileNav) return;

  function setMenu(open) {
    mobileNav.hidden = !open;
    menuToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    menuToggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  }

  menuToggle.addEventListener('click', function () {
    setMenu(mobileNav.hidden);
  });

  // Cerrar al hacer clic en un enlace del menú móvil
  mobileNav.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      setMenu(false);
    });
  });

  // Cerrar con Escape
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !mobileNav.hidden) {
      setMenu(false);
      menuToggle.focus();
    }
  });
})();
