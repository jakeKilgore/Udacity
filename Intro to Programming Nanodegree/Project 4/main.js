$(document).ready(function() {
  $("#content").on("click", {movie: null}, display);
  $(".movie").on("click", {movie: "movie"}, display);
  $("#footer").hide();
  $("#footer").css("visibility", "visible");

  /**

  */
  function display(event) {
    event.cancelBubble = true;
    event.stopPropagation();
    if (event.data.movie === null) {
      $("#footer").slideUp(setContentHeight(null));
      $("#trailer").attr("src", "");
    }
    else {
      $("#trailer").attr("src", "https://www.youtube.com/embed/E7N7v4qy8zM?controls=0&rel=0&autoplay=1");
      $("#footer").slideDown(setContentHeight("#footer"));
      $("html, body").animate({
        scrollTop: scrollHelper(this)
      });
    }
  }

  /**

  */
  function setContentHeight(element) {
    var height = 0;
    if(element !== null) {
      height = $(element).outerHeight();
    }
    $("#content").animate({
      marginBottom: height
    });
  }

  /**

  */
  function scrollHelper(element) {
    var currentOffset = $(element).offset().top;
    var windowOffset = $("#footer").innerHeight() - $(window).height();
    return currentOffset + windowOffset + $(element).innerHeight();
  }
});
