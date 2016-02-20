'use strict';

require('semantic-ui');

var
    React = require('react'),
    // ReactDOM = require('react-dom'),
    App = require('./App.js')
;

$(document)
    .ready(function() {
        // create sidebar and attach to menu open
        $('.ui.sidebar')
            .sidebar('attach events', '.toc.item')
        ;
    })
;

// ReactDOM.render(<App/>, document.body);
