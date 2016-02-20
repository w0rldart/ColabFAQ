/*******************************
            Set-up
*******************************/

var
    gulp         = require('gulp-help')(require('gulp')),

    // config parameters
    config       = require('./gulp/config'),

    // watch for file changes and build
    watch        = require('./gulp/tasks/watch'),

    // build all files
    build        = require('./gulp/tasks/build'),
    buildAssets  = require('./gulp/tasks/build/assets'),
    buildCSS     = require('./gulp/tasks/build/css'),
    buildJS      = require('./gulp/tasks/build/javascript'),

    // utility tasks
    clean        = require('./gulp/tasks/clean')

    // Semantic-UI tasks
    // watchSemantic = require('./vendor/semantic/tasks/watch'),
    // buildSemantic = require('./vendor/semantic/tasks/build')
;

/*******************************
             Tasks
*******************************/

gulp.task('default', false, watch);

gulp.task('watch', 'Watch for front-end changes', watch);
gulp.task('build', 'Builds all files from source', build);
gulp.task('clean', 'Clean dist folder, a.k.a static/', clean);
