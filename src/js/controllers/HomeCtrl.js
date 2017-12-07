angular.module('helloWorldApp')
.controller('HomeCtrl', [
    '$scope',
    function($scope) {
        $scope.message = "Good Initiative"
        $scope.invitation = "Hello There"

    }
]);