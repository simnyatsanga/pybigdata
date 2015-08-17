
var data = null;
var best_restaurants_layer;
qwest.get('/top_10_restaurants')
    .then(function(xhr, response) {
      data = JSON.parse(xhr);

      best_restaurants_layer = new L.LayerGroup();

      data.forEach(function (restaurant) {
         L.marker([restaurant.address.coord[1], restaurant.address.coord[0]]).bindPopup(restaurant.name + " on: "+ restaurant.address.building + " Building, " + restaurant.address.street ).addTo(best_restaurants_layer);
      });

      var map_layer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
           attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>'
       });

      var map = L.map('map', {
        center: [40.7342700, -74.0059700],
        zoom: 13,
        layers: [map_layer, best_restaurants_layer]
      });

      var baseMaps = { "baseMap": map_layer };
      var overlayMaps = { "Top rated restaurants": best_restaurants_layer };

      L.control.layers(baseMaps, overlayMaps).addTo(map);
 });

//TODO: Utilise Three.js code
// var scene = new THREE.Scene();
// var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 1, 1000 );
//
// var directionalLight = new THREE.DirectionalLight( 0xffffff, 0.75 );
// var directionalLight2 = new THREE.DirectionalLight( 0xffffff, 0.75 );
//
// directionalLight.position.set( -10, 5, 0);
// directionalLight2.position.set( 0, 5, 5);
// scene.add( directionalLight );
// scene.add(directionalLight2);
//
// var directionalLight2 = new THREE.DirectionalLight( 0xffffff, 0.5 );
// directionalLight2.position.set( 0, 20, 0);
// scene.add( directionalLight2 );
//
// var loader = new THREE.JSONLoader();
//
// // load a resource
// loader.load(
// 	// resource URL
// 	'models/map2.js',
// 	// Function when resource is loaded
// 	function ( geometry, materials ) {
// 		var material = new THREE.MeshFaceMaterial( materials );
// 		var object = new THREE.Mesh( geometry, material );
// 		scene.add( object );
// 	}
// );
//
// var renderer = new THREE.WebGLRenderer();
// renderer.setSize( window.innerWidth, window.innerHeight );
// document.body.appendChild( renderer.domElement );
//
// //var geometry = new THREE.BoxGeometry( 1, 1, 1 );
// //var material = new THREE.MeshLambertMaterial({color: 0x00ff00, ambient: 0x00ffff, emissive:0x000000, shading: THREE.SmoothShading});
// //var cube = new THREE.Mesh( geometry, material );
// //scene.add( cube );
//
// camera.position.z = 550;
// camera.position.y = 200;
// camera.lookAt(new THREE.Vector3(0, -200, -550))
//
// function render() {
//     requestAnimationFrame(render);
//
//     //cube.rotation.x += 0.01;
// 		//cube.rotation.y += 0.01;
//
//     renderer.render(scene, camera);
// }
// render();
