// admin_project/frontend/craco.config.js
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  webpack: {
    configure: (webpackConfig, { env, paths }) => {
      webpackConfig.output.publicPath = '/static/';
      paths.publicUrlOrPath = '/static/';

      webpackConfig.output.filename = 'js/[name].[contenthash:8].js';
      webpackConfig.output.chunkFilename = 'js/[name].[contenthash:8].chunk.js';

      const miniCssExtractPlugin = webpackConfig.plugins.find(
        (plugin) => plugin.constructor.name === 'MiniCssExtractPlugin',
      );
      if (miniCssExtractPlugin) {
        miniCssExtractPlugin.options.filename = 'css/[name].[contenthash:8].css';
        miniCssExtractPlugin.options.chunkFilename = 'css/[name].[contenthash:8].chunk.css';
      }

      const oneOfRule = webpackConfig.module.rules.find((rule) => rule.oneOf);
      if (oneOfRule) {
        oneOfRule.oneOf.forEach((loaderRule) => {
          if (
            loaderRule.type === 'asset/resource' &&
            typeof loaderRule.generator?.filename === 'string' &&
            loaderRule.generator.filename.includes('static/media/')
          ) {
            loaderRule.generator.filename = loaderRule.generator.filename.replace(
              'static/media/',
              'img/',
            );
          } else if (
            loaderRule.options?.name &&
            typeof loaderRule.options.name === 'string' &&
            loaderRule.options.name.startsWith('static/media/')
          ) {
            loaderRule.options.name = loaderRule.options.name.replace('static/media/', 'img/');
          }
        });
      }

      let htmlPluginAlteredCount = 0;
      if (webpackConfig.plugins) {
        webpackConfig.plugins.forEach((plugin) => {
          if (plugin.constructor.name === 'HtmlWebpackPlugin') {
            // Пытаемся получить доступ к опциям.
            let pluginOptions = plugin.userOptions || plugin.options;

            // Если опции не существуют, создаем их, чтобы можно было установить inject
            if (!pluginOptions) {
              pluginOptions = {};
              // Пытаемся присвоить обратно, если это возможно и имеет смысл
              if (plugin.userOptions === undefined && plugin.options === undefined) {
                plugin.options = pluginOptions; // Устанавливаем для plugin.options, если оба не определены
              } else if (plugin.userOptions !== undefined) {
                plugin.userOptions = pluginOptions;
              } else {
                // plugin.options !== undefined
                plugin.options = pluginOptions;
              }
            }

            pluginOptions.inject = false;
            const filename = pluginOptions.filename || 'unknown (could be default index.html)';
            console.log(
              `craco.config.js: Set inject:false for HtmlWebpackPlugin (filename: ${filename})`,
            );
            htmlPluginAlteredCount++;
          }
        });
      }

      if (htmlPluginAlteredCount === 0) {
        console.warn('craco.config.js: No HtmlWebpackPlugin instances found to modify.');
      } else {
        console.log(
          `craco.config.js: Modified ${htmlPluginAlteredCount} instance(s) of HtmlWebpackPlugin.`,
        );
      }

      return webpackConfig;
    },
    plugins: {
      add: [
        new BundleTracker({
          path: __dirname,
          filename: 'webpack-stats.json',
          publicPath: '/static/',
          logTime: true,
        }),
      ],
    },
  },
};
