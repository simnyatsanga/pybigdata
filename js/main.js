
var data;
$.get('http://localhost:5000/', function(response) {
  data = response;
  console.log(data)
});

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 1, 1000 );

var directionalLight = new THREE.DirectionalLight( 0xffffff, 0.75 );
var directionalLight2 = new THREE.DirectionalLight( 0xffffff, 0.75 );

directionalLight.position.set( -10, 5, 0);
directionalLight2.position.set( 0, 5, 5);
scene.add( directionalLight );
scene.add(directionalLight2);

var directionalLight2 = new THREE.DirectionalLight( 0xffffff, 0.5 );
directionalLight2.position.set( 0, 20, 0);
scene.add( directionalLight2 );

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

var geometry = new THREE.BoxGeometry( 1, 1, 1 );
var material = new THREE.MeshLambertMaterial({color: 0x00ff00, ambient: 0x00ffff, emissive:0x000000, shading: THREE.SmoothShading});
var cube = new THREE.Mesh( geometry, material );
scene.add( cube );

camera.position.z = 5;

function render() {
    requestAnimationFrame(render);

    cube.rotation.x += 0.01;
		cube.rotation.y += 0.01;

    renderer.render(scene, camera);
}
render();
