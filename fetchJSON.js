fetch(results)
  // get the JSON data
  .then(response => response.json())
  // use (display) the JSON data
  .then(data => console.log(data))