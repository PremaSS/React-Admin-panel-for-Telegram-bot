import React from 'react';
import styles from './styles/CategoryItem.module.css';

function CategoryItem({ category, onCategoryClick, level = 0 }) {
  const indent = level * 20;

  return (
    <li style={{ marginLeft: `${indent}px` }}>
      <div className={styles.categoryItem}>
        <span onClick={() => onCategoryClick(category)} className={styles.categoryName}>
          {category.name}
        </span>
      </div>
    </li>
  );
}

export default CategoryItem;
