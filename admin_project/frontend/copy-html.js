// frontend/copy-html.js
const fs = require('fs-extra');
const path = require('path');

const sourceHtml = path.resolve(__dirname, 'build/index.html');

const destinationHtml = path.resolve(__dirname, '../admin_panel/templates/admin_panel/catalog.html');


const destDir = path.dirname(destinationHtml);
fs.ensureDirSync(destDir);

fs.copy(sourceHtml, destinationHtml, { overwrite: true })
  .then(() => console.log(`Successfully copied ${sourceHtml} to ${destinationHtml}`))
  .catch(err => console.error('Error copying HTML:', err));