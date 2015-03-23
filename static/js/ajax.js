$(function(){
	$('#search').keyup(function(){
		$.ajax({
			//dataType: 'json',
			type: "POST",
			url: "busca_cliente/",
			data: {
				'search_text' : $('#search').val(),
				'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType: 'html'
		});
	});

});

function searchSuccess(data, textStatus, jqXHR)
{
	$('#search-results').html(data);
}


 $('#element').on('keypress', function() {
   //code to be executed
 }).on('keydown', function(e) {
   if (e.keyCode==8)
     $('element').trigger('keypress');
 });