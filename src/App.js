import React, { useState, useEffect } from 'react';
import CategoryList from './components/CategoryList';
import CategoryEditor from './components/CategoryEditor';
import styles from './components/styles/App.module.css';

function App() {
  const [categories, setCategories] = useState([
    { id: 1, name: 'Category 1', subcategories: [] },
    { id: 2, name: 'Category 2', subcategories: [] },
    { id: 3, name: 'Category 3', subcategories: [] },
  ]);
  const [selectedCategory, setSelectedCategory] = useState(null);

  useEffect(() => {
    // Здесь будет загрузка данных с сервера (пока используем заглушку)
    // В будущем заменю на реальный fetch запрос
  }, []);

  const handleCategoryClick = (category) => {
    setSelectedCategory(category);
  };

  const handleSaveCategory = (updatedCategory) => {
    // Обновляем категорию в списке
    const updatedCategories = categories.map((cat) =>
      cat.id === updatedCategory.id ? updatedCategory : cat,
    );
    setCategories(updatedCategories);

    // Сбрасываею выбранную категорию, чтобы скрыть редактор
    setSelectedCategory(null);

    // TODO: Отправить обновленные данные на сервер (PUT/PATCH запрос) пока не знаю, как будет
    console.log('Updated category:', updatedCategory); // Это для отладки
  };

  const handleCancelEdit = () => {
    setSelectedCategory(null); // Скрываем редактор
  };

  return (
    <div className={styles.app}>
      <h1 className={styles.adminPanelHeader}>Admin Panel</h1>
      <CategoryList categories={categories} onCategoryClick={handleCategoryClick} level={0} />
      {selectedCategory && (
        <CategoryEditor
          category={selectedCategory}
          onSave={handleSaveCategory}
          onCancel={handleCancelEdit}
        />
      )}
    </div>
  );
}

export default App;
