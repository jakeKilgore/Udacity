function display(movie) {
  if (!e) var e = window.event;
  e.cancelBubble = true;
  if(e.stopPropogation) e.stopPropogation();
  if(movie == null) {
    document.getElementById("footer").style.display = "none";
    document.getElementById("content").style.paddingBottom = "10px";
  }
  else {
    document.getElementById("footer").style.display = "flex";
    document.getElementById("content").style.paddingBottom = "335px";
  }
}
