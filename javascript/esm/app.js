//import './logs.js';
import './stats.js';
// использование определенных классов , функция , констант из импорта.
import { timeout, Client } from './logs.js';
// пример алиаса одинаковых импортированных объектов из разных модулей
// import { timeout as logsTimeout} from './logs.js';
// import { timeout as statsTimeout} from './stats.js';

//импортировать все из модуля.
// import * as logs from './logs.js';
// обращаться как к свойству.
//console.log(logs.timeout)
console.log('app.js executed!');
console.log(timeout, Client);