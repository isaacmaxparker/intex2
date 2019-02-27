$((function(context) {
    return function() {
        
        $("#coolbtn").click(function(){
        
            $.ajax({
                "url": "/catalog/api.getdata/"
            }).done(function(data){
                $('#cooltitle').html(data);
            });
    });


        
    }
})(DMP_CONTEXT.get()));