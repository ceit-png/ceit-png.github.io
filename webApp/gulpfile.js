'use strict';


var csso = require('gulp-csso');
var del = require('del');
var gulp = require('gulp');
var htmlmin = require('gulp-htmlmin');
var runSequence = require('run-sequence');
var uglify = require('gulp-uglify');
var fileinclude = require('gulp-file-include')
const imagemin = require('gulp-imagemin');


// Gulp task to minify CSS files
gulp.task('styles', function () {
  return gulp.src('./src/css/*.css')
    // Minify the file
    .pipe(csso())
    // Output
    .pipe(gulp.dest('./dist/css'))
});


// Gulp task to minify JavaScript files
gulp.task('scripts', function() {
    return gulp.src('./src/js/*.js')
      // Minify the file
      .pipe(uglify())
      // Output
      .pipe(gulp.dest('./dist/js'))
  });



  // Gulp task to minify HTML files
gulp.task('pages', function() {
    return gulp.src(['./src/index.html'])
    .pipe(fileinclude({

      }))
      .pipe(htmlmin({
        collapseWhitespace: true,
        removeComments: true
      }))
      .pipe(gulp.dest('./dist'));
  });

    // Gulp task to minify HTML files
gulp.task('images', function() {
  return gulp.src('src/images/*')
  .pipe(imagemin())
  .pipe(gulp.dest('dist/images'))
});


  // Clean output directory
gulp.task('clean', () => del(['dist']));


// Gulp task to minify all files
gulp.task('default', ['clean'], function () {
    runSequence(
      'styles',
      'scripts',
      'images',
      'pages'
    );
  });
