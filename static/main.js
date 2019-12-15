$(document).ready(function(){
	$("#myInput").on("keyup", function() {
		var value = $(this).val().toLowerCase();
		$("tbody tr").filter(function() {
			$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
		});
		updateTable();
	});
});
function filter(filter,id){
	var value = $("#"+id).text().toLowerCase();
	$("#myInput").val(value);
	$("tbody tr").filter(function() {
		$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
	});
	updateTable();
}
function updateTable(){
		$('tbody tr:visible').each(function(e, v) {
		if (e % 2 == 0) {
			$(this).css({"background-color":"blue","color":"lightgray"});
		} else {
			$(this).css({"background-color":"lightblue","color":"black"});
		}
	});
}