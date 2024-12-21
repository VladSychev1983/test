import { validData, corruptedData } from "./data.js";
export const parseToJSON = function (data) {
    let json = null;
  
    /*
     * Необходимо реализовать преобразование переданных данных
     * из текстового формата в формат json, используя JSON.parse.
     * Функция вернёт результат преобразования. Если в процессе
     * преобразования возникнет ошибка, необходмо вернуть
     * пустой объект {}.
     */
      try {
          json = JSON.parse(data);
          }
      catch(error) {
          json = {};
          }
  
    return json;
  };
  
  let data = parseToJSON(corruptedData);

  console.log(data) // Ожидаем { }
  console.log(data.products?.length) // Ожидаем undefined
  
  data = parseToJSON(validData);
  
  console.log(data) // Ожидаем объект с не пустым свойством users
  console.log(data.users?.length) // Ожидаем 30