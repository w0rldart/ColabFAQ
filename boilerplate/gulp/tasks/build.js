/*******************************
            Build Task
*******************************/

var
    // dependencies
    gulp         = require('gulp-help')(require('gulp')),
    runSequence  = require('run-sequence'),

    // build sub-tasks
    buildAssets  = require('./build/assets'),
    buildCSS     = require('./build/css'),
    buildJS      = require('./build/javascript'),

    // task sequence
    tasks        = []
;

// gulp.task('build', 'Build all assets from source', ['clean', 'build-css', 'build-js', 'build-jsx', 'copy-semantic-themes']);
// gulp.task('build', 'Build all assets from source', ['clean', 'copy-semantic-themes', 'build-css', 'build-js']);

// in case these tasks are undefined during import, less make sure these are available in scope
gulp.task('build-assets', 'Copies all assets from source', buildAssets);
gulp.task('build-css', 'Builds all css from source', buildCSS);
gulp.task('build-javascript', 'Builds all javascript from source', buildJS);

// export task
module.exports = function(callback) {
    console.info('Building FaqColab\'s assets');

    tasks.push('build-assets');
    tasks.push('build-css');
    tasks.push('build-javascript');

    runSequence(tasks, callback);
};
