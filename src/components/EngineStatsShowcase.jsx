import React from 'react';
import styles from './EngineStatsShowcase.module.css';

export default function EngineStatsShowcase({
  eyebrow,
  title,
  accent,
  subtitle,
  items,
  footer,
}) {
  return (
    <section className={styles.showcase}>
      <div className={styles.hero}>
        <p className={styles.eyebrow}>{eyebrow}</p>
        <h1 className={styles.title}>
          {title}
          {accent ? <span className={styles.accent}>{accent}</span> : null}
        </h1>
        <p className={styles.subtitle}>{subtitle}</p>
      </div>

      <div className={styles.stats}>
        {items.map((item) => (
          <article key={item.label} className={styles.card}>
            <p className={styles.value}>{item.value}</p>
            <p className={styles.label}>{item.label}</p>
            <p className={styles.description}>{item.description}</p>
          </article>
        ))}
      </div>

      {footer ? <p className={styles.footer}>{footer}</p> : null}
    </section>
  );
}
