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


$('#myModal').modal(options) 
// calling a pop up modal


// $(function(){
// 	$('#create-account-button').click(function(){
// 		var fname = $('#fname-field').val();
//         var lname = $('#lname-field').val();
//         var email = $('#email-field').val();
//         var password = $('#password-field').val();
// 		$.ajax({
// 			url: '/user',
// 			data: $('form').serialize(),
// 			type: 'POST',
// 			success: function(response){
// 				console.log(response);
// 			},
// 			error: function(error){
// 				console.log(error);
// 			}
// 		});
// 	});
// });