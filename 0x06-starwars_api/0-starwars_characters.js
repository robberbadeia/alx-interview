#!/usr/bin/node
// Start Wars Charachters

const request = require('request');

const argCounts = process.argv.length;
if (argCounts < 3) {
  console.log('Please Enter Movie ID');
} else {
  const movieID = process.argv[2];

  const url = 'https://swapi-api.alx-tools.com/api/films/' + movieID;
  request(url, (error, response, body) => {
    const People = JSON.parse(body).characters;
    People.forEach((PeopleURL) => {
      request(PeopleURL, (err, res, bdy) => {
        const ChName = JSON.parse(bdy).name;
        console.log(ChName);
        if (err) {
          console.log(err);
        }
      });
    });
    if (error) {
      console.log(error);
    }
  });
}
