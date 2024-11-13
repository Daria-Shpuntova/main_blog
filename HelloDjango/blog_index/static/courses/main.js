
$(function(){
    $(".menu-svg").click(function(){
        if ($(".menu").hasClass("show_menu")){
            $(".menu").removeClass("show_menu");
        } else {
            $(".menu").addClass("show_menu");
        }
    });
});





var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("otz-text");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";

}
