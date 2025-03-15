import React, { useState, useEffect } from 'react';
import CategoryList from './components/CategoryList';
import CategoryEditor from './components/CategoryEditor';
import styles from './components/styles/App.module.css'; // Import styles

function App() {
  const [categories, setCategories] = useState([
    { id: 1, name: 'Category 1', subcategories: [] },
    { id: 2, name: 'Category 2', subcategories: [] },
    { id: 3, name: 'Category 3', subcategories: [] },
  ]);
  const [selectedCategory, setSelectedCategory] = useState(null);

  useEffect(() => {
    // Здесь будет загрузка данных с сервера (пока используем заглушку)
    // В будущем заменить на реальный fetch запрос
  }, []);

  const handleCategoryClick = (category) => {
    setSelectedCategory(category);
  };

  return (
    <div className={styles.app}>
      <h1 className={styles.adminPanelHeader}>Admin Panel</h1>
      <CategoryList categories={categories} onCategoryClick={handleCategoryClick} level={0} />
      {selectedCategory && <CategoryEditor category={selectedCategory} />}
    </div>
  );
}

export default App;
