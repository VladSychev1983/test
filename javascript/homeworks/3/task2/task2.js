"use strict";

const getAllRotationsClasses = document.querySelectorAll(".rotator span");
let count = 1;

const rotation = function() {
  getAllRotationsClasses.forEach(function(elem, index) {
    const color = elem.dataset.color;

    if (elem.className == "rotator__case rotator__case_active") {
        elem.classList.remove("rotator__case_active");
    }
    elem.style.color = color;
    elem.classList.toggle("rotator__case", count !== index);
  });

  count++;
  if (count >= getAllRotationsClasses.length) {
    count = 0;
  }
}

setInterval(rotation, 1000);
    