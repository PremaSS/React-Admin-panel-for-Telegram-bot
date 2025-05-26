
const BundleTracker = require('webpack-bundle-tracker');
//const path = require('path');

console.log('craco.config.js is being loaded!');

module.exports = {
  webpack: {
    configure: (webpackConfig, { env,  paths  }) => {
      if (env === 'production') {
        webpackConfig.output.publicPath = '/static/';
        paths.publicUrlOrPath = '/static/';

        webpackConfig.output.filename = 'js/[name].[contenthash:8].js';
        webpackConfig.output.chunkFilename = 'js/[name].[contenthash:8].chunk.js';

        const miniCssExtractPlugin = webpackConfig.plugins.find(
          (plugin) => plugin.constructor.name === 'MiniCssExtractPlugin'
        );
        if (miniCssExtractPlugin) {
          miniCssExtractPlugin.options.filename = 'css/[name].[contenthash:8].css';
          miniCssExtractPlugin.options.chunkFilename = 'css/[name].[contenthash:8].chunk.css';
        } else {
          console.warn('MiniCssExtractPlugin не найден. CSS пути могут быть некорректны.');
        }

        const oneOfRule = webpackConfig.module.rules.find(rule => rule.oneOf);
        if (oneOfRule) {
          oneOfRule.oneOf.forEach(loaderRule => {
            if (loaderRule.type === 'asset/resource' && loaderRule.generator && loaderRule.generator.filename) {
              if (typeof loaderRule.generator.filename === 'string' && loaderRule.generator.filename.includes('static/media/')) {
                loaderRule.generator.filename = loaderRule.generator.filename.replace('static/media/', 'img/');
              }
            } else if (loaderRule.options && loaderRule.options.name && typeof loaderRule.options.name === 'string' && loaderRule.options.name.startsWith('static/media/')) {
              loaderRule.options.name = loaderRule.options.name.replace('static/media/', 'img/');
            }
          });
        }

        const htmlWebpackPluginInstance = webpackConfig.plugins.find(
        plugin => plugin.constructor.name === 'HtmlWebpackPlugin'
      );

      if (htmlWebpackPluginInstance) {
        htmlWebpackPluginInstance.userOptions.inject = false;
        // console.log('HtmlWebpackPlugin inject set to false.');
      } else {
        console.warn('HtmlWebpackPlugin не найден. Автоматическая вставка скриптов/стилей может не отключиться.');
      }
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
      ]
    }
  },
};