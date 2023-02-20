const para = document.querySelectorAll('div#red_header');

para.addEventListener('click', colorize);

function colorize(){
document.getElementsByTagName("header")[0].style.color = "#FF0000";
}