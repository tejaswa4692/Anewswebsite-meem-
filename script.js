async function init() {
    const res = await fetch('http://127.0.0.1:5000/');
    const data = await res.json();

    console.log(data)
    
    data.forEach(c => {
        addcards(c.heading, c.imglnk, c.content, c.date);
    });

    
}

async function addcards(heading,image, content, date) {
    console.log("adding")
    const newdiv = document.getElementById("card");
    const cloned = document.createElement("div");
    cloned.innerHTML = newdiv.innerHTML;

    cloned.querySelector("h1").innerHTML = heading;
    cloned.querySelector("img").src = image;
    cloned.querySelector("p").innerHTML = content;

    cloned.classList.add("card");
    document.getElementById("leftpanel_big").insertBefore(cloned, document.getElementById("leftpanel_big").firstChild)
}


window.onload = init()