import React, { useMemo } from 'react';

const ThunderField = ({ count = 14 }) => {
  const bolts = useMemo(() => {
    return Array.from({ length: count }).map((_, index) => {
      const row = index % count;
      const top = ((row + 1) / (count + 1)) * 100; // even vertical distribution
      const delay = (index % 7) * 0.5; // staggered start
      const duration = 6 + (index % 5); // speed variety
      const scale = 0.7 + (index % 4) * 0.15; // size variety
      const opacity = 0.12 + (index % 6) * 0.08; // opacity variety
      const blur = (index % 3) * 1.2; // blur variety
      return { id: index, top, delay, duration, scale, opacity, blur };
    });
  }, [count]);

  return (
    <div className="thunderfield" aria-hidden="true">
      {bolts.map((b) => (
        <svg
          key={b.id}
          className="thunderbolt-svg"
          viewBox="0 0 24 24"
          style={{
            top: `${b.top}%`,
            animationDelay: `${b.delay}s`,
            animationDuration: `${b.duration}s`,
            opacity: b.opacity,
            filter: `blur(${b.blur}px)`,
            transform: `scale(${b.scale})`,
          }}
        >
          <path d="M13 2L3 14h6l-1 8 11-14h-7z" />
        </svg>
      ))}
    </div>
  );
};

export default ThunderField;


