import React, { useState } from 'react';
import CategoryList from './CategoryList';
import styles from './styles/CategoryItem.module.css';

function CategoryItem({
  category,
  onCategoryClick,
  onAddSubcategory,
  onDeleteCategory,
  level = 0,
  maxLevels,
}) {
  const [isExpanded, setIsExpanded] = useState(false);
  const indent = level * 20;

  const handleToggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  const handleAddSubcategoryClick = (e) => {
    e.stopPropagation(); // Предотвращаем всплытие события, чтобы не вызвать onCategoryClick
    onAddSubcategory(category);
  };

  const handleDeleteCategoryClick = (e) => {
    e.stopPropagation(); // Предотвращаем всплытие события
    onDeleteCategory(category);
  };

  const canAddSubcategory = level < maxLevels - 1;
  const showToggleButton = category.subcategories && category.subcategories.length > 0;

  return (
    <li style={{ marginLeft: `${indent}px` }}>
      <div className={styles.categoryItem}>
        {showToggleButton ? (
          <button className={styles.toggleButton} onClick={handleToggleExpand}>
            {isExpanded ? '-' : '+'}
          </button>
        ) : (
          <span className={styles.toggleButtonPlaceholder}></span>
        )}

        <span onClick={() => onCategoryClick(category)} className={styles.categoryName}>
          {category.name}
        </span>
        {canAddSubcategory && (
          <button className={styles.addButton} onClick={handleAddSubcategoryClick}>
            Add
          </button>
        )}
        <button className={styles.deleteButton} onClick={handleDeleteCategoryClick}>
          Delete
        </button>
      </div>
      {isExpanded && category.subcategories && category.subcategories.length > 0 && (
        <CategoryList
          categories={category.subcategories}
          onCategoryClick={onCategoryClick}
          onAddSubcategory={onAddSubcategory}
          onDeleteCategory={onDeleteCategory}
          level={level + 1}
          maxLevels={maxLevels}
        />
      )}
    </li>
  );
}

export default CategoryItem;
