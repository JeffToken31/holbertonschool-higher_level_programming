document.addEventListener('DOMContentLoaded', () => {
  function fetchData () {
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
      .then(response => response.json())
      .then(data => {
        const listUl = document.getElementById('list_movies');
        for (const film of data.results) {
          const elementLi = document.createElement('li');
          elementLi.textContent = film.title;
          listUl.appendChild(elementLi);
        }
      });
  }
  fetchData();
});
