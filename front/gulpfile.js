'use strict';

// var path = require('path');

// require('fs')
//   .readdirSync('./gulp/tasks/')
//   .forEach(function(task) {
//     if (path.extname(task) !== '.js') return;
//     require('./gulp/tasks/' + task);
//   });

var gulp = require('gulp'),
  connect = require('gulp-connect'),
  watch = require('gulp-watch'),
  webpack = require('webpack-stream'),
  sass = require('gulp-sass');
 
gulp.task('webserver', function() {
  connect.server({
    livereload: true,
    root: ['.', 'static/']
  });
});
 
gulp.task('livereload', function() {
  gulp.src(['static/styles/*.scss', 'static/scripts/*.js'])
    .pipe(watch())
    .pipe(connect.reload());
});
 
gulp.task('sass', function() {
  gulp.src('app/styles/main.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('static/build/'));
});

gulp.task('scripts', function() {
  gulp.src('app/scripts/main.js')
    .pipe(webpack( require('./webpack.config.js') ))
    .pipe(gulp.dest('static/build/'));
});
 

gulp.task('watch', function() {
  gulp.watch('styles/*.scss', ['sass']);
})
 
gulp.task('serve', ['sass', 'scripts', 'webserver', 'livereload', 'watch']);