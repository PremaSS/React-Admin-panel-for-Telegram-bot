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
    // В будущем заменить на реальный fetch запрос
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

    // Сбрасываем выбранную категорию, чтобы скрыть редактор
    setSelectedCategory(null);

    // TODO: Отправить обновленные данные на сервер (PUT/PATCH запрос)
    console.log('Updated category:', updatedCategory); // Для отладки
  };

  const handleCancelEdit = () => {
    setSelectedCategory(null); // Скрываем редактор
  };

  const handleAddSubcategory = (parentCategory) => {
    // Функция генерирования уникального ID
    const generateId = () => Date.now();

    // Функция генерирования имени новой подкатегории
    const generateSubcategoryName = (parent, subcategories) => {
      const nextNumber = subcategories.length + 1;
      if (parent === null) {
        return `Category ${nextNumber}`; // Обработчик top-level категории
      }
      return `${parent.name}.${nextNumber}`;
    };

    const newSubcategory = {
      id: generateId(),
      name: generateSubcategoryName(
        parentCategory,
        parentCategory ? parentCategory.subcategories : [],
      ),
      subcategories: [],
    };

    // Функция для рекурсивного обновления состояния категорий
    const updateCategories = (cats, parentId) => {
      return cats.map((cat) => {
        if (cat.id === parentId) {
          return { ...cat, subcategories: [...cat.subcategories, newSubcategory] };
        } else if (cat.subcategories && cat.subcategories.length > 0) {
          return { ...cat, subcategories: updateCategories(cat.subcategories, parentId) };
        } else {
          return cat;
        }
      });
    };

    // Если родительская категория равна null, добавляем top-level category
    if (parentCategory === null) {
      setCategories([...categories, newSubcategory]);
    } else {
      // В противном случае обновляем подкатегорию родительской категории
      setCategories(updateCategories(categories, parentCategory.id));
    }
  };

  return (
    <div className={styles.app}>
      <h1 className={styles.adminPanelHeader}>Admin Panel</h1>
      <button className={styles.addCategoryButton} onClick={() => handleAddSubcategory(null)}>
        Add Category
      </button>
      <CategoryList
        categories={categories}
        onCategoryClick={handleCategoryClick}
        onAddSubcategory={handleAddSubcategory}
        level={0}
      />
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
