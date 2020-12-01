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
    console.log("clicked")
   $.get('/previous.json', function(data){
        console.log("inside function")
        console.log(data)
        $('#large-photo').attr("src",data.photo_path)
    });
});



