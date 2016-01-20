/*******************************
            Set-up
*******************************/

var
    gulp = require('gulp-help')(require('gulp')),

    // node and other dependencies
    console = require('better-console'),
    del = require('del'),

    // @TODO:
    //   - Implement browserify with watchifiy
    //   - Implement react.js

    // https://github.com/gulpjs/gulp/blob/master/docs/recipes/fast-browserify-builds-with-watchify.md
    // watchify      = require('watchify'),
    // browserify    = require('browserify'),
    // sourcemaps    = require('vinyl-source-stream'),
    // buffer        = require('vinyl-buffer'),
    // sourcemaps    = require('gulp-sourcemaps');

    // gulp dependencies
    autoprefixer = require('gulp-autoprefixer'),
    chmod = require('gulp-chmod'),
    concat = require('gulp-concat'),
    header = require('gulp-header'),
    less = require('gulp-less'),
    minifyCSS = require('gulp-minify-css'),
    plumber = require('gulp-plumber'),
    print = require('gulp-print'),
    rename = require('gulp-rename'),
    replace = require('gulp-replace'),
    uglify = require('gulp-uglify'),
    util = require('gulp-util'),
    watch = require('gulp-watch'),

    // config parameters
    settings = require('./tasks/config'),
    log = settings.log

    // Semantic-UI tasks
    // watchSemantic = require('./vendor/semantic/tasks/watch'),
    // buildSemantic = require('./vendor/semantic/tasks/build')
;


/*-------------------------
    Build related tasks
--------------------------*/
gulp.task('default', false, ['watch']);

gulp.task('build-css', 'Builds main css file from source', function() {
    console.info('Building styles.css from boilerplate.less');

    gulp.src('./stylesheets/boilerplate.less')
        .pipe(plumber())
        .pipe(less())
        .pipe(autoprefixer(settings.prefix))
        .pipe(replace(/themes\//g, '\/static\/themes\/'))
        .pipe(header(settings.header))
        .pipe(rename('styles.css'))
        .pipe(gulp.dest('../static/'))
        .pipe(print(log.created))
    ;
});

gulp.task('build-js', 'Builds main javavascript file from source', function() {
    // var bify = browserify({
    //     entries: './entry.js',
    //     debug: true,
    //     // defining transforms here will avoid crashing your stream
    //     transform: [reactify]
    // });

    console.info('Building scripts.js from source files');

    gulp.src([
            './bower_components/jquery/dist/jquery.js',
            './vendor/semantic/dist/semantic.js',
            './vendor/semantic/dist/semantic.js',
            './scripts/app.js'
        ])
        .pipe(plumber())
        .pipe(concat('scripts.js'))
        .pipe(header(settings.header))
        .pipe(gulp.dest('../static/'))
        .pipe(print(log.created))
    ;
});

// gulp.task('build-jsx', function () {
//     gulp.src('./project/static/scripts/jsx/main.js')
//         .pipe(browserify({transform: ['reactify']}))
//         .pipe(gulp.dest('../static/jsx'))
//     ;
// });

gulp.task('copy-semantic-themes', 'Copy Semantic UI dist files to our dist directory', function() {
    console.info('Copying semantic dist themes directory to our dist');

    gulp.src('./vendor/semantic/dist/themes/**')
        .pipe(gulp.dest('../static/themes/'))
    ;
});

// gulp.task('build', 'Build all assets from source', ['clean', 'build-css', 'build-js', 'build-jsx', 'copy-semantic-themes']);
gulp.task('build', 'Build all assets from source', ['clean', 'copy-semantic-themes', 'build-css', 'build-js']);

/*----------------------------
    Compressing dist tasks
-----------------------------*/
gulp.task('compress', 'General assests compression', ['compress-css', 'compress-js']);

gulp.task('compress-css', 'Minify styles.css', function() {
    console.info('Minifying styles.css');

    gulp.src('../static/styles.css')
        .pipe(plumber())
        .pipe(minifyCSS(settings.minify))
    ;
});

gulp.task('compress-js', 'Uglify scripts.js', function() {
    console.info('Uglifying scripts.js');

    gulp.src('../static/scripts.js')
        .pipe(plumber())
        .pipe(uglify(settings.uglify))
    ;
});


/*----------------------------
          WATCH ME
-----------------------------*/
gulp.task('watch', 'Watch for assets changes', function() {
    console.log('Watching source files for changes');

    /*--------------
        Watch CSS
    ---------------*/
    gulp.watch('./stylesheets/**/*.less', ['build-css'], function(file) {
        // log modified file
        gulp.src(file.path)
            .pipe(print(log.modified))
        ;
    });


    /*--------------
         Watch JS
    ---------------*/
    gulp.watch('./scripts/*.js', ['build-js'], function(file) {
        // log modified file
        gulp.src(file.path)
            .pipe(print(log.modified))
        ;
    });


    /*--------------
        Watch JSX
    ---------------*/
    // gulp.watch('./scripts/jsx/main.js', ['build-jsx'], function(file) {

    //     // log modified file
    //     gulp.src(file.path)
    //         .pipe(print(log.modified))
    //     ;
    // });


    /*--------------------------
        Watch Semantic Assets
    ----------------------------*/
    gulp.watch('./vendor/semantic/dist/themes/**/*.*', ['copy-semantic-themes'], function(file) {
        // log modified file
        gulp.src(file.path)
            .pipe(print(log.modified))
        ;
    });
});

gulp.task('clean', 'Clean dist folder', function() {
    var pattern = [
        '../static/**/*',
        '!../static/images/',
        '!../static/images/**'
    ];

    del(pattern, {
        force: true
    });
});
