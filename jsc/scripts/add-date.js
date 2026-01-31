const fs = require('fs');
const path = require('path');

const docsDir = path.join(__dirname, '../docs');

function addDateToFile(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');

  // 이미 date가 있으면 스킵
  if (content.match(/^date:/m)) {
    return false;
  }

  // frontmatter가 있는지 확인
  if (!content.startsWith('---')) {
    return false;
  }

  // title 다음 줄에 date 추가
  const newContent = content.replace(
    /^(---\ntitle:.*\n)/,
    `$1date: 2026-01-26\n`
  );

  if (newContent !== content) {
    fs.writeFileSync(filePath, newContent);
    return true;
  }
  return false;
}

function walkDir(dir) {
  const files = fs.readdirSync(dir);
  let count = 0;

  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      count += walkDir(filePath);
    } else if (file.endsWith('.md') && file !== 'intro.md') {
      if (addDateToFile(filePath)) {
        console.log(`Added date: ${filePath}`);
        count++;
      }
    }
  }
  return count;
}

const count = walkDir(docsDir);
console.log(`\nTotal: ${count} files updated`);
