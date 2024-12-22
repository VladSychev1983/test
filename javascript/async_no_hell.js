export const authUser = async function (userName, password) {
    const api = "https://dummyjson.com/";
    userName = "oliviaw";
    password = "oliviawpass";
    const result = {
        user: {
            id: null,
            firstName: null,
            lastName: null,
            cart: null,
          },
    };
    let response = await fetch(`${api}auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: userName,
          password: password,
        }),
    });
    let auth = await response.json();
    if (auth) {
        const { id, firstName, lastName } = auth;
        result.user = { id, firstName, lastName };
    }

    //getting cart
    let cart_response = await fetch(`${api}carts/user/${result.user.id}`);
    let carstData  = await cart_response.json();
    if (carstData) {
        let userCart = carstData.carts[0];
        const { total: totalSumm, discountedTotal: discountedSumm } = carstData.carts[0];
        result.user.cart = { totalSumm, discountedSumm };
        //console.log(userCart)
        let ProductsList = [];
        for (const product of userCart.products) {
            //id продукта в element.id
            let product_response = await fetch(`${api}products/${product.id}`);
            let productData = await product_response.json();
            if (productData) {
            const {
                id,
                title,
                description,
                price,
                discountPercentage: discount,
                rating,
              } = productData;
              let products = {
                id,
                title,
                description,
                price,
                discount,
                rating,
                count: product.quantity,
              }
                //console.log("================")
                //console.log(products)
                ProductsList.push(products)
                
            }

        }
        result.user.cart.products = ProductsList;
    }  
    return result;
}



authUser("atuny0", "9uQFF1Lh").then((result) => {
    //console.log(result)
      const user = result.user;
      const fullName = `${user.firstName} ${user.lastName}`;
  
      console.log(`Пользователь: ${fullName}`);
      console.log(`В корзине покупок ${fullName} находится товаров на сумму: ${user.cart.totalSumm}`);
      console.log(`С учетом скидок - ${user.cart.discountedSumm}`);
      console.log(`${fullName} собирается купить:`);
      user.cart.products.forEach((product) => console.log(`  - ${product.title} количеством ${product.count}`));
  });