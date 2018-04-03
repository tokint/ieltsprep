
document.addEventListener("DOMContentLoaded", function(event) {
  scroll_interval = window.setInterval(hist_scroll_animated, 5)
});

content_div = document.getElementById('book_content');

function hist_scroll_animated () {
  scroll = document.cookie.replace(/(?:(?:^|.*;\s*)scroll\s*\=\s*([^;]*).*$)|^.*$/, "$1");
  cu_scroll = document.getElementById('book_content').scrollTop;
   if (cu_scroll < scroll){
     cu_scroll += 50;
     document.getElementById('book_content').scrollTo(0,cu_scroll);
   }else{
     document.getElementById('book_content').scrollTo(0,scroll);
     clearInterval(scroll_interval);
   };
};

window.onbeforeunload = function () {
  scroll = document.getElementById('book_content').scrollTop;
  url = window.location.pathname;
    var d = new Date();
    d.setTime(d.getTime() + (60*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = "scroll=" + scroll + "; " + expires+";"+"path="+url+";";

};

document.getElementById('invert').onclick = function() {
  button_invert = document.getElementById('invert');
  if (content_div.className == "book_content"){
    content_div.className = "book_content_invert";
    button_invert.className = "r_invert";
  }else{
    content_div.className = "book_content";
    button_invert.className = "invert";
  }
};

/*
document.getElementById('increase').onclick = function() {
  if (!content_div.style.fontSize){
    content_div.style.fontSize = "1.4em";
  }else{
    content_div.style.fontSize = parseFloat(content_div.style.fontSize)+0.1+"em";
  }
};

document.getElementById('decrease').onclick = function() {
  if (!content_div.style.fontSize){
    content_div.style.fontSize = "1.3em";
  }else{
    content_div.style.fontSize = parseFloat(content_div.style.fontSize)-0.1+"em";
  }
};
*/

var scrolling;
document.getElementById('auto_scroll_down').onclick = function() {
  if (scrolling){
    clearInterval(scroll_int);
    scrolling = 0;
    document.getElementById('auto_scroll_down').className = "auto_scroll_down";
    document.getElementById('scroll_speed').style.display = "none";
  }else{
    scroll_int = window.setInterval(auto_scroll, 2000-speed.value);
    scrolling = 1;
    document.getElementById('auto_scroll_down').className = "act_auto_scroll_down";
    document.getElementById('scroll_speed').style.display = "inline-block";
  };
};

function auto_scroll () {
  scroll = content_div.scrollTop+2;
  content_div.scrollTo(0,scroll);
};

speed = document.getElementById('speed')
speed.addEventListener("input", function() {
  clearInterval(scroll_int);
  scroll_int = window.setInterval(auto_scroll, 2000-speed.value);

});
