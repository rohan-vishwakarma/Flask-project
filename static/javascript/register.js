// document.addEventListener('DOMContentLoaded', function () {


//     const form = document.forms.namedItem("form");
//     form.addEventListener(
//       "submit", 
//       async (event) =>{
//         event.preventDefault(); 

//             const output = document.querySelector("#output");
//             const formData = new FormData(form);
        

//                 try {
//                     const response = await fetch("authentication/add", {
//                         method: "POST",
//                         body: formData,
//                     });

//                     const data = response.json();
//                     console.log(data)

//                 } catch (error) {
//                     output.innerHTML = "An excd.";
//                 }

//         },
//         false,
//     );
    

// });
