'use strict';

/* Services */


var myAppServices = angular.module('myApp.services', []);


myAppServices.factory('Data', ['$resource', '$http',
  function ($resource, $http) {
    var data = {
      year: 2014,
      years: [2014, 2013, 2012, 2011, 2010],
      office: "Mayor",
      cityWideOffices: ['Mayor', 'Council Chairman', 'Council At-Large'],
      districtWideOffices: ['Council Ward1', 'Council Ward2'],
      api_url: '//rawgit.com/techforelissa/finance-data/master'
    };

    // function setProperty(obj, prop, get) {
    //   Object.defineProperty(obj, prop, {
    //     configurable: true, // property descriptor may be changed
    //     enumerable: true, // property shows up during enumeration of the property
    //     get: get,
    //   });
    // }


    data.fetchCampaigns = function () {
      $http.get(this.api_url + '/years and offices.json', {
        cache: true,
      }).success(function (returned) {
        data.campaigns = returned;
      });
    }

    data.years = function () {
      return Object.keys(this.campaigns);
    }

    data.offices = function () {
      return this.campaigns[this.year];
    }


    data.fetchPieChart = function () {
      $http.get(data.api_url + '/' + data.year + ' ' + data.office + '.json', {
        cache: true,
      }).success(function (returned) {
        data.pieChart = returned;
      }).error(function () {
        data.pieChart = {};
      })
    }

    data.candidates = function () {
      return Object.keys(this.pieChart);
    }

    return data;
  }
]);
