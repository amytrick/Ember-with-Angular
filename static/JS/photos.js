'use strict';

// const selectPhoto = () => {

// }

// $( ".library-img" ).click(function() {
//   console.log('click');
// });

// function addAlbum (evt) {
//   evt.preventDefault();

//   $.get("/add_album", (results) => {
//     $("#test-album").html(results);
//   });
//   console.log(results);
// }

// $('#add-album-button').on('click', addAlbum);


// $("#add-tag").on('submit',function() {
//     console.log('click');
// });

//     function addTag (evt) {
//         evt.preventDefault();

//         $.post("/tag/{{photo.photo_id}}"), (results) => {
//             $("#existing-tags").html(results);
//         };
//     }


// $("#delete-tag<tag_id>").on('click', function {
//     console.log('click');
// });

//     function deleteTag (evt) {
//         evt.preventDefault();

//         $.post("/delete_tag"), (results) => {
//             $("#existing-tags").html(results)
//         };
//     }


// function printDate(evt) {
//     $.get('/print-date', (results) => {
//         $('#date').html(results)
//     });
// }
// $('.library').on( "load", printDate)


// $('#myModal').modal(options) 
// calling a pop up modal




// DISPLAY PREVIOUS PHOTO
$('#previous').on('click', () => {
   $.get('/previous.json', function(data){
        console.log("click")
        $('#large-photo').attr("src",data.photo_path);
        $('input[name=star-radios][value=' + data.photo_rating + ']').prop('checked',true);
    });
});


// DISPLAY NEXT PHOTO
$('#next').on('click', () => {
   $.get('/next.json', function(data){
        console.log("click")
        $('#large-photo').attr("src",data.photo_path)
        $('input[name=star-radios][value=' + data.photo_rating + ']').prop('checked',true);
    });
});


// ALL TOOLTIPS
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })


// AUTOMATICALLY UPLOAD PHOTO FROM FILE SELECTOR
document.getElementById("photo-upload-button").onchange = function() {
    document.getElementById("upload-photo-form").submit();
}



// SUBMIT STAR RATING UPON CLICK
$('input[name=star-radios]').on('change', function() {
    $(this).closest("form").submit();
});


// SUBMIT RATING FILTER UPON CLICK ON STAR PORTION
$('input[name=filter-rating]').on('change', function() {
    $(this).closest("form").submit();
});


// SUBMIT ADD TO ALBUM WITH DELAY

$('input[name=add-to-album]').on('change', function() {
    $(this).closest("form").delay(300).submit();
});


// HIDE ALL HIDDEN DIVS
$(".hidden").hide();

// OPEN RENAME ALBUM TEXTBOX
$("#album-title").click(function() {
    $("#rename-album-div").toggle();
});
   

$("#filter-button").click(function() {
    $("#rating-filter-div").toggle();
});