/*******************************
          Build JS task
*******************************/

var
    gulp         = require('gulp-help')(require('gulp')),

    // node and other dependencies
    console      = require('better-console'),
    del          = require('del'),

    // Reactify
    source       = require('vinyl-source-stream'),
    browserify   = require('browserify'),
    watchify     = require('watchify'),
    reactify     = require('reactify'),

    // Gulp dependencies
    concat       = require('gulp-concat'),
    header       = require('gulp-header'),
    notify       = require('gulp-notify'),
    plumber      = require('gulp-plumber'),
    print        = require('gulp-print'),
    rename       = require('gulp-rename'),
    uglify       = require('gulp-uglify'),
    util         = require('gulp-util'),

    // configs
    config       = require('../../config'),
    log          = config.log
;

// export task
module.exports = function(callback) {
    console.info('Building Javascript');

    var bundler = watchify(browserify({
        entries: './scripts/main.js',
        transform: [reactify],
        debug: true
    }));

    console.log('Executing bundler');

    var start = Date.now();

    bundler.bundle()
        // .pipe(plumber())
        .on('error', util.log)
        .pipe(source('./scripts/main.js'))
        // .pipe(header(config.banner))
        .pipe(rename('scripts.js'))
        .pipe(gulp.dest('../static/'))

        .pipe(print(log.created))
        .pipe(notify('Javascript files compiled in ' + (Date.now() - start) + 'ms'))

        .on('end', function () {
            callback();
        })
    ;
}
