from django.urls import path
from .p_views.category_view import CategoryViewSet
from .p_views.sub_category_view import SubCategoryViewSet
from .p_views.image_view import ImageViewSet
from .p_views.product_view import ProductListViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'subcategory', SubCategoryViewSet, basename='subcategory')
router.register(r'upload', ImageViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-list', ProductListViewSet)

urlpatterns =  router.urls
