// Validarea client-side completeaza validarea obligatorie de pe server.
document.querySelectorAll('.needs-validation').forEach(form => {
  form.addEventListener('submit', event => {
    const date = form.querySelector('#applied_at');
    if (date && date.value && date.max && date.value > date.max) {
      date.setCustomValidity('Data nu poate fi in viitor.');
    } else if (date) { date.setCustomValidity(''); }
    if (!form.checkValidity()) {
      event.preventDefault(); event.stopPropagation();
    }
    form.classList.add('was-validated');
  });
});
document.querySelectorAll('.delete-form').forEach(form => {
  form.addEventListener('submit', event => {
    if (!window.confirm(form.dataset.confirm || 'Sigur doresti sa stergi aceasta candidatura?')) event.preventDefault();
  });
});

// Validare suplimentară pentru formularul de înregistrare.
const confirmPassword = document.getElementById('confirm_password');
if (confirmPassword) {
    const password = document.getElementById('password');
    const validateMatch = () => confirmPassword.setCustomValidity(
        confirmPassword.value && confirmPassword.value !== password.value ? 'Parolele nu coincid.' : ''
    );
    password.addEventListener('input', validateMatch);
    confirmPassword.addEventListener('input', validateMatch);
    confirmPassword.form.addEventListener('submit', validateMatch);
}
