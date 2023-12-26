window.addEventListener('DOMContentLoaded', function () {
	pagePath = window.location.pathname;
	pageViewsAnalytics4 = 0;
	
	if (blog_views.get(pagePath)) {
		pageViewsAnalytics4 = blog_views.get(pagePath); 
	}
	
	document.getElementById('query-output').value = pageViewsAnalytics4;
	
});