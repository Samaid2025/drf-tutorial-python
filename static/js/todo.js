var app = angular.module('toDo', []);
app.controller('toDoController', function($scope, $http) {
    // $scope.todoList = [{todoText: 'Finish this app', done: false}];
    $http.get('/todo/api/').then(function(response) {
        $scope.todoList = [];
        for (var i = 0; i < response.data.length; i++) {

            var todo = {};
            todo.todoText = response.data[i].text

            todo.done = response.data[i].done
            todo.id = response.data[i].id
            $scope.todoList.push(todo);
        }
    });
//    $scope.saveData = function() {
//        var data = {text: $scope.todoInput, done: false}
//        $http.put('/todo/api/', data)
//    }
    $scope.saveData = function() {
        var data = {text: $scope.todoInput}
        console.log("Data from uploads " ,data)
        $http.put('todo/api/uploads', data)
    }
    $scope.selectFile = function(){
        var f = document.getElementById('file').files[0],
            r = new FileReader();
    console.log("ahtesham .. . ." , r , f)
        r.onloadend = function(e) {
          var data = e.target.result;
          var filedata = new FormData();
          filedata.append('file' , f);
          filedata.append('name' ,f.name );

          console.log("i got ",filedata)
          console.log("ahtesham" , r )
     $http.put('todo/api/uploads', filedata)
      //send your binary data via $http or $resource or do anything else with it
    }

    r.readAsBinaryString(f);
        //console.log($scope.fileuploadmodel, '>>>')
    }
    $scope.fileNameChaged = function(){

    }

    $scope.todoAdd = function() {
        $scope.todoList.push({todoText: $scope.todoInput, done: false});
        $scope.todoInput = '';
    };
    $scope.remove = function() {
        var oldList = $scope.todoList;
        $scope.todoList = [];
        angular.forEach(oldList, function(todo) {
            if (todo.done) {
                $http.delete('/todo/api/' + todo.id + '/');
            } else {
                $scope.todoList.push(todo);
            }
        })
    }
})
