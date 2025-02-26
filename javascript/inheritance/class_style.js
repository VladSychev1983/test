class Messanger {
    constructor(name) {
        this.name = name;
        //readonly property inside constructor
        Object.defineProperty(this,  'version', {
            get:  function() {
                return '10.0.6'
            }
        });
    }
    send(recipient, msg) {
        console.log(`message from ${recipient}: ${msg}`);
    }
}

Messanger.recipients = [
    34343,
    6556,
    676
];

class MultiMessanger extends Messanger {
    constructor(name, logo) {
        super(name);
        this.logo = logo;
    }
    send (recipient, msg) {
        if(Messanger.recipients.includes(recipient)) {
            super.send(recipient,  msg);
            return;
        }
        console.log(`message from MultiMessenger: ${recipient}: ${msg}`);

    }
}

const baseMessenger = new Messanger('Basic');
console.log(baseMessenger);

baseMessenger.send(123,'Hello!');

console.log(baseMessenger.version);

const viber = new MultiMessanger('Viber','V');
viber.send(123, 'my msg');
viber.send(676, 'my msg')
console.log(viber)
