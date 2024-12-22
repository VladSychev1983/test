//пример кеширования с использованием коллекции map.

function createDataProvider() {
    const cache = new Map();
    
    return async function (url, options) {
        if (cache.has(url)) {
            return cache.get(url);
        }
        
        const response = await fetch(url, options);
        const data = await response.json();

        cache.set(url, data);

        return data;
    }
}

(async function () {
    const dataProvider = createDataProvider();
    let result = await Promise.all([
      dataProvider("https://dummyjson.com/products"),
      dataProvider("https://dummyjson.com/products/3"),
      dataProvider("https://fakestoreapi.com/users/"),
    ]);
    console.log(result);
})
