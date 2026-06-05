function setupToggle(buttonSelector, targetSelector) {
    const button = document.querySelector(buttonSelector);
    const target = document.querySelector(targetSelector);

    if (!(button instanceof HTMLButtonElement) || !(target instanceof HTMLElement)) {
        return;
    }

    if (button.dataset.navToggleBound === "true") {
        return;
    }

    button.dataset.navToggleBound = "true";

    const header = button.closest(".site-header") ?? target.closest(".site-header");
    const desktopMediaQuery = window.matchMedia("(min-width: 48rem)");

    const isOpen = () => target.classList.contains("is-open");

    const setOpenState = (open) => {
        target.classList.toggle("is-open", open);
        button.setAttribute("aria-expanded", String(open));
    };

    const closeMenu = () => {
        if (!isOpen()) {
            return;
        }

        setOpenState(false);
    };

    button.addEventListener("click", () => {
        setOpenState(!isOpen());
    });

    target.addEventListener("click", (event) => {
        if (!(event.target instanceof HTMLAnchorElement)) {
            return;
        }

        closeMenu();
    });

    document.addEventListener("click", (event) => {
        if (!(event.target instanceof Node) || !isOpen()) {
            return;
        }

        if (header instanceof HTMLElement && header.contains(event.target)) {
            return;
        }

        closeMenu();
    });

    document.addEventListener("keydown", (event) => {
        if (event.key !== "Escape") {
            return;
        }

        closeMenu();
    });

    const resetForDesktop = () => {
        if (!desktopMediaQuery.matches) {
            return;
        }

        closeMenu();
    };

    if (typeof desktopMediaQuery.addEventListener === "function") {
        desktopMediaQuery.addEventListener("change", resetForDesktop);
    } else {
        desktopMediaQuery.addListener(resetForDesktop);
    }

    window.addEventListener("resize", resetForDesktop);
}

setupToggle(".site-nav-toggle", "#primary-navigation");
