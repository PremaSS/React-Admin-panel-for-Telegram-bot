import React from 'react';
import CategoryItem from './CategoryItem';
import styles from './styles/CategoryList.module.css';

function CategoryList({
  categories,
  onCategoryClick,
  onAddSubcategory,
  onDeleteCategory,
  level = 0,
  maxLevels,
}) {
  return (
    <ul className={styles.categoryList}>
      {categories.map((category) => (
        <CategoryItem
          key={category.id}
          category={category}
          onCategoryClick={onCategoryClick}
          onAddSubcategory={onAddSubcategory}
          onDeleteCategory={onDeleteCategory}
          level={level}
          maxLevels={maxLevels}
        />
      ))}
    </ul>
  );
}

export default CategoryList;
