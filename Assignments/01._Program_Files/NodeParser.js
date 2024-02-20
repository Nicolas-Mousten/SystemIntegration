const csv = require('csv-parser');
const fs = require('fs');
const xml2js = require('xml2js');
const yaml = require('js-yaml');


function readText(filePath, callback) {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      return callback(err, null);
    }

    const lines = data.trim().split('\n');

    const parsedData = {};

    lines.forEach(line => {
      const [key, value] = line.split(':').map(item => item.trim());

      if (key && value) {
        if (parsedData[key]) {

          if (!Array.isArray(parsedData[key])) {
            parsedData[key] = [parsedData[key]];
          }
          parsedData[key].push(value);
        } else {

          parsedData[key] = value;
        }
      }
    });
    //console.log(parsedData)

    callback(null, parsedData);
  });

}

function readCSV(filePath, callback) {
  const csvData = [];
  fs.createReadStream(filePath)
    .pipe(csv())
    .on('data', row => {
      csvData.push(row);
    })
    .on('end', () => {
      callback(null, csvData);
    })
    .on('error', err => {
      callback(err, null);
    });
}

function readJSON(filePath, callback) {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      callback(err, null);
      return;
    }
    try {
      const jsonData = JSON.parse(data);
      callback(null, jsonData);
    } catch (parseError) {
      callback(parseError, null);
    }
  });
}

function readXML(filePath, callback) {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      callback(err, null);
      return;
    }

    const parser = new xml2js.Parser({ explicitArray: false });

    parser.parseString(data, (parseError, result) => {
      //console.log(result)
      if (parseError) {
        callback(parseError, null);
        return;
      }
      callback(null, result);
    });
  });
}

function readYAML(filePath, callback) {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      callback(err, null);
      return;
    }
    try {
      const yamlData = yaml.load(data);
      callback(null, yamlData);
    } catch (parseError) {
      callback(parseError, null);
    }
  });
}
// const txtFilePath = '../01._Data_Files/me.txt';
// const csvFilePath = '../01._Data_Files/me.csv';
// const jsonFilePath = '../01._Data_Files/me.json';
// const xmlFilePath = '../01._Data_Files/me.xml';
// const yamlFilePath = '../01._Data_Files/me.yaml';

// //method calls:
// readText(txtFilePath, (err, data) => {
//   if (err) {
//     console.error('Error parsing file:', err);
//     return;
//   } else {
//     console.log('Data from me.txt:');
//     console.log(data);
//   }

// });

// readCSV(csvFilePath, (err, csvData) => {
//   if (err) {
//     console.error('Error reading CSV file:', err);
//   } else {
//     console.log('Data from me.csv:');
//     console.log(csvData);
//   }
// });

// readJSON(jsonFilePath, (err, jsonData) => {
//   if (err) {
//     console.error('Error reading JSON file:', err);
//   } else {
//     console.log('Data from me.json:');
//     console.log(jsonData);
//   }
// });

// readXML(xmlFilePath, (err, xmlData) => {
//   if (err) {
//     console.error('Error reading XML file:', err);
//   } else {
//     console.log('Data from me.xml:');
//     console.log(xmlData.me);
//   }
// });

// readYAML(yamlFilePath, (err, yamlData) => {
//   if (err) {
//     console.error('Error reading YAML file:', err);
//   } else {
//     console.log('Data from me.yaml:');
//     console.log(yamlData);
//   }
// });


module.exports = {
  readText,
  readCSV,
  readJSON,
  readXML,
  readYAML
};