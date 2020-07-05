function Teste(frame){
    
    for (var x = 1; x <= 4; x++){
        $('.show_frame' + x).hide();
    }
    
    $('.show_frame' + frame).show();
    
}