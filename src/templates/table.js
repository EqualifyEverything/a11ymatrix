// GO TO THE END OF THE TEST SCRIPT.
var template = `
<style>
        .fill,
body,
html {
  height: 100%
}

#json_vl,
.td_head,
.td_row_even,
.td_row_odd {
  font-size: small
}

#json_pnl,
#xxa,
.navbar-header,
.navbar-nav,
.navbar-nav>li,
.td_head {
  float: left
}

.fill {
  min-height: 100%
}

#json_vl {
  font-family: Consolas, Monaco, Lucida Console, Liberation Mono, DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace
}

#widget {
  width: 100%
}

.top_size {
  height: 51px
}

#all_panels {
  height: 100%;
  min-height: 100%
}

#aboutLnk {
  position: fixed;
  right: 10px;
  top: 15px
}

#inner_text {
  display: block;
  position: absolute;
  height: auto;
  bottom: 0;
  top: 0;
  left: 0;
  right: 0;
  margin-top: 51px;
  margin-bottom: 0
}

#json_pnl {
  background-color: #ccc;
  width: 33.3%
}

#xxa {
  background-color: #E8E8E8;
  width: 66.7%
}

#table_pnl,
#tree_pnl {
  background-color: #E8E8E8;
  float: left;
  width: 50%
}

#sharethis {
  position: fixed;
  right: 80px;
  top: 10px
}

#inner_tbl {
  padding-left: 2px
}

.td_row_even {
  padding: 2px;
  background-color: #F6F4F0
}

.td_row_odd {
  padding: 2px;
  background-color: #FFF
}

.td_head {
  padding: 2px;
  font-weight: 700
}

input,
p,
select,
td,
textarea,
th {
  font-size: 1em
}

table,
td,
th {
  border: 1px solid gray
}

textarea {
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  display: block;
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 4px;
  border: 1px solid #333;
  overflow-y: auto;
  overflow-x: hidden
}

*,
html {
  font-family: Verdana, Arial, Helvetica, sans-serif
}

form,
h1,
h2,
h3,
h4,
h5,
li,
p,
ul {
  margin: 0;
  padding: 0
}

img {
  border: none
}

p {
  margin: 0 0 1em
}

table {
  font-size: 100%;
  background-color: white;
}

ol.tree {
  padding: 0 0 0 30px;
  width: 300px
}

li {
  position: relative;
  margin-left: -15px;
  list-style: none
}

li.file {
  margin-left: -1px !important
}

li.file a {
  background: url(leaf.png)0 5px no-repeat;
  color: #000;
  padding-left: 12px;
  text-decoration: none;
  display: block;
  font-size: small
}

li.file a[href$='.css'],
li.file a[href$='.js'],
li.file a[href*='.pdf'],
li.file a[href*='.html'] {
  background: url(http://www.thecssninja.com/demo/css_tree/document.png)no-repeat
}

li input {
  position: absolute;
  left: 0;
  margin-left: 0;
  opacity: 0;
  z-index: 2;
  cursor: pointer;
  height: 1em;
  width: 1em;
  top: 0
}

li input+ol {
  background: url(http://www.thecssninja.com/demo/css_tree/toggle-small-expand.png)40px -3px no-repeat;
  margin: -20px 0 0 -44px;
  height: 1em;
  padding: 1.563em 0 0 80px
}

li label.lbl_array,
li label.lbl_obj {
  display: block;
  padding-left: 33px;
  margin-bottom: 2px
}

li input+ol>li {
  display: none;
  margin-left: -14px !important;
  padding-left: 1px
}

li label.lbl_obj {
  background: url(folder.png)15px 1px no-repeat;
  cursor: pointer
}

li label.lbl_array {
  background: url(array.png)15px 1px no-repeat;
  cursor: pointer
}

li input:checked+ol {
  background: url(http://www.thecssninja.com/demo/css_tree/toggle-small.png)40px -3px no-repeat;
  margin: -20px 0 0 -44px;
  padding: 1.563em 0 0 80px;
  height: auto
}

li input:checked+ol>li {
  display: block;
  margin: 0 0 .125em
}

li input:checked+ol>li:last-child {
  margin: 0 0 .063em
}

.container {
  width: 970px;
  max-width: none !important
}

.col-xs-4 {
  padding-top: 15px;
  padding-bottom: 15px;
  background-color: #eee;
  background-color: rgba(86, 61, 124, .15);
  border: 1px solid #ddd;
  border: 1px solid rgba(86, 61, 124, .2)
}

    </style>
<div id="html">
<input type="text" id="json">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<!--<script src="json2table.js"></script>-->
<script>
$(function() {
    pm.getData((err, data) => {
        $("#json").val(JSON.stringify(data.json));
        json2table("#html");
    });
});

function call(a) {
    $("#json").val(JSON.stringify(a, void 0, 2));
    json2table()
}

function json2table(selector) {
    $(selector).html(buildTable(getJsonVar()));
}

function getJsonVar() {
    try {
        var a = $.parseJSON($("#json").val());
        $("#json").val(JSON.stringify(a, void 0, 2));
        return a
    } catch (e) {
        //return $("#error_msg").text(e.message), $("#errorModal").modal("show"), {}
        alert(e);
    }
}

function buildTable(a) {
    var e = document.createElement("table"),
        d, b;
    if (isArray(a)) return buildArray(a);
    for (var c in a) "object" != typeof a[c] || isArray(a[c]) ? "object" == typeof a[c] && isArray(a[c]) ? (d = e.insertRow(-1), b = d.insertCell(-1), b.colSpan = 2, b.innerHTML = '<div class="td_head">' + encodeText(c) + '</div><table style="width:100%">' + $(buildArray(a[c]), !1).html() + "</table>") : (d = e.insertRow(-1), b = d.insertCell(-1), b.innerHTML = "<div class='td_head'>" + encodeText(c) + "</div>", d = d.insertCell(-1), d.innerHTML = "<div class='td_row_even'>" +
        encodeText(a[c]) + "</div>") : (d = e.insertRow(-1), b = d.insertCell(-1), b.colSpan = 2, b.innerHTML = '<div class="td_head">' + encodeText(c) + '</div><table style="width:100%">' + $(buildTable(a[c]), !1).html() + "</table>");
    return e
}

function buildArray(a) {
    var e = document.createElement("table"),
        d, b, c = !1,
        p = !1,
        m = {},
        h = -1,
        n = 0,
        l;
    l = "";
    if (0 == a.length) return "<div></div>";
    d = e.insertRow(-1);
    for (var f = 0; f < a.length; f++)
        if ("object" != typeof a[f] || isArray(a[f])) "object" == typeof a[f] && isArray(a[f]) ? (b = d.insertCell(h), b.colSpan = 2, b.innerHTML = '<div class="td_head"></div><table style="width:100%">' + $(buildArray(a[f]), !1).html() + "</table>", c = !0) : p || (h += 1, p = !0, b = d.insertCell(h), m.empty = h, b.innerHTML = "<div class='td_head'>&nbsp;</div>");
        else
            for (var k in a[f]) l =
                "-" + k, l in m || (c = !0, h += 1, b = d.insertCell(h), m[l] = h, b.innerHTML = "<div class='td_head'>" + encodeText(k) + "</div>");
    c || e.deleteRow(0);
    n = h + 1;
    for (f = 0; f < a.length; f++)
        if (d = e.insertRow(-1), td_class = isEven(f) ? "td_row_even" : "td_row_odd", "object" != typeof a[f] || isArray(a[f]))
            if ("object" == typeof a[f] && isArray(a[f]))
                for (h = m.empty, c = 0; c < n; c++) b = d.insertCell(c), b.className = td_class, l = c == h ? '<table style="width:100%">' + $(buildArray(a[f]), !1).html() + "</table>" : " ", b.innerHTML = "<div class='" + td_class + "'>" + encodeText(l) +
                    "</div>";
            else
                for (h = m.empty, c = 0; c < n; c++) b = d.insertCell(c), l = c == h ? a[f] : " ", b.className = td_class, b.innerHTML = "<div class='" + td_class + "'>" + encodeText(l) + "</div>";
    else {
        for (c = 0; c < n; c++) b = d.insertCell(c), b.className = td_class, b.innerHTML = "<div class='" + td_class + "'>&nbsp;</div>";
        for (k in a[f]) c = a[f], l = "-" + k, h = m[l], b = d.cells[h], b.className = td_class, "object" != typeof c[k] || isArray(c[k]) ? "object" == typeof c[k] && isArray(c[k]) ? b.innerHTML = '<table style="width:100%">' + $(buildArray(c[k]), !1).html() + "</table>" : b.innerHTML =
            "<div class='" + td_class + "'>" + encodeText(c[k]) + "</div>" : b.innerHTML = '<table style="width:100%">' + $(buildTable(c[k]), !1).html() + "</table>"
    }
    return e
}

function encodeText(a) {
    return $("<div />").text(a).html()
}

function isArray(a) {
    return "[object Array]" === Object.prototype.toString.call(a)
}

function isEven(a) {
    return 0 == a % 2
}
</script>`;


// In case you only want a specific property, change it here.
//
// Default: You can set the entire JSON response using pm.response.json()
let tableProps = {
    json: pm.response.json()
};

pm.visualizer.set(template, tableProps);