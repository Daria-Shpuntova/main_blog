var input_name=document.querySelector('.name_text');
input_name.onblur = () => {
    let username = input_name.value;
    if (username.length == 0){
        document.querySelector('.error_name').innerHTML ='Name cannot blank';
    } else if (username.length < 3 || 25 < username.length){
        document.querySelector('.error_name').innerHTML='Name must be between 3 and 25';
    } else {
         document.querySelector('.error_name').innerHTML=" ";
    }
}

$(document).ready(function(){
$( ".email_text" ).focusout(function() {
    var inputvalue = $(this).val();
    var regemail = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if((!regemail.test(inputvalue)) && (inputvalue!='')){
        document.querySelector('.error_email').innerHTML="Email is not valid. It should be in the format 'email@domain.com'";
    }else if(inputvalue == ''){
        document.querySelector('.error_email').innerHTML="Email cannot blank";
    }else{
        document.querySelector('.error_email').innerHTML=" ";
}
});
});

var mestext=document.querySelector('.massage-bt')
mestext.onblur = () => {
    let usermes = mestext.value;
    if (usermes.length == 0){
        document.querySelector('.error_mes').innerHTML ='Massage cannot blank';
    } else if (usermes.length < 10 || 250 < usermes.length){
        document.querySelector('.error_mes').innerHTML='Name must be between 10 and 250';
    } else {
         document.querySelector('.error_mes').innerHTML=" ";
    }
};




