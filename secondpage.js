

const imagebb_api = "80d583c76874d0b710d837acf5d259f1"
let linktoimg;

//REMEMBER TO REMOVE THIS FROM HERE AND USE ENV VARIABLE


document.getElementById("uploadbutton").addEventListener("click", async function(){


    if(linktoimg){
        const heading = document.getElementById("headingbox").value;
        const content = document.getElementById("contentbox").value;
        const date = document.getElementById("datebox").value;
        
        if (!heading || !content || !date) {
            document.getElementById("uploadbutton").innerHTML = "nigga u left a field empty"
        }else{
            addCard(heading, content, date, linktoimg);
            
        }
    }else{
        document.getElementById("uploadbutton").innerHTML = "Upload an image"
    }

    
    






})


document.getElementById("uploadimage").addEventListener("click", async function() {
    const image = document.getElementById("imageUpload");
    await uploadimage(image);
   
})




async function addCard(date, heading, content, imglnk) {
  try {
    const res = await fetch("http://127.0.0.1:5000/add_card", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({date: date, heading: heading, content: content, imglnk: imglnk})
    });

    const data = await res.json();
    console.log("Server response:", data);
  } catch (err) {
    console.error("Error:", err);
  }
}


async function uploadimage(imageee) {
    console.log(imageee)
    const image = imageee.files[0];

    if (!image) {
        document.getElementById("uploadbutton").innerHTML = "Please select an image first";
        return;
    }

    const reader = new FileReader();

    reader.onload = () => {
        const base64image = reader.result.split(',')[1];

        fetch(`https://api.imgbb.com/1/upload?key=${imagebb_api}`, {
            method: 'POST',
            body: new URLSearchParams({
                'image': base64image
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log(data.data.url);
                linktoimg = data.data.url;
                document.getElementById("uploadimage").style.display = "none";
            } else {
                document.getElementById("uploadimage").innerHTML = "image upload failed";
                console.log("Gay ahh nigga u failed")
            }
        })
    }


    reader.readAsDataURL(image);


}


