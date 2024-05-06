import streamlit as st
def image_corousel(height = 450):
    import streamlit.components.v1 as components
    return components.html(
    """
          <!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {box-sizing: border-box;}
body {font-family: Verdana, sans-serif;}
.mySlides {display: none;}
img {vertical-align: middle;}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.8s;
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .text {font-size: 11px}
}
</style>
</head>
<body>


<div class="slideshow-container">

<div class="mySlides fade">
  <div class="numbertext">1 / 3</div>
  <img src="https://unsplash.com/photos/wot0Q5sg91E/download?ixid=M3wxMjA3fDB8MXxzZWFyY2h8MzF8fGhvbWVzfGVufDB8MHx8fDE3MTQ2NzI2MDV8Mg&force=true&w=1920" style="width:100%">
</div>

<div class="mySlides fade">
  <div class="numbertext">2 / 3</div>
  <img src="https://unsplash.com/photos/2gDwlIim3Uw/download?ixid=M3wxMjA3fDB8MXxzZWFyY2h8M3x8aG9tZXN8ZW58MHx8fHwxNzE0NjA0MjU5fDA&force=true&w=1920" style="width:100%">
</div>

<div class="mySlides fade">
  <div class="numbertext">3 / 3</div>
  <img src="https://unsplash.com/photos/wDDfbanbhl8/download?ixid=M3wxMjA3fDB8MXxzZWFyY2h8MTd8fGhvbWVzfGVufDB8MHx8fDE3MTQ2NzI1OTZ8Mg&force=true&w=1920" style="width:100%">
</div>

</div>
<br>

<div style="text-align:center">
  <span class="dot"></span> 
  <span class="dot"></span> 
  <span class="dot"></span> 
</div>

<div style="font-family: Arial, sans-serif; background-color: #f0f0f0; padding: 20px; border: 1px solid #ccc; border-radius: 5px; width: auto; height: auto;text-align: center; display:center; margin: auto;">
    <h2 style="margin-top: 0;">Property Details</h2>
    <p style="margin-bottom: 5px;"><strong>Name:</strong> John Doe</p>
    <p style="margin-bottom: 5px;"><strong>Address:</strong> 123 Main St, Cityville, State, ZIP</p>
    <p style="margin-bottom: 5px;"><strong>Phone:</strong> 555-555-5555</p>
    <p style="margin-bottom: 5px;"><strong>Email:</strong> john.doe@example.com</p>
</div>


<script>
let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides,3000);
}
</script>
</body>
</html> 

    """,
    height=height,
)

""
def property_info(property_name="a",adress="a",city="",state=""):
    return st.markdown(f"""

  <div style="font-family: Arial, sans-serif; background-color: #f0f0f0; padding: 20px; border: 1px solid #ccc; border-radius: 5px; width: auto; height: auto;text-align: center; display:center; margin: auto;">
    <h2 style="margin-top: 0;">Property Details</h2>
    <p style="margin-bottom: 5px;"><strong>Name:</strong>  {property_name}</p>
    <p style="margin-bottom: 5px;"><strong>Address:</strong> {adress}</p>
    <p style="margin-bottom: 5px;"><strong>City:</strong>  {city}</p>
    <p style="margin-bottom: 5px;"><strong>State:</strong>  {state}</p>
</div>


  """,unsafe_allow_html=True)