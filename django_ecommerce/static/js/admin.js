var adminApp = angular.module('adminApp', ['ui.bootstrap']);

adminApp.config(function($interpolateProvider, $httpProvider) {
  $interpolateProvider.startSymbol('[[').endSymbol(']]');
  $httpProvider.defaults.headers.common['X-CSRFToken'] = $('input[name=csrfmiddlewaretoken]').val();
});

adminApp.controller('AdminCtrl', function($scope, AdminUserFactory) {

  $scope.afterReset = false;

  $scope.resetpass = function(userId) {
    $scope.afterReset = false;
    var data = {
      'user': userId,
      'pass': $scope.pass,
      'pass2': $scope.pass2
    };
    return AdminUserFactory.resetPassword(data).then(showAlert, showAlert);
  };

  var showAlert = function(data) {
    $scope.afterReset = true;
    var msg = "";
    $scope.alertClass = "alert-danger";

    if (data.status == 200) {
      $scope.alertClass = "alert-success";
      $scope.pass = "";
      $scope.pass2 = "";
    }

    if (typeof data.data == 'string') {
      msg = data.data;
    } else {
      for (var x in data.data) {
        msg += data.data[x].toString() + " ";
      }
    }

    $scope.msg = msg;
    $scope.isopen = false;
    
  };
});

adminApp.factory("AdminUserFactory", function($http) {
  var factory = {};
  factory.resetPassword = function(data) {
    var pwdData = {password : data.pass, password2 : data.pass2};
    return $http.put("/api/v1/users/password/" + data.user, pwdData)
        .then(function(response)
        {
          return response;
        });
  };

  return factory;
});
