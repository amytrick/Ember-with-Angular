"use strict";

// DISPLAY PREVIOUS PHOTO
$("#previous").on("click", () => {
  $.get("/previous.json", function (data) {
    console.log("click");
    $("#large-photo").attr("src", data.photo_path);
    $("input[name=star-radios][value=" + data.photo_rating + "]").prop(
      "checked",
      true
    );
    $("#add-to-album-form").attr("action", "/add-to-album/" + data.photo_id);
    $("#add-tag-form").attr("action", "/tag/" + data.photo_id);
    $("#individual-tag-div").html("");
    for (var i = 0; i < data.tags.length; i++) {
      $("#individual-tag-div").append(
        "<form action='/delete-tag/" +
          data.photo_id +
          "/" +
          data.tag_ids[i] +
          "'><p><button><div><li><span style='background:transparent' data-toggle='tooltip' data-placement='right' title='Remove tag'>" +
          data.tags[i] +
          "</span></li></div></button></p></form>"
      );
    }
  });
});

// DISPLAY NEXT PHOTO
$("#next").on("click", () => {
  $.get("/next.json", function (data) {
    console.log("click");
    $("#large-photo").attr("src", data.photo_path);
    $("input[name=star-radios][value=" + data.photo_rating + "]").prop(
      "checked",
      true
    );
    $("#add-to-album-form").attr("action", "/add-to-album/" + data.photo_id);
    $("#add-tag-form").attr("action", "/tag/" + data.photo_id);
    $("#individual-tag-div").html("");
    for (var i = 0; i < data.tags.length; i++) {
      $("#individual-tag-div").append(
        "<form action='/delete-tag/" +
          data.photo_id +
          "/" +
          data.tag_ids[i] +
          "'><p><button><div><li><span style='background:transparent' data-toggle='tooltip' data-placement='right' title='Remove tag'>" +
          data.tags[i] +
          "</span></li></div></button></p></form>"
      );
    }
  });
});

// ALL TOOLTIPS
$(function () {
  $('[data-toggle="tooltip"]').tooltip();
});

// AUTOMATICALLY UPLOAD PHOTO FROM FILE SELECTOR
document.getElementById("photo-upload-button").onchange = function () {
  document.getElementById("upload-photo-form").submit();
};

// SUBMIT STAR RATING UPON CLICK
$("input[name=star-radios]").on("change", function () {
  $(this).closest("form").submit();
});

// SUBMIT RATING FILTER UPON CLICK ON STAR PORTION
$("input[name=filter-rating]").on("change", function () {
  $(this).closest("form").submit();
});

// SUBMIT ADD TO ALBUM WITH DELAY

$("input[name=add-to-album]").on("change", function () {
  $(this).closest("form").delay(300).submit();
});

// HIDE ALL HIDDEN DIVS
$(".hidden").hide();

// OPEN RENAME ALBUM TEXTBOX
$("#album-title").click(function () {
  $("#rename-album-div").toggle();
});

$("#filter-button").click(function () {
  $("#rating-filter-div").toggle();
});
