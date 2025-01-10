document.addEventListener("DOMContentLoaded", () => {
    const tabContainers = document.querySelectorAll(".tab__navigation");
  
    tabContainers.forEach((tabContainer) => {
      const tabs = [ ...tabContainer.querySelectorAll(".tab")]; 
      const contents = Array.from(tabContainer.nextElementSibling.querySelectorAll(".tab__content")
    ); 

      // Обрабатываем каждую вкладку.
      tabs.forEach((tab, index) => {
        tab.addEventListener("click", () => {
          // Убираем активные классы 
          tabs.forEach((t) => t.classList.remove("tab_active"));
          contents.forEach((c) => c.classList.remove("tab__content_active"));
          // Добавляем активные классы 
          tab.classList.add("tab_active");
          contents[index].classList.add("tab__content_active");
        });
      });
    });
  });