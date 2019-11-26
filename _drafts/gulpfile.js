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
    .pipe(gulp.dest('../css'))
    .pipe(gulp.dest('./dest/css'))
});


// Gulp task to minify JavaScript files
gulp.task('scripts', function () {
  return gulp.src('./src/js/*.js')
    // Minify the file
    .pipe(uglify())
    // Output
    .pipe(gulp.dest('../js'))
    .pipe(gulp.dest('./dest/js'))
});



// Gulp task to minify HTML files
gulp.task('pages', function () {
  return gulp.src(['./src/index.html'])
    .pipe(fileinclude({

    }))
    .pipe(htmlmin({
      collapseWhitespace: true,
      removeComments: true
    }))
    .pipe(gulp.dest('../'))
    .pipe(gulp.dest('./dest/'));
});


// Gulp task to minify HTML files
gulp.task('schedule-page', function () {
  return gulp.src(['./src/schedule.html'])
    .pipe(htmlmin({
      collapseWhitespace: true,
      removeComments: true
    }))
    .pipe(gulp.dest('../'))
    .pipe(gulp.dest('./dest/'));
});


// Gulp task to minify HTML files
gulp.task('images', function () {
  return gulp.src('src/images/*')
    .pipe(imagemin())
    .pipe(gulp.dest('../images'))
    .pipe(gulp.dest('./dest/images'))
});


// Clean output directory
// gulp.task('clean', () => del(['../js','../css','../images','index.html','schedule.html'],{force: true}));

gulp.task('clean-dest', () => del(['./dest/js', './dest/css', './dest/images', 'index.html', 'schedule.html'], { force: true }));
gulp.task('clean', () => del(['../js', '../css', 'index.html', 'schedule.html'], { force: true }));

// Gulp task to minify all files
gulp.task('default', ['clean'], function () {
  runSequence(
    'styles',
    'scripts',
    'pages',
    'schedule-page',
    'images'
  );
});
