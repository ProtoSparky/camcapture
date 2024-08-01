var client_data = {
    "stats":null,
    "backend":null
};
function init(){
    const client_settings = {
        "stats_loc":"./stats.json",
        "backend_settings":"./settings.json"
    };

    client_data.stats = ReadJSON(client_settings.stats_loc, false);
    client_data.backend = ReadJSON(client_settings.backend_settings, false);
    spawn_img()
}

function spawn_img(){
    const docroot = document.getElementById("content-fullscreen");
    const image = document.createElement("img");
    image.style.position = "absolute";
    image.style.left = "50%";
    image.style.top = "0px";
    console.log(client_data);
    if(client_data.backend.rotate_frame == 90 || client_data.backend.rotate_frame == "270"){
        image.style.width  ="100%";
        image.style.height = "auto";
    }
    else{
        console.info("image scaling set to vertical");
        image.style.width  ="auto";
        image.style.height = "100%";
    }
    image.style.transform = "translate(-50%, 0) rotate("+client_data.backend.rotate_frame+"deg)";
    image.src = "./assets/img/static.png";
    docroot.appendChild(image);
}