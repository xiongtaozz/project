//get或post方法
function do_ajax(){
    word = $("#word").val();
    $.get("/validate/word/", {"word": word}, function(data){
        var str='';
        var i=0;
        if(data.message!=[]){
            $.each($.parseJSON(data.message), function (k, v){
            str +='<li>'+v.fields.word_value+'</li>';
                i++;
            });
            if(str!=''){
                $("#drop_down").css("display", "block");
                $("#word_txt").html(str);
            }else{
                $("#drop_down").css("display", "none");
            }
        }
    })
}
//choose = $("#word_txt").children().attr("onclick", "choose()");

$(function(){
    $("ul").delegate('li','click',function(){
        $("#word").val($(this).text());
        drop_up()
    })
})
// function choose(){
//    $("#word").val($("ul li").text());
//}

function drop_up(){
    $("#drop_down").css("display", "none");
}
