document.addEventListener('DOMContentLoaded', function() {
    console.log("hello");
    const a = document.getElementById('submit').addEventListener('click', (e)=>{
        e.preventDefault()
        console.log("click");
        getdata()
        async function getdata() {
            const response = await fetch("/authentication/add");
            const movies = await response.json();
            console.log(movies);
        }
          
        
    })
  });
  