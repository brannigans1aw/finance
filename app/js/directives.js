'use strict';

/* Directives */


var myAppDirectives = angular.module('myApp.directives', []);

// myAppDirectives.directive('myC3Donyt', function () {
    //     return {
    //       scope: { // isolate scope
    //         'data': '=',
    //       },
    //       link: function postLink(scope, iElement, iAttrs) {
    //         var chart = c3.generate({
    //           data: {
    //             // iris data from R
    //             columns: [
    //               ['data1', 30],
    //               ['data2', 120],
    //             ],
    //             type: 'pie',
    //           },
    //         });
    //         scope.$watch('val', function (newVal, oldVal) {
    //           chart.unload(oldVal);
    //           chart.load(newVal);
    //         });
    //       };
    //     });
