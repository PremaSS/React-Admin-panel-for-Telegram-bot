import React, { useState, useEffect } from 'react';
import styles from './styles/CategoryEditor.module.css';

function CategoryEditor({ category, onSave, onCancel }) {
  const [name, setName] = useState('');

  useEffect(() => {
    if (category) {
      setName(category.name);
    }
  }, [category]);

  const handleSubmit = (event) => {
    event.preventDefault();
    onSave({ ...category, name });
  };

  const handleCancel = () => {
    onCancel();
  };

  if (!category) {
    return <p>Выберите категорию для редактирования.</p>;
  }

  return (
    <div className={styles.editorContainer}>
      <h2 className={styles.editorHeader}>Edit Category</h2>
      <form onSubmit={handleSubmit}>
        <label className={styles.formLabel}>
          Name:
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className={styles.formInput}
          />
        </label>
        <button type="submit" className={styles.saveButton}>
          Save
        </button>
        <button type="button" className={styles.cancelButton} onClick={handleCancel}>
          Cancel
        </button>
      </form>
    </div>
  );
}

export default CategoryEditor;
