/*******************************
           Watch Task
*******************************/

var
    gulp         = require('gulp-help')(require('gulp')),

    // node dependencies
    console      = require('better-console'),
    fs           = require('fs'),

    // tasks
    buildCSS     = require('./build/css'),
    buildJS      = require('./build/javascript'),

    watch        = require('gulp-watch')
;

// export task
module.exports = function(callback) {
    console.log('Watching over Gotham!');

    /*--------------
        Watch CSS
    ---------------*/
    gulp.watch('./stylesheets/**/*.less', buildCSS, function(file) {
        // log modified file
        // gulp.src(file.path)
        //     .pipe(print(log.modified))
        // ;
    });

    /*--------------
         Watch JS
    ---------------*/
    gulp.watch('./scripts/*.js', buildJS, function(file) {
        // log modified file
        // gulp.src(file.path)
        //     .pipe(print(log.modified))
        // ;
    });
};
