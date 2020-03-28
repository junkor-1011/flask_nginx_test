// header

var test_var = "test";

initialize = function(){
    console.log("init.");
};


$(document).ready(function(){
    // init
    initialize();
    console.log(test_var);
});
