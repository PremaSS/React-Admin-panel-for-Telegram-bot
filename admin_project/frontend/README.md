// Подключение node_modules
npm install

// Запуск Реакт
npm start

// Генерация build
npm run build


// Запуск React в Jango

1. При запросе в браузере http://localhost:8000/catalog/ через admin_project/urls.py Джанго говорит отдать шаблон catalog.html ( через (re_path(r'^catalog/(?:.*)/?$', TemplateView.as_view(template_name='admin_panel/catalog.html')'), ...) или жёстко прописанный путь )

2. Джанго берёт admin_panel/templates/admin_panel/catalog.html, и в этом файле говорит использовать {% load render_bundle from webpack_loader %} и бандлы {% render_bundle 'main' 'css' %} и {% render_bundle 'main' 'js' %}. Эти команды-теги помогают Джанго найти и вставить ссылки на наши css и js react сгенерированные в папке build. Джанго отдаёт результат этой обработки (готовый HTML с подставленными ссылками) в браузер, как catalog.html.

3. Браузер читает файл, доходит до <link rel="stylesheet" href="/static/css/main.xxxx.css"> и <script src="/static/js/main.xxxx.js"> и видит, что нужно запросить эти файлы у Джанго. Джанго отдаёт их.

4. Здесь уже запускается сам Реакт (main.xxxx.js). Это и есть наше приложение. Реакт встраивает весь свой код в <div id="root"></div>.

===========================================================================================================

При изменении файлов Реакт делаем пересборку папки build командой npm run build. Эта команда берёт файлы из папок src (обрабатывает их) и public (копирует или использует как шаблон) и формирует содержимое папки build (обновляет её файлы с новыми хеш названиями).

1. Файл craco.config.js настраивает React для работы с Джанго и указывает Webpack (сборочному инструменту React) создать карту webpack-stats.json.

2. webpack-stats.json — это карта, которая говорит, где лежат итоговые файлы. А craco.config.js также настраивает сборку так, чтобы не React-сборщик (HtmlWebpackPlugin) сам вставлял скрипты в HTML, а оставил это для Джанго. Джанго использует webpack-stats.json, чтобы понять, какие ссылки на скрипты нужно вставить (через тег render_bundle, который читает webpack-stats.json). 

3. Файл copy-html.js берёт главный html-файл (index.html) из папки build и быстро переносит его в admin_panel/templates/admin_panel/. Этот файл теперь называется catalog.html (или перезаписывает его, если он там уже был).