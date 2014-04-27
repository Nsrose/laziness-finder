$(document).ready(function(){

	$(".navbar-item").hover(
		function() {
			$(this).fadeOut(100);
			$(this).fadeIn(400);
			// $(".arrow").show();
		});

	$(".link").hover(
		function() {
			$(this).fadeOut(100);
			$(this).fadeIn(100);
		});

	$("input[type=submit]").hover (
		function() {
			$(this).css({
				"box-shadow": "0px 0px 4px 4px",
			})
			$(".quiz").fadeTo(400, 0.5);
		}, function() {
			$(this).css({
				"box-shadow": "0px 0px 1px 1px",
			})
			$(".quiz").fadeTo(400, 1);
		})

	$("#button-wrapper").hover (
		function() {
			$(".state").fadeTo(400, 0.5);
		}, function() {
			$(".state").fadeTo(400, 1);
		})

	$("#buttonlink").hover( 
		function() {
			$(this).fadeOut(100);
			$(this).fadeIn(400);
			$("#title").fadeTo(600, 0);
			$("#subtitle").fadeTo(1000, 0);
			$("#background").fadeTo(1200, 0.5);
		}, function() {
			$("#title").fadeTo(600, 1);
			$("#subtitle").fadeTo(1000, 1);
			$("#background").fadeTo(1200, 1);
		})

	$("#quizaction").hover(
		function (){
			$(this).css({
				"box-shadow": "0px 0px 4px 4px",
				"cursor": "pointer",
			})
			$("#title").fadeTo(500, 0);
			$("#subtitle").fadeTo(900, 0);
			$("#background").fadeTo(1100, 0.5);
		}, function() {
			$(this).css({
				"box-shadow": "0px 0px 1px 1px",
			})
			$("#title").fadeTo(500, 1);
			$("#subtitle").fadeTo(900, 1);
			$("#background").fadeTo(1100, 1);
		})
	$("#quizaction").click(
		function() {
			window.location.href="/quiz";
		})

	var shown = false;
	$("#links").click(
		function() {
		if (!shown) {
			$("#hidden-links").css("display", "inline-block");
			$(".arrow").css({
				"display": "inline-block",
			})
			$(".arrow").animate({ opacity: 1 }, "slow");
			$("#hidden-links").animate({ opacity: 1 }, "slow");
			shown = true;
		} else {
			$("#hidden-links").animate({ opacity: 0 }, "slow");
			$("#hidden-links").css("display", "none");
			$(".arrow").fadeOut(100);
			shown = false;
		}	
		});

	$("#button-wrapper").click(
		function() {
			window.location.href="/quiz";
		})

});