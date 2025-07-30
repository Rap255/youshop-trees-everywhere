document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form');

  form.addEventListener('submit', function (e) {
    const longitude = document.getElementById('longitude');
    const latitude = document.getElementById('latitude');
    const age = document.getElementById('age');


    try {
      longitude.value = parseFloat(longitude.value).toFixed(6);
      latitude.value = parseFloat(latitude.value).toFixed(6);
      age.value = parseInt(age.value);


      const plant = document.querySelector('input[name="plant_id"]:checked');
      const account = document.querySelector('input[name="account_id"]:checked');

      if (plant) {
        plant.value = parseInt(plant.value);
      }

      if (account) {
        account.value = parseInt(account.value);
      }

    } catch (error) {
      e.preventDefault();
      alert("Invalid values in form. Please check your inputs.");
    }
  });
});
