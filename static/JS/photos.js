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


$('#previous').on('click', () => {
   $.get('/previous.json', function(data){
        console.log("click")
        $('#large-photo').attr("src",data.photo_path);
        $('input[name=star-radios][value=' + data.photo_rating + ']').prop('checked',true);
    });
});

$('#next').on('click', () => {
   $.get('/next.json', function(data){
        console.log("click")
        $('#large-photo').attr("src",data.photo_path)
        $('input[name=star-radios][value=' + data.photo_rating + ']').prop('checked',true);
    });
});

$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })

document.getElementById("photo-upload-button").onchange = function() {
    document.getElementById("upload-photo-form").submit();
}

$(function(){
    $('.stars label').click(function() {
          updateSettings($(this).attr('for'), $('#'+$(this).attr('for')).val());
    });
    $('.filters label').click(function() {
          updateSettings($(this).attr('for'), $('#'+$(this).attr('for')).val());
    });
});

function updateSettings(clicked,value){
    alert('clicked : ' +clicked+' ,Value:- '+value);
}
