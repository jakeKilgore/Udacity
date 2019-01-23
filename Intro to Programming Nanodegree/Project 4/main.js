$(document).ready(function() {
  $("html, body").on("click", {movie: null}, display);
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
      setMovieDetails(this);
      $(".footer").slideDown(setContentHeight(".footer"));
      $("html, body").animate({
        scrollTop: scrollHelper(this)
      });
      setDescriptionHeight();
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
    var windowOffset = $(".footer").outerHeight() - $(window).height();
    return currentOffset + windowOffset + $(element).outerHeight();
  }

  /**
  @description Set the trailer, title, and description from the poster data.
  @param {Element} element - Selected movie to take data from.
  */
  function setMovieDetails(element) {
    $(".trailer").attr("src", $(element).data("trailer"));
    $(".title").html($(element).data("title"));
    $(".description").html($(element).data("description"));
  }

  /**
  @description Set the height of the movie description to fit in the footer.
  */
  function setDescriptionHeight() {
    var height = $(".trailer").outerHeight() - $(".title").outerHeight();
    height -= $(".footer").innerHeight() - $(".footer").height();
    $(".description").css("maxHeight", height);
  }


  $(window).resize(function() {
    setDescriptionHeight();
  });
});
