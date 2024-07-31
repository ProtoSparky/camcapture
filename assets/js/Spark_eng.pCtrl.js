
//-------------------------------------------------------------------------------------------------------------
//------------------------------------Player CTRL--------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
const keys = {};
document.addEventListener("keydown",(e) =>{
    keys[e.key] = true;
});
document.addEventListener("keyup",(e)=>{
    keys[e.key] = false;
});
function check_player_input(){
    current_player_X = parseInt(player.style.left);
    current_player_Y = parseInt(player.style.top);
    const key_W = keys["W"] || keys["w"];
    const key_A = keys["A"] || keys["a"];
    const key_S = keys["S"] || keys["s"];
    const key_D = keys["D"] || keys["d"];

    

    if(key_W && key_A){
        if(DEBUG){
            console.log("wa"); 
        }
        //check if player is about to not collide, and move
        if(!IScollided(current_player_X, player_sizeX,  current_player_Y - player_speed,player_sizeY, "col_mesh")[3] && !IScollided(current_player_X - player_speed, player_sizeX,  current_player_Y,player_sizeY, "col_mesh")[1]){
            player.style.top = (current_player_Y - player_speed);
            player.style.left = (current_player_X - player_speed);
        }
        else if(!IScollided(current_player_X, player_sizeX,  current_player_Y - player_speed,player_sizeY, "col_mesh")[3]){
            player.style.top = (current_player_Y - player_speed);
        }
        else if(!IScollided(current_player_X - player_speed, player_sizeX,  current_player_Y,player_sizeY, "col_mesh")[1]){
            player.style.left = (current_player_X - player_speed);
        }
    }
    else if(key_W && key_D){
        if(DEBUG){
            console.log("wd");
        }
        //check if player is about to not collide, and move
        if(!IScollided(current_player_X, player_sizeX,  current_player_Y - player_speed,player_sizeY, "col_mesh")[3] && !IScollided(current_player_X + player_speed, player_sizeX,  current_player_Y,player_sizeY, "col_mesh")[2]){
            player.style.top = (current_player_Y - player_speed);
            player.style.left = (current_player_X + player_speed);
        }
        else if(!IScollided(current_player_X, player_sizeX,  current_player_Y - player_speed,player_sizeY, "col_mesh")[3]){
            player.style.top = (current_player_Y - player_speed);
        }
        else if(!IScollided(current_player_X + player_speed, player_sizeX,  current_player_Y,player_sizeY, "col_mesh")[2]){
            player.style.left = (current_player_X + player_speed);
        }
    }
    else if(key_A && key_S){
        if(DEBUG){
            console.log("as");
        }
        //check if player is about to not collide, and move
        if(!IScollided(current_player_X - player_speed, player_sizeX,  current_player_Y,player_sizeY, "col_mesh")[1] && !IScollided(current_player_X, player_sizeX,  current_player_Y + player_speed,player_sizeY, "col_mesh")[4]){
            player.style.left = (current_player_X - player_speed);
            player.style.top = (current_player_Y + player_speed);
        }
        else if(!IScollided(current_player_X, player_sizeX,  current_player_Y + player_speed,player_sizeY, "col_mesh")[4]){
            player.style.top = (current_player_Y + player_speed);   
        }
        else if(!IScollided(current_player_X - player_speed, player_sizeX,  current_player_Y,player_sizeY, "col_mesh")[1]){
            player.style.left = (current_player_X - player_speed);
        }    

        
        
    }
    else if(key_S && key_D){
        if(DEBUG){
            console.log("sd");
        }
        //check if player is about to not collide, and move
        if(!IScollided(current_player_X + player_speed, player_sizeX,  current_player_Y,player_sizeY, "col_mesh")[2] && !IScollided(current_player_X, player_sizeX,  current_player_Y+ player_speed,player_sizeY, "col_mesh")[4]){
            player.style.top = (current_player_Y + player_speed);
            player.style.left = (current_player_X + player_speed);
        }
        else if (!IScollided(current_player_X, player_sizeX,  current_player_Y+ player_speed,player_sizeY, "col_mesh")[4]){
            player.style.top = (current_player_Y + player_speed);
        }
        else if(!IScollided(current_player_X - player_speed, player_sizeX,  current_player_Y,player_sizeY, "col_mesh")[1] && !IScollided(current_player_X + player_speed, player_sizeX,  current_player_Y,player_sizeY, "col_mesh")[2]){
            player.style.left = (current_player_X + player_speed);
        }
    }
    else if(key_W){
        if(DEBUG){
            console.log("w");
        }
        //check if player is about to not collide, and move
        if(!IScollided(current_player_X, player_sizeX,  current_player_Y- player_speed,player_sizeY, "col_mesh")[3]){
            player.style.top = (current_player_Y - player_speed);
        }
        
    }
    else if(key_A){
        if(DEBUG){
            console.log("a");
        }
        //check if player is about to not collide, and move
        if(!IScollided(current_player_X - player_speed, player_sizeX,  current_player_Y,player_sizeY, "col_mesh")[1]){
            player.style.left = (current_player_X - player_speed);
        }
    }
    else if(key_S){
        if(DEBUG){
            console.log("s");
        }
        //check if player is about to not collide, and move
        if(!IScollided(current_player_X, player_sizeX,  current_player_Y+player_speed,player_sizeY, "col_mesh")[4]){
            player.style.top = (current_player_Y + player_speed);
        }
    }
    else if(key_D){
        if(DEBUG){
            console.log("D");   
        }
        //check if player is about to not collide, and move
        if(!IScollided(current_player_X + player_speed, player_sizeX,  current_player_Y,player_sizeY, "col_mesh")[2]){
            player.style.left = (current_player_X + player_speed);
        }
    }
    
    /*DEBUG*/
    //Press E, and things in here will run.
    const debug_key = keys["E"] || keys["e"];
    if(debug_key){
        
    }
    /*DEBUG*/

}
//-------------------------------------------------------------------------------------------------------------
//------------------------------------Player CTRL--------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
