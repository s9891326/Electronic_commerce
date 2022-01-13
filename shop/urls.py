from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from shop import views

# app_name = "stores"
#
# # rest api
# router = routers.DefaultRouter()
# router.register("store", views.StoreViewSet)
# router.register("menu", views.MenuViewSet, basename="menu_api")
# router.register("comment", views.CommentViewSet, basename="comment_api")

app_name = "shop"

urlpatterns = [
    # path('api/', include(router.urls)),
    # path('', views.hello),
    path('', views.shop_view),
    path('shop/create', views.post_create_view, name="post_create_view"),
    path('test', views.json_response_view),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
