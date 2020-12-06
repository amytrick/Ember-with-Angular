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

// SUBMIT STAR RATING UPON CLICK
$('input[name=star-radios]').on('change', function() {
    $(this).closest("form").submit();
});

// SUBMIT RATING FILTER UPON CLICK ON STAR PORTION
$('input[name=filter-rating]').on('change', function() {
    $(this).closest("form").submit();
});

$('input[name=add-to-album]').on('change', function() {
    $(this).closest("form").submit();
});

//OPEN RENAME ALBUM TEXTBOX
$(".hidden").hide();


$("#album-title").click(function() {
    $(this).next().toggle();
});
   


// DROPDOWN MENU //
$('select').each(function(){
    var $this = $(this), numberOfOptions = $(this).children('option').length;
  
    $this.addClass('select-hidden'); 
    $this.wrap('<div class="select"></div>');
    $this.after('<div class="select-styled"></div>');

    var $styledSelect = $this.next('div.select-styled');
    $styledSelect.text($this.children('option').eq(0).text());
  
    var $list = $('<ul />', {
        'class': 'select-options'
    }).insertAfter($styledSelect);
  
    for (var i = 0; i < numberOfOptions; i++) {
        $('<li />', {
            text: $this.children('option').eq(i).text(),
            rel: $this.children('option').eq(i).val()
        }).appendTo($list);
    }
  
    var $listItems = $list.children('li');
  
    $styledSelect.click(function(e) {
        e.stopPropagation();
        $('div.select-styled.active').not(this).each(function(){
            $(this).removeClass('active').next('ul.select-options').hide();
        });
        $(this).toggleClass('active').next('ul.select-options').toggle();
    });
  
    $listItems.click(function(e) {
        e.stopPropagation();
        $styledSelect.text($(this).text()).removeClass('active');
        $this.val($(this).attr('rel'));
        $list.hide();
        //console.log($this.val());
    });
  
    $(document).click(function() {
        $styledSelect.removeClass('active');
        $list.hide();
    });

});