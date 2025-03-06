/* eslint-disable */
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const ESLintWebpackPlugin = require('eslint-webpack-plugin');

module.exports = {
    entry: './src/index.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader'
                },
            {
            test: /\.html$/,
            loader: 'html-loader'
            },
            {
            test: /\.css$/,
            use: [
                MiniCssExtractPlugin.loader, 
                'css-loader'
                ]  
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: './src/index.html',
            //if not set default index.html
            //filename: 'main.html'
        }),
        new MiniCssExtractPlugin(),
        new ESLintWebpackPlugin()
    ]
}
