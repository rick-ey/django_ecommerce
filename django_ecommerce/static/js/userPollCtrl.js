var pollsApp = angular.module('pollsApp', []);

pollsApp.config(function($interpolateProvider){
  $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

pollsApp.controller('userPollCtrl',
function($scope) {
  $scope.total_votes = 0;
  $scope.vote_data = {}

  $scope.vote = function(voteModel) {
    if (!$scope.vote_data.hasOwnProperty(voteModel)) {
      $scope.vote_data[voteModel] = {"votes": 0, "percent": 0};
      $scope[voteModel]=$scope.vote_data[voteModel];
    }
    $scope.vote_data[voteModel]["votes"] = $scope.vote_data[voteModel]["votes"] + 1;
    $scope.total_votes = $scope.total_votes + 1;
    for (var key in $scope.vote_data) {
      var item = $scope.vote_data[key];
      item["percent"] = item["votes"] / $scope.total_votes * 100;
    }
  };
});
