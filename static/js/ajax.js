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


$(function(){
	$('#buscar_cliente').onclick(function(){
		$.ajax({
			//dataType: 'json',
			type: "POST",
			url: "busca_cliente/",
			data: {
				'search_text' : $('#cliente_nome').val(),
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
