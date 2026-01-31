import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './index.module.css';

// 카테고리 데이터
const categories = [
  { name: 'Python', icon: '🐍', path: '/docs/python/', count: 5 },
  { name: 'Git', icon: '📦', path: '/docs/git/', count: 3 },
  { name: 'Algorithm', icon: '🧮', path: '/docs/algorithm-study/', count: 4 },
  { name: 'Error Log', icon: '🐛', path: '/docs/error-log/', count: 2 },
  { name: 'Inbox', icon: '📥', path: '/docs/Inbox/', count: 1 },
];

// 태그 데이터
const tags = [
  { name: 'python', count: 5 },
  { name: 'git', count: 3 },
  { name: 'algorithm', count: 4 },
  { name: 'error', count: 2 },
  { name: 'tips', count: 3 },
];

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={styles.heroBanner}>
      <div className={styles.container}>
        <h1 className={styles.title}>
          오늘 배운 건<br />오늘 적자
        </h1>
        <p className={styles.subtitle}>{siteConfig.title}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            문서 보기 →
          </Link>
          <Link
            className="button button--outline button--lg"
            to="/blog">
            블로그 →
          </Link>
        </div>
      </div>
    </header>
  );
}

function StatsSection() {
  const totalDocs = categories.reduce((sum, cat) => sum + cat.count, 0);
  return (
    <section className={styles.stats}>
      <div className={styles.statItem}>
        <span className={styles.statNumber}>{totalDocs}</span>
        <span className={styles.statLabel}>문서</span>
      </div>
      <div className={styles.statItem}>
        <span className={styles.statNumber}>{categories.length}</span>
        <span className={styles.statLabel}>카테고리</span>
      </div>
      <div className={styles.statItem}>
        <span className={styles.statNumber}>{tags.length}</span>
        <span className={styles.statLabel}>태그</span>
      </div>
    </section>
  );
}

function CategoriesSection() {
  return (
    <section className={styles.categoriesSection}>
      <h2 className={styles.sectionTitle}>카테고리</h2>
      <div className={styles.categories}>
        {categories.map((cat) => (
          <Link key={cat.name} to={cat.path} className={styles.categoryCard}>
            <span className={styles.categoryIcon}>{cat.icon}</span>
            <span className={styles.categoryName}>{cat.name}</span>
            <span className={styles.categoryCount}>{cat.count}</span>
          </Link>
        ))}
      </div>
    </section>
  );
}

function TagCloud() {
  return (
    <section className={styles.tagSection}>
      <h2 className={styles.sectionTitle}>태그</h2>
      <div className={styles.tagCloud}>
        {tags.map((tag) => (
          <Link
            key={tag.name}
            to={`/docs/tags/${tag.name}`}
            className={styles.tag}
            style={{ fontSize: `${0.8 + tag.count * 0.1}rem` }}
          >
            #{tag.name}
          </Link>
        ))}
      </div>
    </section>
  );
}

function QuickStart() {
  return (
    <section className={styles.quickStart}>
      <h2 className={styles.sectionTitle}>빠른 시작</h2>
      <div className={styles.features}>
        <div className={styles.featureItem}>
          <h3>📝 기록하기</h3>
          <p>매일 배운 것을 짧게 기록합니다</p>
        </div>
        <div className={styles.featureItem}>
          <h3>🔍 찾아보기</h3>
          <p>필요할 때 빠르게 검색합니다</p>
        </div>
        <div className={styles.featureItem}>
          <h3>📈 성장하기</h3>
          <p>꾸준한 기록이 실력이 됩니다</p>
        </div>
      </div>
    </section>
  );
}

export default function Home(): React.JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Home`}
      description={siteConfig.tagline}>
      <HomepageHeader />
      <main className={styles.main}>
        <StatsSection />
        <CategoriesSection />
        <TagCloud />
        <QuickStart />
      </main>
    </Layout>
  );
}
