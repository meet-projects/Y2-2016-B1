
$( document ).ready(function() {
var nameText = $("#name");

btn=$('.xoxo').attr("disabled", "disabled");
text = $('.')
btn.change(function () {
  if(nameText.val().length > 0) {
    nameText.attr("disabled", "");
  } else {
    nameText.attr("disabled", "disabled");
  }

});




}