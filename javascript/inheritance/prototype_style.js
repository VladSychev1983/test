//prototype style.
function Messanger(name) {
    this.name = name;
}
Messanger.prototype.recipients = [
    3434,
    3432,
    3345
];

Messanger.prototype.send = function(recipient, msg) {
    //some code here
    console.log(`message from ${recipient}: ${msg}`);
}

function MultiMessanger(name, logo) {
    Messanger.call(this, name);
    this.logo = logo;
}
//copy prototype's Messanger to Mutimessanger 
MultiMessanger.prototype = Object.create(Messanger.prototype);
MultiMessanger.prototype.constructor = MultiMessanger;
//redefine method send
MultiMessanger.prototype.send = function(recipient,msg) {
    if (this.recipients.includes(recipient)) {
        Messanger.prototype.send.call(this, recipient, msg);
        return;
    }
    console.log(`message from MultiMessenger: ${recipient}: ${msg}`);
}

const viber = new MultiMessanger('Viber', 'V');
console.log(viber)

const messenger = new Messanger('Basic');

viber.send(94343, 'Hello!');
viber.send(3432, 'Hello!');
console.log(Messanger.prototype.testteest);
console.log(viber)
