import React from 'react';
import Footer from '@theme-original/DocItem/Footer';
import type FooterType from '@theme/DocItem/Footer';
import type {WrapperProps} from '@docusaurus/types';
import {useDoc} from '@docusaurus/plugin-content-docs/client';
import Link from '@docusaurus/Link';
import styles from './styles.module.css';

type Props = WrapperProps<typeof FooterType>;

// 간단한 관련 문서 표시 (같은 태그 기반)
function RelatedDocs() {
  const {metadata} = useDoc();
  const {tags} = metadata;

  if (!tags || tags.length === 0) {
    return null;
  }

  return (
    <div className={styles.relatedDocs}>
      <h3 className={styles.relatedTitle}>관련 문서</h3>
      <div className={styles.tagList}>
        {tags.map((tag) => (
          <Link
            key={tag.permalink}
            to={tag.permalink}
            className={styles.tagLink}
          >
            #{tag.label} 문서 보기
          </Link>
        ))}
      </div>
    </div>
  );
}

export default function FooterWrapper(props: Props): JSX.Element {
  return (
    <>
      <RelatedDocs />
      <Footer {...props} />
    </>
  );
}
