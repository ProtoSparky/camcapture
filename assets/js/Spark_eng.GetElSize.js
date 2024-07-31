function GetElementSize(IdOrClass, divname, divID){
    //divID only used for classes
    returnARR = []; 
    if(IdOrClass == 0){
        if(document.getElementById(divname) == null){
            const ERROR = "ERROR element ID"+IdOrClass+" '"+divname+"' not found in GetElementSize()";
            console.log(ERROR);
            return null;
        }
        else{
            //Run for id
            object = document.getElementById(divname);
            const current_object_X = parseInt(object.style.left);
            const current_object_Y = parseInt(object.style.top);
            const current_object_X_W = parseInt(object.clientWidth);
            const current_object_Y_H = parseInt(object.clientHeight);
            const current_object_X_IW = current_object_X + current_object_X_W;
            const current_object_Y_FB = current_object_Y + current_object_Y_H;

            // Current object name; Current object x coordinate; current object width; current object x coordinate inc width; current object y; current object height; current object coordinate inc H
            returnARR = [divname, current_object_X , current_object_X_W, current_object_X_IW, current_object_Y,current_object_Y_H, current_object_Y_FB, divID]; 
            return returnARR; 
        }
    }
    else if(IdOrClass == 1){
        if(document.getElementsByClassName(divname)[divID] == null){
            const ERROR = "ERROR element ID"+IdOrClass+" '"+divname+"' not found in GetElementSize()";
            console.log(ERROR);
            return null;
            
        }
        else{          
            //run for class
            object = document.getElementsByClassName(divname);
            const current_object_X = parseInt(object[divID].offsetLeft);
            const current_object_Y = parseInt(object[divID].offsetTop);
            const current_object_X_W = parseInt(object[divID].offsetWidth);
            const current_object_Y_H = parseInt(object[divID].offsetHeight);
            const current_object_X_IW = current_object_X + current_object_X_W;
            const current_object_Y_FB = current_object_Y + current_object_Y_H;
            
            // Current object name; Current object x coordinate; current object width; current object x coordinate inc width; current object y; current object height; current object coordinate inc H
            returnARR = [divname, current_object_X , current_object_X_W, current_object_X_IW, current_object_Y,current_object_Y_H, current_object_Y_FB, divID]; 
            return returnARR; 
        }
    }    
}