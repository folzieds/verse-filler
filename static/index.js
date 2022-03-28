const form = document.getElementById('my_form');


form.onsubmit = async (event) => { 
  event.preventDefault();

  let response = await fetch('/fill',{
    method:'POST',
    body: new FormData(form)
  });

  let result = await response.data;


  form.reset();
};
// form.addEventListener('submit', function handleSubmit(event) {
//   event.preventDefault();
//   let response = fetch('/fill',{
//     method:'POST',
//     body: new FormData(form)
//   });
//   form.reset();
// });