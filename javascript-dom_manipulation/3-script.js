const header = document.querySelector('header').addEventListener('click', function () {
  if (header.class.Name === 'green') {
    header.class.Name = 'red';
  } else {
    header.class.Name = 'green';
  }
});
