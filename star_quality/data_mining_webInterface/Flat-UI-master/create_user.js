var app = angular.module("userDetailApp", ["firebase","hSweetAlert"]);				// firebase is the real time database module used
												// hSweetAlert is customized alert module


// controller for showfriends.html page.
app.controller("SearchCtrl", function($scope,$window,$http,sweet, $firebaseArray, $firebaseObject) {
    var ref = new Firebase("https://datamining-40114.firebaseio.com/");
                
    var productRef = ref.child("products");    
    $scope.result = $firebaseArray(productRef); 
    
    var ratingRef = ref.child("ratings");  
    
    $scope.fetch_details = function(product) {
    	this_product = productRef.child(product.$id);
    	$scope.id = product.$id
    	
    	this_product.on("value", function(snapshot) {
    		$scope.details = snapshot.val();
    		console.log("hii"+$scope.details)
    	});
    	
    	this_rating = ratingRef.child(product.$id);
    	this_rating.on("value", function(snapshot) {
    		$scope.rating_obj = snapshot.val();
    		console.log("hii"+$scope.rating_obj)
    	});
    	
    	$scope.search_product_title = ""
    	$scope.search_productid = ""
    } 
    
    $scope.get_title =  function(item_id) {
    	this_product = productRef.child(item_id);
    	title = "UnKnown";
    	this_product.on("value", function(snapshot) {
    		item = snapshot.val();
    		if ( item != null && item.title != null ) {
    			title = item.title;
    		}
    		console.log("hii"+title)
    	});
    	
    	return title;
    
    }
   
    
    
   
    
    
});
