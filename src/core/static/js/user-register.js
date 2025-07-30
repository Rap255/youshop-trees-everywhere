function togglePassword() {
  const input = document.getElementById('password');
  input.type = input.type === 'password' ? 'text' : 'password';
}

document.addEventListener('DOMContentLoaded', function () {
  const accessTypeSelect = document.getElementById('type_of_access');
  const accountsBox = document.getElementById('accounts-box');
  const form = document.querySelector('form');

  // Mostrar/ocultar bloco de contas
  function toggleAccountsVisibility() {
    const value = accessTypeSelect.value;
    accountsBox.style.display = value === '2' ? 'block' : 'none';
  }

  toggleAccountsVisibility();
  accessTypeSelect.addEventListener('change', toggleAccountsVisibility);

  // Validação antes do envio do formulário
  form.addEventListener('submit', function (e) {
    const accessType = accessTypeSelect.value;

    if (accessType === '2') {
      const checkedAccounts = document.querySelectorAll('input[name="accounts"]:checked');
      if (checkedAccounts.length === 0) {
        e.preventDefault();
        alert("Uma conta para o usuário precisa ser selecionada.");
      }
    }
  });
});