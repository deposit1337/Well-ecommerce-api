
$(document).ready(function () {
  var searchForm = $(".search-form");
  var searchIcon = $("#search-icon");
  var findButton = $(".find-btn");

  $(document).on("click", function (event) {
    if (
      !searchForm.is(event.target) &&
      searchForm.has(event.target).length === 0
    ) {
      if (searchForm.hasClass("expanded")) {
        searchForm
          .css("visibility", "visible")
          .animate({ width: 0, opacity: 0 }, 300, function () {
            searchForm.removeClass("expanded");
            searchForm
              .addClass("hidden")
              .css({ width: "100%", visibility: "hidden" });
            findButton.css("opacity", 0);
            searchIcon.fadeIn(100);
          });
      }
    }
  });

  $("#search-icon").click(function () {
    if (searchForm.hasClass("expanded")) {
      searchForm
        .css("visibility", "visible")
        .animate({ width: 0, opacity: 0 }, 300, function () {
          searchForm.removeClass("expanded");
          searchForm
            .addClass("hidden")
            .css({ width: "100%", visibility: "hidden" });
          findButton.css("opacity", 0);
          searchIcon.fadeIn(100);
        });
    } else {
      searchIcon.hide();
      searchForm.removeClass("hidden").css({ width: 0, visibility: "visible" });

      searchForm.animate({ width: 300, opacity: 1 }, 300, function () {
        findButton.css("opacity", 1);
        searchForm.addClass("expanded");
        findButton.addClass("test");
      });
    }
  });
});
