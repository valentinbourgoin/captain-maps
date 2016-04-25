var webpack = require('webpack');

module.exports = {
    entry: './app/scripts/main.js',
    output: {
        filename: 'app.js'
    },
    module: {
        noParse: /es6-promise\.js$/,
        loaders: [
            {
                test: /\.vue$/, 
                loader: 'vue'  
            },
            {
                test: /\.js$/,
                exclude: /node_modules|vue\/dist|vue-loader\/|vue-hot-reload-api\//,
                loader: 'babel'
            }
            
        ]
    },
    babel: {
        presets: ['es2015'],
        plugins: ['transform-runtime']
    }
}