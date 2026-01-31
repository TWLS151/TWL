import React, { useMemo, useState } from 'react';
import Link from '@docusaurus/Link';
import activityData from '@site/src/data/activity.json';
import styles from './styles.module.css';

interface DocInfo {
  title: string;
  path: string;
}

type ActivityData = {
  [date: string]: DocInfo[];
};

const MONTHS = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'];
const DAYS = ['일', '월', '화', '수', '목', '금', '토'];

export default function ActivityCalendar(): JSX.Element {
  const data = activityData as ActivityData;
  const [selectedDate, setSelectedDate] = useState<string | null>(null);
  const [tooltip, setTooltip] = useState<{ date: string; count: number; x: number; y: number } | null>(null);

  // 최근 12주 (84일) 기준 날짜 배열 생성
  const { weeks, monthLabels } = useMemo(() => {
    const today = new Date();
    const weeks: Date[][] = [];
    const monthLabels: { month: string; col: number }[] = [];

    // 12주 전 일요일부터 시작
    const startDate = new Date(today);
    startDate.setDate(startDate.getDate() - 83);
    // 가장 가까운 일요일로 이동
    startDate.setDate(startDate.getDate() - startDate.getDay());

    let currentWeek: Date[] = [];
    let lastMonth = -1;

    for (let i = 0; i < 91; i++) {
      const date = new Date(startDate);
      date.setDate(startDate.getDate() + i);

      if (date > today) break;

      if (date.getDay() === 0 && currentWeek.length > 0) {
        weeks.push(currentWeek);
        currentWeek = [];
      }

      // 월 라벨 추가
      if (date.getMonth() !== lastMonth) {
        monthLabels.push({ month: MONTHS[date.getMonth()], col: weeks.length });
        lastMonth = date.getMonth();
      }

      currentWeek.push(date);
    }

    if (currentWeek.length > 0) {
      weeks.push(currentWeek);
    }

    return { weeks, monthLabels };
  }, []);

  const formatDate = (date: Date): string => {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
  };

  const getActivityLevel = (date: Date): number => {
    const dateStr = formatDate(date);
    const count = data[dateStr]?.length || 0;
    if (count === 0) return 0;
    if (count === 1) return 1;
    if (count <= 3) return 2;
    if (count <= 5) return 3;
    return 4;
  };

  const handleCellClick = (date: Date) => {
    const dateStr = formatDate(date);
    if (data[dateStr]) {
      setSelectedDate(selectedDate === dateStr ? null : dateStr);
    }
  };

  const handleMouseEnter = (e: React.MouseEvent, date: Date) => {
    const dateStr = formatDate(date);
    const count = data[dateStr]?.length || 0;
    const rect = (e.target as HTMLElement).getBoundingClientRect();
    setTooltip({ date: dateStr, count, x: rect.left, y: rect.top - 30 });
  };

  const handleMouseLeave = () => {
    setTooltip(null);
  };

  const totalContributions = Object.values(data).reduce((sum, docs) => sum + docs.length, 0);

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <span className={styles.title}>학습 기록</span>
        <span className={styles.count}>{totalContributions}개 문서 작성</span>
      </div>

      <div className={styles.calendar}>
        {/* 요일 라벨 */}
        <div className={styles.dayLabels}>
          {DAYS.map((day, i) => (
            <span key={day} className={styles.dayLabel} style={{ gridRow: i + 1 }}>
              {i % 2 === 1 ? day : ''}
            </span>
          ))}
        </div>

        {/* 캘린더 그리드 */}
        <div className={styles.grid}>
          {/* 월 라벨 */}
          <div className={styles.monthLabels}>
            {monthLabels.map(({ month, col }, i) => (
              <span
                key={i}
                className={styles.monthLabel}
                style={{ gridColumn: col + 1 }}
              >
                {month}
              </span>
            ))}
          </div>

          {/* 잔디 셀 */}
          <div className={styles.cells}>
            {weeks.map((week, weekIdx) => (
              <div key={weekIdx} className={styles.week}>
                {week.map((date) => {
                  const level = getActivityLevel(date);
                  const dateStr = formatDate(date);
                  const hasActivity = level > 0;

                  return (
                    <div
                      key={dateStr}
                      className={`${styles.cell} ${styles[`level${level}`]} ${hasActivity ? styles.clickable : ''} ${selectedDate === dateStr ? styles.selected : ''}`}
                      onClick={() => handleCellClick(date)}
                      onMouseEnter={(e) => handleMouseEnter(e, date)}
                      onMouseLeave={handleMouseLeave}
                    />
                  );
                })}
              </div>
            ))}
          </div>
        </div>

        {/* 범례 */}
        <div className={styles.legend}>
          <span>Less</span>
          <div className={`${styles.cell} ${styles.level0}`} />
          <div className={`${styles.cell} ${styles.level1}`} />
          <div className={`${styles.cell} ${styles.level2}`} />
          <div className={`${styles.cell} ${styles.level3}`} />
          <div className={`${styles.cell} ${styles.level4}`} />
          <span>More</span>
        </div>
      </div>

      {/* 툴팁 */}
      {tooltip && (
        <div
          className={styles.tooltip}
          style={{ left: tooltip.x, top: tooltip.y }}
        >
          {tooltip.count > 0
            ? `${tooltip.date}: ${tooltip.count}개 문서`
            : `${tooltip.date}: 기록 없음`}
        </div>
      )}

      {/* 선택된 날짜의 문서 목록 */}
      {selectedDate && data[selectedDate] && (
        <div className={styles.docList}>
          <h4>{selectedDate} 작성 문서</h4>
          <ul>
            {data[selectedDate].map((doc, i) => (
              <li key={i}>
                <Link to={doc.path}>{doc.title}</Link>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
