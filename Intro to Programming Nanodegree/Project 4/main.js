$(document).ready(function() {
  $("#content").on("click", {movie: null}, display);
  $(".movie").on("click", {movie: "movie"}, display);
  $("#footer").hide();
});

function display(event) {
  event.cancelBubble = true;
  event.stopPropagation();
  if (event.data.movie == null) {
    $("#footer").slideUp(400, setContentHeight(null));
  }
  else {
    $("#footer").slideDown(400, setContentHeight("#footer"));
    $("html, body").animate({
      scrollTop: $(this).offset().top
    });
  }
}

function setContentHeight(element) {
  var height = 0;
  if(element != null) {
    height = $(element).outerHeight();
  }
  $("#content").animate({
    marginBottom: height
  });
}
