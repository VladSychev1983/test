//Как в родительском классе, вызвать метод из дочернего?
//1 Создать объект дочернего класса:

class parentClass {
    constructor() {
      this.extendMethod();
    }
    extendMethod() { }
  }
  
  class extendClass extends parentClass {
    extendMethod() {
      console.log('Hi');
    }
  }
  
  new extendClass();

  //Передать дочерний элемент в родительский:

  class parentClass2 {
    constructor(child = null) {
      child?.extendMethod();
    }
  }
  
  class extendClass2 extends parentClass2 {
    extendMethod() {
      console.log('Hi');
    }
  }
  
  new parentClass2(new extendClass2());

  //Создать интерфейс (базовый класс) и оба класса унаследовать от него:

  class IBase {
    constructor() {
      this.extendMethod();
    }
    extendMethod() { }
  }
  
  class A extends IBase {
    extendMethod() {
      console.log('Hi from A');
    }
  }
  class B extends IBase {
    extendMethod() {
      console.log('Hi from B');
    }
  }

  const objParent = new IBase();
 //const obj1 = new IBase(new A());
 //const obj2 = new IBase(new B());

  const car = {
    model: 'Toyota',
    year: 2007,
    showModel: function(color, engine){
      console.log(this.model, color, engine);
    }
  };
  const anotherCar = {
    model: 'Benz',
    year: 1998,
    showModel: function(model, year){
    console.log(this.model);
    }
  };

  car.showModel.call(anotherCar, 'red', 'diesel');
  car.showModel.apply(anotherCar,['red', 'diesel']);
