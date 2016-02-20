/*******************************
         Build CSS task
*******************************/

var
    gulp         = require('gulp-help')(require('gulp')),

    // node and other dependencies
    console      = require('better-console'),
    del          = require('del'),

    // gulp dependencies
    autoprefixer = require('gulp-autoprefixer'),
    header       = require('gulp-header'),
    less         = require('gulp-less'),
    minifyCSS    = require('gulp-cssnano'),
    notify       = require('gulp-notify'),
    plumber      = require('gulp-plumber'),
    print        = require('gulp-print'),
    rename       = require('gulp-rename'),
    replace      = require('gulp-replace'),
    util         = require('gulp-util'),

    // configs
    config       = require('../../config'),
    log          = config.log
;

// export task
module.exports = function(callback) {
    console.info('Building stylesheets');

    var start = Date.now();

    gulp.src('./stylesheets/boilerplate.less')
        .pipe(plumber())
        .on('error', util.log)
        .pipe(less())
        .pipe(autoprefixer(config.prefix))
        .pipe(replace(/themes\//g, '\/static\/themes\/'))
        // .pipe(header(settings.header))
        .pipe(rename('styles.css'))
        .pipe(gulp.dest('../static/'))

        .pipe(print(log.created))
        .pipe(notify('Stylesheets compiled in ' + (Date.now() - start) + 'ms'))

        .on('end', function () {
            callback();
        })
    ;
};
