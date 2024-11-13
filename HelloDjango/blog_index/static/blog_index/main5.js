function onEntry(entry) {
  entry.forEach(change => {
    if (change.isIntersecting) {
     change.target.classList.add('element-show');
    }
  });
}

let options = {
  threshold: [0.5] };
let observer = new IntersectionObserver(onEntry, options);
let elements = document.querySelectorAll('.jsshow ');

for (let elm of elements) {
  observer.observe(elm);
}


$(function(){
    $(".headersvg").click(function(){
        if ($(".header_menu").hasClass("show_menu")){
            $(".header_menu").removeClass("show_menu");
        } else {
            $(".header_menu").addClass("show_menu");
        }
    });
});

