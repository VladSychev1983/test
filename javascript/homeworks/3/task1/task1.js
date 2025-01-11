window.addEventListener("scroll", () => {
    const allreveals = document.querySelectorAll(".reveal");
    for (const element of allreveals) {
        const StateVisible = isVisible(element);
        if (StateVisible === true) {
            element.classList.add("reveal_active");
        }
        else {
            element.classList.remove("reveal_active");
        }
    }

    function isVisible(el) {
        const {top, bottom} = el.getBoundingClientRect();
        if (bottom < 0) {
            return false;
        }
        if (top > window.innerHeight) {
            return false;
        }
        return true;
    }

});
