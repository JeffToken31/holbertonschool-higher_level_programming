document.addEventListener('DOMContentLoaded', () => {
  async function fetchData () {
    const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
    const data = await response.json();
    const totraduct = document.getElementById('hello');
    totraduct.textContent = data.hello;
  }
  fetchData();
});
