window.addEventListener('DOMContentLoaded', function () {
	pagePath = window.location.pathname;
	
	//Google Analytics 4
	pageViewsAnalytics4 = 0;
	
	//Google Universal Analytics
	pageViewsAnalyticsUniversal = 0;
	
	//Google Analytics 4
	if (blog_views.get(pagePath)) {
		pageViewsAnalytics4 = blog_views.get(pagePath); 
	}
	
	//Google Universal Analytics
	if (blog_views_universal.get(pagePath)) {
		pageViewsAnalyticsUniversal = blog_views_universal.get(pagePath); 
	}
	
	//Combine 2 analytics
	pageViewsAnalytics = pageViewsAnalytics4 + pageViewsAnalyticsUniversal;
	
	document.getElementById('query-output').value = pageViewsAnalytics;
	
});