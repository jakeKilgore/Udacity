$(document).ready(function() {
  $(".content").on("click", {movie: null}, display);
  $(".poster").on("click", {movie: "movie"}, display);
  $(".footer").hide();
  $(".footer").css("visibility", "visible");

  /**
  @description Toggle the existance of the footer when a poster is clicked on.
  */
  function display(event) {
    event.cancelBubble = true;
    event.stopPropagation();
    if (event.data.movie === null) {
      $(".footer").slideUp(setContentHeight(null));
      $(".trailer").attr("src", "");
    }
    else {
      $(".trailer").attr("src", "https://www.youtube.com/embed/E7N7v4qy8zM?controls=0&rel=0&autoplay=1");
      $(".footer").slideDown(setContentHeight(".footer"));
      $("html, body").animate({
        scrollTop: scrollHelper(this)
      });
    }
  }

  /**
  @description Place extra space at the bottom based on the element passed in.
  @param {Element} element - Element to base the space at the bottom of content on.
  */
  function setContentHeight(element) {
    var height = 0;
    if(element) {
      height = $(element).outerHeight();
    }
    $(".content").animate({
      marginBottom: height
    });
  }

  /**
  @description Smoothly scroll to target element. Place it directly above the footer.
  @param {Element} element - Target element for scrolling.
  */
  function scrollHelper(element) {
    var currentOffset = $(element).offset().top;
    var windowOffset = $(".footer").innerHeight() - $(window).height();
    return currentOffset + windowOffset + $(element).innerHeight();
  }
});
