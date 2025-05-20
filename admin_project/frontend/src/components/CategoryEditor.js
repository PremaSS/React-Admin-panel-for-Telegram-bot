import React, { useState, useEffect } from 'react';
import styles from './styles/CategoryEditor.module.css';

const MAX_CAT_NAME_LENGTH = 127;

function CategoryEditor({ category, onSave, onCancel }) {
  const [name, setName] = useState('');

  useEffect(() => {
    if (category) {
      setName(category.name.slice(0, MAX_CAT_NAME_LENGTH));
    } else {
      setName('');
    }
  }, [category]);

  const handleSubmit = (event) => {
    event.preventDefault();
    const finalName = name.trim().slice(0, MAX_CAT_NAME_LENGTH);
    if (finalName) {
      onSave({ ...category, name: finalName });
    } else {
      alert('Category name cannot be empty.');
    }
  };

  const handleCancel = () => {
    onCancel();
  };

  const handleNameChange = (e) => {
    setName(e.target.value.slice(0, MAX_CAT_NAME_LENGTH));
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
            onChange={handleNameChange}
            className={styles.formInput}
            maxLength={MAX_CAT_NAME_LENGTH}
            required
            placeholder="Enter category name"
          />
        </label>
        <div className={styles.charCounter}>
          {name.length} / {MAX_CAT_NAME_LENGTH}
        </div>
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
