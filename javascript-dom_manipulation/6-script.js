document.addEventListener('DOMContentLoaded', () => {
    function fetchData() {
        fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
            .then(response => response.json())
            .then(data => {
                const charater = document.getElementById('character');
                charater.textContent = data.name;
        })
    }
    fetchData();
})