/**
 * Created by hunter on 16/7/12.
 */


    //自动执行函数jia()

function del() {
    var fn = document.getElementById("ta2").rows.length; //统计当前表格行数
    if (fn > 2) {
        document.getElementById('ta2').deleteRow(-1);
    }

}
//科目下拉列之通过查询表实现函数
function opt(o) {
    var subject = document.getElementById("se");
    for (var i = 0; i < subject.length; i++) {
        var val = subject.options[i].value;
        var txt = subject.options[i].text;
        o.options.add(new Option(txt, val))
    }
}
//科目下拉列之通过form实现函数
function suboptform(o) {
    var subject = document.getElementById("id_subject");
    for (var i = 0; i < subject.length; i++) {
        var val = subject.options[i].value;
        var txt = subject.options[i].text;
        o.options.add(new Option(txt, val))
    }
}
//部门下拉列之通过form实现函数
function deptoptform(o) {
    var subject = document.getElementById("id_dept");
    for (var i = 0; i < subject.length; i++) {
        var val = subject.options[i].value;
        var txt = subject.options[i].text;
        o.options.add(new Option(txt, val))
    }
}

function curren() {
    //货币格式显示实现函数
    $('.amt').formatCurrency();
    //非货币格式清除
    $('.amt').toNumber();
}

