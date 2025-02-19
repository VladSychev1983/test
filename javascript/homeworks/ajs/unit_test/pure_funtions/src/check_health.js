export default function check_health(health_obj) {
    if (health_obj.health >= 50) {
        return 'healthy';
    }
    else if (health_obj.health >= 15  && health_obj.health < 50 ) {
        return 'wounded';
    }
    else {
        return 'critical';
    }
}
//let obj = {name: 'Маг', health: 30};
//let res = check_health(obj);
//console.log(res);