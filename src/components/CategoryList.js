import React from 'react';
import CategoryItem from './CategoryItem';
import styles from './styles/CategoryList.module.css';

function CategoryList({ categories, onCategoryClick, onAddSubcategory, level = 0 }) {
  return (
    <ul className={styles.categoryList}>
      {categories.map((category) => (
        <CategoryItem
          key={category.id}
          category={category}
          onCategoryClick={onCategoryClick}
          onAddSubcategory={onAddSubcategory}
          level={level}
        />
      ))}
    </ul>
  );
}

export default CategoryList;
