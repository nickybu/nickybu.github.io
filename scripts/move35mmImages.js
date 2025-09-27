const fs = require('fs');
const path = require('path');

const imagesDir = path.join(__dirname, '../content/garden/35mm/images');
const files = fs.readdirSync(imagesDir).filter(f => f.match(/\.jpe?g$/i));
let startIndex = 14;

function formatDate(dt) {
  const pad = n => String(n).padStart(2, '0');
  return (
    dt.getFullYear() +
    pad(dt.getMonth() + 1) +
    pad(dt.getDate()) +
    pad(dt.getHours()) +
    pad(dt.getMinutes()) +
    pad(dt.getSeconds())
  );
}

files.forEach((file, i) => {
  const folderName = `image${String(startIndex + i).padStart(3, '0')}`;
  const folderPath = path.join(imagesDir, folderName);

  if (!fs.existsSync(folderPath)) {
    fs.mkdirSync(folderPath);
  }

  // Get file datetime
  const filePath = path.join(imagesDir, file);
  const stats = fs.statSync(filePath);
  const datetime = formatDate(stats.mtime);

  // Rename image file with image-YYYYMMDDHHMMSS.jpg
  const ext = path.extname(file).toLowerCase();
  const newImageName = `image-${datetime}${ext}`;
  fs.renameSync(
    filePath,
    path.join(folderPath, newImageName)
  );

  // Create index.md
  const mdContent = `---
title: "Example caption"
---
`;
  fs.writeFileSync(path.join(folderPath, 'index.md'), mdContent);
});

console.log('Done!');