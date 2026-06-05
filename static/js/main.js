const initializedToggles = new WeakSet();

function setupToggle(buttonSelector, targetSelector) {
    const button = document.querySelector(buttonSelector);
    const target = document.querySelector(targetSelector);

    if (!(button instanceof HTMLButtonElement) || !(target instanceof HTMLElement)) {
        return;
    }

    if (initializedToggles.has(button)) {
        return;
    }

    initializedToggles.add(button);

    const desktopNavigation = window.matchMedia("(min-width: 48rem)");
    const header = button.closest(".site-header");

    function setOpen(isOpen) {
        target.classList.toggle("is-open", isOpen);
        button.setAttribute("aria-expanded", String(isOpen));
    }

    function isOpen() {
        return target.classList.contains("is-open");
    }

    button.addEventListener("click", () => {
        setOpen(!isOpen());
    });

    target.addEventListener("click", (event) => {
        if (!(event.target instanceof HTMLAnchorElement)) {
            return;
        }

        setOpen(false);
    });

    document.addEventListener("keydown", (event) => {
        if (event.key !== "Escape" || !isOpen()) {
            return;
        }

        setOpen(false);
        button.focus();
    });

    document.addEventListener("click", (event) => {
        if (!isOpen() || !(event.target instanceof Node)) {
            return;
        }

        if (header instanceof HTMLElement && header.contains(event.target)) {
            return;
        }

        setOpen(false);
    });

    desktopNavigation.addEventListener("change", (event) => {
        if (event.matches) {
            setOpen(false);
        }
    });
}

setupToggle(".site-nav-toggle", "#primary-navigation");
