class Service {
    publicMethod() {
        this.#hidden();
    }
    #hidden() {
        console.log("this is a hidden method");
    }
}

const service = new Service;
service.publicMethod();