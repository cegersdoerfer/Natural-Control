const webpack = require('webpack');
const config = {
    entry:  __dirname + '/static/js/components/index.js',
    output: {
        path: __dirname + '/static/bundles',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
  
    module: {
        rules: [
            {
            test: /\.(js|jsx)?/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-react']
                    }   
                }
        }]
    }
};
module.exports = config;