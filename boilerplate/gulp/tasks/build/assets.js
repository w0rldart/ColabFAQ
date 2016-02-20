var
    gulp    = require('gulp-help')(require('gulp')),
    console = require('better-console')
;

// export task
module.exports = function(callback) {
    console.info('Copying semantic dist themes directory to our dist');

    gulp
        .src('./vendor/semantic/dist/themes/**')
        .pipe(gulp.dest('../static/themes/'))
    ;
}
