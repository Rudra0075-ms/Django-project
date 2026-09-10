(function () {
  "use strict";

  function qs(selector, root) {
    return (root || document).querySelector(selector);
  }

  function qsa(selector, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(selector));
  }

  /* ----- Mobile sidebar ----- */
  function initSidebar() {
    var shell = qs("#app-shell");
    var sidebar = qs("#sidebar");
    var overlay = qs("#sidebar-overlay");
    var toggle = qs("#menu-toggle");

    if (!shell || !sidebar || !toggle) return;

    function setOpen(open) {
      sidebar.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close navigation" : "Open navigation");
      if (overlay) {
        if (open) {
          overlay.hidden = false;
        } else {
          overlay.hidden = true;
        }
      }
      document.body.style.overflow = open ? "hidden" : "";
    }

    toggle.addEventListener("click", function () {
      setOpen(!sidebar.classList.contains("is-open"));
    });

    if (overlay) {
      overlay.addEventListener("click", function () {
        setOpen(false);
      });
    }

    qsa(".nav-link", sidebar).forEach(function (link) {
      link.addEventListener("click", function () {
        if (window.matchMedia("(max-width: 899px)").matches) {
          setOpen(false);
        }
      });
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") setOpen(false);
    });

    window.addEventListener("resize", function () {
      if (window.matchMedia("(min-width: 900px)").matches) {
        setOpen(false);
      }
    });
  }

  /* ----- Flash dismiss ----- */
  function initFlash() {
    qsa(".flash-dismiss").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var flash = btn.closest(".flash");
        if (flash) flash.remove();
      });
    });
  }

  /* ----- Password show / hide ----- */
  function initPasswordToggle() {
    qsa("[data-password-toggle]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var wrap = btn.closest(".input-wrap");
        var input = wrap ? qs("[data-password-input]", wrap) : null;
        if (!input) return;

        var show = input.type === "password";
        input.type = show ? "text" : "password";
        btn.setAttribute("aria-label", show ? "Hide password" : "Show password");
        btn.setAttribute("title", show ? "Hide password" : "Show password");

        var icon = qs("i", btn);
        if (icon) {
          icon.className = show ? "fa-regular fa-eye-slash" : "fa-regular fa-eye";
        }
      });
    });
  }

  /* ----- Photo preview ----- */
  function initPhotoPreview() {
    qsa("[data-photo-upload]").forEach(function (block) {
      var input = qs('input[type="file"]', block);
      var preview = qs("[data-photo-preview]", block);
      if (!input || !preview) return;

      input.addEventListener("change", function () {
        var file = input.files && input.files[0];
        if (!file || !file.type.match(/^image\//)) return;

        var reader = new FileReader();
        reader.onload = function (event) {
          preview.innerHTML = "";
          var img = document.createElement("img");
          img.src = event.target.result;
          img.alt = "Selected photo preview";
          preview.appendChild(img);
        };
        reader.readAsDataURL(file);
      });
    });
  }

  /* ----- Delete confirmation ----- */
  function initDeleteConfirm() {
    qsa("[data-confirm-delete]").forEach(function (form) {
      form.addEventListener("submit", function (event) {
        var message =
          form.getAttribute("data-confirm-message") ||
          "Delete this student? This cannot be undone.";
        if (!window.confirm(message)) {
          event.preventDefault();
        }
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initSidebar();
    initFlash();
    initPasswordToggle();
    initPhotoPreview();
    initDeleteConfirm();
  });
})();
