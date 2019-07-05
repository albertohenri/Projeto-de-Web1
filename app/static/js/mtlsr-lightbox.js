$(document).ready(function() {
			var current = '.mtlsr-images-for-lightbox ul li.current';
 
			//Função para verificar a posição atual da imagem e remover as setas(prev e next) conforme necessário
			function check_image_position(){				
				if ($(current).is(':last-child')) {
					$('.next').hide();
					$('.prev').show();
				}else if ($(current).is(':first-child')) {
					$('.next').show();
					$('.prev').hide();
				}else{
					$('.next, .prev').show();
				}
			}			
 
			$('.mtlsr-images-for-lightbox ul li').on('click', 'a', function(event) {
				event.preventDefault();
				var big_image_href = $(this).attr('href');
 
				$(this).parent().addClass('current');
				$('.mtlsr-lightbox').fadeIn();
				$('.mtlsr-lightbox').append('<img class="image-in-lightbox" src="'+big_image_href+'" alt=""></div>');
 
				check_image_position();
			});
			//Fechar
			$('.mtlsr-lightbox').on('click', '.close', function(event) {
				$('.mtlsr-lightbox').fadeOut();
				$('.mtlsr-lightbox .image-in-lightbox').remove();
				$(current).removeClass('current');
			});
			//Função Next e Prev
			$('.mtlsr-lightbox a').on('click', function(e){				
				if($(this).attr('class')=='next'){
					var big_image_href = $(current).next().find('a').attr('href');					
 
					$(current).next().addClass('current');
					$(current).prev().removeClass('current');
 
				}else if($(this).attr('class')=='prev'){
					var big_image_href = $(current).prev().find('a').attr('href');
 
					$(current).prev().addClass('current');
					$(current).next().removeClass('current');
				}
				check_image_position();
 
				$('.mtlsr-lightbox .image-in-lightbox').remove();
				$('.mtlsr-lightbox').append('<img class="image-in-lightbox" src="'+big_image_href+'" alt=""></div>');
			});
		});