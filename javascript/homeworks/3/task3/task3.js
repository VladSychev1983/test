window.addEventListener("DOMContentLoaded", () => {
const book = document.getElementById('book');
const fontsbuttoms = [ ...document.querySelectorAll(".font-size")];

for (const element of fontsbuttoms) {
    element.addEventListener("click",  () => {
        fontsbuttoms.forEach((item) =>
            item.classList.remove("font-size_active")
          );
          element.classList.add('font-size_active');
          book.classList.remove("book_fs-big", "book_fs-small");
          const size = element.dataset.size;
          if (size === "small") {
            book.classList.add("book_fs-small");
          } else if (size === "big") {
            book.classList.add("book_fs-big");
          }
    })
    }
})