document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form');
  form.addEventListener('submit', function (e) {
    const name = document.getElementById('name').value.trim();
    if (name === '') {
      e.preventDefault();
      alert('Please enter an account name.');
    }
  });
});