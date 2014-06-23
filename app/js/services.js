'use strict';

/* Services */


var myAppServices = angular.module('myApp.services', []);

myAppServices.factory('Data', ['$http',
  function ($http) {
    var data = {
      year: 2014,

      cityWideOffices: ['Mayor', 'Council Chairman', 'Council At-Large'],
      districtWideOffices: ['Council Ward1', 'Council Ward2'],
      office: "Mayor"
    }
    Object.defineProperty(data, "years", {
      get: function () {
        return Object.keys(this.tree);
      }
    });
    Object.defineProperty(data, "offices", {
      get: function () {
        return Object.keys(this.tree[this.year]);
      }
    });
    Object.defineProperty(data, "candidates", {
      get: function () {
        return this.tree[this.year][this.office];
      }
    });
    return data
  }
]);
