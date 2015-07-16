
var data;
$.get('http://localhost:5000/', function(response) {
  data = response;
  console.log(data)
});


var map = L.map('map').setView([40.7142700, -74.0059700], 17);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([40.7142700, -74.0059700]).addTo(map)
    .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
    .openPopup();


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
