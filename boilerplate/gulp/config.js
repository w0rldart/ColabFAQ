/*******************************
         Release Config
*******************************/

var
    package = require('../package.json')
;


/*******************************
             Export
*******************************/

module.exports = {
    log: {
        created: function(file) {
            return 'Created: ' + file;
        },
        modified: function(file) {
            return 'Modified: ' + file;
        }
    },

    title      : package.name,
    version    : package.version,
    repository : package.repository.url,
    url        : package.homepage,

    banner: ''
        + ' /*' + '\n'
        // + ' * # <%= title %> - <%= version %>' + '\n'
        // + ' * <%= repository %>' + '\n'
        // + ' * <%= url %>' + '\n'
        + ' *' + '\n'
        + ' * Copyright 2015 Contributors' + '\n'
        + ' * Released under the AGPL-3.0 license' + '\n'
        + ' * http://opensource.org/licenses/AGPL-3.0' + '\n'
        + ' *' + '\n'
        + ' */' + '\n',

    /* What Browsers to Prefix */
    prefix: {
        browsers: [
            'last 2 version',
            '> 1%',
            'opera 12.1',
            'safari 6',
            'ie 9',
            'bb 10',
            'android 4'
        ]
    },

    /* Minified CSS Concat */
    minify: {
        processImport       : false,
        restructuring       : false,
        keepSpecialComments : 1
    },

    /* Minified JS Settings */
    uglify: {
        mangle           : true,
        preserveComments : 'some'
    },

    /* Minified Concat CSS Settings */
    concatMinify: {
        processImport       : false,
        restructuring       : false,
        keepSpecialComments : false
    },

    /* Minified Concat JS */
    concatUglify: {
        mangle           : true,
        preserveComments : false
    }
};
