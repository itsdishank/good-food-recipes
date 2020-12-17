// JavaScript source code
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "anuragn") {
    x.className += " responsive";
  } else {
    x.className = "anuragn";
  }
  var y = document.getElementById("mainclear");
    if (y.className === "maincut") {
        y.className += " responsive";
    } else {
        y.className = "anuragn";
    }
}

