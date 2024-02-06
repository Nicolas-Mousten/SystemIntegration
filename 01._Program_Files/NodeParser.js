const csv = require('csv-parser');
const fs = require('fs');
const xml2js = require('xml2js');
const yaml = require('js-yaml');
csv_data  = [];
fs.createReadStream('../01._Data_Files/me.csv')
  .pipe(csv())
  .on('data', (row) => {
    csv_data.push(row)
  })
  .on('end', () => {
    console.log('Data from me.csv: \n', csv_data);
  });

const jsonData = fs.readFileSync('../01._Data_Files/me.json', 'utf8');
const jsonDataParsed = JSON.parse(jsonData);
console.log('Data from me.json:');
console.log(jsonDataParsed);

const xmlData = fs.readFileSync('../01._Data_Files/me.xml', 'utf8');
xml2js.parseString(xmlData, (err, result) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('Data from me.xml:');
  console.log(result.me);
});

const yamlData = fs.readFileSync('../01._Data_Files/me.yaml', 'utf8');
const yamlDataParsed = yaml.load(yamlData);
console.log('Data from me.yaml:');
console.log(yamlDataParsed);
