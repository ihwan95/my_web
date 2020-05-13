function day_night() {
  var target = document.querySelector('body');
  if (self.value === 'Day_Mode'){
  target.style.color ='black';
  self.value = 'Night_Mode';

  $('body').css('backgroundColor', 'white');
  $('body').css('color', 'black');
  $('a').css('color', '#551A8B');

  } else  {
    self.value = 'Day_Mode';

    $('body').css('backgroundColor', 'rgb(30, 30, 30)');
    $('body').css('color', 'white');
    $('a').css('color', 'powderblue');
  }
}
