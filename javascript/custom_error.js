export const validate = function (amount) {
    //добавляем в класс error собственную ошибку.
    let objerror = {
        name: 'NegativeAmountError',
        message: "Недопустимое значение суммы денежных средств. Нельзя отправлять отрицательную сумму."
    }
      class NegativeAmountError extends Error {
          constructor(message) {
              super(message);
              this.name = objerror.name;
          }
      }
      const myCustomError = new  NegativeAmountError(objerror.message);
      if (amount < 0) {
          throw myCustomError;
            }
      return amount;
  };

  let amount = 426;
  try {
    validate(amount);
  } catch (error) {
    // Ожидаем что этот блок не сработает для amount = 426
    console.log("сумма =", amount);
    console.log("Ошибка:", error.name);
    console.log("Описание:", error.message);
  }
  
  amount = -17;
  
  try {
    validate(amount);
  } catch (error) {
    // Ожидаем что этот блок сработает для amount = -17
    console.log("сумма =", amount);
    console.log(error.name); // Ожидаем имя ошибки - "NegativeAmountError"
    console.log(error.message); // Ожидаем описание ошибки - "Недопустимое значение суммы денежных средств. Нельзя отправлять отрицательную сумму.
  }