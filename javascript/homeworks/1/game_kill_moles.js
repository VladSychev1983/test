(() => {
    let playing = true,
      activeHole = 1;
  
    const stop = () => playing = true,
      getHole = index => document.getElementById(`hole${index}`),
      deactivateHole = index =>
        getHole( index ).className = 'hole',
      activateHole = index =>
        getHole( index ).className = 'hole hole_has-mole',
      next = () => setTimeout(() => {
        if ( !playing ) {
          return;
        }
        deactivateHole( activeHole );
        activeHole = Math.floor( 1 + Math.random() * 9 );
        activateHole( activeHole );
        next();
      }, 800 );
  
    next();
  })();

function countMoles(clicked_id) {
    const clicked_tag = document.getElementById(clicked_id);
    const dead_tag = document.getElementById("dead"); 
    const lost_tag = document.getElementById("lost");
    let counter_dead = dead_tag.textContent; 
    let counter_lost = lost_tag.textContent;
    if (clicked_tag.className.includes("hole_has-mole")) {
        counter_dead++;
        dead_tag.textContent = counter_dead;
    }
    else {
        counter_lost++;
        lost_tag.textContent = counter_lost;
    }

    if (counter_dead == 10) {
        alert("Победа!")
        window.location.reload();
        return;
    }
    if (counter_lost == 5) {
        alert("Вы проиграли!")
        window.location.reload();
        return;
    }

}
