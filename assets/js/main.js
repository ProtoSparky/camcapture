function init(){
    console.info("init run");
    const docroot = document.getElementById("content-fullscreen");
    const image = document.createElement("img");
    image.style.position = "absolute";
    image.style.left = "50%";
    image.style.width  ="auto";
    image.style.height = "100%";
    image.style.top = "0px";
    image.style.transform = "translate(-50%, 0)";
    image.src = "./assets/img/static.png";
    docroot.appendChild(image);
}