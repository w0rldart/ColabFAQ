
/*******************************
          Clean Task
*******************************/

var
    del = require('del')
;

// export task
module.exports = function(callback) {
    var pattern = [
        '../static/**/*',
        '!../static/images/',
        '!../static/images/**'
    ];

    return del(pattern, {
        force: true
    }, callback());
}
