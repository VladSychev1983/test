export const getAllProducts = async function () {
    let result = [];
      try {
      const response = await fetch("https://dummyjson.com/products");
      result = response.json();
      }
      catch(error) {
          console.error('Произошла ошибка!', error)
          }
    return result;
  };

  getAllProducts().then((products) => {
    console.log("Получен список товаров");
    console.log(products); // Ожидаем что список товаров не пустой
  });