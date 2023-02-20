const fs = require('fs');

fs.readFile('stars.json', 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  try {
    const jsonData = JSON.parse(data);
    console.log(jsonData);
  } catch (err) {
    console.error('Error parsing JSON', err);
  }
});






