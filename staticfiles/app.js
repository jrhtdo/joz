var x = document.getElementById('nav-item'); 

function openNav() {
    if ( x.style.display === 'none' ) {
        x.style.display = 'block';
        x.style.transition = '0.3s'; 
} else {
x.style.display = 'none';
} 
}