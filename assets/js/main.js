var client_data = {
    "stats":null,
    "backend":null
};
var img_stacker = 0; 
var docroot = null;
function init(){
    const client_settings = {
        "stats_loc":"./stats.json",
        "backend_settings":"./settings.json"
    };

    client_data.stats = ReadJSON(client_settings.stats_loc, false);
    client_data.backend = ReadJSON(client_settings.backend_settings, false);
    docroot = document.getElementById("content-fullscreen");
    spawn_img();
    spawninfo();
    refresh();

}

function spawn_img(){    
    const image = document.createElement("img");
    image.id = "image0";
    image.style.position = "absolute";
    image.style.left = "50%";
    image.style.top = "140px";
    image.style.width = "600px";
    image.style.height = "auto";
    image.style.backgroundColor = AccessCSSVar("--col_bg_content");
    image.style.zIndex = 0; 
    image.style.transform = "translate(-50%, 0) rotate("+client_data.backend.rotate_frame+"deg)";
    image.src  =`${"./assets/img/static.png"}?t=${new Date().getTime()}`;
    docroot.appendChild(image);
    /*
    const image1 = document.createElement("img");
    image1.id = "image1";
    image1.style.position = "absolute";
    image1.style.left = "50%";
    image1.style.top = "140px";
    image1.style.width = "600px";
    image1.style.height = "auto";
    image1.style.zIndex = 0; 
    image1.style.backgroundColor = AccessCSSVar("--col_bg_content");
    image1.style.transform = "translate(-50%, 0) rotate("+client_data.backend.rotate_frame+"deg)";
    image1.src  =`${"./assets/img/static.png"}?t=${new Date().getTime()}`;
    docroot.appendChild(image1);*/
}

function spawninfo(){
    const infobox = document.createElement("div");
    infobox.style.position = "absolute";
    infobox.style.top = "50%";
    infobox.style.left = 0;
    infobox.style.transform = "translate(0, -50%)";
    infobox.style.width = 150;
    infobox.style.height = 300;
    infobox.style.color = AccessCSSVar("--col_normalTXT");
    infobox.className  ="text";
    docroot.appendChild(infobox);

    const album_size = document.createElement("div");
    album_size.style.position = "absolute";
    album_size.style.top = 0;
    album_size.style.height = 100;
    album_size.style.left = 0;
    album_size.innerHTML = "History Size: " + client_data.stats.history_storage_size + " <br>Images in history: " + (client_data.stats.history_size-1); 
    album_size.style.textWrap = "balance";
    infobox.appendChild(album_size);

    const backend_settings = document.createElement("div");
    backend_settings.style.top = album_size.style.height;
    backend_settings.style.position = "absolute";
    backend_settings.style.left = 0;
    backend_settings.style.height = 100; 
    backend_settings.innerHTML = "Images pr hour: " + client_data.backend.constant_update_freq + "<br> Viewport fps: " + client_data.backend.burst_fps + "<br> Viewport rotated by: " + client_data.backend.rotate_frame + " degrees";
    infobox.appendChild(backend_settings);

    const enable_refresh = document.createElement("button");
    enable_refresh.style.position = "absolute";
    enable_refresh.style.left = 0;
    enable_refresh.style.top = parseInt(backend_settings.style.height) + parseInt(album_size.style.height);
    enable_refresh.id = "enable_refresh";
    enable_refresh.innerHTML = "Enable Refresh";
    enable_refresh.addEventListener("click", function(){
        set_refresh();
    });
    infobox.appendChild(enable_refresh);    
}

function set_refresh(){
    console.log("press");
    if(localStorage.getItem("refresh") == "true"){
        console.info("turning off refresh interval");
        localStorage.setItem("refresh", false);
        document.getElementById("enable_refresh").innerHTML = "Enable Refresh";
    }
    else{
        console.info("turning on refresh interval");
        localStorage.setItem("refresh", true);
        document.getElementById("enable_refresh").innerHTML = "Disable Refresh";
    }
}
function refresh(){
    setInterval(function() {
        if(localStorage.getItem("refresh") == "true"){            
            refresh_img();
        }
    }, 1000);

};

function refresh_img(){
    const img = document.getElementById("image"+0);
    img.src = `${"./assets/img/static.png"}?t=${new Date().getTime()}`;     
    /*
    if(img_stacker>1){
        img_stacker = 0;
    }
    const past_image = document.getElementById("image"+ num_invert(img_stacker));
    past_image.style.zIndex = 0;
    past_image.src  =`${"./assets/img/static.png"}?t=${new Date().getTime()}`;
    const current_image = document.getElementById("image"+img_stacker);
    current_image.src  =`${"./assets/img/static.png"}?t=${new Date().getTime()}`;
    current_image.style.zIndex = 999;
    img_stacker ++; */
}
function num_invert(num){
    return num === 0 ? 1 : 0;
}