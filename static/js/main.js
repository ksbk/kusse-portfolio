function setupToggle(buttonSelector, targetSelector) {
    const button = document.querySelector(buttonSelector);
    const target = document.querySelector(targetSelector);

    if (!(button instanceof HTMLButtonElement) || !(target instanceof HTMLElement)) {
        return;
    }

    button.addEventListener("click", () => {
        const isOpen = target.classList.toggle("is-open");
        button.setAttribute("aria-expanded", String(isOpen));
    });

    target.addEventListener("click", (event) => {
        if (!(event.target instanceof HTMLAnchorElement)) {
            return;
        }

        target.classList.remove("is-open");
        button.setAttribute("aria-expanded", "false");
    });
}

setupToggle(".site-nav-toggle", "#primary-navigation");
