/* Andrés Vargas — Sastrería · interacciones */
(function () {
  "use strict";

  /* Header con fondo al hacer scroll */
  const header = document.querySelector(".site-header");
  const onScroll = () => {
    if (!header) return;
    header.classList.toggle("scrolled", window.scrollY > 40);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Menú móvil */
  const toggle = document.querySelector(".nav__toggle");
  const menu = document.querySelector(".nav__menu");
  if (toggle && menu) {
    toggle.addEventListener("click", () => {
      const open = menu.classList.toggle("open");
      toggle.classList.toggle("active", open);
      document.body.style.overflow = open ? "hidden" : "";
    });
    menu.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        menu.classList.remove("open");
        toggle.classList.remove("active");
        document.body.style.overflow = "";
      })
    );
  }

  /* Animaciones al entrar en viewport */
  const reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("visible");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -60px 0px" }
    );
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add("visible"));
  }

  /* Filtros de chips (telas / blog) */
  document.querySelectorAll("[data-filter-group]").forEach((group) => {
    const chips = group.querySelectorAll(".chip");
    const targetSel = group.getAttribute("data-filter-target");
    const items = document.querySelectorAll(targetSel + " [data-cat]");
    chips.forEach((chip) => {
      chip.addEventListener("click", () => {
        chips.forEach((c) => c.classList.remove("active"));
        chip.classList.add("active");
        const cat = chip.getAttribute("data-cat");
        items.forEach((item) => {
          const show = cat === "all" || item.getAttribute("data-cat") === cat;
          item.style.display = show ? "" : "none";
        });
      });
    });
  });

  /* Newsletter (demo, sin envío) */
  document.querySelectorAll(".newsletter").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const input = form.querySelector("input");
      if (input && input.value) {
        input.value = "";
        input.placeholder = "¡Gracias por suscribirte!";
      }
    });
  });
})();
