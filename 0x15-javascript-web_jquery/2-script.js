const para = document.querySelector("div#red_header");
//.getElementsById("red_header")[0];

para.addEventListener('click', colorize);

function colorize(){
document.getElementsByTagName("header")[0].style.color = "#FF0000";
}