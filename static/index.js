
document.getElementById('search').addEventListener('click', function () {
  fetch('/getData', { method: 'POST', body: JSON.stringify({ name: document.getElementById('name').value, state: document.getElementById('state').value }) })
    .then(res => res.json())
    .then(res => {
      document.getElementById("display").innerText = res.name + '\n' + res.age + '\n' + res.address + '\n' + res.phone;
    });
});