const fs = require('fs');
const path = require('path');

const docsDir = path.join(__dirname, '../docs');

function getTagFromPath(filePath) {
  const relativePath = path.relative(docsDir, filePath);
  const parts = relativePath.split(path.sep);

  // 첫 번째 폴더명을 태그로 사용
  if (parts.length > 1) {
    return parts[0].toLowerCase().replace(/-/g, '-');
  }
  return 'general';
}

function getDescription(lines, startLine) {
  // 첫 번째 의미있는 텍스트 줄을 description으로 사용
  for (let i = startLine; i < Math.min(startLine + 10, lines.length); i++) {
    const line = lines[i].trim();
    // 코드 블록, 헤더, 빈 줄 제외
    if (line && !line.startsWith('#') && !line.startsWith('```') && !line.startsWith('-') && !line.startsWith('>')) {
      // 100자로 제한
      return line.substring(0, 100).replace(/"/g, '\\"');
    }
  }
  return '';
}

function addFrontmatter(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split('\n');

  // 기존 frontmatter 파싱
  let existingFrontmatter = {};
  let contentStartLine = 0;

  if (content.startsWith('---')) {
    const endIndex = content.indexOf('---', 3);
    if (endIndex !== -1) {
      const fmContent = content.substring(3, endIndex).trim();
      fmContent.split('\n').forEach(line => {
        const match = line.match(/^(\w+):\s*(.+)$/);
        if (match) {
          existingFrontmatter[match[1]] = match[2].replace(/^["']|["']$/g, '');
        }
      });
      // frontmatter 이후 시작 줄 찾기
      const fmLines = content.substring(0, endIndex + 3).split('\n').length;
      contentStartLine = fmLines;
    }
  }

  const tag = getTagFromPath(filePath);
  const title = existingFrontmatter.title || path.basename(filePath, '.md');
  const date = existingFrontmatter.date || '';
  const description = getDescription(lines, contentStartLine) || title;

  // 새 frontmatter 생성
  let frontmatter = '---\n';
  frontmatter += `title: "${title}"\n`;
  if (date) {
    frontmatter += `date: ${date}\n`;
  }
  frontmatter += `tags: [${tag}]\n`;
  frontmatter += `authors: jsc\n`;
  frontmatter += `description: "${description}"\n`;
  frontmatter += '---\n';

  // 기존 내용에서 frontmatter 제거 후 새로 조합
  let newContent;
  if (content.startsWith('---')) {
    const endIndex = content.indexOf('---', 3);
    newContent = frontmatter + content.substring(endIndex + 4);
  } else {
    newContent = frontmatter + '\n' + content;
  }

  fs.writeFileSync(filePath, newContent);
  console.log(`Updated: ${filePath}`);
}

function processDirectory(dir) {
  const items = fs.readdirSync(dir);

  for (const item of items) {
    const fullPath = path.join(dir, item);
    const stat = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      processDirectory(fullPath);
    } else if (item.endsWith('.md') && item !== 'intro.md') {
      addFrontmatter(fullPath);
    }
  }
}

processDirectory(docsDir);
console.log('Done!');
