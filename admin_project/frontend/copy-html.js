// admin_project/frontend/copy-html.js
const fs = require('fs-extra');
const path = require('path');

const sourceHtmlPath = path.resolve(__dirname, 'build/index.html');

const destinationHtmlPath = path.resolve(
  __dirname,
  '../admin_panel/templates/admin_panel/catalog.html',
);

console.log(`Source HTML for copy: ${sourceHtmlPath}`);
console.log(`Destination HTML for copy: ${destinationHtmlPath}`);

try {
  if (!fs.existsSync(sourceHtmlPath)) {
    console.error(`Source file not found: ${sourceHtmlPath}`);
    console.error(
      'Please ensure "npm run build" (or "craco build") has run successfully before this script.',
    );
    process.exit(1);
  }

  let htmlContent = fs.readFileSync(sourceHtmlPath, 'utf8');
  console.log('Original HTML content (first 300 chars):', htmlContent.substring(0, 300));

  const mainJsScriptRegex =
    /<script\s+(defer="defer"\s+)?src="\/static\/js\/main\.[a-f0-9]+\.js"><\/script>/g;
  const cleanedJsContent = htmlContent.replace(mainJsScriptRegex, (match) => {
    console.log(`Removing auto-injected JS: ${match}`);
    return '';
  });

  const mainCssLinkRegex =
    /<link\s+href="\/static\/css\/main\.[a-f0-9]+\.css"\s+rel="stylesheet">/g;
  const cleanedContent = cleanedJsContent.replace(mainCssLinkRegex, (match) => {
    console.log(`Removing auto-injected CSS: ${match}`);
    return '';
  });

  if (htmlContent.length !== cleanedContent.length) {
    console.log('HTML content has been modified (cleaned).');
    console.log('Cleaned HTML content (first 300 chars):', cleanedContent.substring(0, 300));
  } else {
    console.log('No auto-injected main JS/CSS tags found to remove, or regex did not match.');
  }

  htmlContent = cleanedContent;

  const destDir = path.dirname(destinationHtmlPath);
  fs.ensureDirSync(destDir);
  console.log(`Ensured destination directory exists: ${destDir}`);

  fs.writeFileSync(destinationHtmlPath, htmlContent, 'utf8');

  console.log(`Successfully processed and copied HTML to ${destinationHtmlPath}`);
} catch (err) {
  console.error('Error during HTML copy and processing:', err);
  process.exit(1);
}
