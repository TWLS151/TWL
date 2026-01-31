const fs = require('fs');
const path = require('path');

const docsDir = path.join(__dirname, '../docs');
const outputPath = path.join(__dirname, '../src/data/activity.json');

function extractDate(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const match = content.match(/^date:\s*(.+)$/m);
  if (match) {
    return match[1].trim().replace(/['"]/g, '');
  }
  return null;
}

function extractTitle(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const match = content.match(/^title:\s*["']?(.+?)["']?\s*$/m);
  if (match) {
    return match[1];
  }
  return path.basename(filePath, '.md');
}

function walkDir(dir, basePath = '') {
  const files = fs.readdirSync(dir);
  const results = [];

  for (const file of files) {
    const filePath = path.join(dir, file);
    const relativePath = path.join(basePath, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      results.push(...walkDir(filePath, relativePath));
    } else if (file.endsWith('.md') && file !== 'intro.md') {
      const date = extractDate(filePath);
      const title = extractTitle(filePath);
      if (date) {
        // docs path 생성
        const docPath = '/docs/' + relativePath.replace('.md', '').replace(/\\/g, '/');
        results.push({ date, title, path: docPath });
      }
    }
  }
  return results;
}

// 데이터 수집
const activities = walkDir(docsDir);

// 날짜별로 그룹화
const dateMap = {};
activities.forEach(({ date, title, path }) => {
  if (!dateMap[date]) {
    dateMap[date] = [];
  }
  dateMap[date].push({ title, path });
});

// 출력 디렉토리 생성
const outputDir = path.dirname(outputPath);
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

// JSON 저장
fs.writeFileSync(outputPath, JSON.stringify(dateMap, null, 2));
console.log(`Generated: ${outputPath}`);
console.log(`Total dates: ${Object.keys(dateMap).length}`);
console.log(`Total docs: ${activities.length}`);
