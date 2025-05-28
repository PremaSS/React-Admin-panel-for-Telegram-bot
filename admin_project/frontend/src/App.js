import React, { useState, useEffect } from 'react';
import CategoryList from './components/CategoryList';
import CategoryEditor from './components/CategoryEditor';
import styles from './components/styles/App.module.css';

const MAX_CATEGORY_LEVELS = 6;
const MAX_CAT_NAME_LENGTH_FOR_GEN = 127;

function App() {
  const [categories, setCategories] = useState([
    { id: 1, name: 'Category 1', subcategories: [] },
    { id: 2, name: 'Category 2', subcategories: [] },
    { id: 3, name: 'Category 3', subcategories: [] },
  ]);
  const [selectedCategory, setSelectedCategory] = useState(null);

  useEffect(() => {
    // Здесь будет загрузка данных с сервера (пока используем заглушку)
    // В будущем заменим на реальный fetch запрос
  }, []);

  const handleCategoryClick = (category) => {
    setSelectedCategory(category);
  };

  const handleSaveCategory = (updatedCategory) => {
    const updateCategoriesRecursively = (cats) => {
      return cats.map((cat) => {
        if (cat.id === updatedCategory.id) {
          return updatedCategory; // Меняю старую категорию на обновлённую
        }

        if (cat.subcategories && cat.subcategories.length > 0) {
          return { ...cat, subcategories: updateCategoriesRecursively(cat.subcategories) }; // Если у текущей категории уже есть подкатегории, рекурсивно вызываем для них
        }
        return cat;
      });
    };
    setCategories(updateCategoriesRecursively(categories)); // Обновляем сост.

    // Сбрасываем выбранную категорию, чтобы скрыть редактор
    setSelectedCategory(null);

    // TODO: Отправить обновленные данные на сервер (PUT/PATCH запрос)
    console.log('Updated category:', updatedCategory); // Для отладки
  };

  const handleCancelEdit = () => {
    setSelectedCategory(null); // Скрываем редактор, отмена редактирования
  };

  const handleAddSubcategory = (parentCategory) => {
    // Генератор ID
    const generateId = () => Date.now();

    // Функция генерирования имени для новой (под)категории
    const generateSubcategoryName = (parent, existingSubcategories) => {
      const nextNumber = existingSubcategories.length + 1;
      let baseName;
      if (parent === null) {
        let maxTopLevelNum = 0;
        categories.forEach((cat) => {
          // Проверка совпадает ли имя формату "Category[число]"
          const match = cat.name.match(/^Category (\d+)$/);
          if (match) {
            maxTopLevelNum = Math.max(maxTopLevelNum, parseInt(match[1], 10));
          }
        });
        baseName = `Category ${maxTopLevelNum + 1}`;
      } else {
        const parentNamePart = parent.name.slice(0, MAX_CAT_NAME_LENGTH_FOR_GEN - 10);
        baseName = `${parentNamePart}.${nextNumber}`;
      }
      return baseName.slice(0, MAX_CAT_NAME_LENGTH_FOR_GEN);
    };

    const newSubcategory = {
      id: generateId(),
      name: generateSubcategoryName(
        parentCategory,
        parentCategory ? parentCategory.subcategories : categories,
      ),
      subcategories: [],
    };

    // Функция рекурсивного обновления состояния категорий
    const updateCategoriesRecursively = (cats, parentId) => {
      if (parentId === null) {
        return [...cats, newSubcategory];
      }
      return cats.map((cat) => {
        // Ищем род. категорию
        if (cat.id === parentId) {
          // Нашли род. категорию
          return { ...cat, subcategories: [...cat.subcategories, newSubcategory] };
        } else if (cat.subcategories && cat.subcategories.length > 0) {
          // Если есть подкатегории, рекурсивно ищем в них
          return {
            ...cat,
            subcategories: updateCategoriesRecursively(cat.subcategories, parentId),
          };
        }
        return cat;
      });
    };

    if (parentCategory === null) {
      // если нет ParentCategory, значит добавляем на top-level
      setCategories(updateCategoriesRecursively(categories, null));
    } else {
      // иначе, добавляем как подкатегорию
      setCategories(updateCategoriesRecursively(categories, parentCategory.id));
    }
  };

  // Удаление категорий
  const handleDeleteCategory = (categoryToDelete) => {
    const updateCategoriesRecursively = (cats, categoryId) => {
      return cats
        .filter((cat) => cat.id !== categoryId) // Удаляем
        .map((cat) => {
          if (cat.subcategories && cat.subcategories.length > 0) {
            return {
              ...cat,
              subcategories: updateCategoriesRecursively(cat.subcategories, categoryId),
            };
          }
          return cat;
        });
    };

    setCategories(updateCategoriesRecursively(categories, categoryToDelete.id));

    if (selectedCategory && selectedCategory.id === categoryToDelete.id) {
      setSelectedCategory(null);
    }
  };

  return (
    <div className={styles.app}>
      <h1 className={styles.adminPanelHeader}>Admin Panel</h1>
      <button className={styles.addCategoryButton} onClick={() => handleAddSubcategory(null)}>
        Add Root Category
      </button>

      <div className={styles.categoryListContainer}>
        <CategoryList
          categories={categories} // Передаем загруженные категории
          onCategoryClick={handleCategoryClick}
          onAddSubcategory={handleAddSubcategory}
          onDeleteCategory={handleDeleteCategory}
          level={0} // Для корневых категорий
          maxLevels={MAX_CATEGORY_LEVELS}
        />
      </div>

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
