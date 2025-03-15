import React from 'react';
import styles from './styles/CategoryEditor.module.css';

function CategoryEditor({ category }) {
  if (!category) {
    return <p>Выберите категорию для редактирования.</p>;
  }

  return (
    <div className={styles.editorContainer}>
      <h2 className={styles.editorHeader}>Edit Category</h2>
      <p>Выбрана категория: {category.name}</p>
    </div>
  );
}

export default CategoryEditor;
