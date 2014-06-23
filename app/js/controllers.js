'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
  .controller('SelectController', ['$scope', 'Data', '$http',

    function ($scope, Data, $http) {
      $scope.data = Data;


      $http({
        method: 'GET',
        url: 'https://raw.githubusercontent.com/techforelissa/finance-data/master/years%20and%20offices.json'
      }).
      success(function (data) {
        $scope.data.tree = data;
      })

      $scope.officeContended = function (office) {
        return _.contains($scope.data.offices, office);
      }

      $scope.setOffice = function (office) {
        $scope.data.office = office;
        $scope.data.fetch();
      }

      $scope.setYear = function (year) {
        $scope.data.year = year;
        $scope.data.fetch();
      }
    }
  ])
  .controller('GraphsController', ['$scope', 'Data', '$http',
    function ($scope, Data, $http) {
      $scope.data = Data;
      $scope.data.fetch = function () {
        $http({
          method: 'GET',
          url: 'https://raw.githubusercontent.com/techforelissa/finance-data/master/' + $scope.data.year + ' ' + $scope.data.office + '.json'
        }).
        success(function (data, status, headers, config) {
          $scope.data.piestuff = data;
          // this callback will be called asynchronously
          // when the response is available
        }).
        error(function (data, status, headers, config) {
          // called asynchronously if an error occurs
          // or server returns response with an error status.
        });
      }
      $scope.pieChartData = function (name) {
        return _.pairs($scope.data.piestuff[name])
      }

      function sum(a) {
        return _.reduce(a, function (memo, num) {
          return memo + num;
        }, 0);
      }
      $scope.totalContr = function (name) {
        return sum(_.values($scope.data.piestuff[name]));
      }
    }
  ]);
